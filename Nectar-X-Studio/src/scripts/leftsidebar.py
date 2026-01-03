import socket

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt, QTimer, QSize, QPropertyAnimation, QRect

from PyQt6.QtGui import QIcon

from scripts.components.Service.find_icon import find_icon
from scripts.components.WidgetBased.AnimatedDot import AnimatedDot

#--------------------------------------------------------------------------------
# Main App Logic
#--------------------------------------------------------------------------------

class LeftSidebar(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowOpacity(1.0)
        self.stacked_widget.currentChanged.connect(self.update_indicator)
        self.setFixedWidth(72)
        self.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.2, y2:1, stop:0 #0f0f0f, stop:1 #111010);")
        # --- Sidebar Layout ---
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(16, 8, 8, 8)
        self.layout.setSpacing(12)

        icon_path1 = find_icon("background/main.png")
        icon_path2 = find_icon("menu/sys.png")
        icon_path3 = find_icon("menu/broadcast.png")
        icon_path4 = find_icon("menu/download.png")
        icon_path5 = find_icon("menu/update.png")
        icon_path6 = find_icon("menu/plugin.png")

        # --- Icons ---
        self.icons = {
            "Landing": f"{icon_path1}",
            "Test Lab": f"{icon_path2}",
            "Broadcast": f"{icon_path3}",
            "Model Downloader": f"{icon_path4}",
            "Update": f"{icon_path5}",
            "Plugin": f"{icon_path6}",
        }

        self.labels = []

        for i, (name, icon_path) in enumerate(self.icons.items()):
            icon = QIcon(icon_path)
            lbl = QLabel()
            lbl.setPixmap(icon.pixmap(QSize(56, 56)))
            lbl.setFixedSize(56, 56)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setStyleSheet("""
                background: transparent;
                border-radius: 12px;
            """)
            lbl.mousePressEvent = lambda event, idx=i: self.switch_page(idx)
            self.layout.addWidget(lbl)
            self.labels.append(lbl)

        self.layout.addStretch()

        # --- Indicator Bar ---
        self.indicator = QFrame(self)
        self.indicator.setFixedWidth(4)
        self.indicator.setFixedHeight(60)
        self.indicator.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 #ffffff, stop:1 #ffffff
            );
            border-radius: 12px;
        """)
        self.indicator.show()

        # --- Animation ---
        self.anim = QPropertyAnimation(self.indicator, b"geometry", self)
        self.anim.setDuration(250)

        # Initialize position
        self.current_index = 0
        self.update_indicator(0)

        self.layout.addStretch()

        # Animated dot (status indicator)
        self.dot = AnimatedDot()
        self.dot.setFixedSize(50, 50)
        self.dot.setToolTip("Online Model Status")
        self.dot.setStyleSheet("""
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
        self.layout.addWidget(self.dot, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setup_timers()

    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
        self.update_indicator(index)

    def update_indicator(self, index):
        if index < 0 or index >= len(self.labels):
            return

        target_label = self.labels[index]
        label_pos = target_label.pos()
        label_height = target_label.height()

        x_offset = 4  # places it slightly to the left
        self.anim.stop()
        self.anim.setStartValue(self.indicator.geometry())
        self.anim.setEndValue(QRect(
            x_offset,
            label_pos.y(),
            self.indicator.width(),
            label_height
        ))
        self.anim.start()
        self.current_index = index

    def setup_timers(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_server)
        self.timer.start(3000)
        self.check_server()

    def check_server(self):
        is_active = self.ping("127.0.0.1", 5005)
        self.dot.set_active(is_active)

    def ping(self, host, port, timeout=0.5):
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False