import os
import subprocess
import psutil
import base64
import threading

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton, QLineEdit, QMessageBox, QCheckBox, QHBoxLayout, QFrame, QScrollArea, QGroupBox, QMenu
from PyQt6.QtCore import Qt, QTimer, QSize, QPropertyAnimation, QEasingCurve, QVariantAnimation
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPainter, QPainterPath, QColor, QAction, QPalette

import psutil

from PyQt6.QtCore import QSettings
from winotify import Notification, audio
from email.mime.text import MIMEText
from googleapiclient.discovery import build

from scripts.components.Card import Card
from scripts.components.Service.find_icon import find_icon
from scripts.components.WidgetBased.Notify import Notify
from scripts.components.Utility.write_to_log import write_to_log
from scripts.components.GoogleAuth.GoogleAuthHelper import GoogleAuthHelper, GoogleAuthWorker, GmailPollingWorker
from scripts.components.WidgetBased.SearchLineEdit import SearchLineEdit
from scripts.components.WidgetBased.WatermarkedDeveloper import WatermarkedDeveloperContactView
from scripts.SYS_Config.Config import licenseagreement_info, load_license_data, verify_license

class ToggleButton_Close(QCheckBox):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.circle_x = 2  # Default unchecked position (left side)
        self.setStyleSheet("""
            QCheckBox {
                spacing: 10px;
                font-size: 12px;
            }
            QCheckBox::indicator {
                width: 40px;
                height: 20px;
                border-radius: 10px;
                background: transparent;
            }
        """)

        self.animation = QVariantAnimation(self)
        self.animation.setDuration(300)
        self.animation.valueChanged.connect(self.update_position)
        self.stateChanged.connect(self.animate_slider)

        # Settings integration
        self.settings = QSettings("Zashiron", "Nectar-X-Studio")
        self._sync_from_settings()

    def _sync_from_settings(self):
        """Load initial state from settings and set slider position."""
        if self.settings:
            checked = self.settings.value('append_close_action', True, type=bool)
            self.setChecked(checked)
            # Critical: Set initial slider position based on loaded state
            self.circle_x = 22 if checked else 2
            self.update()  # Force repaint with correct position

    def _on_state_changed(self, state):
        """Save state to settings when toggled."""
        if self.settings:
            checked = state == Qt.CheckState.Checked.value
            self.settings.setValue('append_close_action', checked)

    def update_position(self, value):
        self.circle_x = value
        self.update()

    def animate_slider(self, state):
        """Animate based on checkbox state."""
        self._on_state_changed(state)  # Save to settings
        checked = state == Qt.CheckState.Checked.value
        start_x = self.circle_x
        end_x = 22 if checked else 2
        self.animation.stop()
        self.animation.setStartValue(start_x)
        self.animation.setEndValue(end_x)
        self.animation.start()

    def paintEvent(self, event):
        """Custom toggle switch drawing - NO super() call."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Background track (positioned in indicator area)
        color = QColor('#ff4444') if self.isChecked() else QColor('#444444')
        painter.setBrush(color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 2, 40, 16, 8, 8)

        # Circle slider
        painter.setBrush(QColor('#ffffff'))
        painter.drawEllipse(int(self.circle_x), 4, 12, 12)

        # Draw text manually (super() handled this before)
        painter.setPen(self.palette().color(QPalette.ColorRole.WindowText))
        painter.drawText(50, 0, self.width() - 50, self.height(), 
                        Qt.AlignmentFlag.AlignVCenter, self.text())

        painter.end()

class RightPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(340)
        self.setWindowOpacity(1.0)
        #self.setStyleSheet('background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,0,0,0.6), stop:1 rgba(20,20,20,0.9));')
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16,16,16,16)
        layout.setSpacing(14)

        self.settings = QSettings("Zashiron", "Nectar-X-Studio")
        self.google_auth = GoogleAuthHelper(self.settings)

        # ---------- Process ----------
        self.process = psutil.Process(os.getpid())

        # Store last I/O values for speed calculation
        self.last_io = self.process.io_counters()
        self.last_upload = self.last_io.write_bytes
        self.last_download = self.last_io.read_bytes

        # ---------- Timer ----------
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_app_metrics)
        self.timer.start(1000)  # update every second

        # User header
        header = QFrame()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0,0,0,0)
        self.google_profile_label = QLabel()
        self.google_profile_label.setFixedSize(40,40)
        # Set the cursor programmatically
        self.google_profile_label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.google_profile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.google_profile_label.setStyleSheet('font-size:20px; background: rgba(255,255,255,0.03); border-radius:20px;')
        self.user_label = QLabel(self.settings.value("google/name", "Not Logged In"))
        self.user_label.setStyleSheet('color:#ffffff; font-weight:600;')
        header_layout.addWidget(self.google_profile_label)
        header_layout.addSpacing(8)
        header_layout.addWidget(self.user_label)
        header_layout.addStretch()
        layout.addWidget(header)

        # --- Usage inside your layout ---
        search_box = SearchLineEdit()
        # Access the completer popup (it's a QListView)
        popup = search_box.completer.popup()

        # Apply QSS to style the suggestion list
        popup.setStyleSheet("""
            QListView {
                background-color: #1e1e1e;  /* dark background */
                border: 1px solid #555;     /* border around the list */
                border-radius: 8px;          /* rounded corners */
                padding: 4px;
                color: #ffffff;              /* text color */
                font-size: 14px;
            }
            QListView::item {
                padding: 8px 12px;
                border-radius: 4px;
            }
            QListView::item:selected {
                background-color: #3a3a3a;  /* hover / selected background */
                color: #ffffff;             /* selected text color */
            }
        """)
        layout.addWidget(search_box)

        # Horizontal container for the quick buttons
        btn_container = QWidget()
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.setSpacing(8)  # spacing between buttons

        # Function to create a reusable quick button
        def create_quick_button(icon_path, tooltip, callback):
            btn = QPushButton()
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(32, 32))
            btn.setFixedSize(48, 48)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(self.icon_button_stylesheet())
            btn.setToolTip(tooltip)
            btn.clicked.connect(callback)
            return btn

        quick_buttons = [
            {
                "icon": find_icon('background/store.png'),
                "tooltip": "NectarStore",
                "callback": self.open_NectarStore
            },
            {
                "icon": find_icon('background/mic.png'),
                "tooltip": "NectarSTT",
                "callback": self.open_NectarSTT
            },
            {
                "icon": find_icon('background/easel.png'),
                "tooltip": "NectarGraphix",
                "callback": self.open_ngx 
            },
            {
                "icon": find_icon('background/settings.png'),
                "tooltip": "Self Service",
                "callback": self.open_settings 
            },
        ]

        # Create and add buttons dynamically
        for info in quick_buttons:
            btn = create_quick_button(info["icon"], info["tooltip"], info["callback"])
            btn_layout.addWidget(btn)

        layout.addWidget(btn_container)


        # Party card mock
        party = Card()
        pl = QVBoxLayout(party)
        ptitle = QLabel('App License')
        ptitle.setStyleSheet('color:#ffffff; font-weight:500;')
        pl.addWidget(ptitle)
        # --- License Info ---
        license_group = QGroupBox("License")
        license_layout = QVBoxLayout()
        license_layout.addWidget(self.create_license_widget())
        license_group.setLayout(license_layout)
        pl.addWidget(license_group)
        layout.addWidget(party)
        #layout.addStretch()

        # metrics card mock
        metrics = Card()
        pl = QVBoxLayout(metrics)
        ptitle = QLabel('App Consumption')
        ptitle.setStyleSheet('color:#ffffff; font-weight:500;')
        pl.addWidget(ptitle)
        # --- System Info ---
        perf_group = QGroupBox("Metrics")
        perf_layout = QVBoxLayout()
        perf_layout.addWidget(self.create_performance_info_widget())
        perf_group.setLayout(perf_layout)
        pl.addWidget(perf_group)
        layout.addWidget(metrics)
        layout.addStretch()

        # Refresh button
        icon_path_refresh = find_icon("menu/dot.png")
        side_btn2 = QPushButton()
        side_btn2.setIcon(QIcon(icon_path_refresh))
        side_btn2.setFixedSize(50, 50)
        side_btn2.clicked.connect(lambda: self.app_info())
        side_btn2.setStyleSheet("""
            QPushButton {
                border-radius: 12px;
                background-color: #ffffff;
                color: #fff;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2e2e2e;
            }
            QPushButton:pressed {
                background-color: #0d0d0d;
            }
        """)
        layout.addWidget(side_btn2, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        self.load_google_account()

    def app_info(self):
        # Prevents reopening multiple times
        if hasattr(self, "settings_widget") and self.info_widget.isVisible():
            return

        # Create a small internal settings widget
        self.info_widget = QWidget(self)
        self.info_widget.setWindowTitle("  ")
        self.info_widget.setFixedSize(300, 320)
        self.info_widget.setWindowFlags(Qt.WindowType.Dialog)
        #self.info_widget.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        #self.info_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.info_widget.setStyleSheet("""
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

        layout = QVBoxLayout(self.info_widget)
        #layout.setContentsMargins(15, 15, 15, 15)

        # Title
        title_label = QLabel("<h1>Setting</h1>")
        title_label.setFixedHeight(50)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # --- Info body---
        body = QLabel()
        body.setText(
            "<h2>App Info</h2><br>"
            "<span style='font-size:13px; font-weight:600;'>Nectar-X-Studio</span><br>"
            "<span style='font-size:11px; color:#9ca3af;'>Edition</span> · "
            "<span style='font-size:11px; color:#e5e7eb;'>CPU Optimized</span><br><br>"

            "<span style='font-size:11px; color:#9ca3af;'>Logic Unit</span><br>"
            "<span style='font-size:11px; color:#e5e7eb;'>Model: Decision‑k2 (Zashiron)</span><br>"
            "<span style='font-size:11px; color:#e5e7eb;'>Engine Type: Co‑Linear</span><br>"
            "<span style='font-size:11px; color:#e5e7eb;'>Integration: L1 Primitive</span><br>"
            "<span style='font-size:11px; color:#e5e7eb;'>Speciation: Query Compulsion</span><br><br>"

            "<span style='font-size:11px; color:#9ca3af;'>Processing</span><br>"
            "<span style='font-size:11px; color:#e5e7eb;'>Unit: IDPU (Integrated Decision Processing Unit)</span><br>"
            "<span style='font-size:11px; color:#e5e7eb;'>Type: Loaded Model N01</span><br><br>"

            "<span style='font-size:11px; color:#9ca3af;'>Engine</span><br>"
            "<span style='font-size:11px; color:#e5e7eb;'>Framework: CUDA + CPU Support</span><br>"
            "<span style='font-size:11px; color:#e5e7eb;'>Platform: ZASHIR 0.0001 System</span>"
        )
        body.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        body.setWordWrap(True)
        body.setStyleSheet("""
            QLabel {
                padding: 12px 16px;
                border-radius: 16px;
                background-color: #000000;      /* slate-950 */
                color: white;                  /* zinc-200 */
                border: None;       /* gray-800 */
            }
        """)

        # --- Modern scroll container (shadcn-like) ---
        scroll = QScrollArea()
        scroll.setWidget(body)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        #scroll.setFixedHeight(220)  # Adjusts height to control visible area

        scroll.setStyleSheet("""
            /* Vertical Scrollbar */
            QScrollBar:vertical {
                background: transparent;
                width: 8px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:vertical {
                background: #1e1e1e;
                min-height: 20px;
                border-radius: 4px;
            }

            QScrollBar::handle:vertical:hover {
                background: #ffffff;
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
        """)

        layout.addWidget(scroll)

        title_label2 = QLabel("<h3>Other</h3>")
        title_label2.setFixedHeight(50)
        title_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label2)

        buttom_layout = QHBoxLayout()
        buttom_layout.setSpacing(2)

        toggle_label = QLabel('Close To Hide:')
        toggle_label.setStyleSheet('font-size: 14px; padding: 5px;')

        self.checkbox = ToggleButton_Close()
        self.checkbox.stateChanged.connect(self.on_close_action_toggle)

        buttom_layout.addWidget(toggle_label)
        buttom_layout.addWidget(self.checkbox)

        layout.addLayout(buttom_layout)

        # Position it at the center of the main window
        parent_rect = self.geometry()
        x = parent_rect.x() + (parent_rect.width() - self.info_widget.width()) // 8
        y = parent_rect.y() + (parent_rect.height() - self.info_widget.height()) // 2
        self.info_widget.move(680, y)

        # Fade-in animation
        self.info_widget.setWindowOpacity(0.0)
        self.info_widget.show()

        fade_in = QPropertyAnimation(self.info_widget, b"windowOpacity")
        fade_in.setDuration(600)
        fade_in.setStartValue(0.0)
        fade_in.setEndValue(1.0)
        fade_in.setEasingCurve(QEasingCurve.Type.InOutQuad)
        fade_in.start()

        # Keep reference so animation doesn’t get garbage collected
        self.fade_in_animation = fade_in
    
    def on_close_action_toggle(self):
        if self.checkbox.isChecked():
            self.settings.value('append_close_action', True, type=bool)
        else:
            self.checkbox.stateChanged.connect(self.save_close_action_setting)

    def save_close_action_setting(self):
        self.settings.setValue('append_close_action', self.checkbox.isChecked())

    def fade_out_settings(self):
        if not hasattr(self, "info_widget") or not self.info_widget.isVisible():
            return

        fade_out = QPropertyAnimation(self.info_widget, b"windowOpacity")
        fade_out.setDuration(600)
        fade_out.setStartValue(1.0)
        fade_out.setEndValue(0.0)
        fade_out.setEasingCurve(QEasingCurve.Type.InOutQuad)
        fade_out.finished.connect(self.info_widget.close)
        fade_out.start()

        # Keep reference alive
        self.fade_out_animation = fade_out

    def open_settings(self):
        # Prevent reopening multiple times
        if hasattr(self, "settings_widget") and self.settings_widget.isVisible():
            return

        # Create a small internal settings widget
        self.settings_widget = QWidget(self)
        self.settings_widget.setWindowTitle("SUPPORT")
        self.settings_widget.setFixedSize(300, 220)
        self.settings_widget.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.settings_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.settings_widget.setStyleSheet("""
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

        layout = QVBoxLayout(self.settings_widget)
        #layout.setContentsMargins(15, 15, 15, 15)

        # Title
        title_label = QLabel("Self Service")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Close button
        contact_button = QPushButton("Contact Developer")
        contact_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 12px;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #ffffff; color: #000000;}
            QPushButton:pressed { background-color: #1e1e1e; }
        """)
        contact_button.clicked.connect(lambda: self.contact_developer())
        layout.addWidget(contact_button)

        license_button = QPushButton("License")
        license_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 12px;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #ffffff; color: #000000;}
            QPushButton:pressed { background-color: #1e1e1e; }
        """)
        license_button.clicked.connect(lambda: self.license_view())
        layout.addWidget(license_button)

        # Close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 12px;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #ffffff; color: #000000;}
            QPushButton:pressed { background-color: #1e1e1e; }
        """)
        close_button.clicked.connect(lambda: self.fade_out_settings())
        layout.addWidget(close_button)

        # Position it at the center of the main window
        parent_rect = self.geometry()
        x = parent_rect.x() + (parent_rect.width() - self.settings_widget.width()) // 8
        y = parent_rect.y() + (parent_rect.height() - self.settings_widget.height()) // 2
        self.settings_widget.move(680, y)

        # Fade-in animation
        self.settings_widget.setWindowOpacity(0.0)
        self.settings_widget.show()

        fade_in = QPropertyAnimation(self.settings_widget, b"windowOpacity")
        fade_in.setDuration(600)
        fade_in.setStartValue(0.0)
        fade_in.setEndValue(1.0)
        fade_in.setEasingCurve(QEasingCurve.Type.InOutQuad)
        fade_in.start()

        # Keep reference so animation doesn’t get garbage collected
        self.fade_in_animation = fade_in

    def fade_out_settings(self):
        if not hasattr(self, "settings_widget") or not self.settings_widget.isVisible():
            return

        fade_out = QPropertyAnimation(self.settings_widget, b"windowOpacity")
        fade_out.setDuration(600)
        fade_out.setStartValue(1.0)
        fade_out.setEndValue(0.0)
        fade_out.setEasingCurve(QEasingCurve.Type.InOutQuad)
        fade_out.finished.connect(self.settings_widget.close)
        fade_out.start()

        # Keep reference alive
        self.fade_out_animation = fade_out

    def license_view(self):
        if hasattr(self, "licence_widget") and self.license_widget.isVisible():
            return

        # === CREATE CHAT WINDOW ===
        self.license_widget = QWidget(self)
        self.license_widget.setWindowTitle("Contact Developer")
        self.license_widget.setFixedSize(330, 400)
        #self.license_widget.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        #self.license_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # === STYLES ===
        self.license_widget.setStyleSheet("""
            QWidget { background-color: #000000; border: transparent; border-radius:12px; }
            QLabel { font-size:16px; font-weight:bold; color:white; }
            QLineEdit { background-color:#2a2a2a; color:white; border-radius:8px; border:1px solid #444; padding:5px; }
            QPushButton { background-color:#3c3c3c; color:white; border:none; border-radius:6px; padding:6px 12px; }
            QPushButton:hover { background-color:#505050; }
        """)

        layout = QVBoxLayout(self.license_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Chat scroll area
        self.license_scroll = QScrollArea()
        self.license_scroll.setStyleSheet("""
            /* Vertical Scrollbar */
            QScrollBar:vertical {
                background: transparent;
                width: 8px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:vertical {
                background: #1e1e1e;
                min-height: 20px;
                border-radius: 4px;
            }

            QScrollBar::handle:vertical:hover {
                background: #ffffff;
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
            """)
        self.license_scroll.setWidgetResizable(True)
        self.license_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        layout.addWidget(self.license_scroll)

        # Container for chat bubbles
        self.license_container = WatermarkedDeveloperContactView("Nectar-X-Studio")
        self.license_layout = QVBoxLayout(self.license_container)
        self.license_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.license_scroll.setWidget(self.license_container)

        self.license_container.append(licenseagreement_info)

        # Input area
        msg_layout = QHBoxLayout()

        send_button = QPushButton("GitHub")
        send_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 12px;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #ffffff; color: #000000;}
            QPushButton:pressed { background-color: #1e1e1e; }
        """)
        send_button.clicked.connect(self.open_github_page)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 12px;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #ffffff; color: #000000;}
            QPushButton:pressed { background-color: #1e1e1e; }
        """)
        close_button.clicked.connect(lambda: self.license_widget.close())

        msg_layout.addWidget(send_button)
        msg_layout.addWidget(close_button)
        layout.addLayout(msg_layout)

        # Fade-in animation
        self.license_widget.setWindowOpacity(0.0)
        self.license_widget.show()

    def open_github_page(self):
        import webbrowser
        url = "https://github.com/Zashiron"
        webbrowser.open(url)

    def contact_developer(self):
        if hasattr(self, "chat_widget") and self.chat_widget.isVisible():
            return

        # === CREATE CHAT WINDOW ===
        self.chat_widget = QWidget(self)
        self.chat_widget.setWindowTitle("Contact Developer")
        self.chat_widget.setFixedSize(330, 400)
        #self.chat_widget.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        #self.chat_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # === STYLES ===
        self.chat_widget.setStyleSheet("""
            QWidget { background-color: #000000; border: transparent; border-radius:12px; }
            QLabel { font-size:16px; font-weight:bold; color:white; }
            QLineEdit { background-color:#2a2a2a; color:white; border-radius:8px; border:1px solid #444; padding:5px; }
            QPushButton { background-color:#3c3c3c; color:white; border:none; border-radius:6px; padding:6px 12px; }
            QPushButton:hover { background-color:#505050; }
        """)

        layout = QVBoxLayout(self.chat_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Chat scroll area
        self.chat_scroll = QScrollArea()
        self.chat_scroll.setStyleSheet("""
            /* Vertical Scrollbar */
            QScrollBar:vertical {
                background: transparent;
                width: 8px;
                margin: 0px;
                border: none;
            }

            QScrollBar::handle:vertical {
                background: #1e1e1e;
                min-height: 20px;
                border-radius: 4px;
            }

            QScrollBar::handle:vertical:hover {
                background: #ffffff;
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
            """)
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        layout.addWidget(self.chat_scroll)

        # Container for chat bubbles
        self.chat_container = WatermarkedDeveloperContactView("Nectar-X-Studio")
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.chat_scroll.setWidget(self.chat_container)

        # Input area
        msg_layout = QHBoxLayout()
        self.msg_input = QLineEdit()
        self.msg_input.setPlaceholderText("Type your message...")
        self.msg_input.setFixedHeight(50)

        send_button = QPushButton("Send")
        send_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 12px;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #ffffff; color: #000000;}
            QPushButton:pressed { background-color: #1e1e1e; }
        """)
        send_button.clicked.connect(self.send_message_via_gmail)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 12px;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #ffffff; color: #000000;}
            QPushButton:pressed { background-color: #1e1e1e; }
        """)
        close_button.clicked.connect(lambda: self.chat_widget.close())

        msg_layout.addWidget(self.msg_input)
        msg_layout.addWidget(send_button)
        msg_layout.addWidget(close_button)
        layout.addLayout(msg_layout)

        # Fade-in animation
        self.chat_widget.setWindowOpacity(0.0)
        self.chat_widget.show()

        # Start Gmail polling in thread
        self.start_polling_threaded()

    def add_message(self, text, sender="user"):
        # Create bubble
        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(int(self.chat_widget.width() * 0.65))  # slightly narrower
        bubble.setMargin(10)

        # Bubble style
        if sender == "user":
            bubble_color = "#4b4b4b"  # dark gray for user
            text_color = "#ffffff"
            align = Qt.AlignmentFlag.AlignRight
        else:
            bubble_color = "#1e1e1e"  # blue for developer
            text_color = "#ffffff"
            align = Qt.AlignmentFlag.AlignLeft

        bubble.setStyleSheet(f"""
            QLabel {{
                background-color: {bubble_color};
                color: {text_color};
                border-radius: 12px;
                padding: 10px;
                font-size: 14px;
            }}
        """)

        # Wrapper layout for alignment
        wrapper = QHBoxLayout()
        wrapper.setAlignment(align)
        wrapper.addStretch() if sender == "developer" else None
        wrapper.addWidget(bubble)
        wrapper.addStretch() if sender == "user" else None

        # Add a small margin between messages
        wrapper.setContentsMargins(5, 5, 5, 5)

        self.chat_layout.addLayout(wrapper)

        # Auto-scroll to latest message
        QTimer.singleShot(50, lambda: self.chat_scroll.verticalScrollBar().setValue(
            self.chat_scroll.verticalScrollBar().maximum()
        ))

    def send_message_via_gmail(self):
        message_text = self.msg_input.text()
        if not message_text.strip():
            return

        creds = self.google_auth.load_credentials()
        if not creds:
            self.add_message("❌ Google credentials not found. Please log in again.", "developer")
            return

        service = build('gmail', 'v1', credentials=creds)
        try:
            self._send_gmail(service, 'Zashiron.inc@gmail.com', 'App Feedback', message_text)
            self.add_message(message_text, "user")
            self.msg_input.clear()
        except Exception as e:
            self.add_message(f"❌ Failed to send: {str(e)}", "developer")

    def _send_gmail(self, service, to, subject, body):
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message_obj = {'raw': raw}
        service.users().messages().send(userId='me', body=message_obj).execute()

    # ----------------- Threaded Polling -----------------
    def start_polling_threaded(self):
        self.poll_thread = GmailPollingWorker(self.google_auth)
        self.poll_thread.new_message.connect(lambda msg: self.add_message(msg, "developer"))
        self.poll_thread.error.connect(lambda err: self.add_message(err, "developer"))
        self.poll_thread.start()

    def closeEvent(self, event):
        if hasattr(self, "poll_thread"):
            self.poll_thread.stop()
        event.accept()

    def open_NectarSTT(self):
        # Paths to search for NectarSTT.exe
        possible_paths = [
            r"C:\Program Files\NectarSTT\NectarSTT.exe",
            r"C:\Program Files (x86)\NectarSTT\NectarSTT.exe"
        ]
        
        nectar_path = None
        for path in possible_paths:
            if os.path.exists(path):
                nectar_path = path
                break

        # If not found, search deeper in Program Files directories
        if not nectar_path:
            for root, dirs, files in os.walk(r"C:\Program Files"):
                if "NectarSTT.exe" in files:
                    nectar_path = os.path.join(root, "NectarSTT.exe")
                    break
            if not nectar_path:
                for root, dirs, files in os.walk(r"C:\Program Files (x86)"):
                    if "NectarSTT.exe" in files:
                        nectar_path = os.path.join(root, "NectarSTT.exe")
                        break

        if nectar_path:
            try:
                subprocess.Popen([nectar_path], shell=True)
                toast = Notification(
                    app_id="Nectar-X-Studio",
                    title="NectarSTT",
                    msg=f"Launching NectarSTT",
                    icon=find_icon('background/NectarX.png'),
                    duration="short"
                )
                toast.set_audio(audio.SMS, loop=False)
                toast.show()
            except Exception as e:
                Notify(f"Error launching NectarSTT: {e}", parent=self)
        else:
            Notify("NectarSTT.exe not found in Program Files.", parent=self)

    def open_ngx(self):
        try:
            subprocess.Popen(["NectarGraphix", os.path.expanduser("~")])
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="NectarGraphix",
                msg=f"Launching NectarGraphix",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()
        except Exception as e:
            Notify(f"Error opening File NectarGraphix: {e}", parent=self )

    def open_NectarGraphix(self):
        possible_paths = [
            r"C:\Program Files\Imagen-Studio\Imagen-Studio.exe",
            r"C:\Program Files (x86)\Imagen-Studio\Imagen-Studio.exe"
        ]
        
        nectar_path = None
        for path in possible_paths:
            if os.path.exists(path):
                nectar_path = path
                break

        # If not found, search deeper in Program Files directories
        if not nectar_path:
            for root, dirs, files in os.walk(r"C:\Program Files"):
                if "Imagen-Studio.exe" in files:
                    nectar_path = os.path.join(root, "Imagen-Studio.exe")
                    break
            if not nectar_path:
                for root, dirs, files in os.walk(r"C:\Program Files (x86)"):
                    if "Imagen-Studio.exe" in files:
                        nectar_path = os.path.join(root, "Imagen-Studio.exe")
                        break

        if nectar_path:
            try:
                subprocess.Popen([nectar_path], shell=True)
            except Exception as e:
                Notify(f"Error launching Imagen-Studio: {e}", parent=self)
        else:
            Notify("Imagen-Studio.exe not found in Program Files.", parent=self)

        # Fade out and close the current window
        #self.fade_animation = QPropertyAnimation(self, b"windowOpacity")
        #self.fade_animation.setDuration(1000)  # 1 second
        #self.fade_animation.setStartValue(1.0)
        #self.fade_animation.setEndValue(0.0)
        #self.fade_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        #self.fade_animation.finished.connect(self.close)
        #self.fade_animation.start()

    def find_utils4(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'App_Docs', icon_name), 
                          os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:
            return None

    def show_message_box(self, title, text):
        QMessageBox.information(None, title, text)

    def open_NectarStore(self):
        # Paths to search for NectarsStore.exe
        possible_paths = [
            r"C:\Program Files\NectarStore\NectarStore.exe",
            r"C:\Program Files (x86)\NectarStore\NectarStore.exe"
        ]
        
        nectar_path = None
        for path in possible_paths:
            if os.path.exists(path):
                nectar_path = path
                break

        # If not found, search deeper in Program Files directories
        if not nectar_path:
            for root, dirs, files in os.walk(r"C:\Program Files"):
                if "NectarStore.exe" in files:
                    nectar_path = os.path.join(root, "NectarStore.exe")
                    break
            if not nectar_path:
                for root, dirs, files in os.walk(r"C:\Program Files (x86)"):
                    if "NectarStore.exe" in files:
                        nectar_path = os.path.join(root, "NectarStore.exe")
                        break

        if nectar_path:
            try:
                subprocess.Popen([nectar_path], shell=True)
                toast = Notification(
                    app_id="Nectar-X-Studio",
                    title="NectarStore",
                    msg=f"Launching NectarStore",
                    icon=find_icon('background/NectarX.png'),
                    duration="short"
                )
                toast.set_audio(audio.SMS, loop=False)
                toast.show()
            except Exception as e:
                Notify(f"Error launching NectarStore: {e}", parent=self)
        else:
            Notify("NectarStore.exe not found in Program Files.", parent=self)

    def icon_button_stylesheet(self):
        return """
            QPushButton {
                border: none;
                background-color: #000000;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #3a3a3a;
                border-radius: 8px;
            }

            QPushButton:pressed {
                background-color: #1a1a1a;
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
        """

    def create_license_widget(self):
        """
        Creates a QWidget displaying license information.
        Automatically pulls verified license data from local storage.
        """
        # Ensure data is loaded for display
        license_data = load_license_data() 
        if not license_data:
            # Try to verify or initialize license if none exists
            license_data = verify_license()
            if not license_data:
                license_data = {
                    "licensor": "Unknown",
                    "license_key": "Unavailable",
                    "expiration_date": "N/A"
                }

        info_layout = QVBoxLayout()
        info_layout.setSpacing(5)

        license_info = {
            "SOFTWARE OWNER": "Zashiron Inc",
            "DEVELOPER": "Ikenna Christian Great",
            "CONTACT": "Zashiron.inc@gmail.com",
            "LICENSE": f"verified by {license_data.get('licensor', 'Unknown')}.",
            "EXPIRES": f"{license_data.get('expiration_date', 'N/A')}"
        }

        for k, v in license_info.items():
            lbl = QLabel(f"<b>{k}:</b> {v}")
            lbl.setStyleSheet("padding: 2px;")
            info_layout.addWidget(lbl)

        container = QWidget()
        container.setLayout(info_layout)
        return container

    def create_performance_info_widget(self):
        perf_layout = QVBoxLayout()
        perf_layout.setSpacing(5)

        self.monitor_label = QLabel("Nectar-X-Studio Performance")
        self.monitor_label.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        self.monitor_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_label = QLabel("Status: Monitoring self")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont("Segoe UI", 12))

        # ---------- Bars ----------
        self.cpu_bar = self.create_progress_bar("CPU Usage")
        self.ram_bar = self.create_progress_bar("Memory Usage")

        # ---------- Network Labels ----------
        self.upload_label = QLabel("Upload: 0.00 KB/s")
        self.download_label = QLabel("Download: 0.00 KB/s")
        self.upload_label.setFont(QFont("Segoe UI", 12))
        self.download_label.setFont(QFont("Segoe UI", 12))
        self.upload_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.download_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add all widgets side by side
        perf_layout.addWidget(self.monitor_label)
        perf_layout.addWidget(self.cpu_bar)
        perf_layout.addWidget(self.ram_bar)
        perf_layout.addWidget(self.upload_label)
        perf_layout.addWidget(self.download_label)

        container = QWidget()
        container.setLayout(perf_layout)
        return container
    
    def create_progress_bar(self, title):
        frame = QFrame()
        vbox = QVBoxLayout(frame)
        label = QLabel(title)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QFont("Segoe UI", 12))
        bar = QProgressBar()
        bar.setRange(0, 100)
        bar.setValue(0)
        bar.setTextVisible(False)
        bar.setFixedHeight(12)
        bar.setStyleSheet("""
                QProgressBar {
                border-radius: 10px;
                height: 20px;
                background: #ffffff;
                text-align: center;
                color: #000;
            }
            QProgressBar {
                background-color: #ffffff;
                border-radius: 4px;
            }
            QProgressBar::chunk {
                background-color: #ff7a00;
                border-radius: 4px;
            }
        """)
        vbox.addWidget(label)
        vbox.addWidget(bar)
        return frame

    # ---------- Metrics ----------
    def update_app_metrics(self):
        try:
            cpu_usage = self.process.cpu_percent(interval=None) / psutil.cpu_count()
            mem_usage = self.process.memory_percent()

            # Calculate I/O speed
            io_counters = self.process.io_counters()
            upload_diff = io_counters.write_bytes - self.last_upload
            download_diff = io_counters.read_bytes - self.last_download
            self.last_upload = io_counters.write_bytes
            self.last_download = io_counters.read_bytes
            upload_speed = upload_diff / 1024  # KB/s
            download_speed = download_diff / 1024  # KB/s

            # Update UI
            self.status_label.setText(f"Status: Running (PID {self.process.pid})")
            self.monitor_label.setText(f"CPU: {cpu_usage:.1f}% | RAM: {mem_usage:.1f}%")
            self.upload_label.setText(f"Upload: {upload_speed:.2f} KB/s")
            self.download_label.setText(f"Download: {download_speed:.2f} KB/s")

            self.update_bar(self.cpu_bar, cpu_usage)
            self.update_bar(self.ram_bar, mem_usage)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            self.status_label.setText("Status: Process not available")
            self.update_bar(self.cpu_bar, 0)
            self.update_bar(self.ram_bar, 0)
            self.upload_label.setText("Upload: 0.00 KB/s")
            self.download_label.setText("Download: 0.00 KB/s")

    def update_bar(self, frame, value):
        bar = frame.findChild(QProgressBar)
        bar.setValue(int(value))

    def load_google_account(self):
        settings1 = QSettings("Zashiron", "Nectar-X-Studio")
        """Load saved Google profile (if any)."""
        if self.google_auth.is_authenticated():
            settings1.beginGroup("google")
            name1 = settings1.value("name", "User")
            picture_url = settings1.value("picture", "")
            settings1.endGroup()

            # Update username text instead of creating a new label
            self.user_label.setText(name1)

            if hasattr(self, "google_profile_label"):
                try:
                    pixmap = None
                    if picture_url.startswith("http"):
                        import requests
                        from io import BytesIO
                        response = requests.get(picture_url)
                        image_data = BytesIO(response.content)
                        pixmap = QPixmap()
                        pixmap.loadFromData(image_data.read())
                    else:
                        import qtawesome as qta
                        icon = qta.icon('fa5s.user', color='red')
                        pixmap = QPixmap(icon.pixmap(32, 32))

                    if not pixmap.isNull():
                        size = 40
                        radius = 8

                        scaled = pixmap.scaled(
                            size, size,
                            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                            Qt.TransformationMode.SmoothTransformation
                        )

                        rounded = QPixmap(size, size)
                        rounded.fill(Qt.GlobalColor.transparent)

                        painter = QPainter(rounded)
                        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                        path = QPainterPath()
                        path.addRoundedRect(0, 0, size, size, radius, radius)
                        painter.setClipPath(path)
                        painter.drawPixmap(0, 0, scaled)
                        painter.end()

                        self.google_profile_label.setPixmap(rounded)
                        self.google_profile_label.setFixedSize(size, size)

                except Exception as e:
                    write_to_log(f"Error loading profile picture: {e}")
                    Notify(f"Error loading profile picture:", parent=self)

            self.google_profile_label.setToolTip(name1)
            self.google_profile_label.mousePressEvent = lambda e: self.show_google_menu(e)

        else:
            import qtawesome as qta
            icon = qta.icon('fa5s.user', color='red')
            self.google_profile_label.setPixmap(icon.pixmap(32, 32))
            self.google_profile_label.setToolTip("Click to sign in with Google")
            self.google_profile_label.mousePressEvent = lambda e: self.connect_google_account_threaded()
            
            # Update existing label instead of creating new one
            self.user_label.setText("Not Logged In")

    def connect_google_account_threaded(self):
        """Start Google OAuth in background thread (non-blocking)."""
        self.google_profile_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        import qtawesome as qta
        icon = qta.icon('fa5s.user', color='red')
        self.google_profile_label.setPixmap(icon.pixmap(32, 32))

        worker = GoogleAuthWorker(
            self.google_auth.client_secret_file,
            self.google_auth.SCOPES,
            self.google_auth  # this IS the helper
        )

        # Connect signals
        worker.finished.connect(self.on_google_auth_success)
        worker.failed.connect(self.on_google_auth_fail)

        # Run in background
        thread = threading.Thread(target=worker.run, daemon=True)
        thread.start()

    def on_google_auth_success(self, profile):
        """Handle successful login."""
        self.google_auth.save_profile(profile)
        QMessageBox.information(self, "Google Sign-In", f"Welcome, {profile.get('name')}!")
        self.user_label.setText(profile.get("name", "User"))
        self.load_google_account()

    def on_google_auth_fail(self, error):
        """Handle failed login."""
        QMessageBox.critical(self, "Google Sign-In Failed", error)
        import qtawesome as qta
        icon = qta.icon('fa5s.user', color='red')
        self.google_profile_label.setPixmap(icon.pixmap(32, 32))
        self.google_profile_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.user_label.setText("Login Failed. Try Later!")

    def show_google_menu(self, event):
        """Display dropdown menu for Google tools."""
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: #000000;
                color: #ffffff;
                border: 1px solid #555;
                border-radius: 8px;
                padding: 5px;
                font: 12pt "Segoe UI", "Arial";
            }

            QMenu::item {
                padding: 5px 25px 5px 20px;
                border-radius: 5px;
            }

            QMenu::item:selected {
                background-color: #ffffff; /* blue hover */
                color: #000000;
            }

            QMenu::separator {
                height: 1px;
                background: #555;
                margin: 5px 10px 5px 10px;
            }
        """)

        name = self.settings.value("google/name", "Google Account")
        email = self.settings.value("google/email", "")
        menu.addSection(f"{name}\n{email}")

        # Add tools
        actions = {
            "Gmail": "https://mail.google.com/",
            "Drive": "https://drive.google.com/",
            "Calendar": "https://calendar.google.com/",
            "Maps": "https://maps.google.com/",
            "Search": "https://www.google.com/",
        }

        for label, url in actions.items():
            action = QAction(label, self)
            import webbrowser
            action.triggered.connect(lambda _, link=url: webbrowser.open(link))
            menu.addAction(action)

        menu.addSeparator()

        # Logout option
        logout_action = QAction("Logout", self)
        logout_action.triggered.connect(self.logout_google_account)
        menu.addAction(logout_action)

        # Position the menu under the profile picture
        menu.exec(self.google_profile_label.mapToGlobal(event.pos()))

    def logout_google_account(self):
        """Clear all saved account info."""
        self.settings.remove("google/name")
        self.settings.remove("google/email")
        self.settings.remove("google/picture")
        self.settings.setValue("google/authorized", False)

        import qtawesome as qta
        icon = qta.icon('fa5s.user', color='red')
        self.google_profile_label.setPixmap(icon.pixmap(32, 32))
        self.google_profile_label.setToolTip("Click to sign in with Google")
        self.google_profile_label.mousePressEvent = lambda e: self.connect_google_account_threaded()

        self.user_label.setText("Not Logged In")
        QMessageBox.information(self, "Logout", "You have been logged out of your Google account.")


    def get_google_account_info(self):
        """Return Google account info if logged in, else None."""
        if self.google_auth.is_authenticated():
            return {
                "name": self.settings.value("google/name"),
                "email": self.settings.value("google/email"),
                "picture": self.settings.value("google/picture"),
            }
        return None