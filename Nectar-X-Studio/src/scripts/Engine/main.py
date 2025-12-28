import struct
import sys
import os
import socket
import threading
 
try:
    from llama_cpp import Llama
except Exception:
    Llama = None

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton, QMessageBox,
    QTextEdit, QCheckBox, QHBoxLayout, QFrame, QFileDialog,
    QPlainTextEdit, QStackedLayout, QFormLayout,
    QSlider, QScrollArea, QListWidgetItem, QComboBox, QGroupBox
)
from PyQt6.QtCore import (
    Qt, QTimer, pyqtSignal, QElapsedTimer,
    QObject, QSize, QPropertyAnimation, QFileSystemWatcher, QPoint, QUrl, QEasingCurve
)
from PyQt6.QtGui import (
    QIcon, QFont, QPainter,
    QColor, QCursor
)
from PyQt6.QtWebEngineWidgets import QWebEngineView

from PyQt6.QtCore import QSettings
from winotify import Notification, audio
import scripts.SYS_PROMPTS.sys_msgs as sys_msgs
import torch

from scripts.webrag import WebRAG
from scripts.ragengine import RAGEngine
from scripts.chat import Chat

from scripts.components.Service.find_icon import find_icon
from scripts.components.Service.find_menu import find_menu
from scripts.components.Utility.write_to_log import write_to_log
from scripts.SYS_Config.Config import WEB_RAG_SYSTEM_PROMPT
from scripts.components.WidgetBased.Notify import Notify
from scripts.Engine.Logic_Unit.main import query_generator, model_decides_web_rag

def auto_batch_sizes():
    """
    Auto-tune n_batch and n_ubatch based on VRAM and model size.
    Optimized for RTX 4060 (8GB) + Qwen2.5-1.5B.
    """
    try:
        if not torch.cuda.is_available():
            return 256, 256
        
        props = torch.cuda.get_device_properties(0)
        vram_gb = props.total_memory / (1024**3)
        model_size_gb = 1.5 
        
        # VRAM budget: 70% max for safety
        available_vram = vram_gb * 0.7
        
        if available_vram >= 6.0:
            n_ubatch = 2048 
        elif available_vram >= 4.0:
            n_ubatch = 1024
        elif available_vram >= 2.5:
            n_ubatch = 512
        else:
            n_ubatch = 256
            
        write_to_log(f"Auto-batch: n_ubatch={n_ubatch} "
              f"(VRAM: {vram_gb:.1f}GB, model: {model_size_gb}GB)")
        toast = Notification(
            app_id="Nectar-X-Studio",
            title="Zashir K47B-LS5 Engine",
            msg=f"Auto-batch: n_ubatch={n_ubatch} (VRAM: {vram_gb:.1f}GB, model: {model_size_gb}GB)",
            icon=find_icon('background/NectarX.png'),
            duration="short"
        )
        toast.set_audio(audio.SMS, loop=False)
        toast.show()
        return n_ubatch
        
    except Exception:
        return 256 

#------------------------------------------------------------------------------
# Auxilary Utilities
#------------------------------------------------------------------------------

class EmittingStream(QObject):
    text_written = pyqtSignal(str)

    def write(self, text):
        self.text_written.emit(str(text))

    def flush(self):
        return

class SignalEmitter(QObject):
    auto_run = pyqtSignal()
    stop = pyqtSignal()

class ClickableLabel1(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.default_style = """
            background-color: #000000;
            color: #ffffff;
            padding: 10px 15px;
            border-radius: 10px;
            font-size: 13px;
            """

        self.hover_style = """
            background-color: #ffffff;
            color: #000000;
            padding: 10px 15px;
            border-radius: 10px;
            font-size: 13px;
            """

        self.setStyleSheet(self.default_style)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def enterEvent(self, event):
        self.setStyleSheet(self.hover_style)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(self.default_style)
        super().leaveEvent(event)

class AppState:
    loaded_model_path = ''

class Loader_chat(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Speech Simulation Loader')
        self.setFixedSize(200, 200)
        self.setStyleSheet('background-color: #ffffff; color: #E0E0E0; padding: 10px; border-radius: 5px;')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.max_radius = 50
        self.min_radius = 5
        self.circles = []
        self.time = QElapsedTimer()
        self.time.start()
        for i in range(5):
            self.circles.append({'radius': self.min_radius, 'angle': i * 72.0})
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_loader)
        self.timer.start(10)

    def paintEvent(self, event):
        from PyQt6.QtGui import QColor, QPainter, QBrush
        import math

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        center_x = self.width() / 2
        center_y = self.height() / 2

        for circle in self.circles:
            x = center_x + math.cos(math.radians(circle['angle'])) * 20
            y = center_y + math.sin(math.radians(circle['angle'])) * 20
            painter.setPen(Qt.PenStyle.NoPen)

            color = QColor(255, 0, 0)
            color.setAlpha(180)
            painter.setBrush(QBrush(color))

            # Cast to int for PyQt6 compatibility
            painter.drawEllipse(
                int(x - circle['radius'] / 2),
                int(y - circle['radius'] / 2),
                int(circle['radius']),
                int(circle['radius'])
            )

    def update_loader(self):
        import math
        elapsed_time = self.time.elapsed()
        for circle in self.circles:
            fluctuation = math.sin(elapsed_time / 1000 * 2 * math.pi)
            circle['radius'] = self.min_radius + fluctuation * (self.max_radius - self.min_radius)
            circle['radius'] = max(self.min_radius, min(circle['radius'], self.max_radius))
            circle['angle'] += 3
            if circle['angle'] >= 360:
                circle['angle'] -= 360
        self.update()

from PyQt6.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QApplication
from PyQt6.QtGui import QCursor, QColor, QPalette

class ModelListPopup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | 
                            Qt.WindowType.Popup | 
                            Qt.WindowType.NoDropShadowWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 6, 6, 6)
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("""
            QListWidget {
                background-color: rgba(20, 20, 20, 240);
                border: 1px solid #444;
                border-radius: 10px;
                padding: 8px;
                color: #ffffff;
                font-size: 13px;
                outline: none;
            }
            QListWidget::item {
                border-radius: 6px;
                padding: 6px 10px;
            }
            QListWidget::item:hover {
                background-color: #2a2a2a;
            }
            QListWidget::item:selected {
                background-color: #3a3a3a;
            }
        """)
        layout.addWidget(self.list_widget)

        # Fade-in animation
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(150)

        # Connect item click
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        self.callback = None

    def populate(self, models, callback):
        """Fill the popup with models."""
        self.list_widget.clear()
        for name, path in models:
            item = QListWidgetItem(name)
            item.setData(Qt.ItemDataRole.UserRole, path)
            self.list_widget.addItem(item)
        self.callback = callback

    def show_popup(self, parent_widget):
        """Show popup near the parent label."""
        cursor_pos = parent_widget.mapToGlobal(QPoint(0, parent_widget.height()))
        self.move(cursor_pos.x(), cursor_pos.y() + 5)
        self.resize(345, 220)

        # Start fade animation
        self.setWindowOpacity(0)
        self.show()
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()

    def on_item_clicked(self, item):
        path = item.data(Qt.ItemDataRole.UserRole)
        if self.callback:
            self.callback(path)
        self.hide()

    def focusOutEvent(self, event):
        self.hide()
        super().focusOutEvent(event)

# ----------------- CUSTOM LOG VIEW WITH WATERMARK -----------------
class WatermarkedLogView(QTextEdit):
    def __init__(self, watermark_text="Nectar-X-Studio"):
        super().__init__()
        self.watermark_text = watermark_text
        self.setReadOnly(True)
        self.setStyleSheet("""
            QTextEdit {
                background-color: #000000;
                color: #ffffff;
                border: none;
                border-radius: 16px;
                padding: 8px;
            }
        """)

    def paintEvent(self, event):
        """Draw watermark centered in the widget background."""
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QColor(255, 255, 255, 30))  # Semi-transparent white
        font = QFont("Consolas", 36, QFont.Weight.Bold)
        painter.setFont(font)

        # Calculate text position for perfect centering
        text_rect = self.rect()
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, self.watermark_text)
        painter.end()

#------------------------------------------------------------------------------------
# LLM Engine Class
#------------------------------------------------------------------------------------

class LLM_Engine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowOpacity(1.0)
        self.setup_model_watcher()
        self.setWindowTitle('Engine - Nectar-X-Studio')
        self.settings1 = QSettings('Zashiron', 'Modelpath')
        self.signals = SignalEmitter()
        self.signals.auto_run.connect(self.auto_run)
        self.signals.stop.connect(self.terminate)
        self.loaded_model_path = ''
        self.executable_path = ''
        self.process = None
        self.llm_server_thread = None
        self.llm_instance = None
        
        AppState.loaded_model_path = self.loaded_model_path
        self.init_ui()

    def init_ui(self):
        import qtawesome as qta
        main_layout = QHBoxLayout()
        from PyQt6.QtWidgets import QSizePolicy
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(12)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        icon_path51 = find_menu('menu/net.png')
        icon_path52 = find_menu('menu/AI.png')
        icon_path53 = find_menu('menu/sett.png')
        icon_path54 = find_menu('menu/plus.png')
        icons = {'Load': QIcon(icon_path51), 'Output': QIcon(icon_path52), 'Settings': QIcon(icon_path53)}
        for i, name in enumerate(['Load', 'Output', 'Settings']):
            btn = QPushButton()
            btn.setIcon(icons[name])
            btn.setIconSize(QSize(24, 24))
            btn.setToolTip(name)
            btn.setFixedSize(44, 44)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #1e1e1e;
                    border-radius: 10px;
                }

                QPushButton:hover {
                    background-color: #000000;
                }

                QPushButton:pressed {
                    background-color: #000000;
                }
                
                QToolTip {
                background-color: #000000;
                color: #ffffff;
                border: 1px solid #444444;
                padding: 6px;
                font-size: 12px;
                font-family: Consolas, monospace;
                border-radius: 4px;
            }
                """)

            btn.clicked.connect(lambda _, idx=i: self.card_layout.setCurrentIndex(idx))
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch(1)

        self.rag_web_button = QPushButton()
        self.rag_web_button.setIcon(qta.icon('fa5s.globe', color='red'))
        self.rag_web_button.setToolTip('Web Search')
        self.rag_web_button.setIconSize(QSize(20, 20))
        self.rag_web_button.setFixedSize(44, 44)
        self.rag_web_button.setStyleSheet("""
            QPushButton {
                background-color: #1e1e1e;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #ffffff;
            }
            QToolTip {
                background-color: #000000;
                color: #ffffff;
                border: 1px solid #444444;
                padding: 6px;
                font-size: 12px;
                font-family: Consolas, monospace;
                border-radius: 4px;
            }
            """)

        self.rag_web_button.clicked.connect(self.web_view)

        self.rag_button = QPushButton()
        self.rag_button.setIcon(qta.icon('fa5s.plus', color='red'))
        self.rag_button.setToolTip('Retrieval-Augmented Generation')
        self.rag_button.setIconSize(QSize(20, 20))
        self.rag_button.setFixedSize(44, 44)
        self.rag_button.setStyleSheet("""
            QPushButton {
                background-color: #1e1e1e;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #ffffff;
            }
            QToolTip {
                background-color: #000000;
                color: #ffffff;
                border: 1px solid #444444;
                padding: 6px;
                font-size: 12px;
                font-family: Consolas, monospace;
                border-radius: 4px;
            }
            """)

        self.rag_button.clicked.connect(self.load_document_ui)

        self.stop_server_button = QPushButton()
        self.stop_server_button.setIcon(qta.icon('fa5s.power-off', color='orange'))
        self.stop_server_button.setToolTip('Stop')
        self.stop_server_button.setIconSize(QSize(20, 20))
        self.stop_server_button.setFixedSize(44, 44)
        self.stop_server_button.setStyleSheet("""
            QPushButton {
                background-color: #1e1e1e;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #ffffff;
            }
            QToolTip {
                background-color: #000000;
                color: #ffffff;
                border: 1px solid #444444;
                padding: 6px;
                font-size: 12px;
                font-family: Consolas, monospace;
                border-radius: 4px;
            }
            """)

        self.stop_server_button.clicked.connect(self.terminate)
        sidebar_layout.addWidget(self.rag_web_button)
        sidebar_layout.addWidget(self.rag_button)
        sidebar_layout.addWidget(self.stop_server_button)
        sidebar_widget = QWidget()
        sidebar_widget.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sidebar_widget.setFixedHeight(400)
        sidebar_widget.setStyleSheet('border-radius: 10px; background-color: #000000')
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_widget.setFixedWidth(64)
        self.card_layout = QStackedLayout()
        
        self.page_load = self.Engine()
        self.page_output = self.output_win()
        self.page_settings = self.create_settings_page()

        self.card_layout.addWidget(self.page_load)
        self.card_layout.addWidget(self.page_output)
        self.card_layout.addWidget(self.page_settings)

        self.label_model_path = ClickableLabel1('Click to load Model')
        self.label_model_path.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_model_path.setWordWrap(True)
        self.label_model_path.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_model_path.clicked.connect(self.load_model)
        self.label_model_path.setStyleSheet("""
            QLabel {
                background-color: #000000;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                color: #dddddd;
            }
            """)
        
        # Create a vertical layout that will hold the label and the main content
        content_main_layout = QVBoxLayout()
        #content_main_layout.setSpacing(0)
        #content_main_layout.setContentsMargins(0, 8, 0, 0)

        # Center the label horizontally
        label_container = QWidget()
        label_layout = QHBoxLayout(label_container)
        label_layout.setContentsMargins(0, 0, 0, 0)
        #label_layout.addStretch(1)
        label_layout.addWidget(self.label_model_path)
        #label_layout.addStretch(1)

        # Add the label and the stacked layout
        content_main_layout.addWidget(label_container)
        content_main_layout.addLayout(self.card_layout)

        # Set this layout on content_widget
        content_widget = QWidget()
        content_widget.setLayout(content_main_layout)

        # Add content_widget to the main layout alongside the sidebar
        main_layout.addWidget(sidebar_widget)
        main_layout.addWidget(content_widget)
        self.setLayout(main_layout)

        self.setup_overlay()

    def Engine(self):
        page = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        model_loader_frame = QFrame()
        model_loader_layout = QVBoxLayout(model_loader_frame)
        model_loader_layout.setContentsMargins(0, 0, 0, 0)
        model_loader_layout.setSpacing(8)

        self.combo_model_list = QComboBox()
        self.combo_model_list.addItem('Select Model to Load')
        self.combo_model_list.setStyleSheet("""
            QComboBox {
                background-color: #000000;
                border: 1px solid #444;
                border-radius: 8px;
                padding: 8px 35px 8px 12px;
                font-size: 13px;
                color: #ffffff;
            }

            QComboBox:hover {
                border: 1px solid #6c6c6c;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 28px;
                border-left: 1px solid #444;
                border-top-right-radius: 8px;
                border-bottom-right-radius: 8px;
                background-color: #ffffff;
            }

            QComboBox QAbstractItemView {
                background-color: #3a3a3a;
                color: #ffffff;
                selection-background-color: #1b1b1b;
                padding: 8px 12px;
                outline: 0;
                border-radius: 20px;
            }
            """)
        
        from pathlib import Path
        close_icon = find_icon('background/close.png')
        if close_icon:
            icon_path = Path(close_icon).as_posix()  # ensures forward slashes
            self.combo_model_list.setStyleSheet(f"""
                QComboBox::down-arrow {{
                image: url("{icon_path}");  /* Replace this with your icon */
                width: 12px;
                height: 12px;
            }},
            """)
        else:
            Notify("Close icon not found!", parent=self)

        self.combo_model_list.hide()

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)

        self.chat_layout = QStackedLayout()

        self.chat = Chat()

        self.chat_layout.addWidget(self.chat)
        
        content_widget = QWidget()
        content_widget.setLayout(self.chat_layout)
        #layout.addWidget(sidebar_widget)
        layout.addWidget(content_widget)
        page.setLayout(layout)
        return page
    
    def create_group(self, title: str, options: list):
        """
        Create a group box with combo boxes based on options.

        Parameters:
            options (list of tuples): Each tuple contains a label text and a list of options.
                Example: [("Label Text", [Option1, Option2, ...])]
        """

        group_box = QGroupBox(title)
        layout = QVBoxLayout(group_box)
        self.group_controls = getattr(self, 'group_controls', {})
        self.group_controls[title] = {}
        for label_text, values in options:
            label = QLabel(label_text)
            label.setStyleSheet('background-color: #000000; color: #ffffff;')
            combo = QComboBox()
            combo.setStyleSheet('background-color: #ffffff; color: #000000;')
            combo.addItems(values)
            layout.addWidget(label)
            layout.addWidget(combo)
            self.group_controls[title][label_text] = combo
        return group_box
    
    def create_group_kv(self, title: str, options: list):
        """
        Create a group box with combo boxes based on options.

        Parameters:
            options (list of tuples): Each tuple contains a label text and a list of options.
                Example: [("Label Text", [Option1, Option2, ...])]
        """

        group_box1 = QGroupBox(title)
        layout = QVBoxLayout(group_box1)
        self.group_controls1 = getattr(self, 'group_controls', {})
        self.group_controls1[title] = {}
        for label_text, values in options:
            label = QLabel(label_text)
            label.setStyleSheet('background-color: #000000; color: #ffffff;')
            kv_combo = QComboBox()
            kv_combo.setStyleSheet('background-color: #ffffff; color: #000000;')
            kv_combo.addItems(values)
            layout.addWidget(label)
            layout.addWidget(kv_combo)
            self.group_controls1[title][label_text] = kv_combo
        return group_box1

    def get_group_value(self, group_title: str, label_text: str):
        """
        Retrieve the currently selected value from a group combo box.
        """
        return self.group_controls[group_title][label_text].currentText()
    
    def get_group_value_kv(self, group_title: str, label_text: str):
        """
        Retrieve the currently selected value from a group combo box.
        """
        return self.group_controls1[group_title][label_text].currentText()
    
    def output_win(self):
        page = QWidget()

        # === MAIN LAYOUT ===
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # ---------- Log View with Centered Watermark ----------
        self.log_view = WatermarkedLogView("Nectar-X-Studio")
        layout.addWidget(self.log_view)

        self.output_area = QPlainTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet("""
            QPlainTextEdit {
                background-color: transparent;
                color: #e8e8e8;
                padding: 12px;
                border-radius: 10px;
                font-family: Consolas, monospace;
                font-size: 13px;
            }
            """)

        #layout.addWidget(self.output_area)
        self.stdout_stream = EmittingStream()
        self.stdout_stream.text_written.connect(self.append_output)
        sys.stdout = self.stdout_stream
        sys.stderr = self.stdout_stream
        page.setLayout(layout)
        return page

    def append_output(self, text):
        #self.output_area.appendPlainText(text.rstrip())
        self.log_view.append(text.rstrip())
    

    def create_settings_page(self):
        self.set_light_theme()
        self.settings = QSettings('Zashiron', 'Nectar_File')
        page = QWidget()
        # === MAIN LAYOUT ===
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # === SLIDERS SECTION ===
        sliders_layout = QFormLayout()
        sliders_layout.setSpacing(20)

        def add_slider(key, name, slider, label, min_val, max_val, default_val, formatter=str):
            slider.setOrientation(Qt.Orientation.Horizontal)
            slider.setRange(min_val, max_val)
            start_val = int(self.settings.value(key, default_val))
            slider.setValue(start_val)
            label.setText(formatter(start_val))
            label.setMinimumWidth(40)
            slider.valueChanged.connect(
                lambda val: (
                    label.setText(formatter(val)),
                    self.settings.setValue(key, val)
                )
            )
            h_layout = QHBoxLayout()
            h_layout.setSpacing(12)
            h_layout.addWidget(slider)
            h_layout.addWidget(label)

            container = QWidget()
            container.setStyleSheet('background-color: #ffffff; color: #000000; border-radius: 18px;')
            container.setLayout(h_layout)
            sliders_layout.addRow(f'{name}:', container)

        # === SECTION TITLE ===
        title_label = QLabel('<h3>⚙️ Settings</h3>')
        title_label.setFixedHeight(50)
        title_label.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                font-size: 18px;
                font-weight: bold;
                color: #000000;
                padding: 8px 16px;
                border-radius: 8px;
            }
        """)
        sliders_layout.addRow(title_label)

        # === SLIDERS ===

        def get_gpu_count():
            try:
                return torch.cuda.device_count() or 0
            except Exception:
                return 0

        self.main_gpu_label = QLabel()
        self.main_gpu = QSlider()
        add_slider('main_gpu', 'Main GPU', self.main_gpu, self.main_gpu_label, 0, 0, 0)

        gpu_count = get_gpu_count()
        if gpu_count <= 1:
            self.main_gpu.setRange(0, 0)
            self.main_gpu.setEnabled(False)
            self.main_gpu_label.setText("(only one GPU available)")
        else:
            self.main_gpu.setRange(0, gpu_count - 1)
            self.main_gpu.setEnabled(True)
            self.main_gpu_label.setText(f"{gpu_count - 1}")

        self.max_tokens_label = QLabel()
        self.max_tokens = QSlider()
        add_slider('max_tokens', 'Max Tokens', self.max_tokens, self.max_tokens_label, 10, 10000, 248)

        self.context_size_label = QLabel()
        self.context_size = QSlider()
        add_slider('context_size', 'Context Size', self.context_size, self.context_size_label, 512, 131072, 4096)

        self.batch_size_label = QLabel()
        self.batch_size = QSlider()
        add_slider('batch_size', 'Batch Size', self.batch_size, self.batch_size_label, 512, 65536, 512)

        self.thread_num_label = QLabel()
        self.thread_num = QSlider()
        add_slider('thread_num', 'Threads', self.thread_num, self.thread_num_label, 0, 32, 4)

        self.gpu_layer_label = QLabel()
        self.gpu_layer = QSlider()
        add_slider('gpu_layer', 'GPU Layers', self.gpu_layer, self.gpu_layer_label, 0, 32, 1)

        self.seed_label = QLabel()
        self.seed = QSlider()
        add_slider('seed', 'Seed', self.seed, self.seed_label, -1, 9999, -1)

        self.temperature_label = QLabel()
        self.temperature = QSlider()
        add_slider('temperature', 'Temperature', self.temperature, self.temperature_label, 0, 100, 0, lambda v: f'{v / 100:.2f}')

        # === KV CACHE TYPE DROPDOWN ===
        self.kv_cache_group = self.create_group_kv(
            'KV Cache Type',
            [('Select Type', [
                'q8_0',     # 8-bit quantized (default, good balance)
                'q4_0',     # 4-bit quantized (lower VRAM)
                'f16',      # 16-bit float (highest quality, most VRAM)
                'f32',      # 32-bit float (max quality, max VRAM)
                'auto'      # Let llama.cpp choose
            ])]
        )

        kv_combo = self.group_controls1['KV Cache Type']['Select Type']
        saved_cache_type = QSettings('Zashiron', 'Nectar-X-Studio').value('kv_cache_dtype', 'q8_0')
        index = kv_combo.findText(saved_cache_type)
        if index >= 0:
            kv_combo.setCurrentIndex(index)

        kv_combo.currentTextChanged.connect(
            lambda value: QSettings('Zashiron', 'Nectar-X-Studio').setValue('kv_cache_dtype', value)
        )

        # === CHAT TEMPLATE DROPDOWN (Expanded) ===
        self.chat_template_group = self.create_group(
            'Chat Template',
            [('Select Template', [
                'chatml',           # OpenAI ChatML (default, most compatible)
                'llama-2',          # Meta Llama 2/3
                'llama-3',          # Llama 3 (newer)
                'mistral-instruct', # Mistral Instruct
                'mistral-nemo',     # Mistral Nemo
                'zephyr',           # HuggingFace Zephyr
                'openchat',         # OpenChat
                'qwen2',            # Qwen2 (your model!) [memory:8]
                'phi-3',            # Microsoft Phi-3
                'gemma-2',          # Google Gemma 2
                'qwen',             # Original Qwen
                'mixtral',          # Mixtral 8x7B
                'command-r',        # Cohere Command-R
                'None'              # Raw (no template)
            ])]
        )

        combo = self.group_controls['Chat Template']['Select Template']
        saved_template = QSettings('Zashiron', 'Nectar-X-Studio').value('chat_template', 'qwen2')  # Qwen2 default
        index = combo.findText(saved_template)
        if index >= 0:
            combo.setCurrentIndex(index)
        combo.currentTextChanged.connect(
            lambda value: QSettings('Zashiron', 'Nectar-X-Studio').setValue('chat_template', value)
        )

        # === SIDEBAR CHECKBOXES ===
        sidebar = QVBoxLayout()
        sidebar.setSpacing(10)
        sidebar.setContentsMargins(15, 15, 15, 15)

        def add_checkbox(key, text, default_checked):
            checkbox = QCheckBox(text)
            checked = self.settings.value(key, 'true' if default_checked else 'false') == 'true'
            checkbox.setChecked(checked)
            checkbox.setStyleSheet("""
                QCheckBox {
                    font-size: 13px;
                    font-weight: 500;
                    spacing: 10px;
                }
                QCheckBox::indicator {
                    width: 16px;
                    height: 16px;
                }
            """)
            checkbox.stateChanged.connect(lambda state: self.settings.setValue(key, checkbox.isChecked()))
            sidebar.addWidget(checkbox)
            return checkbox

        self.use_mlock = add_checkbox('use_mlock', 'Use Memory Lock (mlock)', False)
        self.use_verbose = add_checkbox('use_verbose', 'Enable Verbose Logging', False)
        self.use_low_ram = add_checkbox('use_low_ram', 'Enable Low Ram', False)
        self.KV_cache = add_checkbox('kv_cache', 'Enable Kv cache', False)
        self.flash_attn = add_checkbox('flash_attn', 'Enable Flash Attention', False)
        self.qmmog = add_checkbox('qmmog', 'Enable Quantized Matrix Multiply', False)

        self.offload_kqv = add_checkbox('offload_kqv', 'Enable Offload Kqv', False)
        self.logits_all = add_checkbox('logits_all', 'Enable Token Inspection', False)
        self.embedding = add_checkbox('embedding', 'Enable Embedding Mode', False)
        self.cont_batching = add_checkbox('cont_batching', 'Enable Continuous Batching', False)
        self.log_disable = add_checkbox('log_disable', 'Disable Llama.Cpp Logs', True)

        self.use_numa = add_checkbox('use_numa', 'Enable NUMA', True)
        self.use_mmap = add_checkbox('use_mmap', 'Enable Memory Map', True)
        self.use_mmap_backend = add_checkbox('use_mmap_backend', 'Use mmap backend', True)

        sidebar_frame = QFrame()
        sidebar_frame.setLayout(sidebar)
        sidebar_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border: 1px solid #ccc;
                border-radius: 10px;
            }
        """)

        # === INFO CARD ===
        info_card = QFrame()
        #info_card.setFixedHeight(120)
        info_card.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 12px;
                padding: 16px;
            }
            QLabel {
                color: #333;
                font-size: 13px;
            }
        """)
        info_layout = QVBoxLayout()
        info_layout.setSpacing(8)

        def get_llama_version():
            try:
                import llama_cpp
                return llama_cpp.__version__
            except Exception:
                return 'Unavailable'

        def get_gpu_info():
            """Get GPU name and CUDA version"""
            try:
                if torch.cuda.is_available():
                    gpu_name = torch.cuda.get_device_name(0)
                    cuda_version = torch.version.cuda
                    return f"GPU: {gpu_name} (CUDA: {cuda_version})"
                else:
                    return "GPU: Back-end Runtime Missing (CPU only)"
            except Exception:
                return "GPU: Unknown"
            
        def get_llama_build_flags():
            """Extract build flags from llama.cpp system info"""
            try:
                import llama_cpp as cpp
                info = cpp.llama_print_system_info()
                info_str = info.decode() if isinstance(info, bytes) else str(info)
                # Look for GPU/CUDA flags
                flags = []
                if "CUDA = 1" in info_str or "cuBLAS = 1" in info_str:
                    flags.append("CUDA")
                if "AVX2 = 1" in info_str:
                    flags.append("AVX2")
                if "F16C = 1" in info_str:
                    flags.append("F16C")
                if "OPENMP = 1" in info_str:
                    flags.append("OpenMP")
                return ", ".join(flags) if flags else "CPU Only"
            except Exception:
                return "Not Available"

        def get_runtime_mode():
            try:
                import llama_cpp as cpp

                info = cpp.llama_print_system_info()
                info = info.decode() if isinstance(info, bytes) else str(info)
                info_upper = info.upper()

                # NVIDIA
                if 'CUDA' in info_upper:
                    return 'GPU (NVIDIA CUDA)'

                # Apple
                if 'METAL' in info_upper:
                    return 'GPU (Apple Metal)'

                # AMD (Linux ROCm / HIP)
                if 'ROCM' in info_upper or 'HIP' in info_upper:
                    return 'GPU (AMD Radeon - ROCm)'

                # AMD / Cross-vendor (Windows/Linux Vulkan)
                if 'VULKAN' in info_upper:
                    return 'GPU (AMD Radeon - Vulkan)'

                # CPU optimized paths
                if any(x in info_upper for x in ['OPENBLAS', 'AVX', 'AVX2', 'AVX512', 'FMA']):
                    return 'CPU (Optimized)'

                return 'CPU (Basic)'

            except Exception:
                return 'Unknown'

        # Updated info layout
        engine_type = QLabel('Engine: Zashir K47B-LS5')
        llama_version = QLabel(f'LLAMA.cpp Version: {get_llama_version()}')
        runtime_mode = QLabel(f'Runtime Mode: {get_runtime_mode()}')
        gpu_info = QLabel(get_gpu_info())  # NEW: GPU + CUDA
        self.build_flags = QLabel(f'Engine Flags: {get_llama_build_flags()}')  # ENHANCED
        self.build_flags_label = QLabel('Build Flags: Not Available')

        info_layout.addWidget(engine_type)
        info_layout.addWidget(llama_version)
        info_layout.addWidget(runtime_mode)
        info_layout.addWidget(gpu_info)      # NEW LINE
        info_layout.addWidget(self.build_flags)
        info_layout.addWidget(self.build_flags_label)
        info_card.setLayout(info_layout)

        # === RIGHT PANEL ===
        right_panel = QVBoxLayout()
        right_panel.setSpacing(20)
        right_panel.addLayout(sliders_layout)
        right_panel.addWidget(info_card)
        right_panel.addWidget(self.kv_cache_group)
        right_panel.addWidget(self.chat_template_group)
        right_panel.addStretch()

        # === COMBINE EVERYTHING ===
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        # Wrap the sidebar and right panel in a container if both are used
        container_widget = QWidget()
        container_layout = QHBoxLayout(container_widget)
        container_layout.setContentsMargins(20, 20, 20, 20)
        container_layout.setSpacing(18)

        # Add sidebar and right panel (uncomment whichever you need)
        container_layout.addWidget(sidebar_frame)
        container_layout.addLayout(right_panel)

        scroll.setWidget(container_widget)

        # Apply custom scrollbar styles
        scroll.setStyleSheet("""
            /* Vertical Scrollbar */
            QScrollBar:vertical {
                background: transparent;
                width: 8px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:vertical {
                background: #ffffff;
                min-height: 20px;
                border-radius: 4px;
            }

            QScrollBar::handle:vertical:hover {
                background: rgba(0, 0, 0, 0.2);
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical,
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
                height: 0px;
                border: none;
            }

            /* Horizontal Scrollbar */
            QScrollBar:horizontal {
                background: transparent;
                height: 8px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:horizontal {
                background: #ffffff;
                min-width: 20px;
                border-radius: 4px;
            }

            QScrollBar::handle:horizontal:hover {
                background: rgba(0, 0, 0, 0.4);
            }

            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal,
            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: none;
                width: 0px;
                border: none;
            }
        """)

        # Add scroll area to main layout
        main_layout.addWidget(scroll)
        page.setLayout(main_layout)

        return page


    def update_build_flags_label(self, llm_instance):
        if hasattr(self, 'build_flags_label'):
            flags = self.get_build_flags(llm_instance)
            self.build_flags_label.setText(f'Build Flags: {flags}')

    def get_build_flags(self, llm_instance):
        flags = []
        if getattr(llm_instance, 'use_mlock', False):
            flags.append('mlock')
        if getattr(llm_instance, 'use_mmap', False):
            flags.append('mmap')
        if getattr(llm_instance, 'numa', False):
            flags.append('NUMA')
        if getattr(llm_instance, 'verbose', False):
            flags.append('Verbose')
        if flags:
            return ', '.join(flags)

    def set_light_theme(self):
        """Set light (Chrome-like) theme for the application.""" 
        light_stylesheet = """
            QWidget{
                background-color: transparent;
            }
            QCheckBox {
                spacing: 8px;
                border-radius: 10px;
                background-color: #ffffff;
                font-size: 14px;
                color: #000000;
                padding: 5px;
            }

            QLabel {
                border-radius: 5px;
                background-color: #000000;
                padding: 10px;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 4px;
                background: #444;
                border: 1px solid #888;
            }

            QCheckBox::indicator:checked {
                background-color: #ffb700;
                border: 1px solid #ffb700;
            }

            QCheckBox::indicator:unchecked {
                background-color: #222;
                border: 1px solid #666;
            }

            QCheckBox:hover {
                color: #00bfff;
            }

            QSlider::groove:horizontal {
                height: 6px;
                background: #353535;
                margin: 2px 0;
                border-radius: 3px;
            }

            QSlider::handle:horizontal {
                background: #1E90FF;
                width: 14px;
                height: 14px;
                margin: -4px 0;
                border-radius: 7px;
            }

            QLineEdit, QTextEdit, QPlainTextEdit {
                background-color: #2a2c31;
                color: #ffffff;
                border: none;
                padding: 5px;
                border-radius: 10px;
            }

            QListWidget {
                background-color: #3c3f41;
                color: #d3d3d3;
                border: 1px solid #444444;
            }

            QGroupBox {
                background-color: #ffffff;
                color: #000000;
                margin: 5px;
                padding: 10px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;  /* can be left, right, center */
                padding: 0 10px;
                color: #000000;
                font-size: 16px;
                font-weight: bold;
                background-color: #ffffff;
                border-radius: 6px;
            }

            QFormLayout {
                background-color: #2b2b2b;
                color: #d3d3d3;
            }

            /* Vertical Scrollbar */
            QScrollBar:vertical {
                background: transparent;
                width: 8px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:vertical {
                background: rgba(0, 0, 0, 0.2);
                min-height: 20px;
                border-radius: 4px;
            }

            QScrollBar::handle:vertical:hover {
                background: rgba(0, 0, 0, 0.4);
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical,
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
                height: 0px;
                border: none;
            }

            /* Horizontal Scrollbar */
            QScrollBar:horizontal {
                background: transparent;
                height: 8px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:horizontal {
                background: rgba(0, 0, 0, 0.2);
                min-width: 20px;
                border-radius: 4px;
            }

            QScrollBar::handle:horizontal:hover {
                background: rgba(0, 0, 0, 0.4);
            }

            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal,
            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: none;
                width: 0px;
                border: none;
            }
            """

        self.setStyleSheet(light_stylesheet)

    def update_max_tokens(self, value):
        self.max_tokens_label.setText(f'Max Token: {value}')

    def update_context_size(self, value):
        self.context_size_label.setText(f'Context Size: {value}')

    def update_batch_size(self, value):
        self.batch_size_label.setText(f'Batch Size: {value}')

    def update_thread_num(self, value):
        self.thread_num_label.setText(f'Thread: {value}')

    def update_gpu_layer(self, value):
        self.gpu_layer_label.setText(f'GPU_Layer: {value}')

    def update_temperature(self, value):
        self.temperature_label.setText(f'Temperature: {value / 100:.2f}')

    def rag_util(self):
        self.load_document_ui()

    def load_document_ui(self):
        # Open file dialog
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Document", "", "Text Files (*.txt);;All Files (*)"
        )

        if not file_path:
            return  # User canceled

        # Read the document
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to read file: {e}")
            return

        # Add to RAG engine
        if not hasattr(self, "rag_engine"):
            QMessageBox.warning(self, "RAG Not Ready", "Start the LLM server first.")
            return

        self.rag_engine.add_documents([content])
        QMessageBox.information(self, "Document Added", f"{os.path.basename(file_path)} added to RAG.")

    #def load_web_document_ui(self):
    #    from PyQt6.QtWidgets import QInputDialog, QMessageBox
#
    #    query, ok = QInputDialog.getText(self, "Web Search Document", "Enter search query:")
    #    if not ok or not query.strip():
    #        return
#
    #    if not hasattr(self, "rag_engine"):
    #        QMessageBox.warning(self, "RAG Not Ready", "Start the LLM server first.")
    #        return
    #    
    #    #API_KEY = "AIzaSyD4Au69N-YV36kXA3g1YQcD-n55jpFf6Y8"
    #    #CX = "028c5f61bafcb4194"
#
    #    web_rag = WebRAG(self.rag_engine)
    #    web_rag.add_web_docs(query, num_results=5)
#
    #    QMessageBox.information(self, "Web Docs Added", f"Documents from web search added to RAG.")

    def web_view(self):
        # Prevent reopening multiple times
        if hasattr(self, "web_widget") and self.web_widget.isVisible():
            return

        # Create a small internal settings widget
        self.web_widget = QWidget(self)
        self.web_widget.setWindowTitle(" ")
        self.web_widget.setFixedSize(800, 620)
        self.web_widget.setWindowFlags(Qt.WindowType.Dialog)
        #self.web_widget.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        #self.web_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.web_widget.setStyleSheet("""
            QWidget {
                background-color: #000000;
                border: trabsparent;
                border-radius: 12px;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
            QPushButton {
                background-color: #3c3c3c;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QCheckBox {
                color: white;
                font-size: 13px;
            }
        """)

        layout = QVBoxLayout(self.web_widget)
        #layout.setContentsMargins(15, 15, 15, 15)

        # Web View
        self.web_viewer = QWebEngineView(self.web_widget)
        self.web_viewer.setUrl(QUrl("https://search.brave.com/")) 
        self.web_viewer.setStyleSheet("""
            background: transparent;
            border-radius: 10px;
        """)

        self.web_viewer.settings().setAttribute(
            self.web_viewer.settings().WebAttribute.JavascriptEnabled, True
        )
        self.web_viewer.settings().setAttribute(
            self.web_viewer.settings().WebAttribute.LocalStorageEnabled, True
        )

        layout.addWidget(self.web_viewer)

        # Position it at the center of the main window
        parent_rect = self.geometry()
        x = parent_rect.x() + (parent_rect.width() - self.web_widget.width()) // 8
        y = parent_rect.y() + (parent_rect.height() - self.web_widget.height()) // 2
        self.web_widget.move(680, y)

        # Fade-in animation
        self.web_widget.setWindowOpacity(0.0)
        self.web_widget.show()

        fade_in = QPropertyAnimation(self.web_widget, b"windowOpacity")
        fade_in.setDuration(600)
        fade_in.setStartValue(0.0)
        fade_in.setEndValue(1.0)
        fade_in.setEasingCurve(QEasingCurve.Type.InOutQuad)
        fade_in.start()

        # Keep reference so animation doesn’t get garbage collected
        self.fade_in_animation = fade_in

    def fade_out_settings(self):
        if not hasattr(self, "web_widget") or not self.web_widget.isVisible():
            return

        fade_out = QPropertyAnimation(self.web_widget, b"windowOpacity")
        fade_out.setDuration(600)
        fade_out.setStartValue(1.0)
        fade_out.setEndValue(0.0)
        fade_out.setEasingCurve(QEasingCurve.Type.InOutQuad)
        fade_out.finished.connect(self.web_widget.close)
        fade_out.start()

        # Keep reference alive
        self.fade_out_animation = fade_out

    def setup_model_watcher(self):
        """Initializes the folder watcher for NectarHub.""" 
        self.model_watcher = QFileSystemWatcher()
        nectarhub_path = self.ensure_nectarhub_folder()
        if nectarhub_path:
            self.model_watcher.addPath(nectarhub_path)
            self.model_watcher.directoryChanged.connect(self.load_model)

    def find_path(self, name: str):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, name), os.path.abspath(os.path.join(script_dir, os.pardir, name)), os.path.expanduser(f'~/{name}'), os.path.normpath(f'C:/Program Files/{name}')]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:
            return None

    def stop_lay(self):
        if hasattr(self, 'overlay') and self.overlay is not None and self.overlay.isWidgetType():
            self.overlay.setVisible(False)

    def ensure_nectarhub_folder(self):
        program_files = os.environ.get('ProgramFiles', 'C:\\Program Files')
        nectarhub_path = os.path.join(program_files, 'NectarHub')
        try:
            if not os.path.exists(nectarhub_path):
                import ctypes
                if ctypes.windll.shell32.IsUserAnAdmin():
                    os.makedirs(nectarhub_path, exist_ok=True)
                else:
                    QMessageBox.warning(self, 'Administrator Required', 'You need administrator privileges to create a folder in Program Files.')
                    return
            return nectarhub_path
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Could not create/access \'NectarHub\' folder:\n{str(e)}')
            return None

    def load_model(self):
        nectarhub_path = self.ensure_nectarhub_folder()
        if not nectarhub_path:
            return
        gguf_models = []
        try:
            for root, _, files in os.walk(nectarhub_path):
                for file in files:
                    if file.lower().endswith('.gguf'):
                        gguf_models.append((file, os.path.join(root, file)))
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error while scanning for models:\n{str(e)}')
            return

        gguf_models.append(("Load External Model", "custom_path"))

        # Create popup if not already
        if not hasattr(self, "model_popup"):
            self.model_popup = ModelListPopup(self)
        
        self.model_popup.populate(gguf_models, self.model_selected_popup)
        self.model_popup.show_popup(self.label_model_path)

    def model_selected_popup(self, path):
        if path == "custom_path":
            file_path, _ = QFileDialog.getOpenFileName(
                self, "Select GGUF Model", "", "GGUF Files (*.gguf);;All Files (*)"
            )
            if file_path:
                self.loaded_model_path = file_path
                self.settings1.setValue("models/last_used_path", self.loaded_model_path)
                self.label_model_path.setText(os.path.basename(file_path))
                self.start_server()
        else:
            self.loaded_model_path = path
            self.settings1.setValue("models/last_used_path", path)
            self.label_model_path.setText(os.path.basename(path))
            self.start_server()

    def auto_run(self):
        """Reloads the last used model from QSettings if it exists."""
        last_path = self.settings1.value('models/last_used_path', '')
        if last_path and os.path.exists(last_path):
            self.loaded_model_path = last_path
            self.label_model_path.setText(os.path.basename(last_path))
            self.start_server()
        else:
            QMessageBox.information(self, 'Auto Run', 'No previously loaded model found or file no longer exists.')

    def start_server(self):
        if not self.loaded_model_path:
            QMessageBox.warning(self, 'Error', 'Please load a GGUF model first.')
            return
        if self.llm_server_thread is not None and self.llm_server_thread.is_alive():
            QMessageBox.information(self, 'Engine', 'Engine is already running.')
            return
        self.overlay.setVisible(True)
        self.llm_server_thread = threading.Thread(target=self.start_llm_server, daemon=True)
        self.llm_server_thread.start()

    #QApplication.processEvents()  # refresh UI
    def start_llm_server(self):
        if Llama is None:
            Notify(f"llama-cpp-python is not installed.", parent=self)
            QMessageBox.information(self, 'llama-cpp-python', 'llama-cpp-python is not installed.')
            return
        
        # Initialize RAG engine
        self.rag_engine = RAGEngine()
        #self.rag_engine.add_documents([sys_msgs.assistant_msg])
        try:
            n_ubatch = auto_batch_sizes()
            main_gpu_count = self.main_gpu.value()
            seed = self.seed.value()
            ctx_value = self.context_size.value()
            thread_value = self.thread_num.value()
            gpu_layer_amount = self.gpu_layer.value()
            use_mem_lock = self.use_mlock.isChecked()
            use_verbose = self.use_verbose.isChecked()
            use_low_ram = self.use_low_ram.isChecked()
            KV_cache = self.KV_cache.isChecked()
            qmmog = self.qmmog.isChecked()
            use_numa = self.use_numa.isChecked()
            use_mmap_activate = self.use_mmap.isChecked()
            use_mmap_active = self.use_mmap_backend.isChecked()
            flas_attn = self.flash_attn.isChecked()

            offload = self.offload_kqv.isChecked()
            logits = self.logits_all.isChecked()
            embed = self.embedding.isChecked()
            batching = self.cont_batching.isChecked()
            logs = self.log_disable.isChecked()

            btx_value = self.batch_size.value()
            chat_format_selected = self.get_group_value('Chat Template', 'Select Template')
            kv_cache_dtype_selected = self.get_group_value_kv('KV Cache Type', 'Select Type')

            self.llm_instance = Llama(
                model_path=self.loaded_model_path, 
                n_ctx=ctx_value, 
                chat_format=chat_format_selected,
                n_threads=thread_value, 
                n_gpu_layers=gpu_layer_amount,
                use_mlock=use_mem_lock, 
                verbose=use_verbose, 
                numa=use_numa,
                mmap=use_mmap_activate, 
                use_mmap=use_mmap_active, 
                n_batch=btx_value,
                main_gpu=main_gpu_count,
                #tensor_split=None,
                f16_kv=KV_cache,
                kv_cache_dtype=kv_cache_dtype_selected,
                low_vram=use_low_ram,
                flash_attn=flas_attn,
                mul_mat_q=qmmog,
                #n_ubatch=n_ubatch,
                offload_kqv=offload,
                #split_mode=1,
                seed=seed,
                logits_all=logits,
                embedding=embed,
                cont_batching=batching,
                #defrag_thold=0.1,
                #last_n_tokens_size=64,
                log_disable=logs,
                )
            
            self.update_build_flags_label(self.llm_instance)
            
            import mmap
            import struct
            # -----------------------------
            # Fast in-memory conversation buffer
            # -----------------------------
            self.memory_size = 2 * 1024 * 1024  # 2 MB buffer
            self.memory = mmap.mmap(-1, self.memory_size)
            self.memory_offset = 0
            self.memory_lock = threading.Lock()
            self.memory_full = False

            import socket
            self.server_running = True
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind(('127.0.0.1', 5005))
            self.server.listen(5)

            while self.server_running:
                try:
                    client, _ = self.server.accept()
                except OSError:
                    break  # server closed, exit loop safely
                threading.Thread(target=self.handle_client, args=(client,), daemon=True).start()

        except Exception as e:
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="Engine Error ⚠️",
                msg=f"{e}",
                icon=find_icon('background/NectarX.png'),  
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()
            self.stop_lay()
            self.label_model_path.setText("Click to load Model")
    
    # -----------------------------
    # Efficient ring-buffer operations
    # -----------------------------
    def append_message(self, role, content):
        msg = f"{role}:{content}".encode('utf-8')
        total_size = 4 + len(msg)

        with self.memory_lock:
            # Wrap if memory is full
            if self.memory_offset + total_size > self.memory_size:
                self.memory_offset = 0
                self.memory_full = True

            # Write message length and content in one block
            self.memory[self.memory_offset:self.memory_offset+4] = struct.pack('I', len(msg))
            end_offset = self.memory_offset + 4
            self.memory[end_offset:end_offset+len(msg)] = msg
            self.memory_offset += total_size


    def read_all_messages(self):
        messages = []

        # Only read memory buffer; do not touch GUI
        with self.memory_lock:
            read_from = 0 if not self.memory_full else self.memory_offset
            available = self.memory_size if self.memory_full else self.memory_offset

            ptr = read_from
            while ptr < available:
                if ptr + 4 > self.memory_size:
                    break  # incomplete length field at end
                msg_len = struct.unpack('I', self.memory[ptr:ptr+4])[0]
                ptr += 4
                if msg_len <= 0 or ptr + msg_len > self.memory_size:
                    break

                msg_data = self.memory[ptr:ptr+msg_len]
                ptr += msg_len

                try:
                    decoded = msg_data.decode('utf-8')
                    if ':' in decoded:
                        role, content = decoded.split(':', 1)
                        messages.append({'role': role, 'content': content})
                except UnicodeDecodeError:
                    continue

        return messages
    
    # -----------------------------
    # Updated client handler
    # -----------------------------
    def handle_client(self, client_socket):
        self.stop_lay()
        AUTH_KEY = "NEC-892657"

        try:
            data = client_socket.recv(8192).decode('utf-8').strip()
            if not data:
                # client may already be gone; best effort send, then return
                try:
                    client_socket.send(b'No data received')
                except OSError:
                    pass
                return

            if not data.startswith(AUTH_KEY):
                try:
                    client_socket.send(b"Unauthorized")
                except OSError:
                    pass
                return

            data = data[len(AUTH_KEY):].strip()

            if data.startswith('LOAD_MODEL::'):
                self.append_message('user', data)
                try:
                    client_socket.send(b'OK')
                except OSError:
                    pass
                return

            # ---------------- CORE LOGIC ----------------
            self.append_message('user', data)

            query = data
            conversation_list = self.read_all_messages()
            conversation_list.insert(0, sys_msgs.NORMAL_SYSTEM_PROMPT)

            if hasattr(self, "rag_engine"):
                retrieved_docs = self.rag_engine.retrieve(data)
                for doc in retrieved_docs:
                    conversation_list.append(
                        {"role": "system", "content": f"[Context] {doc}"}
                    )

            use_web = model_decides_web_rag(self.llm_instance, query)

            if use_web:
                search_query = query_generator(query)
                search_query = search_query.strip().strip('"')

                toast = Notification(
                    app_id="Nectar-X-Studio",
                    title="AI Auto-Generated WebRAG Query",
                    msg=f"Search Query → {search_query}",
                    icon=find_icon('background/NectarX.png'),
                    duration="short"
                )
                toast.set_audio(audio.SMS, loop=False)
                toast.show()

                conversation_list.insert(0, WEB_RAG_SYSTEM_PROMPT)

                web_rag = WebRAG(self.rag_engine)
                web_rag.add_web_docs(search_query, num_results=10, recent="d7")

                web_docs = self.rag_engine.retrieve(search_query, top_k=10)
                for doc in web_docs:
                    conversation_list.append({
                        "role": "system",
                        "content": f"[Web Context]\n{doc}"
                    })

            # ---------- STREAMING REPLY ----------
            stream = self.llm_instance.create_chat_completion(
                conversation_list,
                max_tokens=self.max_tokens.value(),
                temperature=self.temperature.value() / 100,
                stream=True,
            )

            full_reply = []

            for chunk in stream:
                delta = chunk["choices"][0]["delta"]
                if "content" in delta:
                    token = delta["content"]
                    full_reply.append(token)
                    try:
                        client_socket.sendall(token.encode("utf-8"))
                    except OSError:
                        # client disconnected → stop streaming immediately
                        return

            # 🔥 SEND END MARKER (ONCE, CLEAN)
            try:
                client_socket.sendall(b"<<END_OF_RESPONSE>>")
            except OSError:
                return

            reply = "".join(full_reply).strip()
            if reply:
                self.append_message("assistant", reply)

        except Exception as e:
            print(f"[handle_client] unexpected error: {e}")

        finally:
            try:
                client_socket.shutdown(socket.SHUT_WR)  # 👈 important
            except OSError:
                pass
            client_socket.close()

    def terminate(self):
        """Terminate the server and clean up resources."""
        try:
            if self.llm_server_thread and self.server:
                self.server_running = False
                try:
                    # Forcefully unblock accept() by connecting once
                    import socket
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect(('127.0.0.1', 5005))
                        s.close()
                except Exception:
                    pass

                self.server.close()
                self.llm_server_thread = None

            self.loaded_model_path = None
            self.label_model_path.setText('No model selected')
            self.llm_instance = None
            self.output_area.clear()
            Notify(f"🚀 Engine Stopped", parent=self)
        except Exception as e:
            Notify(f"❌ Error during termination: {e}", parent=self)

    def setup_overlay(self):
        # Create the semi-transparent overlay
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        self.overlay.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.overlay.setVisible(False)

        # Main overlay layout (centers contents)
        overlay_layout = QVBoxLayout(self.overlay)
        overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Sub-layout for loader + text side by side
        sublay = QHBoxLayout()
        sublay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sublay.setSpacing(15)

        # Loader widget
        self.loader = Loader_chat()
        self.loader.setFixedSize(150, 150)
        self.loader.setVisible(True)
        self.loader.setStyleSheet("""
            background-color: #ffffff;
            color: #E0E0E0;
            padding: 10px;
            border-radius: 10px;
        """)

        # Loading text
        self.text = QLabel("🚧 Loading Model! Please Wait. 🚧")
        self.text.setStyleSheet("""
            background-color: transparent;
            color: #ffffff;
            font-size: 20px;
            padding: 10px;
            border-radius: 5px;
        """)
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text.setVisible(True)

        # Add both to the sublayout
        sublay.addWidget(self.loader)
        sublay.addWidget(self.text)

        # Add sublayout to main layout
        overlay_layout.addLayout(sublay)

    def resizeEvent(self, event):
        """Ensure overlay resizes with the main window."""
        self.overlay.setGeometry(self.rect())
        super().resizeEvent(event)

    def last_func(self):
        self.overlay.setVisible(False)