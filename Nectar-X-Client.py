import asyncio
from PyQt6.QtCore import QSettings
import sys
import os
import subprocess
import platform
import socket
import tempfile
import zipfile
import traceback
import ctypes
import shutil
import psutil
import re
import requests
import time
from urllib.parse import urlparse
from urllib.request import urlopen
from datetime import datetime
import datetime
import base64
import json
import warnings
import multiprocessing
import threading

from edge_tts import Communicate

# Third-party dependencies
# PyQt6
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton,
    QSpacerItem, QSizePolicy, QSplashScreen, QLineEdit, QGridLayout, QMessageBox,
    QTextEdit, QCheckBox, QHBoxLayout, QFrame, QSpinBox, QFileDialog, QInputDialog,
    QPlainTextEdit, QSplitter, QStackedWidget, QStackedLayout, QFormLayout, QListWidget,
    QSlider, QScrollArea, QGraphicsOpacityEffect, QListWidgetItem, QComboBox, QGroupBox,
    QTabWidget, QCompleter, QStatusBar, QSystemTrayIcon, QMenu, QToolTip, QToolButton,
    QDialogButtonBox, QDialog, QDoubleSpinBox
)
from PyQt6.QtCore import (
    Qt, QTimer, QSharedMemory, QSystemSemaphore, QThread, pyqtSignal, QElapsedTimer,
    QObject, QSize, QRegularExpression, QProcess, QPropertyAnimation, QEvent,
    QFileSystemWatcher, QStringListModel, QPoint, QUrl, QEasingCurve, QVariantAnimation, QRect,
    pyqtProperty, pyqtSlot # Added pyqtSlot for completeness although not explicitly imported
)
from PyQt6.QtGui import (
   QIcon , QFont, QPixmap, QPainter, QPainterPath, QDesktopServices, QShortcut,
    QColor, QSyntaxHighlighter, QTextCharFormat, QTextCursor, QTextFormat, QAction,
    QPen, QKeySequence, QGuiApplication, QCursor, QBrush, QImage
)
from PyQt6.QtWebEngineWidgets import QWebEngineView

# Logging
import logging

#Webengine
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings, QWebEngineScript, QWebEnginePage
import webbrowser

# Other
QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)

# ----------------- UTILITY FUNCTIONS -----------------
def is_admin():
    """Check if the script is running with admin privileges on Windows."""
    try:
        if platform.system() != "Windows":
            return True
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

# Base directory handling for PyInstaller .exe
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.realpath(__file__))

HORIZONTAL_GAP = 20  # Gap in pixels between parent and child

PROGRAM_FILES_DIRS = [
    r"C:\Program Files",
    r"C:\Program Files (x86)"
]

EXCLUDED_FOLDERS = ["Nectar-X-Client"]

def find_exact_nectar_folders(root_paths):
    """Scan Program Files directories for folders containing 'Nectar' except excluded ones"""
    found_folders = []

    for root_path in root_paths:
        if not os.path.exists(root_path):
            continue
        for dirpath, dirnames, filenames in os.walk(root_path):
            for dirname in dirnames:
                if "Nectar" in dirname and dirname not in EXCLUDED_FOLDERS:
                    full_path = os.path.join(dirpath, dirname)
                    found_folders.append(full_path)
    return found_folders
    
import webbrowser

def open_link(url: str):
    """
    Opens the given URL in the default web browser.
    
    Args:
        url (str): The URL to open.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Ensure URL is valid
    try:
        webbrowser.open(url, new=2)  # new=2 opens in a new tab if possible
        print(f"Opening URL: {url}")
    except Exception as e:
        print(f"Failed to open URL {url}: {e}")

class Notify(QWidget):
    def __init__(self, message, duration=3000, parent=None):
        super().__init__(parent, flags=Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        self.label = QLabel(message, self)
        self.label.setStyleSheet("""
            QLabel {
                background-color: #333333;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                padding: 10px 20px;
                border-radius: 8px;
            }
        """)
        self.label.adjustSize()
        self.resize(self.label.size())

        # Center on parent if given, else center on screen
        if parent:
            parent_rect = parent.geometry()
            self.move(
                parent_rect.center().x() - self.width() // 2,
                parent_rect.top() + 50
            )
        else:
            screen = self.screen().geometry()
            self.move(
                screen.center().x() - self.width() // 2,
                50
            )

        # Auto-close timer
        QTimer.singleShot(duration, self.close)
        self.show()

import base64

# ----------------------------
# Find a browse agent
# ----------------------------
exe_name1 = "ChatServe.exe"
exe_name2 = "ChatServe"
exe_name3 = "ChatServe.app"

def find_exe():
    """Find the correct executable based on the platform."""
    script_dir = os.path.dirname(os.path.realpath(__file__))

    if sys.platform.startswith("win"):
        exe_name = exe_name1
        possible_paths = [
            os.path.join(script_dir, exe_name),
            os.path.join(script_dir, "Utils", exe_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, exe_name))
        ]
    elif sys.platform.startswith("linux"):
        exe_name = exe_name2
        possible_paths = [
            os.path.join(script_dir, exe_name),
            os.path.join(script_dir, "App_Docs", exe_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, exe_name))
        ]
    elif sys.platform.startswith("darwin"):
        exe_name = exe_name3
        possible_paths = [
            os.path.join(script_dir, exe_name),
            os.path.join(script_dir, "App_Docs", exe_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, exe_name))
        ]
    else:
        raise Exception(f"Unsupported platform: {sys.platform}")

    for path in possible_paths:
        if os.path.exists(path):
            return exe_name, path  # return both name and path

    return exe_name, None

def find_utils4(icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'Utils', icon_name), 
                          os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from datetime import datetime

def find_icon(icon_name):
    """Attempts to find the icon in and out of the script\'s directory."""  # inserted
    script_dir = os.path.dirname(os.path.realpath(__file__))
    possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    else:  # inserted
        return None

# Mapping folder names to icon file paths
ICON_MAPPING = {
    "NectarStore": find_icon('background/store.png'),
    "NectarSTT": find_icon('background/mic.png'),
    "NectarGraphix": find_icon('background/easel.png'),
    "NectarHub": find_icon('background/ruin.png'),
    "Nectar-X-Studio": find_icon('background/factory.png')
}

DEFAULT_ICON = find_icon('background/default.png')

def check_browser_agent():
    exe_name, exe_path = find_exe()
    if not exe_path:
        raise Exception(f"{exe_name} not found in expected locations.")

    # Check if process is already running
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc_name = proc.info['name'].lower() if proc.info['name'] else ""
            if (sys.platform.startswith("win") and proc_name == "chatserve.exe") or \
               (sys.platform.startswith("linux") and proc_name == "chatserve") or \
               (sys.platform.startswith("darwin") and proc_name == "chatserve"):
                print(f"{exe_name} is already running.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    # Start the application
    try:
        if sys.platform.startswith("win"):
            os.startfile(exe_path)
        elif sys.platform.startswith("linux"):
            subprocess.Popen([exe_path])
        elif sys.platform.startswith("darwin"):
            subprocess.Popen(["open", exe_path])
        print(f"{exe_name} started successfully from: {exe_path}")
    except Exception as e:
        raise Exception(f"Failed to start {exe_name}: {e}")

def send_to_AlphaLLM(question):
    import socket
    
    SERVER_ADDRESS = ('127.0.0.1', 5005)
    AUTH_KEY = ("NEC-892657") # 🔒 Security Key  # must match the server’s key

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client.settimeout(10)  # optional safety timeout
        client.connect(SERVER_ADDRESS)

        # Prepend the key before the question
        secure_message = f"{AUTH_KEY} {question}"
        client.sendall(secure_message.encode('utf-8'))

        response = client.recv(8192).decode('utf-8').strip()
        client.close()

        return response

    except (socket.error, socket.timeout) as e:
        return f"[Error] Could not connect to AlphaLLM: {e}"
    
class FloatingNotification(QWidget):
    def __init__(self, parent, message, duration=120000, bg_color='#222222', text_color='#ffffff'):
        super().__init__(parent)
        self.parent_widget = parent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.SubWindow | Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {bg_color};
                border-radius: 10px;
            }}
            QLabel {{
                color: {text_color};
                font-size: 13px;
                padding-left: 10px;
            }}
            QPushButton {{
                background: transparent;
                color: {text_color};
                border: none;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                color: red;
            }}
        """)

        self.message_label = QLabel(message)
        self.close_button = QPushButton('❌')
        self.close_button.setFixedSize(24, 24)
        self.close_button.clicked.connect(self.close)
        layout = QHBoxLayout()
        layout.addWidget(self.message_label)
        layout.addStretch()
        layout.addWidget(self.close_button)
        layout.setContentsMargins(12, 8, 12, 8)
        self.setLayout(layout)
        self.adjustSize()
        self.move_to_mid_right()
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.fade_in = QPropertyAnimation(self.opacity_effect, b'opacity')
        self.fade_in.setDuration(300)
        self.fade_in.setStartValue(0)
        self.fade_in.setEndValue(1)
        self.fade_in.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.fade_in.start()
        self.show()
        self.auto_close_timer = QTimer()
        self.auto_close_timer.setSingleShot(True)
        self.auto_close_timer.timeout.connect(self.close)
        self.auto_close_timer.start(duration)
        parent.installEventFilter(self)

    def move_to_mid_right(self):
        if not self.parent_widget:
            return
        parent_geom = self.parent_widget.geometry()
        x = parent_geom.width() - self.width() - 30
        y = 250
        self.move(x, y)

    def eventFilter(self, obj, event):
        if obj == self.parent_widget and event.type() == QEvent.Type.Resize:
            self.move_to_mid_right()
        return super().eventFilter(obj, event)
    
class AnimatedDot(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._radius = 5
        self._color = QColor('#808080')
        self._opacity = 1.0
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._radius_anim = QPropertyAnimation(self, b'radius')
        self._radius_anim.setStartValue(12)
        self._radius_anim.setEndValue(18)
        self._radius_anim.setDuration(900)
        self._radius_anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self._radius_anim.finished.connect(self._reverse_radius_animation)
        self._opacity_anim = QPropertyAnimation(self, b'opacity')
        self._opacity_anim.setStartValue(0.7)
        self._opacity_anim.setEndValue(0.9)
        self._opacity_anim.setDuration(900)
        self._opacity_anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self._opacity_anim.finished.connect(self._reverse_opacity_animation)
        self._color_anim = QVariantAnimation()
        self._color_anim.setStartValue(QColor('#000000'))
        self._color_anim.setEndValue(QColor('#faf7f7'))
        self._color_anim.setDuration(600)
        self._color_anim.valueChanged.connect(self.set_color)

    def _reverse_radius_animation(self):
        direction = self._radius_anim.direction()
        if direction == QPropertyAnimation.Direction.Forward:
            self._radius_anim.setDirection(QPropertyAnimation.Direction.Backward)
        else:  # inserted
            self._radius_anim.setDirection(QPropertyAnimation.Direction.Forward)
        self._radius_anim.start()

    def _reverse_opacity_animation(self):
        direction = self._opacity_anim.direction()
        if direction == QPropertyAnimation.Direction.Forward:
            self._opacity_anim.setDirection(QPropertyAnimation.Direction.Backward)
        else:  # inserted
            self._opacity_anim.setDirection(QPropertyAnimation.Direction.Forward)
        self._opacity_anim.start()

    def show_notification(self, message, bg_color='#000000', text_color='#ffffff', duration=10000):
        QTimer.singleShot(0, lambda: FloatingNotification(self, message, duration, bg_color, text_color))

    def set_active(self, is_active: bool):
        if is_active:
            self.setToolTip('Engine Status: ONLINE - Model Loaded.')
            self.show_notification('Model Loaded.')
            self._color_anim.setDirection(QVariantAnimation.Direction.Forward)
            self._color_anim.start()
            self._radius_anim.setDirection(QPropertyAnimation.Direction.Forward)
            self._radius_anim.start()
            self._opacity_anim.setDirection(QPropertyAnimation.Direction.Forward)
            self._opacity_anim.start()
        else:  # inserted
            self.setToolTip('Engine Status: OFFLINE - Please Loaded A Model, Click to Auto Run Last Loaded Model.')
            self.show_notification('NO Model Loaded, Please Loaded A Model.')
            self._color_anim.setDirection(QVariantAnimation.Direction.Backward)
            self._color_anim.start()
            self._radius_anim.finished.disconnect(self._reverse_radius_animation)
            self._opacity_anim.finished.disconnect(self._reverse_opacity_animation)
            self._radius_anim.stop()
            self._opacity_anim.stop()
            self._radius = 5
            self._opacity = 1.0
            self.update()
            self._radius_anim.finished.connect(self._reverse_radius_animation)
            self._opacity_anim.finished.connect(self._reverse_opacity_animation)

    def set_color(self, color: QColor):
        self._color = color
        self.update()

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value
        self.update()

    def get_opacity(self):
        return self._opacity

    def set_opacity(self, value):
        self._opacity = value
        self.update()
    radius = pyqtProperty(int, fget=get_radius, fset=set_radius)
    opacity = pyqtProperty(float, fget=get_opacity, fset=set_opacity)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        center = self.rect().center()
        glow_color = QColor(self._color)
        glow_color.setAlphaF(0.15 * self._opacity)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(glow_color))
        painter.drawEllipse(center, int(self._radius + 2), int(self._radius + 2))
        painter.setOpacity(self._opacity)
        painter.setBrush(QBrush(self._color))
        painter.drawEllipse(center, self._radius, self._radius)

    def handle_command_result(self, result):
        def tts_and_playback(text):
            output_file = os.path.abspath('output.mp3')

            async def generate_tts():
                communicate = Communicate(text=text, voice='en-US-JennyNeural', rate='+20%')
                await communicate.save(output_file)
            asyncio.run(generate_tts())
            while True:  # inserted
                while not (os.path.exists(output_file) and os.path.getsize(output_file) > 0):
                    time.sleep(0.1)
            try:
                pygame.mixer.quit()
                pygame.mixer.init()
                pygame.mixer.music.load(output_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            except Exception as e:
                write_to_log(f'[Error during playback] {e}', file_path='logs/errors.log')
            finally:  # inserted
                try:
                    pygame.mixer.music.stop()
                    pygame.mixer.quit()
                except:
                    pass
            if os.path.exists(output_file):
                try:
                    os.remove(output_file)
                except Exception as e:
                    write_to_log(f'[Error deleting output file] {e}', file_path='logs/errors.log')
            else:  # inserted
                pass  # postinserted
            try:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            except:
                pass
            os.path.exists(output_file) and os.remove(output_file)
        icon_path101 = find_icon('NectarX.ico')
        tooltip_text = (
            f'<img src="{icon_path101}" width="32" height="32" '
            f'style="vertical-align:middle; margin-right:30px;">'
            f'<span style="font-size:20px; margin-left:30px; font-weight:bold; '
            f'display:inline-block; text-align:center; width:100%;">Nectar-X-Studio</span>'
            f'<br>{result}'
        )

        threading.Thread(target=tts_and_playback, args=(result,), daemon=True).start()
        tooltip = PersistentTooltip(tooltip_text, self)
        global_pos = self.output.mapToGlobal(QPoint(0, -tooltip.height()))
        tooltip.show_for_duration(global_pos, duration_ms=300000)

    def closeEvent(self, event):
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()
        event.accept()

class CommandTooltip(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Tool)
        self.setWindowTitle('Command Tooltip')
        self.setFixedSize(320, 140)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(12)
        self.text_label = QLabel(text, self)
        self.text_label.setWordWrap(True)
        self.text_label.setFont(QFont('Consolas', 11))
        self.text_label.setStyleSheet('\n            QLabel {\n                color: #f0f0f0;\n            }\n        ')
        layout.addWidget(self.text_label)
        self.setLayout(layout)
        self.setStyleSheet('\n            QWidget {\n                background-color: #1b1b1b;\n                border: 2px solid #1b1b1b;\n                border-radius: 8px;\n            }\n        ')

    def show_tooltip(self, position):
        self.move(position)
        self.show()
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import pyqtSignal

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._is_clicked = False

    def mousePressEvent(self, event):
        self._is_clicked = not self._is_clicked
        self.clicked.emit()
        super().mousePressEvent(event)

    def isClicked(self):
        return self._is_clicked

    def setClicked(self, value: bool):
        self._is_clicked = value
HISTORY_FILE = 'search_history.json'
MAX_HISTORY = 5
DEFAULT_SUGGESTIONS = ['cmd', 'notepad', 'control panel', 'task manager', 'settings', 'chrome', 'edge', 'word', 'device manager']

def find_icon(icon_name):
    """Attempts to find the icon in and out of the script\'s directory."""  # inserted
    script_dir = os.path.dirname(os.path.realpath(__file__))
    possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    else:  # inserted
        return None
    
# ----------------------- DOWNLOAD THREAD -----------------------

class DownloadThread(QThread):
    progress_changed = pyqtSignal(int)
    eta_changed = pyqtSignal(str)
    state_changed = pyqtSignal(str)   # running, paused, cancelled, done
    download_done = pyqtSignal(str)

    def __init__(self, url, output_path):
        super().__init__()
        self.url = url
        self.output_path = output_path
        self.paused = False
        self.cancelled = False

    def pause(self):
        self.paused = True
        self.state_changed.emit("paused")

    def resume(self):
        self.paused = False
        self.state_changed.emit("running")

    def cancel(self):
        self.cancelled = True
        self.state_changed.emit("cancelled")

    def run(self):
        response = requests.get(self.url, stream=True)
        total = int(response.headers.get("content-length", 0))

        downloaded = 0
        chunk_size = 1024 * 512  # 512 KB
        start_time = time.time()

        with open(self.output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if self.cancelled:
                    try:
                        os.remove(self.output_path)
                    except:
                        pass
                    return

                while self.paused:
                    time.sleep(0.2)
                    if self.cancelled:
                        return

                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)

                    progress = int((downloaded / total) * 100)
                    self.progress_changed.emit(progress)

                    elapsed = time.time() - start_time
                    speed = downloaded / elapsed if elapsed > 0 else 1
                    eta = (total - downloaded) / speed
                    self.eta_changed.emit(f"ETA: {int(eta)}s")

        self.download_done.emit(self.output_path)
        self.state_changed.emit("done")


# ----------------------- DOWNLOAD CARD -----------------------

class DownloadCard(QFrame):
    def __init__(self, filename, url, manager_callback_start):
        super().__init__()

        self.filename = filename
        self.url = url
        self.output_path = os.path.join(os.getcwd(), filename)
        self.thread = None
        self.manager_callback_start = manager_callback_start

        # ---- Unified card background ----
        self.setStyleSheet("""
            QFrame {
                background-color: #000000;
                border-radius: 12px;
                padding: 12px;
            }
            QLabel, QProgressBar, QPushButton {
                background: transparent;    /* inner widgets transparent */
            }
            QLabel {
                color: white;
                font-size: 13px;
            }
            QProgressBar {
                background-color: #1e1e1e;
                border: transparent;
                border-radius: 4px;
                text-align: center;
                color: #444444;
                font-weight: bold;
            }

            QProgressBar::chunk {
                background-color: #6e6e6e;
                color: #ffffff;
                border-radius: 4px;
            }
            QPushButton {
                color: white;
                font-size: 12px;
                border-radius: 6px;
                padding: 6px 12px;
                border: transparent;
            }
            QPushButton:hover { background-color: #333; }
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 12)

        # ---- File label ----
        self.label_name = QLabel(f"{filename}")
        layout.addWidget(self.label_name)

        # ---- Progress bar ----
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        layout.addWidget(self.progress)

        # ---- ETA label ----
        self.label_eta = QLabel("ETA: calculating...")
        layout.addWidget(self.label_eta)

        # ---- Buttons ----
        btn_layout = QHBoxLayout()
        self.btn_pause = QPushButton("Pause")
        self.btn_pause.clicked.connect(self.pause_download)
        self.btn_resume = QPushButton("Resume")
        self.btn_resume.clicked.connect(self.resume_download)
        self.btn_resume.hide()
        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.clicked.connect(self.cancel_download)

        btn_layout.addWidget(self.btn_pause)
        btn_layout.addWidget(self.btn_resume)
        btn_layout.addWidget(self.btn_cancel)
        layout.addLayout(btn_layout)

        # ---- Start download automatically ----
        self.start_download()

    # ------------------ THREAD CONTROL ---------------------
    def start_download(self):
        self.thread = self.manager_callback_start(self.url, self.output_path)
        self.thread.progress_changed.connect(self.progress.setValue)
        self.thread.eta_changed.connect(self.label_eta.setText)
        self.thread.state_changed.connect(self.on_state_changed)
        self.thread.download_done.connect(self.on_done)

    def pause_download(self):
        if self.thread:
            self.thread.pause()

    def resume_download(self):
        if self.thread:
            self.thread.resume()

    def cancel_download(self):
        if self.thread:
            self.thread.cancel()
            self.label_eta.setText("Cancelled")
            self.progress.setValue(0)

    # ------------------ STATE EVENTS -----------------------
    @pyqtSlot(str)
    def on_state_changed(self, state):
        if state == "paused":
            self.btn_pause.hide()
            self.btn_resume.show()
            self.label_eta.setText("Paused")
        elif state == "running":
            self.btn_resume.hide()
            self.btn_pause.show()
        elif state == "cancelled":
            self.btn_pause.hide()
            self.btn_resume.hide()
            self.btn_cancel.hide()
            self.label_eta.setText("Cancelled")
        elif state == "done":
            self.btn_pause.hide()
            self.btn_resume.hide()
            self.btn_cancel.hide()

    @pyqtSlot(str)
    def on_done(self, filepath):
        self.label_eta.setText("Complete")
        self.progress.setValue(100)
        try:
            os.startfile(filepath)
        except:
            pass


# ----------------------- DOWNLOAD MANAGER -----------------------

class DownloadManager(QWidget):
    def __init__(self):
        super().__init__()
        # Set this widget as a dialog window
        self.setWindowTitle("Nectar-X-Client")
        self.setFixedSize(400, 450)
        self.setWindowOpacity(0.95)
        self.setWindowIcon(QIcon(find_icon('background/NectarX.png') or 'background/NectarX.png'))
        self.setWindowFlags(Qt.WindowType.Dialog)
        #self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Make window transparent
        self.setStyleSheet("""
            QWidget {
                background-color: transparent
                border: transparent;
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

        # Main layout
        layout = QVBoxLayout(self)

        # Scroll area for download cards
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll.setWidget(self.container)
        layout.addWidget(self.scroll)

        # Thread reference list
        self.threads = []

    def start_thread(self, url, output_path):
        thread = DownloadThread(url, output_path)
        self.threads.append(thread)
        thread.start()
        return thread

    def add_download(self, filename, url):
        card = DownloadCard(filename, url, self.start_thread)
        self.container_layout.addWidget(card)

from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSlot

class RunnableTask(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)
from PyQt6.QtWidgets import QMainWindow, QPushButton

class DetachableWebView(QWidget):
    def __init__(self, title, url, zoom_key, url_key, parent_assets, download_info=None):
        super().__init__()
        self.parent_assets = parent_assets
        self.title = title
        self.url = url
        self.zoom_key = zoom_key
        self.url_key = url_key
        self.download_info = download_info  # store download info
        self.layout = QVBoxLayout(self)
        header_layout = QHBoxLayout()
        self.label = QLabel(title)
        self.label.setStyleSheet('color: white; font-size: 14pt; font-weight: bold;')
        header_layout.addWidget(self.label)

        self.download_button = QPushButton('Download')
        self.download_button.setFixedWidth(80)
        self.download_button.clicked.connect(self.download_file)
        self.download_button.setStyleSheet('\n            QPushButton {\n                background-color: #111111;\n                color: #ffffff;\n                border: 1px solid #444444;\n                border-radius: 6px;\n                padding: 6px 12px;\n                font-size: 12px;\n                font-weight: bold;\n                font-family: Consolas, monospace;\n            }\n            QPushButton:hover {\n                background-color: #222222;\n                border: 1px solid #666666;\n                color: cyan;\n            }\n            QPushButton:pressed {\n                background-color: #000000;\n                border: 1px solid #888888;\n            }\n        ')
        header_layout.addWidget(self.download_button)

        self.detach_button = QPushButton('Detach')
        self.detach_button.setFixedWidth(70)
        self.detach_button.clicked.connect(self.toggle_detach)
        self.detach_button.setStyleSheet('\n            QPushButton {\n                background-color: #111111;\n                color: #ffffff;\n                border: 1px solid #444444;\n                border-radius: 6px;\n                padding: 6px 12px;\n                font-size: 12px;\n                font-weight: bold;\n                font-family: Consolas, monospace;\n            }\n            QPushButton:hover {\n                background-color: #222222;\n                border: 1px solid #666666;\n                color: cyan;\n            }\n            QPushButton:pressed {\n                background-color: #000000;\n                border: 1px solid #888888;\n            }\n        ')
        header_layout.addWidget(self.detach_button)
        
        self.layout.addLayout(header_layout)
        self.web_view = QWebEngineView(self.parent_assets.web_profile)
        self.web_view.setMinimumHeight(300)
        self.layout.addWidget(self.web_view)
        last_url = self.parent_assets.settings.value(f'news/{url_key}', url)
        zoom_level = float(self.parent_assets.settings.value(f'news/{zoom_key}', 1.0))
        self.web_view.setZoomFactor(zoom_level)
        self.web_view.load(QUrl(last_url))
        self.web_view.urlChanged.connect(lambda url: self.parent_assets.settings.setValue(f'news/{url_key}', url.toString()))
        self.web_view.page().zoomFactorChanged.connect(lambda z: self.parent_assets.settings.setValue(f'news/{zoom_key}', z))
        self.detached_window = None
        self.download_manager = None

        # --- Internet check ---
        self.check_internet()
        self.internet_timer = QTimer()
        self.internet_timer.timeout.connect(self.check_internet)
        self.internet_timer.start(5000)  # check every 5 seconds

    def is_connected(self, host="8.8.8.8", port=53, timeout=3):
        """Check internet connection by trying to connect to Google DNS."""
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except Exception:
            return False

    def check_internet(self):
        if self.download_info:
            connected = self.is_connected()
            self.download_button.setEnabled(connected)
            if connected:
                self.download_button.setToolTip("")  # clear tooltip
            else:
                self.download_button.setToolTip("No internet connection")

    def download_file(self):
        if not self.download_info:
            print("No download info provided for this web view.")
            return
        if not self.download_manager:
            self.download_manager = DownloadManager()
        self.download_manager.show()
        self.download_manager.add_download(self.download_info['filename'], self.download_info['url'])

    def toggle_detach(self):
        if self.detached_window is None:
            self.layout.removeWidget(self.web_view)
            self.web_view.setParent(None)
            self.detached_window = QMainWindow()
            self.detached_window.setWindowTitle(self.title)
            self.detached_window.resize(800, 600)
            self.detached_window.setCentralWidget(self.web_view)
            self.detached_window.show()
            icon_path = find_icon('background/NectarX.png')
            if icon_path:
                self.detached_window.setWindowIcon(QIcon(icon_path))
            else:  # inserted
                self.detached_window.setWindowIcon(QIcon('background/NectarX.png'))
                self.detach_button.setText('Dock')
                self.hide()
            self.detached_window.closeEvent = self.handle_detached_close
        else:  # inserted
            self.web_view.setParent(self)
            self.layout.addWidget(self.web_view)
            self.show()
            self.detached_window.hide()
            self.detached_window.deleteLater()
            self.detached_window = None
            self.detach_button.setText('Detach')

    def handle_detached_close(self, event):
        self.web_view.setParent(self)
        self.layout.addWidget(self.web_view)
        self.show()
        self.detach_button.setText('Detach')
        self.detached_window = None
        event.accept()
        
from PyQt6.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt6.QtWebEngineCore import QWebEngineUrlRequestInterceptor

class BlockTrackerInterceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        url = info.requestUrl().toString().lower()
        blocklist = ['https://donate.python.org/', 'doubleclick.net', 'google-analytics.com', 'googletagmanager.com', 'googlesyndication.com', 'googleadservices.com', 'adsafeprotected.com', 'adnxs.com', 'ads.yahoo.com', 'ads.twitter.com', 'ads.pubmatic.com', 'adform.net', 'adzerk.net', 'criteo.com', 'rubiconproject.com', 'scorecardresearch.com', 'quantserve.com', 'facebook.net', 'facebook.com/tr', 'connect.facebook.net', 'fbcdn.net', 'taboola.com', 'outbrain.com', 'moatads.com', 'zopim.com', 'hotjar.com', 'newrelic.com', 'optimizely.com', 'segment.com', 'tracking', 'track', 'ad.', '/ads?', '/ads/', 'pixel.', 'tracker.', 'log.doubleclick.net', 'pagead2.googlesyndication.com', 'bam.nr-data.net', 'cdn.heapanalytics.com']
        if any((domain in url for domain in blocklist)):
            info.block(True)

class StatusDot(QWidget):
    def __init__(self, diameter=10):
        super().__init__()
        self.diameter = diameter
        self.color = QColor('#d9534f')
        self.setFixedSize(diameter, diameter)

    def set_color(self, color_name):
        self.color = QColor(color_name)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(self.color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, self.diameter, self.diameter)

class StatusBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(50)
        self.setStyleSheet('\n            background-color: #1c1c1c;\n            color: #e0e0e0;\n            font-family: \'Segoe UI\', sans-serif;\n        ')
        layout = QHBoxLayout()
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(25)
        self.setLayout(layout)
        self.cpu_bar = self.create_metric_widget('CPU')
        layout.addWidget(self.cpu_bar['frame'])
        self.ram_bar = self.create_metric_widget('RAM')
        layout.addWidget(self.ram_bar['frame'])
        self.net_status_dot = StatusDot()
        self.net_status_label = QLabel('Network...')
        self.net_status_label.setFont(QFont('Segoe UI', 9, QFont.Weight.Normal))
        self.net_status_label.setStyleSheet('color: #bbbbbb;')
        net_layout = QHBoxLayout()
        net_layout.setSpacing(6)
        net_layout.setContentsMargins(10, 0, 10, 0)
        net_layout.addWidget(self.net_status_dot)
        net_layout.addWidget(self.net_status_label)
        net_frame = QFrame()
        net_frame.setLayout(net_layout)
        net_frame.setStyleSheet('\n            background-color: #000000;\n            border-radius: 6px;\n        ')
        net_frame.setFixedSize(200, 30)
        layout.addWidget(net_frame)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)

    def create_metric_widget(self, name):
        frame = QFrame()
        frame.setStyleSheet('\n            background-color: #000000;\n            border-radius: 6px;\n        ')
        frame.setFixedSize(140, 30)
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(8)
        frame.setLayout(layout)
        label = QLabel(name)
        label.setFont(QFont('Segoe UI', 9))
        label.setStyleSheet('color: #bbbbbb;')
        progress = QProgressBar()
        progress.setRange(0, 100)
        progress.setValue(0)
        progress.setTextVisible(False)
        progress.setFixedHeight(8)
        progress.setStyleSheet("""
            QProgressBar {
                background-color: #1c1c1c;
                border-radius: 4px;
            }
            QProgressBar::chunk {
                background-color: #ffffff;
                border-radius: 4px;
            }
        """)
        layout.addWidget(label)
        layout.addWidget(progress)
        return {'frame': frame, 'label': label, 'progress': progress}

    def update_metrics(self):
        self.cpu_bar['progress'].setValue(int(psutil.cpu_percent()))
        self.ram_bar['progress'].setValue(int(psutil.virtual_memory().percent))
        net_info = self.get_network_status()
        if net_info['connected']:
            self.net_status_dot.set_color('#ffffff')
            self.net_status_label.setText(f"{net_info['iface_name']}")
        else:  # inserted
            self.net_status_dot.set_color('#d9534f')
            self.net_status_label.setText('No Network')

    def get_network_status(self):
        try:
            addrs = psutil.net_if_addrs()
            stats = psutil.net_if_stats()
            for iface_name, iface_addrs in addrs.items():
                if iface_name.lower().startswith('loopback') or iface_name == 'lo':
                    continue
                if iface_name not in stats or not stats[iface_name].isup:
                    continue
                has_ip = any((snic.family in (socket.AF_INET, socket.AF_INET6) for snic in iface_addrs))
                if has_ip:
                    return {'connected': True, 'iface_name': iface_name}
            else:  # inserted
                return {'connected': False, 'iface_name': None}
        except Exception:
            return {'connected': False, 'iface_name': None}

class Loader1(QWidget):
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

            # ✅ Cast to int for PyQt6 compatibility
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

from PyQt6.QtCore import QThread, pyqtSignal
import socket

class ChatWorker6(QThread):
    result_signal = pyqtSignal(str)  # ✅ define signal

    def __init__(self, user_command):
        super().__init__()
        self.user_command = user_command

    def run(self):
        reply = send_to_AlphaLLM(self.user_command)

        # Emit response back to the main thread
        self.result_signal.emit(reply)

class PersistentTooltip(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet('''
            QLabel {
                background-color: #000000;
                color: #ffffff;
                border: 1px solid None ;  /* gray */
                padding: 8px;
                border-radius: 10px;
                font-size: 14px;
            }
        ''')

        self.setWordWrap(True)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMaximumWidth(400)
        self.setMinimumWidth(200)
        self.setWindowFlags(Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)
        self.adjustSize()
        self._drag_active = False
        self._drag_position = QPoint()
        self.setup_shortcuts()

    def setup_shortcuts(self):
        shortcut = QShortcut(QKeySequence('Ctrl+C'), self)
        shortcut.activated.connect(self.copy_text)

    def copy_text(self):
        raw_text = self.text()
        plain_text = re.sub('<[^>]+>', '', raw_text).strip()
        QGuiApplication.clipboard().setText(plain_text)

    def show_for_duration(self, pos: QPoint, duration_ms=300000):
        self.move(pos)
        self.adjustSize()
        self.show()
        QTimer.singleShot(duration_ms, self.hide)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_active = True
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_active and event.buttons() & Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_active = False
            event.accept()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.hide()
            event.accept()

class ClickableCard(QWidget):
    """A clickable card widget for a folder with icon + label"""
    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = folder_path
        self.folder_name = os.path.basename(folder_path)

        self.setStyleSheet("""
            QWidget {
                background-color: #fefefe;
                border: none;
                border-radius: 8px;
                padding: 10px;
            }
            QWidget:hover {
                background-color: #f0f0f0;
            }
        """)

        # Reduced spacing in layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.setContentsMargins(5, 5, 5, 5)  # smaller margins
        layout.setSpacing(2)  # reduce spacing between icon and label
        self.setLayout(layout)

        # --- Icon ---
        icon_path = ICON_MAPPING.get(self.folder_name, DEFAULT_ICON)
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path).scaled(
                48, 48, Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        else:
            pixmap = QPixmap(DEFAULT_ICON).scaled(
                48, 48, Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

        icon_label = QLabel()
        icon_label.setPixmap(pixmap)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(icon_label)

        # --- Folder name label ---
        text_label = QLabel(self.folder_name)
        text_label.setStyleSheet("background-color: transparent; font-size: 9px; color: orange; margin: 0px;")
        text_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(text_label)

        # Make the card expand in width
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

    def mousePressEvent(self, event):
        """Open folder when card is clicked"""
        if os.path.exists(self.folder_path):
            subprocess.Popen(f'explorer "{self.folder_path}"')

class ChildWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        # Keep title bar, allow closing, but prevent independent dragging
        self.setWindowFlags(
            Qt.WindowType.SubWindow |
            Qt.WindowType.Window |
            Qt.WindowType.WindowTitleHint |
            Qt.WindowType.WindowCloseButtonHint     
        )

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setFixedSize(200, 550)
        self.setStyleSheet("""
            QWidget {
                background-color: #20201f;
                border: transparent;
                border-radius: 12px;
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
        """)

        self.setWindowTitle("      ")

        # Layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        package_card = QWidget()
        package_card.setStyleSheet("background-color: #eeeee4; padding: 4px 8px; border-radius: 6px;")
        package_layout = QVBoxLayout(package_card)
        #package_layout.setContentsMargins(0, 0, 0, 0)

        # Grid layout
        self.scroll_layout = QGridLayout()
        self.scroll_layout.setSpacing(0)

        # Wrap inside a QWidget
        scroll_container = QWidget()
        scroll_container.setLayout(self.scroll_layout)

        # Add the container to the package layout
        package_layout.addWidget(scroll_container)

        layout.addWidget(package_card)

        self.add_code_block(layout, "NectarGraphix")

        layout.addStretch(10)

        # Button row
        self.installed_tab_btn_layout = QHBoxLayout()
        layout.addLayout(self.installed_tab_btn_layout)

        icon_path_refresh = find_icon("background/main.png")
        side_btn1 = QPushButton()
        side_btn1.setIcon(QIcon(icon_path_refresh))
        side_btn1.setStyleSheet("""
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
        side_btn1.setFixedSize(50, 50)
        side_btn1.clicked.connect(self.open_settings)
        self.installed_tab_btn_layout.addWidget(side_btn1, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        # Refresh button
        icon_path_refresh = find_icon("background/mini.png")
        side_btn2 = QPushButton()
        side_btn2.setIcon(QIcon(icon_path_refresh))
        side_btn2.setFixedSize(50, 50)
        side_btn2.clicked.connect(lambda: self.Hidden())
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
        self.installed_tab_btn_layout.addWidget(side_btn2, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        # Refresh button
        icon_path_refresh = find_icon("background/settings.png")
        side_btn3 = QPushButton()
        side_btn3.setIcon(QIcon(icon_path_refresh))
        side_btn3.setFixedSize(50, 50)
        side_btn3.clicked.connect(lambda: open_link("https://github.com/headlessripper/Nectar-X-Studio"))
        side_btn3.setStyleSheet("""
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
        self.installed_tab_btn_layout.addWidget(side_btn3, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        layout.addStretch()

        # Set dark background for main window
        self.setStyleSheet("background-color: #121212;")

        
        self.scan_folders()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.update_position()

    def add_code_block(self, parent_layout, code_text: str):
        # Container widget
        code_container = QWidget()
        code_layout = QHBoxLayout(code_container)
        code_layout.setContentsMargins(10, 8, 10, 8)
        code_layout.setSpacing(6)

        # Code label
        code_label = QLabel(code_text)
        code_label.setFont(QFont("Consolas", 10))
        code_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        code_label.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: white;
            }
        """)

        # Copy button
        copy_button = QPushButton("Copy")
        copy_button.setCursor(Qt.CursorShape.PointingHandCursor)
        copy_button.setFixedHeight(24)
        copy_button.setStyleSheet("""
            QPushButton {
                padding: 0 10px;
                border-radius: 6px;
                background-color: #000000;
                color: white;
                font-size: 10px;
                border: None;
            }
            QPushButton:hover {
                background-color: #2d2d2d;
            }
            QPushButton:pressed {
                background-color: #1e1e1e;
            }
        """)

        def copy_code():
            QGuiApplication.clipboard().setText("pip install NectarGraphix")
            copy_button.setText("Copied")
            QTimer.singleShot(1200, lambda: copy_button.setText("Copy"))

        copy_button.clicked.connect(copy_code)

        # Outer container style (code block)
        code_container.setStyleSheet("""
            QWidget {
                background-color: #000000;
                border-radius: 8px;
                border: None;
            }
        """)

        code_layout.addWidget(code_label, stretch=1)
        code_layout.addWidget(copy_button, 0, Qt.AlignmentFlag.AlignRight)

        parent_layout.addWidget(code_container)

    def open_settings(self):
        # Prevent reopening multiple times
        if hasattr(self, "settings_widget") and self.settings_widget.isVisible():
            return

        # Create a small internal settings widget
        self.settings_widget = QWidget(self)
        self.settings_widget.setWindowTitle("  ")
        self.settings_widget.setWindowIcon(QIcon(find_icon('background/NectarX.png') or 'background/NectarX.png'))
        self.settings_widget.setFixedSize(300, 220)
        self.settings_widget.setWindowFlags(Qt.WindowType.Dialog)
        #self.settings_widget.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        #self.settings_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
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

        # Close button
        contact_button = QPushButton("Python")
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
        contact_button.clicked.connect(lambda: self.Python_insta())
        layout.addWidget(contact_button)

        license_button = QPushButton("Terminal")
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
        license_button.clicked.connect(lambda: self.open_terminal())
        layout.addWidget(license_button)

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

    def close(self):
        self.fade_out_settings()

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

    def Hidden(self):
        app_name = "Hidden/Hidden.exe"
        app_path = find_utils4(app_name)

        if not app_path:
            Notify(f"Application '{app_name}' not found.", parent=self)
            return

        if not os.path.exists(app_path):
            Notify(f"Application path does not exist: {app_path}", parent=self)
            return

        try:
            if sys.platform == "darwin":  # macOS
                if app_path.endswith(".app"):
                    # Use 'open' to launch .app bundles
                    subprocess.Popen(["open", app_path])
                else:
                    subprocess.Popen([app_path])
            elif sys.platform == "win32":  # Windows
                subprocess.Popen([app_path])
            else:  # Linux / other Unix-like
                subprocess.Popen([app_path])
        except FileNotFoundError:
            Notify(f"Application not found at path: {app_path}", parent=self)
        except PermissionError:
            Notify(f"Permission denied when trying to launch: {app_path}", parent=self)
        except Exception as e:
            Notify(f"Unexpected error launching '{app_name}': {e}", parent=self)

    def Python_insta(self):
        app_name = "Python/python-3.11.0-amd64.exe"
        app_path = find_utils4(app_name)

        if not app_path:
            Notify(f"Application '{app_name}' not found.", parent=self)
            return

        if not os.path.exists(app_path):
            Notify(f"Application path does not exist: {app_path}", parent=self)
            return

        try:
            if sys.platform == "darwin":  # macOS
                if app_path.endswith(".app"):
                    # Use 'open' to launch .app bundles
                    subprocess.Popen(["open", app_path])
                else:
                    subprocess.Popen([app_path])
            elif sys.platform == "win32":  # Windows
                subprocess.Popen([app_path])
            else:  # Linux / other Unix-like
                subprocess.Popen([app_path])
        except FileNotFoundError:
            Notify(f"Application not found at path: {app_path}", parent=self)
        except PermissionError:
            Notify(f"Permission denied when trying to launch: {app_path}", parent=self)
        except Exception as e:
            Notify(f"Unexpected error launching '{app_name}': {e}", parent=self)

    def open_terminal(self):
        # Open Windows File Explorer at "This PC"
        try:
            subprocess.Popen(["cmd.exe", os.path.expanduser("~")])
        except Exception as e:
            Notify(f"Error opening File cmd.exe: {e}", parent=self )

    def scan_folders(self):
        """Scan Program Files for Nectar folders and display them as clickable cards"""
        # Clear previous cards
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        folders = find_exact_nectar_folders(PROGRAM_FILES_DIRS)
        if folders:
            row = 0
            col = 0
            for folder in folders:
                card = ClickableCard(folder)
                card.setFixedSize(76, 108)  # uniform size
                self.scroll_layout.addWidget(card, row, col)
                col += 1
                if col >= 2:  # 2 cards per row
                    col = 0
                    row += 1
        else:
            label = QLabel("No Nectar folders found (excluding " + ", ".join(EXCLUDED_FOLDERS) + ").")
            label.setStyleSheet("font-style: italic; margin: 10px; color: white;")
            self.scroll_layout.addWidget(label, 0, 0)

    def update_position(self):
        """Always stay to the right of the parent with the gap."""
        parent_geom = self.parent_window.geometry()
        x = parent_geom.x() + parent_geom.width() + HORIZONTAL_GAP
        y = parent_geom.y()
        width = parent_geom.width()
        height = parent_geom.height()
        self.setGeometry(x, y, width, height)

    def moveEvent(self, event):
        """Prevent independent dragging by snapping to parent"""
        self.update_position()
        super().moveEvent(event)

    def showEvent(self, event):
        """Ensure child stays above parent when shown"""
        self.raise_()
        super().showEvent(event)

class Assets(QWidget):
    def __init__(self, max_apps=30):
        super().__init__()
        self.setWindowTitle('Nectar-X-Client')
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowCloseButtonHint)
        self.setWindowOpacity(0.93)
        self.setGeometry(400, 100, 700, 550)
        self.search_history = self.load_history()
        self.setup_ui()
        self.setup_autocomplete()
        self.typing_timer = QTimer()
        self.typing_timer.setInterval(0)
        self.typing_timer.timeout.connect(self.fetch_web_suggestions)
        icon_path = find_icon('background/NectarX.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:  # inserted
            self.setWindowIcon(QIcon('background/NectarX.png'))
        self.threadpool = QThreadPool.globalInstance()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.search_history = self.load_history()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Search')
        self.search_input.setTextMargins(30, 0, 0, 0)

        icon_path_search = find_icon('background/NectarX.png')

        self.icon_button = QToolButton(self.search_input)
        self.icon_button.setIcon(QIcon(icon_path_search))
        self.icon_button.setIconSize(QSize(32, 32))
        self.icon_button.setCursor(Qt.CursorShape.ArrowCursor)
        self.icon_button.setStyleSheet('QToolButton { border: none; padding: 0px; }')
        self.icon_button.setEnabled(True)

        def center_icon():
            icon_x = 5
            icon_y = (self.search_input.height() - self.icon_button.height()) // 2
            self.icon_button.move(icon_x, icon_y)

        def resize_event_override(event):
            center_icon()
            QLineEdit.resizeEvent(self.search_input, event)
        self.search_input.resizeEvent = resize_event_override
        self.search_input.returnPressed.connect(self.run_search_thread)
        self.search_input.textChanged.connect(self.on_text_changed)
        self.completer_model = QStringListModel()
        self.completer = QCompleter(self.completer_model, self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.search_input.setCompleter(self.completer)
        self.completer.popup().setStyleSheet('\n            QListView {\n                background-color: #0f0f0f;\n                color: white;\n                border: 1px solid #444;\n                font-size: 13px;\n                font-family: Consolas, monospace;\n                padding: 2px;\n                outline: none;\n                show-decoration-selected: 1;\n            }\n\n            QListView::item {\n                padding: 8px 12px;\n                border-bottom: 1px solid #222;\n            }\n\n            QListView::item:selected {\n                background-color: #222;\n                color: cyan;\n            }\n\n            QListView::item:hover {\n                background-color: #1a1a1a;\n            }\n        ')
        self.search_input.setStyleSheet('\n            QLineEdit {\n                background-color: #000000;\n                color: white;\n                padding: 12px 20px;\n                border-radius: 5px;\n                font-size: 14px;\n            }\n            QLineEdit:hover {\n                background-color: #171616;\n            }\n        ')
        layout = QHBoxLayout()
        layout.addWidget(self.search_input)
        main_layout.addLayout(layout)
        quick_access_layout = QHBoxLayout()
        quick_access_layout.setSpacing(10)

        def create_quick_button(icon_path, callback):
            btn = QPushButton()
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(32, 32))
            btn.setFixedSize(48, 48)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(self.icon_button_stylesheet())
            btn.clicked.connect(callback)
            return btn
        
        main_layout.addLayout(quick_access_layout)

        interceptor = BlockTrackerInterceptor()
        #sys.stderr = open(os.devnull, 'w')
        os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = (
            '--disable-features=InterestCohortAPI,TrackingProtection '
            '--enable-popup-blocking --enable-features=AllowPopupsForUserActivation'
            #'--disable-3d-apis --disable-webgl --disable-notifications '
            #'--disable-background-networking --disable-sync --disable-logging '
            #'--disable-domain-reliability --disable-default-apps '
            #'--disable-webrtc '
            '--enable-features="DnsOverHttps" '
            '--dns-over-https-mode=secure '
            '--dns-over-https-templates=https://cloudflare-dns.com/dns-query'
            '--disable-features=PaymentRequest'
        )

        #os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '0.0.0.0:9222'
        #os.environ['QTWEBENGINE_DICTIONARIES_PATH'] = os.path.join(os.getcwd(), 'dummy_dictionaries')
        #os.makedirs('dummy_dictionaries', exist_ok=True)

        # --- Profile setup ---
        self.settings = QSettings('Zashiron', 'NewsPreference')
        persistent_profile_path = os.path.join(os.getcwd(), 'web_profile')
        persistent_cache_path = os.path.join(os.getcwd(), 'web_profile/cache')
        os.makedirs(persistent_profile_path, exist_ok=True)

        self.web_profile = QWebEngineProfile('Default', self)
        self.web_profile.setPersistentStoragePath(persistent_profile_path)
        self.web_profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)
        self.web_profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.DiskHttpCache)
        self.web_profile.setCachePath(persistent_cache_path)
        self.web_profile.setHttpCacheMaximumSize(0)
        self.web_profile.setHttpUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                                        'Chrome/125.0.6422.112 Safari/537.36 Referrer-Policy: no-referrer')

        settings = self.web_profile.settings()

        self.web_profile.setUrlRequestInterceptor(interceptor)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled, True)
        settings.setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptCanOpenWindows, True
        )
        settings.setAttribute(
            QWebEngineSettings.WebAttribute.JavascriptCanAccessClipboard, True
        )

        # Remove “webdriver” fingerprint
        script = QWebEngineScript()
        script.setInjectionPoint(QWebEngineScript.InjectionPoint.DocumentReady)
        script.setSourceCode("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
        self.web_profile.scripts().insert(script)
        
        last_url = self.settings.value('news/last_url', 'https://github.com/headlessripper/Nectar-X-Studio/wiki')
        zoom_level = float(self.settings.value('news/zoom', 1.0))
        news_container = QWidget()
        news_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        news_layout = QVBoxLayout(news_container)
        news_layout.setSpacing(20)
        # Try to check/start the browser agent, but continue even if it fails
        try:
            check_browser_agent()
        except Exception as e:
            print(f"[Warning] ChatServe not found or failed to start: {e}")
            # Continue running the app regardless

        def create_quick_button(icon_path, callback):
            btn = QPushButton()
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(32, 32))
            btn.setFixedSize(48, 48)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(self.icon_button_stylesheet())
            btn.clicked.connect(callback)
            return btn
        
        self.btn_mini = create_quick_button(find_icon('background/NectarX.png'), self.open_Nectar)
        self.btn_mid = create_quick_button(find_icon('background/syrup.png'), self.Nectar_X_Model)

        self.dot = AnimatedDot()
        self.dot.setFixedSize(50, 50)
        self.dot.setToolTip('Online Model Status')
        
        self.search_bar = QLineEdit(self)
        self.search_bar.setFixedHeight(50)
        self.search_bar.setPlaceholderText('Ask AI')
        self.search_bar.returnPressed.connect(self.execute_command)
        self.search_bar.setStyleSheet('padding: 10px; font-size: 14px; border-radius: 5px; color: white; background-color: #000000;')
        self.search_bar.setContentsMargins(0, 0, 0, 0)
        news_layout.addWidget(self.search_bar)

        search_layout = QHBoxLayout()
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.addWidget(self.dot, alignment=Qt.AlignmentFlag.AlignCenter)
        search_layout.addWidget(self.search_bar)
        
        self.btn_mini.setToolTip('Nectar-X-Studio')
        search_layout.addWidget(self.btn_mini)
        self.btn_mid.setToolTip('Nectar-X-Engine')
        self.btn_mid.setEnabled(False)
        search_layout.addWidget(self.btn_mid)

        news_layout.addLayout(search_layout)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(StatusBar())
        news_layout.addLayout(layout)

        def create_news_row(left_title, left_url, left_keys):
            row_layout = QHBoxLayout()
            row_layout.setSpacing(15)

            left_col = QVBoxLayout()
            self.add_news_section(left_col, left_title, left_url, *left_keys)
            row_layout.addLayout(left_col)

            #right_col = QVBoxLayout()
            #self.add_news_section(right_col, right_title, right_url, *right_keys)
            #row_layout.addLayout(right_col)
            news_layout.addLayout(row_layout)

       # pending_left = {"title": None, "url": None, "keys": None}

       # def create_news_row(title, url, keys):
        #    nonlocal pending_left

            # If no left saved yet → store this as left
           # if pending_left["title"] is None:
           #     pending_left = {
           #         "title": title,
           #         "url": url,
           #         "keys": keys
           #     }
           #     return  # wait for right side

            # If left already saved → this call becomes RIGHT, build row
           # left = pending_left
            #right = {"title": title, "url": url, "keys": keys}

           # row_layout = QHBoxLayout()
           # row_layout.setSpacing(15)

            # LEFT COLUMN
           # left_col = QVBoxLayout()
           # self.add_news_section(left_col, left["title"], left["url"], *left["keys"])
           # row_layout.addLayout(left_col)

            # RIGHT COLUMN
           # right_col = QVBoxLayout()
           # self.add_news_section(right_col, right["title"], right["url"], *right["keys"])
           # row_layout.addLayout(right_col)

           # news_layout.addLayout(row_layout)

            # Reset pending left for next pair
           # pending_left = {"title": None, "url": None, "keys": None}

        create_news_row('Nectar-X-Studio', 'https://github.com/headlessripper/Nectar-X-Studio/wiki#nectarxstudio--wiki-home', ('nect_zoom', 'nect_url'))
        #create_news_row('NectarGraphix', 'https://pypi.org/project/NectarGraphix',  ('nectG_zoom', 'nectG_url'))

        #self.youtube_detachable = DetachableWebView('YouTube', 'https://www.youtube.com/results?search_query=news', 'yt_zoom', 'yt_url', self)
        #news_layout.addWidget(self.youtube_detachable)
        self.NectarStore_detachable = DetachableWebView(
            title='NectarStore',
            url='https://github.com/headlessripper/PluginStore/releases/tag/v6',
            zoom_key='nectar_store_zoom',
            url_key='nectar_store_url',
            parent_assets=self,
            download_info={
                'filename': 'NectarStore-Setup.exe',
                'url': 'https://github.com/headlessripper/PluginStore/releases/download/v6/NectarStore-Setup.exe'
            }
        )
        self.NectarSTT_detachable = DetachableWebView(
            title='NectarSTT',
            url='https://github.com/headlessripper/PluginStore/releases/tag/v26',
            zoom_key='nectar_stt_zoom',
            url_key='nectar_stt_url',
            parent_assets=self,
            download_info={
                'filename': 'NectarSTT-Setup.exe',
                'url': 'https://github.com/headlessripper/PluginStore/releases/download/v26/NectarSTT-Setup.exe'
            }
        )
        news_layout.addWidget(self.NectarSTT_detachable)
        #news_layout.addWidget(self.ground_detachable)
        news_layout.addWidget(self.NectarStore_detachable)

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet('\n                                QScrollBar:vertical {\n                                background: transparent;\n                                width: 8px;\n                                margin: 0px;\n                                border: none;\n                            }\n\n                            QScrollBar::handle:vertical {\n                                background: #ffffff;\n                                min-height: 20px;\n                                border-radius: 4px;\n                            }\n\n                            QScrollBar::handle:vertical:hover {\n                                background: #1b1b1b;\n                            }\n\n                            QScrollBar::add-line:vertical,\n                            QScrollBar::sub-line:vertical,\n                            QScrollBar::add-page:vertical,\n                            QScrollBar::sub-page:vertical {\n                                background: none;\n                                height: 0px;\n                                border: none;\n                            }\n\n                            /* Horizontal Scrollbar */\n                            QScrollBar:horizontal {\n                                background: transparent;\n                                height: 8px;\n                                margin: 0px;\n                                border: none;\n                            }\n\n                            QScrollBar::handle:horizontal {\n                                background: rgba(0, 0, 0, 0.2);\n                                min-width: 20px;\n                                border-radius: 4px;\n                            }\n\n                            QScrollBar::handle:horizontal:hover {\n                                background: rgba(0, 0, 0, 0.4);\n                            }\n\n                            QScrollBar::add-line:horizontal,\n                            QScrollBar::sub-line:horizontal,\n                            QScrollBar::add-page:horizontal,\n                            QScrollBar::sub-page:horizontal {\n                                background: none;\n                                width: 0px;\n                                border: none;\n                            }\n                            QToolTip {\n                                background-color: #000000;\n                                color: white;\n                                border: 1px solid #444;\n                                padding: 6px;\n                                font-size: 12px;\n                                font-family: Consolas, monospace;\n                                border-radius: 4px;\n                            }\n            ')
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setWidget(news_container)
        end_label = QLabel()
        end_label.setText('By Samuel Ikenna Great')
        end_label.setStyleSheet('color: white;')
        end_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon_path = find_icon('background/NectarX.png')
        if icon_path and os.path.exists(icon_path):
            self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)
            self.tray_icon.show()
        else:
            print("[INFO] Tray icon skipped (icon not found)")
        tray_menu = QMenu()
        restore_action = QAction('Restore', self)
        restore_action.triggered.connect(self.show)
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(QApplication.quit)
        tray_menu.addAction(restore_action)
        tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        main_layout.addWidget(scroll_area)
        main_layout.addWidget(end_label)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_server)
        self.timer.start(3000)
        self.check_server()
        self.setup_overlay()

        # Create child window
        self.child_window = ChildWindow(self)
        self.child_window.show()

    def Nectar_X_Model(self):
        app_name = "Nectar-X-Engine/Nectar-X-Engine.exe"
        app_path = find_utils4(app_name)

        if not app_path:
            Notify(f"Application '{app_name}' not found.", parent=self)
            return

        if not os.path.exists(app_path):
            Notify(f"Application path does not exist: {app_path}", parent=self)
            return

        try:
            if sys.platform == "darwin":  # macOS
                if app_path.endswith(".app"):
                    # Use 'open' to launch .app bundles
                    subprocess.Popen(["open", app_path])
                else:
                    subprocess.Popen([app_path])
            elif sys.platform == "win32":  # Windows
                subprocess.Popen([app_path])
            else:  # Linux / other Unix-like
                subprocess.Popen([app_path])
        except FileNotFoundError:
            Notify(f"Application not found at path: {app_path}", parent=self)
        except PermissionError:
            Notify(f"Permission denied when trying to launch: {app_path}", parent=self)
        except Exception as e:
            Notify(f"Unexpected error launching '{app_name}': {e}", parent=self)

    def Nectar_X_Main(self):
        app_name = "Nectar-X-Main/Nectar-X-Main.exe"
        app_path = find_utils4(app_name)

        if not app_path:
            Notify(f"Application '{app_name}' not found.", parent=self)
            return

        if not os.path.exists(app_path):
            Notify(f"Application path does not exist: {app_path}", parent=self)
            return

        try:
            if sys.platform == "darwin":  # macOS
                if app_path.endswith(".app"):
                    # Use 'open' to launch .app bundles
                    subprocess.Popen(["open", app_path])
                else:
                    subprocess.Popen([app_path])
            elif sys.platform == "win32":  # Windows
                subprocess.Popen([app_path])
            else:  # Linux / other Unix-like
                subprocess.Popen([app_path])
        except FileNotFoundError:
            Notify(f"Application not found at path: {app_path}", parent=self)
        except PermissionError:
            Notify(f"Permission denied when trying to launch: {app_path}", parent=self)
        except Exception as e:
            Notify(f"Unexpected error launching '{app_name}': {e}", parent=self)

    def moveEvent(self, event):
        """Update child position when parent moves"""
        if hasattr(self, "child_window") and self.child_window.isVisible():
            self.child_window.update_position()
            self.child_window.raise_()  # keep child above parent
        super().moveEvent(event)

    def resizeEvent(self, event):
        """Update child size when parent resizes"""
        if hasattr(self, "child_window") and self.child_window.isVisible():
            self.child_window.update_position()
        super().resizeEvent(event)

    def raiseEvent(self):
        """Bring both parent and child to front"""
        self.raise_()
        self.child_window.raise_()

    def find_NectarX(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'Nectar_Venv', icon_name), 
                          os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

    def open_Nectar(self):
        # Paths to search for Nectar-X-Studio.exe
        self.check_core_models_installed_once()
        self.check_core_installed()
        possible_paths = [
            r"C:\Program Files\Nectar-X-Studio\Nectar-X-Studio.exe",
            r"C:\Program Files (x86)\Nectar-X-Studio\Nectar-X-Studio.exe"
        ]
        
        nectar_path = None
        for path in possible_paths:
            if os.path.exists(path):
                nectar_path = path
                break

        # If not found, search deeper in Program Files directories
        if not nectar_path:
            for root, dirs, files in os.walk(r"C:\Program Files"):
                if "Nectar-X-Studio.exe" in files:
                    nectar_path = os.path.join(root, "Nectar-X-Studio.exe")
                    break
            if not nectar_path:
                for root, dirs, files in os.walk(r"C:\Program Files (x86)"):
                    if "Nectar-X-Studio.exe" in files:
                        nectar_path = os.path.join(root, "Nectar-X-Studio.exe")
                        break

        if nectar_path:
            try:
                subprocess.Popen([nectar_path], shell=True)
            except Exception as e:
                Notify(f"Error launching Nectar-X-Studio: {e}", parent=self)
        else:
            Notify("Nectar-X-Studio.exe not found in Program Files.", parent=self)
            self.Nectar_X_Main()

    def check_core_models_installed_once(self):
        settings = QSettings("Zashiron", "Nectar-X-Studio")
        already_checked = settings.value("core_models_checked", False, type=bool)
        if already_checked:
            return

        self.check_core_models_installed()
        settings.setValue("core_models_checked", True)

    def check_core_models_installed(self):
        home = os.path.expanduser("~")
        emb_path = os.path.join(home, "all-MiniLM-L12-v2")
        dec_path = os.path.join(home, "Decision-Model", "decision-k2.gguf")

        if os.path.exists(emb_path):
            Notify(f"Embedding Engine model: INSTALLED ({emb_path})", parent=self)
        else:
            Notify(f"Embedding Engine model: NOT INSTALLED ({emb_path})", parent=self)
            self.Nectar_X_Model()

        if os.path.exists(dec_path):
            Notify(f"Decision Engine model: INSTALLED ({dec_path})", parent=self)
        else:
            Notify(f"Decision Engine model: NOT INSTALLED ({dec_path})", parent=self)
            self.Nectar_X_Model()

    def check_core_installed(self):
        home = os.path.expanduser("~")
        emb_path = os.path.join(home, "all-MiniLM-L12-v2")
        dec_path = os.path.join(home, "Decision-Model", "decision-k2.gguf")


        # Embedding model
        if os.path.exists(emb_path):
            print(f"Embedding Engine model: INSTALLED ({emb_path})")
        else:
            Notify(f"Embedding Engine model: NOT INSTALLED ({emb_path})", parent=self)
            self.Nectar_X_Model()


        # Decision model
        if os.path.exists(dec_path):
            print(f"Decision Engine model: INSTALLED ({dec_path})")
        else:
            Notify(f"Decision Engine model: NOT INSTALLED ({dec_path})", parent=self)
            self.Nectar_X_Model()

    def check_server(self):
        is_active = self.ping("127.0.0.1", 5005)
        self.dot.set_active(is_active)

    def ping(self, host, port, timeout=0.5):
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

    def setup_overlay(self):
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet('background-color: rgba(0, 0, 0, 180);')
        self.overlay.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.overlay.setVisible(False)
        overlay_layout = QVBoxLayout(self.overlay)
        overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loader = Loader1()
        self.loader.setFixedSize(150, 150)
        self.loader.setVisible(True)
        self.loader.setStyleSheet('background-color: #ffffff; color: #E0E0E0; padding: 10px; border-radius: 5px;')
        overlay_layout.addWidget(self.loader)

    def resizeEvent(self, event):
        """Ensure overlay resizes with the main window."""  # inserted
        self.overlay.setGeometry(self.rect())
        super().resizeEvent(event)

    def last_func(self):
        self.overlay.setVisible(False)

    def execute_command(self):
        user_command = self.search_bar.text().strip()
        if user_command.lower() == 'clear':
            self.search_bar.clear()
        elif user_command:
            self.overlay.setVisible(True)
            self.search_bar.clear()

            self.worker = ChatWorker6(user_command)
            self.worker.result_signal.connect(self.on_result_received)
            self.worker.finished.connect(lambda: self.overlay.setVisible(False))
            self.worker.start()

    def on_result_received(self, result):
        if result == 'No output from command.':
            tooltip_text = 'Retry'
        else:  # inserted
            tooltip_text = f'{result}'
            self.overlay.setVisible(False)
        icon_path101 = find_icon('NectarX.ico')
        tooltip_text = f'<img src=\"{icon_path101}\" width=\"32\" height=\"32\" style=\"vertical-align:middle; margin-right:30px;\"> <span style=\"font-size:20px; margin-left:30px; font-weight:bold; display:inline-block; text-align:center; width:100%; \">Nectar-X-Studio</span> <br> {result}'
        tooltip = PersistentTooltip(tooltip_text, self)
        global_pos = self.search_bar.mapToGlobal(QPoint(0, -tooltip.height()))
        tooltip.show_for_duration(global_pos, duration_ms=300000)

    def add_news_section(self, layout, title, default_url, zoom_key, url_key, min_height=300):
        # Section label
        label = QLabel(f'{title}')
        label.setStyleSheet('color: white; font-size: 14pt; font-weight: bold;')
        layout.addWidget(label)

        # ----------------- Web Profile Setup -----------------
        settings = self.web_profile.settings()

        # Enable JavaScript, popups, local storage
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)

        # Allow third-party cookies (important for OAuth)
        self.web_profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)

        # ----------------- Custom Page Class -----------------
        class OAuthFriendlyPage(QWebEnginePage):
        
            def createWindow(self, window_type):
                """Intercept popups and redirect OAuth/logins to system browser."""
                popup_view = QWebEngineView(self.profile())
                popup_view.setWindowTitle(" ")
                popup_view.setWindowIcon(QIcon(find_icon('background/NectarX.png') or 'background/NectarX.png'))
                popup_view.setWindowFlags(Qt.WindowType.Dialog)

                # --- Set a custom User-Agent (agent spoofing) ---
                custom_agent = (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0 Safari/537.36 NectarBrowser/1.0"
                )
                #profile().setHttpUserAgent(custom_agent)

                adblock_list = [
                    "doubleclick.net",
                    "googleads.g.doubleclick.net",
                    "googlesyndication.com",
                    "adservice.google.com",
                    "ads.youtube.com",
                    "taboola.com",
                    "outbrain.com",
                    "adroll.com",
                    "revcontent.com",
                    "https://donate.python.org/",
                ]
                
                def handle_url_change(url):
                    url_str = url.toString()
                    # --- Ad Blocking ---
                    if any(ad_domain in url_str for ad_domain in adblock_list):
                        print("[AdBlock] Blocked:", url_str)
                        popup_view.close()
                        return
                    
                    # If URL is OAuth/login (Google, Qwant, etc.) open in system browser
                    if any(s in url_str for s in ("accounts.google.com", "oauth", "login", "qwant.com")):
                        webbrowser.open(url_str)
                        popup_view.close()  # Close internal popup
                    else:
                        # Otherwise, show popup inside the app
                        popup_view.load(url)
                        popup_view.show()
                
                popup_view.urlChanged.connect(handle_url_change)
                return popup_view.page()

        # ----------------- Create WebEngineView -----------------
        web_view = QWebEngineView(self.web_profile)
        web_view.setPage(OAuthFriendlyPage(self.web_profile, web_view))
        # --- Enable JavaScript ---
        web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)

        # Style and sizing
        web_view.setStyleSheet('QWebEngineView { border-radius: 8px; }')
        web_view.setMinimumHeight(min_height)

        # ----------------- Load last URL & zoom -----------------
        try:
            last_url = self.settings.value(f'news/{url_key}', default_url)
            zoom_level = float(self.settings.value(f'news/{zoom_key}', 1.0))
        except Exception:
            last_url = default_url
            zoom_level = 1.0

        if not last_url or not str(last_url).startswith(("http://", "https://")):
            last_url = default_url

        web_view.setZoomFactor(zoom_level)
        web_view.load(QUrl(last_url))

        # ----------------- Auto-save preferences -----------------
        web_view.urlChanged.connect(lambda url: self.settings.setValue(f'news/{url_key}', url.toString()))
        web_view.page().zoomFactorChanged.connect(lambda z: self.settings.setValue(f'news/{zoom_key}', z))

        layout.addWidget(web_view)
        Notify(f"News section loaded on {platform.system()} ({last_url})", parent=self)


    def icon_button_stylesheet(self):
        return """
            QWidget {
                background-color: #000000;
            }

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

    def closeEvent(self, event):
        event.ignore()
        #self.hide()

    def setup_autocomplete(self):
        self.completer_model = QStringListModel()
        self.completer = QCompleter(self.completer_model, self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.search_input.setCompleter(self.completer)

    def on_text_changed(self):
        self.typing_timer.start()

    def fetch_web_suggestions(self):
        self.typing_timer.stop()
        import re
        query = re.sub('[^a-zA-Z0-9\\s]', '', self.search_input.text()).strip()
        if not query:
            return
        self.threadpool.start(RunnableTask(self._fetch_suggestions_threaded, query))

    def _fetch_suggestions_threaded(self, query):
        try:
            response = requests.get('https://suggestqueries.google.com/complete/search', params={'client': 'firefox', 'q': query}, timeout=2)
            suggestions = response.json()[1]
        except Exception as e:
            Notify(f'Web suggestion error: {e}', parent=self)
            suggestions = []
        combined = list(dict.fromkeys(map(str, suggestions + self.search_history + DEFAULT_SUGGESTIONS)))
        self.completer_model.setStringList(combined)

    def run_search_thread(self):
        query = self.search_input.text().strip()
        if not query:
            return
        QTimer.singleShot(0, lambda: self.simulate_start_search(query))

    def simulate_start_search(self, query):
        if not query:
            return
        if query not in self.search_history:
            self.search_history.insert(0, query)
            self.search_history = self.search_history[:MAX_HISTORY]
            self.save_history()
        self.cli_search(query)

    def cli_search(self, query):
        import webbrowser

        # Make sure the query is not empty
        query = query.strip()
        if not query:
            print("❌ Empty query!")
            return

        # Format the query for a Google search (or any search engine)
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

        # Open the query in the default web browser
        webbrowser.open(search_url)
        print(f"🌐 Opening browser for query: {query}")

        # Clear the input field
        self.search_input.clear()

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_history(self):
        try:
            with open(HISTORY_FILE, 'w') as f:
                json.dump(self.search_history, f)
        except Exception as e:
            Notify(f'Error saving history: {e}', parent=self)

    def closeEvent(self, event):
        # Stop any background threads here if needed
        print("Application is closing...")
        QApplication.quit()  # Ensures the app fully quits
        event.accept()  # Accept the close event

def is_windows():
    return os.name == "nt"

def is_admin():
    """Return True if the current process is running with admin privileges (Windows)."""
    if not is_windows():
        return False
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

def relaunch_as_admin():
    """Relaunch the current script/executable with admin rights (UAC). Returns True if relaunch was started."""
    if not is_windows():
        return False

    # Path to Python executable (when running via `python script.py`) or the frozen exe.
    executable = sys.executable

    # If running a script (not frozen), use the Python executable and pass the script path as arg.
    # If frozen (PyInstaller), the executable is the app itself and sys.argv[0] is the exe path.
    if getattr(sys, "frozen", False):
        # frozen bundle: run the exe directly
        exe_path = sys.executable
        params = " ".join(f'"{arg}"' for arg in sys.argv[1:])  # preserve args
    else:
        # running from interpreter: call python with the script path
        exe_path = sys.executable
        # sys.argv[0] can be a relative path; make it absolute
        script = os.path.abspath(sys.argv[0])
        params = " ".join([f'"{script}"'] + [f'"{arg}"' for arg in sys.argv[1:]])

    # ShellExecuteW requires wide strings
    try:
        # SW_SHOWNORMAL = 1
        hinstance = ctypes.windll.shell32.ShellExecuteW(None, "runas", exe_path, params, None, 1)
        # If > 32, succeeded in launching; if <= 32, failed.
        return hinstance > 32
    except Exception:
        traceback.print_exc()
        return False

# ----------------- Your main app code -----------------
def start_app():
    app = QApplication(sys.argv)

    # Try to check/start the browser agent, but continue even if it fails
    try:
        check_browser_agent()
    except Exception as e:
        print(f"[Warning] ChatServe not found or failed to start: {e}")

    # Initialize main window
    main_window = Assets()
    main_window.show()

    sys.exit(app.exec())

def main():
    # Only attempt elevation on Windows
    if is_windows() and not is_admin():
        # Attempt to relaunch as admin
        launched = relaunch_as_admin()
        if launched:
            print("Relaunching with administrator privileges (UAC prompt)... exiting current process.")
            sys.exit(0)
        else:
            print("[Warning] Failed to relaunch as administrator. Continuing without elevation.")
    # If already admin, or relaunch failed / non-Windows, start the app normally.
    start_app()

if __name__ == "__main__":
    # If packaging with multiprocessing on Windows and freezing, keep this
    import multiprocessing
    multiprocessing.freeze_support()
    main()
