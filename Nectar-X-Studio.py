"""
\nLicense Key: CIRB-5002-NGWG-4132
\nUnique Numerical Signature: 4153318607422408869
\nSeriel No: D51CD0192107E1E6F03746B510264E29
\n
"""
global _logger_initialized  # inserted

Encoded_License_Details = 'eyJsaWNlbnNvciI6ICJaYXNoaXJpb24gaW5jIiwgImxpY2Vuc2Vfa2V5IjogIkNJUkItNTAwMi1OR1dHLTQxMzIiLCAiZXhwaXJhdGlvbl9kYXRlIjogIjIwMjctMTItMjMifQ=='

import asyncio
import pygame
from PyQt6.QtWebEngineWidgets import QWebEngineView
import time
from PyQt6.QtCore import QPoint
from edge_tts import Communicate
import multiprocessing
import subprocess
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QThread, QElapsedTimer, QObject, QSize, QRegularExpression, QProcess, QPropertyAnimation, QEvent, QFileSystemWatcher, QStringListModel
from PyQt6.QtWidgets import QDialogButtonBox, QDialog, QApplication, QWidget, QLabel, QPushButton, QSplashScreen, QLineEdit, QGridLayout, QVBoxLayout, QMessageBox, QProgressBar, QMainWindow, QTextEdit, QCheckBox, QHBoxLayout, QFrame, QSpinBox, QFileDialog, QMessageBox, QLineEdit, QProgressBar, QInputDialog, QPlainTextEdit, QSplitter, QStackedWidget, QStackedLayout, QFormLayout, QListWidget, QSlider, QScrollArea, QSizePolicy, QGraphicsOpacityEffect, QListWidgetItem, QComboBox, QGroupBox, QTabWidget, QCompleter, QStatusBar, QSystemTrayIcon, QMenu, QToolTip, QToolButton
import logging
import os
from PyQt6.QtGui import QFont, QPixmap, QPainter, QPainterPath, QDesktopServices, QShortcut
from PyQt6.QtGui import QColor, QFont, QSyntaxHighlighter, QTextCharFormat, QTextCursor, QPainter, QTextFormat, QAction, QPen
from PyQt6.QtGui import QFont, QKeySequence, QTextCursor, QAction
from PyQt6.QtCore import Qt, QRect, QRegularExpression, QSize
import warnings
import psutil
from datetime import datetime
import datetime
import base64
from PyQt6.QtCore import Qt, QUrl
import platform
import psutil
from cpuinfo import get_cpu_info
import re
import json
import xml.etree.ElementTree as ET
import sys
from scapy.all import IP, TCP, sr1, send
QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)
import threading
try:
    from llama_cpp import Llama
except ImportError:
    Llama = None
from PyQt6.QtGui import QIcon
_logger_initialized = False
_logger_lock = threading.Lock()
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

def setup_logger(log_file_path='logs/Debug.log'):
    global _logger_initialized  # inserted
    with _logger_lock:
        if _logger_initialized:
            return
        try:
            log_dir = os.path.dirname(log_file_path)
            if log_dir:
                try:
                    os.makedirs(log_dir, exist_ok=True)
                except Exception:
                    log_file_path = os.path.basename(log_file_path)
            try:
                logging.basicConfig(filename=log_file_path, filemode='a', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8')
            except Exception:
                logging.basicConfig(filename=log_file_path, filemode='a', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        logging.raiseExceptions = False
        try:
            logging.debug('Logger initialized successfully.')
        except Exception:
            pass
        _logger_initialized = True
        except Exception:
            _logger_initialized = True
setup_logger()

def write_log(message: str, level=logging.DEBUG):
    try:
        if not _logger_initialized:
            setup_logger()
        logging.log(level, message)
    except Exception:
        pass
setup_logger()
from datetime import datetime

def write_to_log(message: str, file_path: str='Nectar-Studio.log'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
    timestamped_message = f'[{datetime.now().isoformat()}] {message}\n'
    with open(file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(timestamped_message)

def find_icon(icon_name):
    """Attempts to find the icon in and out of the script\'s directory."""  # inserted
    script_dir = os.path.dirname(os.path.realpath(__file__))
    possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    else:  # inserted
        return None

class SplashScreen(QSplashScreen):
    def __init__(self):
        pixmap_path = self.find_pixmap('background/NectarX.png') or 'background/NectarX.png'
        splash_pix = QPixmap(pixmap_path).scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        super().__init__(splash_pix)
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.SplashScreen | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.X11BypassWindowManagerHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setMask(splash_pix.mask())

    def show_splash(self):
        self.show()
        self.start_splash_timer()

    def start_splash_timer(self):
        QTimer.singleShot(10000, self.finish_splash)

    def close_splash(self):
        self.close()

    def finish_splash(self):
        Studio_Nectar.show()
        self.close_splash()

    def find_pixmap(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

def check_program_installed(program_name):
    import shutil
    return shutil.which(program_name) is not None

class Check_Installed(QWidget):
    def __init__(self):
        super().__init__()
        self.is_dark_mode = True
        self.countdown_timer = QTimer(self)
        self.update_text_timer = QTimer(self)
        self.update_stylesheet()
        self.initUI()

    def update_stylesheet(self):
        """Update the application stylesheet based on the current mode."""  # inserted
        if self.is_dark_mode:
            self.setStyleSheet(' \n                QWidget {\n                                background-color: transparent; \n                                color: #cccccc;\n                }\n                QPushButton {\n                                background-color: #000000;\n                                color: #d3d3d3;\n                                border: none;\n                                padding: 15px;\n                                border-radius: 10px;\n                }\n                QPushButton:hover {\n                                background-color: #000000;\n                }\n                QPushButton:pressed {\n                                background-color: #000000;\n                }\n            ')

    def initUI(self):
        from PyQt6.QtWidgets import QVBoxLayout, QLabel
        from PyQt6.QtGui import QFont, QIcon, QPixmap
        from PyQt6.QtCore import Qt
        import os
        self.setWindowTitle('Nectar-X-Studio')
        self.setFixedSize(710, 450)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        icon_path = self.find_icon('background/NectarX.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:  # inserted
            self.setWindowIcon(QIcon('background/NectarX.png'))
        main_layout = QVBoxLayout()
        main_layout.setSpacing(2)
        self.title_label = QLabel(' ')
        self.title_label.setFont(QFont('Exo 2', 20, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.completed_label = QLabel(' ')
        self.completed_label.setFont(QFont('Arial', 14))
        self.completed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label = QLabel(self)
        icon_path = self.find_icon('background/NectarX.png')
        pixmap = QPixmap(icon_path) if icon_path else QPixmap()
        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overlay_text = QLabel(self)
        self.overlay_text.setStyleSheet('\n\t\t\tQLabel {\n\t\t\t\tcolor: black;\n\t\t\t\tfont-size: 18px;\n\t\t\t\tbackground-color: rgba(0, 0, 0, 120);\n\t\t\t\tborder-radius: 8px;\n\t\t\t\tpadding: 6px 12px;\n\t\t\t}\n\t\t')
        self.overlay_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overlay_text.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.overlay_text.resize(250, 40)
        self.overlay_text.raise_()
        opacity = QGraphicsOpacityEffect(self.overlay_text)
        self.overlay_text.setGraphicsEffect(opacity)
        self.animation = QPropertyAnimation(opacity, b'opacity')
        self.animation.setDuration(1500)
        self.animation.setStartValue(0.3)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.animation.setLoopCount((-1))
        self.overlay_text.show()
        self.animation.start()
        self.loader = Loader()
        self.loader.setFixedSize(30, 40)
        self.loader.setVisible(False)
        self.loader.setStyleSheet('background-color: #ffffff; color: #E0E0E0; padding: 10px; border-radius: 5px;')
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(image_label)
        main_layout.addWidget(self.loader, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.completed_label)
        self.setLayout(main_layout)
        self.countdown_time = 10
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.missing_apps = self.check_and_display_programs()

    def showEvent(self, event):
        """ Start the timer only when the window is shown. """  # inserted
        super().showEvent(event)
        self.check_internet_and_start_timer()

    def resizeEvent(self, event):
        self.overlay_text.move((self.width() - self.overlay_text.width()) // 2, (self.height() - self.overlay_text.height()) // 2)
        super().resizeEvent(event)

    def check_and_display_programs(self):
        programs = ['cmake']
        missing_apps = []
        for program in programs:
            installed = check_program_installed(program)
            status = 'Installed' if installed else 'Not Installed'
            write_to_log(f'{program}: {status}\n' + self.completed_label.text())
            if not installed:
                missing_apps.append(program)
        return missing_apps

    def check_internet(self):
        import socket
        try:
            socket.create_connection(('127.0.0.1', 1001), timeout=3)
            return True
        except OSError:
            return False

    def check_internet_and_start_timer(self):
        """Check internet connectivity and handle countdown timer accordingly."""  # inserted
        if self.check_internet():
            if not self.timer.isActive():
                self.timer.start(1000)
            self.overlay_text.setText(f'{self.countdown_time}')
        else:  # inserted
            self.completed_label.setText('No internet connection. Retrying...')
            if not hasattr(self, 'retry_timer'):
                self.retry_timer = QTimer(self)
                self.retry_timer.timeout.connect(self.check_internet_and_start_timer)
            if not self.retry_timer.isActive():
                self.retry_timer.start(3000)

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script\'s directory."""  # inserted
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

    def update_countdown(self):
        """Updates the countdown message, pauses if no internet, and closes the app when time runs out."""  # inserted
        if not self.check_internet():
            self.completed_label.setText('Internet lost. Pausing countdown...')
            self.timer.stop()
            self.check_internet_and_resume()
            return
        self.countdown_time -= 1
        self.overlay_text.setText(f'{self.countdown_time}')
        if self.countdown_time <= 0:
            self.timer.stop()
            self.loader.setVisible(False)
            if self.missing_apps:
                self.show_missing_apps_message()
            else:  # inserted
                Studio_Nectar.show()
                QTimer.singleShot(2000, self.close)

    def check_internet_and_resume(self):
        """Continuously checks for internet connection and resumes countdown when restored."""  # inserted
        if self.check_internet():
            if hasattr(self, 'retry_timer') and self.retry_timer.isActive():
                self.retry_timer.stop()
            self.overlay_text.setText(f'{self.countdown_time}')
            if not self.timer.isActive():
                self.timer.start(1000)
        else:  # inserted
            if not hasattr(self, 'retry_timer'):
                self.retry_timer = QTimer(self)
                self.retry_timer.timeout.connect(self.check_internet_and_resume)
            if not self.retry_timer.isActive():
                self.retry_timer.start(3000)

    def show_missing_apps_message(self):
        """Displays a message box showing the missing applications."""  # inserted
        missing_apps = ', '.join(self.missing_apps)
        message = f'The following applications are missing or not added to the PATH:<br>{missing_apps}<br>Please install or add them to the PATH and restart the application. \n if not installed install at: <a href=\"https://github.com/headlessripper/Mount_Utils/releases/download/0.0.0.0.0/Mount_Utils.7z\">Mount_Utils</a>'
        self.completed_label.setText(f'AI engine not able to boot\n missing dependency: {missing_apps}')
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle('Missing Applications')
        msg.setText('Missing Applications')
        msg.setInformativeText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def closeEvent(self, event):
        """Ensure all timers are stopped when closing."""  # inserted
        if self.timer.isActive():
            self.timer.stop()
        if hasattr(self, 'retry_timer') and self.retry_timer.isActive():
            self.retry_timer.stop()
        super().closeEvent(event)

class FloatingNotification(QWidget):
    def __init__(self, parent, message, duration=120000, bg_color='#222222', text_color='#ffffff'):
        super().__init__(parent)
        self.parent_widget = parent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.SubWindow | Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(f'\n            QWidget {\n                background-color: {bg_color};\n                border-radius: 10px;\n            }\n            QLabel {\n                color: {text_color};\n                font-size: 13px;\n                padding-left: 10px;\n            }\n            QPushButton {\n                background: transparent;\n                color: {text_color};\n                border: none;\n                font-weight: bold;\n                font-size: 14px;\n            }\n            QPushButton:hover {\n                color: red;\n            }\n        ')
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

def is_system_dark_mode():
    """Detects if the system is in dark mode."""  # inserted
    if platform.system() == 'Windows':
        try:
            import winreg
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize')
            value, _ = winreg.QueryValueEx(key, 'AppsUseLightTheme')
            return value == 0
        except Exception:
            return False
    else:  # inserted
        if platform.system() == 'Darwin':
            try:
                result = subprocess.run(['defaults', 'read', '-g', 'AppleInterfaceStyle'], capture_output=True, text=True)
                return 'Dark' in result.stdout
            except Exception:
                return False
        else:  # inserted
            return False
light_theme = '\nQMainWindow {\n    background-color: #1b1b1b;\n    color: black;\n}\n'
dark_theme = '\nQMainWindow {\n    background-color: #000000;\n    color: #ffffff;\n}\n'

def apply_theme(mode='dark'):
    """Applies a light or dark theme to the app."""  # inserted
    app = QApplication.instance()
    if app:
        if mode == 'dark':
            set_user_theme('dark')
            app.setStyleSheet(dark_theme)
        else:  # inserted
            if mode == 'light':
                set_user_theme('light')
                app.setStyleSheet(light_theme)
            else:  # inserted
                if mode == 'system':
                    if is_system_dark_mode():
                        app.setStyleSheet(dark_theme)
                    else:  # inserted
                        app.setStyleSheet(light_theme)
from PyQt6.QtCore import QSettings

def get_user_theme():
    settings = QSettings('Zashirion', 'Nectar-X')
    return settings.value('theme', 'dark')

def set_user_theme(theme):
    settings = QSettings('Zashirion', 'Nectar-X')
    settings.setValue('theme', theme)

def set_dark_theme1(self):
    """Set dark theme for the application."""  # inserted
    dark_stylesheet = '\n        QWidget {\n            background-color: #1E1E1E;\n            color: #ffffff;\n        }\n    '
    self.setStyleSheet(dark_stylesheet)

def set_light_theme(self):
    """Set dark theme for the application."""  # inserted
    light_stylesheet = '\n\tQWidget {\n\t\tbackground-color: transparent;\n\t\tcolor: #f50000;\n\t}\n\tQLineEdit, QTextEdit, QPlainTextEdit {\n\t\tbackground-color: #2a2c31;\n\t\tcolor: #ffffff;\n\t\tborder: none;\n\t\tpadding: 5px;\n\t\tborder-radius: 10px;\n\t}\n\tQPushButton {\n\t\tbackground-color: #000000; \n\t\tcolor: white; \n\t\tfont-size: 16px; \n\t\tpadding: 10px; \n\t\tborder-radius: 5px;\n\t}\n\tQPushButton:hover {\n\t\tbackground-color: #f50000;\n\t}\n\tQPushButton:pressed {\n\t\tbackground-color: #FFFFFF;\n\t}\n\tQListWidget {\n\t\tbackground-color: #3c3f41;\n\t\tcolor: #d3d3d3;\n\t\tborder: 1px solid #444444;\n\t}\n\tQGroupBox {\n\t\tborder: 1px solid #444444;\n\t\tbackground-color: #2b2b2b;\n\t\tcolor: #d3d3d3;\n\t\tmargin: 5px;\n\t\tpadding: 10px;\n\t}\n\tQFormLayout {\n\t\tbackground-color: #2b2b2b;\n\t\tcolor: #d3d3d3;\n\t}\n\t'
    self.setStyleSheet(light_stylesheet)
import subprocess
import platform
import psutil
import shutil
import os
import re

def get_llm_hardware_recommendation():
    info = {}
    info['cpu_name'] = platform.processor()
    info['cpu_cores'] = psutil.cpu_count(logical=False)
    info['cpu_threads'] = psutil.cpu_count(logical=True)
    total_ram_gb = round(psutil.virtual_memory().total / 1073741824, 2)
    info['total_ram_gb'] = total_ram_gb
    info['gpu_name'] = 'Unknown'
    info['gpu_memory_gb'] = 0
    if shutil.which('nvidia-smi'):
        try:
            result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader,nounits'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=True)
            gpu_info = result.stdout.strip().split('\n')[0]
            if gpu_info:
                gpu_name, gpu_mem = map(str.strip, gpu_info.split(','))
                info['gpu_name'] = gpu_name
                info['gpu_memory_gb'] = round(int(gpu_mem) / 1024, 2)
        except subprocess.CalledProcessError:
            info['gpu_name'] = 'nvidia-smi failed'
    else:  # inserted
        if shutil.which('rocm-smi'):
            try:
                result = subprocess.run(['rocm-smi', '--showproductname', '--showmeminfo', 'vram'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=True)
                output = result.stdout
                name_match = re.search('Card\\s*\\d+\\s*:\\s*(.*)', output)
                mem_match = re.search('Total Memory.*?(\\d+)\\s*MiB', output)
                if name_match:
                    info['gpu_name'] = name_match.group(1).strip()
                if mem_match:
                    info['gpu_memory_gb'] = round(int(mem_match.group(1)) / 1024, 2)
            except subprocess.CalledProcessError:
                info['gpu_name'] = 'rocm-smi failed'
        else:  # inserted
            if os.name == 'nt' and shutil.which('dxdiag'):
                try:
                    dxdiag_file = 'dxinfo.txt'
                    subprocess.run(['dxdiag', '/t', dxdiag_file], check=True)
                    with open(dxdiag_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    gpu_lines = re.findall('Card name:\\s*(.+)', content)
                    if gpu_lines:
                        gpu_name = gpu_lines[0].strip()
                        info['gpu_name'] = gpu_name
                        info['gpu_memory_gb'] = 1
                except Exception:
                    info['gpu_name'] = 'Intel GPU detection failed'
    ram = info['total_ram_gb']
    gpu_vram = info['gpu_memory_gb']
    recommendation = []
    if ram < 4:
        recommendation.append('Not recommended to run LLMs locally (too little RAM).')
    else:  # inserted
        if 4 <= ram < 8:
            recommendation.append('Run small quantized models like 7B (Q4_0 or Q5_0) using CPU.')
        else:  # inserted
            if 8 <= ram < 16:
                recommendation.append('Run 7B models comfortably (Q4_0 to Q6_K).')
            else:  # inserted
                if 16 <= ram < 32:
                    recommendation.append('Run 13B (Q4/Q5), 7B full precision possible.')
                else:  # inserted
                    if ram >= 32:
                        recommendation.append('Run 13B easily, 33B quantized models possible (Q4).')
    if gpu_vram >= 12:
        recommendation.append('Run 13B or even 33B models in GGUF on GPU.')
    else:  # inserted
        if 6 <= gpu_vram < 12:
            recommendation.append('Run 7B GGUF models on GPU (Q4 or Q5 quantization).')
        else:  # inserted
            if 0 < gpu_vram < 6:
                recommendation.append('Very limited GPU use CPU instead.')
            else:  # inserted
                recommendation.append('No GPU acceleration available; CPU-only inference recommended.')
    rec_text = '                '.join(recommendation)
    summary = f"\n    LLM Recommendation: With {ram} GB RAM and GPU: {info['gpu_name']} ({gpu_vram} GB VRAM) {rec_text}\n    "
    return summary

class RepoCard(QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, repo_id, description, downloads):
        super().__init__()
        self.repo_id = repo_id
        layout = QVBoxLayout()
        self.name_label = QLabel(f'<b>{repo_id}</b>')
        self.name_label.setStyleSheet('font-size: 16px; color: #ffffff;')
        self.card_frame = QFrame()
        self.original_width = 965
        self.card_layout = QVBoxLayout(self.card_frame)
        self.card_frame.setFixedWidth(self.original_width)
        self.card_frame.setStyleSheet('\n            QWidget {\n                background-color: #1b1b1b; \n                border-radius: 12px; \n                padding: 16px; \n                margin: 8px;\n            }\n            QFrame {\n                background-color: #000000;\n                border: 1px solid transparent;\n                border-radius: 12px;\n                padding: 16px;\n            }\n            QLabel {\n\t\t\t\t\tcolor: #333;\n\t\t\t\t\tfont-size: 13px;\n\t\t\t}\n\t\t\tQWidget:hover {\n                background-color: #1e1e1e;\n                color: #ffffff;\n            }\n        ')
        self.desc_label = QLabel(description)
        self.desc_label.setStyleSheet('font-size: 12px; color: #cccccc;')
        self.download_label = QLabel(f'Downloads: {downloads}')
        self.download_label.setStyleSheet('font-size: 12px; color: #aaaaaa;')
        self.card_layout.addWidget(self.name_label)
        self.card_layout.addWidget(self.desc_label)
        self.card_layout.addWidget(self.download_label)
        layout.addWidget(self.card_frame)
        self.setLayout(layout)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        self.clicked.emit(self.repo_id)
        super().mousePressEvent(event)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.isMaximized():
            self.card_frame.setFixedWidth(1065)
        else:  # inserted
            self.card_frame.setFixedWidth(965)

    def changeEvent(self, event):
        from PyQt6.QtCore import Qt, QEvent
        if event.type() == QEvent.Type.WindowStateChange:
            if self.isMaximized():
                self.card_frame.setFixedWidth(self.original_width + 100)
            else:  # inserted
                self.card_frame.setFixedWidth(self.original_width)
        super().changeEvent(event)

class ModelCard(QWidget):
    clicked = pyqtSignal(str, bool)

    def __init__(self, model_name, model_size, too_large=False, parent=None):
        super().__init__(parent)
        self.model_name = model_name
        self.too_large = too_large
        base_color = '#a83232' if too_large else '#23272a'
        hover_color = '#ff5555' if too_large else '#7289da'
        self.setStyleSheet(f'\n            QWidget {\n                background-color: {base_color};\n                border-radius: 12px;\n                padding: 15px;\n                margin: 8px;\n            }\n            QWidget:hover {\n                background-color: {hover_color};\n            }\n        ')
        layout = QHBoxLayout()
        self.name_label = QLabel(model_name)
        self.name_label.setStyleSheet('color: white; font-size: 14px;')
        self.size_label = QLabel(model_size)
        self.size_label.setStyleSheet('color: #bbbbbb; font-size: 12px;')
        layout.addWidget(self.name_label)
        layout.addStretch()
        layout.addWidget(self.size_label)
        self.setLayout(layout)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        self.clicked.emit(self.model_name, self.too_large)
        super().mousePressEvent(event)
import psutil

class ModelViewerWindow(QWidget):
    def __init__(self, repo_id, files, on_model_click_callback):
        super().__init__()
        self.setWindowTitle(f'{repo_id}')
        self.setMinimumSize(600, 400)
        self.setStyleSheet('background-color: #1e1e1e; color: white;')
        icon_path = find_icon('background/NectarX.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:  # inserted
            self.setWindowIcon(QIcon('background/NectarX.png'))
        layout = QVBoxLayout()
        self.model_container_layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setStyleSheet('\n                                    QScrollBar:vertical {\n\t\t\t\t\t\t\t\t\tbackground: transparent;\n\t\t\t\t\t\t\t\t\twidth: 8px;\n\t\t\t\t\t\t\t\t\tmargin: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:vertical {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.2);\n\t\t\t\t\t\t\t\t\tmin-height: 20px;\n\t\t\t\t\t\t\t\t\tborder-radius: 4px;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:vertical:hover {\n\t\t\t\t\t\t\t\t\tbackground: #ffffff;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::add-line:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::sub-line:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::add-page:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::sub-page:vertical {\n\t\t\t\t\t\t\t\t\tbackground: none;\n\t\t\t\t\t\t\t\t\theight: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\t/* Horizontal Scrollbar */\n\t\t\t\t\t\t\t\tQScrollBar:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: transparent;\n\t\t\t\t\t\t\t\t\theight: 8px;\n\t\t\t\t\t\t\t\t\tmargin: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.2);\n\t\t\t\t\t\t\t\t\tmin-width: 20px;\n\t\t\t\t\t\t\t\t\tborder-radius: 4px;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:horizontal:hover {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.4);\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::add-line:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::sub-line:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::add-page:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::sub-page:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: none;\n\t\t\t\t\t\t\t\t\twidth: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t} ')
        scroll.setWidgetResizable(True)
        model_container_widget = QWidget()
        model_container_widget.setLayout(self.model_container_layout)
        scroll.setWidget(model_container_widget)
        layout.addWidget(scroll)
        self.setLayout(layout)
        for file in files:
            card = ModelCard(file['path'], file['size'], file.get('too_large', False))
            card.clicked.connect(self.handle_model_click)
            self.model_container_layout.addWidget(card)
        self.on_model_click_callback = on_model_click_callback

    def handle_model_click(self, model_path, too_large):
        total_memory_bytes = psutil.virtual_memory().total
        total_memory_gb = total_memory_bytes / 1073741824
        if too_large:
            QMessageBox.warning(self, 'Warning Model Too Large', f'The model \'{model_path}\' exceeds your system\'s RAM \'{total_memory_gb:.2f} GB\' and may not run properly. Download is blocked.')
        else:  # inserted
            self.on_model_click_callback(model_path)

class AnimatedCheckBox(QCheckBox):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setChecked(True)
        self.circle_x = 2
        self.setStyleSheet('\n            QCheckBox {\n                spacing: 10px;\n            }\n            QCheckBox::indicator {\n                width: 40px;\n                height: 20px;\n                border-radius: 10px;\n                background: transparent;\n            }\n        ')
        self.circle_x = 2 if not self.isChecked() else 22
        from PyQt6.QtCore import QVariantAnimation
        self.animation = QVariantAnimation(self)
        self.animation.setDuration(300)
        self.animation.valueChanged.connect(self.update_position)
        self.stateChanged.connect(self.animate_slider)

    def update_position(self, value):
        """Update the circle position during animation."""  # inserted
        self.circle_x = value
        self.update()

    def animate_slider(self, state):
        """Animate the toggle switch movement."""  # inserted
        checked = state == Qt.Checked
        start_x = 2 if not checked else 22
        end_x = 22 if not checked else 2
        self.animation.stop()
        self.animation.setStartValue(start_x)
        self.animation.setEndValue(end_x)
        self.animation.start()

    def paintEvent(self, event):
        """Custom paint event for drawing the switch."""  # inserted
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor('#ff0000') if self.isChecked() else QColor('#000000'))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, 40, 20, 10, 10)
        painter.setBrush(QColor('#fff'))
        painter.drawEllipse(self.circle_x, 2, 16, 16)
        painter.end()
CONVERSATION_HISTORY_FILE = 'conversation_history.json'
HISTORY_FILE = 'history.json'

def clear_conversation_history():
    with open(CONVERSATION_HISTORY_FILE, 'w') as file:
        file.write('[]')
    write_to_log('Conversation history cleared.')

def load_conversation_history():
    try:
        with open(CONVERSATION_HISTORY_FILE, 'r') as file:
            import json
            return json.load(file)
    except FileNotFoundError:
        return []

def load_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            import json
            return json.load(file)
    except FileNotFoundError:
        return []

def save_conversation_history():
    with open(CONVERSATION_HISTORY_FILE, 'w') as file:
        json.dump(conversation_history, file, indent=4)

def save_history():
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file, indent=4)

def send_to_AlphaLLM(question):
    import socket
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 5005))
        client.send(question.encode('utf-8'))
        response = client.recv(4096)
        client.close()
        return response.decode('utf-8')
    except (socket.error, socket.timeout) as e:
        return f'[Error] Could not connect to AlphaLLM: {e}'

class ChatWorker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, user_text):
        super().__init__()
        self.user_text = user_text

    def run(self):
        reply = send_to_AlphaLLM(self.user_text)
        self.finished.emit(reply)

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

class Communicator(QObject):
    new_speech = pyqtSignal(str)
    new_stdout = pyqtSignal(str)
    new_stderr = pyqtSignal(str)

class CommandTooltip(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.ToolTip)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        layout = QVBoxLayout(self)
        self.text_label = QLabel(text, self)
        self.text_label.setStyleSheet('color: white; font-size: 14px;')
        layout.addWidget(self.text_label)
        self.close_button = QPushButton('Close', self)
        self.close_button.setStyleSheet('\n\t\t\t\t\t\t\t\t\t\t\t\tQPushButton {\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tbackground-color: red;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tcolor: white;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tfont-size: 12px;\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tborder-radius: 5px;\n\t\t\t\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t\t\t\t\tQPushButton:hover {\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tbackground-color: darkred;\n\t\t\t\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t')
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

    def show_tooltip(self, position):
        self.move(position)
        self.show()

class Loader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Speech Simulation Loader')
        self.setFixedSize(100, 100)
        self.setStyleSheet('background-color: #ffffff; color: #E0E0E0; padding: 10px; border-radius: 5px;')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.max_radius = 10
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
            x = center_x + math.cos(math.radians(circle['angle'])) * 10
            y = center_y + math.sin(math.radians(circle['angle'])) * 10
            painter.setPen(Qt.PenStyle.NoPen)
            color = QColor(255, 0, 0)
            color.setAlpha(180)
            painter.setBrush(QBrush(color))
            painter.drawEllipse(x - circle['radius'] / 2, y - circle['radius'] / 2, circle['radius'], circle['radius'])

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

class Home1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)
        button_names = ['Developer Mode', 'Documentation', 'Server API', 'Voice Chat']
        for i, name in enumerate(button_names, start=1):
            button = QPushButton(name)
            button.setFixedHeight(50)
            button.setStyleSheet('\n                                                            QPushButton {\n                                                                            background-color: #1b1b1b;\n                                                                            color: white;\n                                                                            font-size: 16px;\n                                                                            border: none;\n                                                                            padding: 10px;\n                                                                            text-align: center;\n                                                                            border-radius: 5px;\n                                                            }\n                                                            QPushButton:hover {\n                                                                            background-color: #ffffff;\n                                                                            color: #000000;\n                                                            }\n                                                            QPushButton:pressed {\n                                                                            background-color: #1b1b1b;\n                                                            }\n                                            ')
            button.clicked.connect(getattr(self, f'button_{i}_clicked'))
            layout.addWidget(button)

    def button_1_clicked(self):
        Studio_Nectar.load_tool_and_highlight('Dev')

    def button_2_clicked(self):
        import webbrowser
        url = 'https://github.com/headlessripper/Nectar'
        webbrowser.open(url)

    def button_3_clicked(self):
        viewer.show()

    def button_4_clicked(self):
        app_path = self.find_utils4('VoiceChat.exe')
        try:
            subprocess.Popen([app_path])
        except Exception as e:
            logging.error(f'Error opening application: {e}')

    def button_5_clicked(self):
        write_to_log('Not Yet')

    def find_utils4(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'App_Docs', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

    def show_message_box(self, title, text):
        QMessageBox.information(None, title, text)
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import pyqtSignal

class ClickableCard(QFrame):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt, QUrl
import webbrowser

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet('\n            QLabel {\n                color: #f2f2f2;\n            }\n\n            QTextEdit {\n                background-color: #555000;\n                border: 1px solid #ccc;\n                padding: 10px;\n                font-family: Consolas;\n            }\n\n            QPushButton {\n                background-color: #ffffff;\n                border: 1px solid #ccc;\n                padding: 6px 12px;\n                border-radius: 6px;\n            }\n\n            QPushButton:hover {\n                background-color: #e0f0ff;\n                border-color: #007acc;\n                color: #007acc;\n            }\n\n            QFrame#Card {\n                background-color: #eef6f0;\n                border: 1px solid #c8d6c1;\n                border-radius: 12px;\n            }\n\n            QFrame#Card:hover {\n\t\t\t\tbackground-color: #1b1b1b; /* Slightly darker for hover effect */\n\t\t\t\tborder: 1px solid #a9c4a2; /* Slightly stronger border on hover */\n\t\t\t}\n\n            QLabel#Title {\n                font-size: 20px;\n                font-weight: bold;\n            }\n\n            QLabel#Subtitle {\n                font-size: 12px;\n                color: #555;\n            }\n        ')
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        welcome_label = QLabel('<h2><b>Welcome to Nectar<b></h2>')
        welcome_label.setStyleSheet('\n\t\t\t\tcolor: #ffffff;\n\t\t\t\tfont-family: \'Segoe UI\';\n\t\t\t\tfont-size: 16pt;\n\t\t\t\tfont-weight: 500;\n\t\t\t')
        welcome_label.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtext_label = QLabel('The security-first LLM chat application')
        subtext_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(subtext_label)
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        start_chat_btn = self.create_main_card('Start Chatting', 'Chat with any LLM', 'menu\\chat1.png', self.start_chat_action)
        local_docs_btn = self.create_main_card('LocalDocs', 'Chat with your local files', 'menu\\stack.png', self.local_docs_action)
        find_models_btn = self.create_main_card('Find Models', 'Explore and download models', 'menu\\box.png', self.find_models_action)
        button_layout.addWidget(start_chat_btn)
        button_layout.addWidget(local_docs_btn)
        button_layout.addWidget(find_models_btn)
        main_layout.addLayout(button_layout)
        news_frame = QFrame()
        news_layout = QVBoxLayout(news_frame)
        news_title = QLabel('')
        news_title.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        news_content = QTextEdit()
        news_content.setFixedHeight(300)
        news_content.setReadOnly(True)
        news_content.setStyleSheet('background-color: #f2f2f2 ; border-radius: 8px; color: #555000;')
        news_content.setText('<h2><b>Latest News<b></h2>Nectar v1.1 was released on June 18. Changes include: <h3>Inference Engine:</h3>    <ul><li>More Powerful Engine mounted: Zashirions K47B-LS5.</ul></li> <h3>UI Updates:</h3>    <ul><li>New Settings page allow\'s for further Customizations.</li></ul>    <ul><li>New Engine state Indicator in sidebar.</li></ul> <h3>General Features:</h3>    <ul><li>New Code Sand box for Developers.</li></ul>    <ul><li>New API Usage and Broadcasting Services.</li></ul>    <ul><li>New Double Click to rename and delete Sessions individually, in the Chat page.</li></ul>    <ul><li>New Network and Port Monitoring Features for Developers.</li></ul>    <ul><li>New News Feed in Minimized Mode.</li></ul>    <ul><li>New Voice Chat Mode Beta.</li></ul>')
        news_layout.addWidget(news_title)
        news_layout.addWidget(news_content)
        main_layout.addWidget(news_frame)
        footer_layout = QHBoxLayout()
        footer_layout.setSpacing(10)
        footer_items = ['Release Notes', 'Documentation', 'Discord', 'X (Twitter)', 'Github']
        for item in footer_items:
            footer_layout.addWidget(QPushButton(item))
        footer_layout.addStretch()
        main_layout.addStretch()
        main_layout.addLayout(self.create_footer())

    def create_main_card(self, title, subtitle, icon_path, on_click_callback):
        card = ClickableCard()
        card.setObjectName('Card')
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(5)
        icon = QLabel()
        pixmap = QPixmap(icon_path)
        if not pixmap.isNull():
            icon.setPixmap(pixmap.scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label = QLabel(title)
        title_label.setObjectName('Title')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label = QLabel(subtitle)
        subtitle_label.setObjectName('Subtitle')
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icon)
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        card.clicked.connect(on_click_callback)
        return card

    def start_chat_action(self):
        Studio_Nectar.load_tool_and_highlight('Chat')

    def local_docs_action(self):
        Studio_Nectar.load_tool_and_highlight('Docs')

    def find_models_action(self):
        Studio_Nectar.load_tool_and_highlight('Model Downloader')

    def create_footer(self):
        footer_layout = QHBoxLayout()
        footer_layout.setSpacing(15)
        footer_links = {'Release Notes': ('fa5s.scroll', 'https://github.com/headlessripper/Nectar/releases'), 'Documentation': ('fa5s.book', 'https://github.com/headlessripper/Alpha-x/wiki'), 'Discord': ('fa5b.discord', ''), 'X (Twitter)': ('fa5b.twitter', ''), 'Github': ('fa5b.github', 'https://github.com/headlessripper/Nectar')}
        for label, (icon_name, url) in footer_links.items():
            import qtawesome as qta
            icon = qta.icon(icon_name, color='#555000')
            btn = QPushButton(f' {label}')
            btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            btn.setIcon(icon)
            btn.setStyleSheet('\n\t\t\t\tQPushButton {\n\t\t\t\t\tbackground-color: #f0f0f0;\n\t\t\t\t\tcolor: #555000;\n\t\t\t\t\tborder: 1px solid #ccc;\n\t\t\t\t\tpadding: 6px 12px;\n\t\t\t\t\tborder-radius: 6px;\n\t\t\t\t\tfont-weight: bold;\n\t\t\t\t}\n\t\t\t\tQPushButton:hover {\n\t\t\t\t\tbackground-color: #e0e0e0;\n\t\t\t\t\tcolor: #555000;\n\t\t\t\t}\n\t\t\t')
            btn.clicked.connect(lambda checked, link=url: webbrowser.open(link))
            footer_layout.addWidget(btn)
        return footer_layout
import os
import requests
import shutil
import subprocess
import sys
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar, QLabel

def set_dark_theme(self):
    """Set dark theme for the application."""  # inserted
    dark_stylesheet = '\n\t\t\t\tQWidget {\n\t\t\t\t\t\t\t\tbackground-color: #484848;\n\t\t\t\t}\n\t\t\t\t'
    self.setStyleSheet(dark_stylesheet)
import os
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGraphicsOpacityEffect
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve

class DisplayImage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nectar-X-Studio')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet('background-color: transparent;')
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.center())
        top_left_point = qr.center()
        x = top_left_point.x()
        y = top_left_point.y()
        manual_x = x - 120
        manual_y = y - 140
        self.move(manual_x, manual_y)
        set_light_theme(self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        image_label = QLabel(self)
        icon_path = self.find_icon('background/NectarX.png')
        pixmap = QPixmap(icon_path) if icon_path else QPixmap()
        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        self.overlay_text = QLabel(self)
        self.overlay_text.setStyleSheet('\n\t\t\tQLabel {\n\t\t\t\tcolor: black;\n\t\t\t\tfont-size: 18px;\n\t\t\t\tbackground-color: rgba(0, 0, 0, 120);\n\t\t\t\tborder-radius: 8px;\n\t\t\t\tpadding: 6px 12px;\n\t\t\t}\n\t\t')
        self.overlay_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overlay_text.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.overlay_text.resize(250, 40)
        self.overlay_text.raise_()
        opacity = QGraphicsOpacityEffect(self.overlay_text)
        self.overlay_text.setGraphicsEffect(opacity)
        self.animation = QPropertyAnimation(opacity, b'opacity')
        self.animation.setDuration(1500)
        self.animation.setStartValue(0.3)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.animation.setLoopCount((-1))
        self.overlay_text.show()
        self.animation.start()

    def resizeEvent(self, event):
        self.overlay_text.move((self.width() - self.overlay_text.width()) // 2, (self.height() - self.overlay_text.height()) // 2)
        super().resizeEvent(event)

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

class Chat(QWidget):
    def __init__(self):
        super().__init__()
        self.sessions_file = 'chat_sessions.json'
        self.chat_sessions = {}
        self.current_session = None
        self.load_sessions()
        self.initUI()

    def initUI(self):
        self.setStyleSheet('\n\t\t\t\t\tQWidget { background-color: #1b1b1b; color: white; font-size: 14px; border-radius: 8px; padding: 10px;}\n\t\t\t\t\tQLineEdit { background-color: #1b1b1b; color: #ffffff; border-radius: 6px; padding: 10px; border: 1px solid #444; }\n\t\t\t\t\tQPushButton { padding: 12px; background-color: #1b1b1b; color: white; border-radius: 5px;} \n\t\t\t\t\tQPushButton:hover { background-color: #242424; color: #ffffff;}\n\t\t\t\t\tQLabel { color: #e0e0e0; }\n\t\t\t\t\tQFrame { background-color: #1b1b1b; border-radius: 8px; padding: 10px; }\n\t\t\t\t\tQScrollBar:vertical {\n\t\t\t\t\t\t\t\t\tbackground: transparent;\n\t\t\t\t\t\t\t\t\twidth: 8px;\n\t\t\t\t\t\t\t\t\tmargin: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:vertical {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.2);\n\t\t\t\t\t\t\t\t\tmin-height: 20px;\n\t\t\t\t\t\t\t\t\tborder-radius: 4px;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:vertical:hover {\n\t\t\t\t\t\t\t\t\tbackground: #ffffff;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::add-line:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::sub-line:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::add-page:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::sub-page:vertical {\n\t\t\t\t\t\t\t\t\tbackground: none;\n\t\t\t\t\t\t\t\t\theight: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\t/* Horizontal Scrollbar */\n\t\t\t\t\t\t\t\tQScrollBar:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: transparent;\n\t\t\t\t\t\t\t\t\theight: 8px;\n\t\t\t\t\t\t\t\t\tmargin: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.2);\n\t\t\t\t\t\t\t\t\tmin-width: 20px;\n\t\t\t\t\t\t\t\t\tborder-radius: 4px;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:horizontal:hover {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.4);\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::add-line:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::sub-line:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::add-page:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::sub-page:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: none;\n\t\t\t\t\t\t\t\t\twidth: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\t\t\t\t')
        main_layout = QHBoxLayout()
        chat_layout = QVBoxLayout()
        from PyQt6.QtWidgets import QScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.chat_display = QVBoxLayout()
        self.chat_container = QWidget()
        self.chat_container.setLayout(self.chat_display)
        self.scroll_area.setWidget(self.chat_container)
        self.watermark = QLabel('Nectar-X', self)
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watermark.setStyleSheet('color: rgba(255, 255, 255, 0.07); font-size: 50px; font-weight: bold;')
        self.chat_display.addWidget(self.watermark)
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Type your message...')
        self.input_field.returnPressed.connect(self.send_message)
        self.send_button = QPushButton('Send')
        from PyQt6.QtWidgets import QSizePolicy
        self.send_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.send_button.clicked.connect(self.send_message)
        self.clear_button = QPushButton('Clear Chat')
        self.clear_button.clicked.connect(self.clear_everything)
        self.session_button = QPushButton('New Session')
        self.session_button.clicked.connect(self.create_new_session)
        self.session_button.hide()
        self.loader_label = QLabel('Processing...')
        self.loader_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loader_label.hide()
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)
        input_layout.addWidget(self.clear_button)
        input_layout.addWidget(self.session_button)
        chat_layout.addWidget(self.scroll_area)
        chat_layout.addWidget(self.loader_label)
        chat_layout.addWidget(self.progress_bar)
        chat_layout.addLayout(input_layout)
        self.history_panel_widget = QWidget()
        self.history_panel_widget.setFixedWidth(220)
        self.history_panel_widget.setStyleSheet('border-radius: 8px; padding: 5px;')
        self.history_panel = QVBoxLayout(self.history_panel_widget)
        self.history_title = QLabel('Chat History')
        self.history_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.history_title.setStyleSheet('font-size: 16px; font-weight: bold; color: #dddddd; padding: 5px;')
        from PyQt6.QtWidgets import QListWidget
        self.history_list = QListWidget()
        self.history_list.setSpacing(4)
        self.history_list.setEditTriggers(QListWidget.EditTrigger.DoubleClicked)
        self.history_list.itemDoubleClicked.connect(self.rename_session)
        self.history_list.setToolTip('Double Click to Rename or Delete Session.')
        self.history_list.setStyleSheet('\n\t\t\t\t\t\t\t\t\t\t\t\tQListWidget { background-color: #ffffff; border-radius: 6px; padding: 5px; }\n\t\t\t\t\t\t\t\t\t\t\t\tQListWidget::item { background-color: #000000; padding: 8px; color: #ffffff; border-radius:6px; }\n\t\t\t\t\t\t\t\t\t\t\t\tQListWidget::item:selected { background-color: #242424; border-radius:6px; }\n\t\t\t\t\t\t\t\t\t\t\t\tQListWidget::item:hover { background-color: #1b1b1b; border-radius:6px; }\n\t\t\t\t\t\t\t\t')
        self.history_list.itemClicked.connect(self.load_session)
        new_chat_button = QPushButton('+ New Chat')
        new_chat_button.clicked.connect(self.create_new_session)
        new_chat_button.setFixedHeight(40)
        self.history_panel.addWidget(self.history_title)
        self.history_panel.addWidget(new_chat_button)
        self.history_panel.addWidget(self.history_list)
        sidebar_widget = QWidget()
        sidebar_widget.setLayout(self.history_panel)
        main_layout.addWidget(sidebar_widget)
        main_layout.addLayout(chat_layout)
        self.setLayout(main_layout)
        self.update_history()
    from PyQt6.QtCore import QTimer

    def start_auto_clear_timer(self):
        self.clear_timer = QTimer(self)
        self.clear_timer.timeout.connect(self.reset_conversation_session)
        self.clear_timer.start(1800000)

    def reset_conversation_session(self):
        clear_conversation_history()
        load_conversation_history()

    def load_sessions(self):
        if os.path.exists(self.sessions_file):
            try:
                with open(self.sessions_file, 'r') as file:
                    self.chat_sessions = json.load(file)
            except Exception as e:
                write_to_log(f'Error loading chat sessions: {e}', file_path='logs/errors.log')

    def create_new_session(self, session_name=None):
        if not session_name:
            from datetime import datetime
            session_name = 'New Chat'
        if session_name in self.chat_sessions:
            counter = 1
            base_name = session_name
            while session_name in self.chat_sessions:
                session_name = f'{base_name} ({counter})'
                counter += 1
        self.current_session = session_name
        self.chat_sessions[session_name] = []
        self.clear_screen()
        self.update_history()
        self.save_sessions()
        self.session_button.hide()
        self.clear_button.show()
        self.watermark = QLabel('Nectar-X', self)
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watermark.setStyleSheet('color: rgba(255, 255, 255, 0.07); font-size: 50px; font-weight: bold;')
        self.chat_display.addWidget(self.watermark)

    def save_sessions(self):
        try:
            with open(self.sessions_file, 'w') as file:
                json.dump(self.chat_sessions, file, indent=4)
        except Exception as e:
            write_to_log(f'Error saving chat sessions: {e}', file_path='logs/errors.log')

    def clear_sessions(self):
        """Clears all saved chat sessions both in memory and in the file (without deleting the file)."""  # inserted
        try:
            self.chat_sessions = {}
            with open(self.sessions_file, 'w') as file:
                json.dump(self.chat_sessions, file, indent=4)
            write_to_log('All chat sessions have been cleared (file retained).')
        except Exception as e:
            write_to_log(f'Error clearing chat sessions: {e}', file_path='logs/errors.log')

    def append_to_session(self, message):
        if self.current_session not in self.chat_sessions:
            self.chat_sessions[self.current_session] = []
        self.chat_sessions[self.current_session].append(message)

    def send_message(self):
        user_text = self.input_field.text().strip()
        if not user_text:
            return
        if self.current_session is None:
            self.current_session = user_text[:20]
            self.chat_sessions[self.current_session] = []
        self.append_to_session(f'You: {user_text}')
        self.display_message(user_text, 'user')
        self.input_field.clear()
        self.loader_label.show()
        self.progress_bar.show()
        self.worker = ChatWorker(user_text)
        self.worker.finished.connect(self.handle_ai_response)
        self.worker.start()
        self.update_history()
        self.save_sessions()

    def display_message(self, text, sender):
        bubble = QFrame()
        bubble_layout = QVBoxLayout()
        message_label = QLabel(text)
        message_label.setWordWrap(True)
        message_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse | Qt.TextInteractionFlag.LinksAccessibleByMouse)
        if sender == 'user':
            bubble.setStyleSheet('background-color: #444; color: white; padding: 10px; border-radius: 6px;')
            message_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        else:  # inserted
            if sender == 'ai':
                bubble.setStyleSheet('background-color: #333; color: white; padding: 10px; border-radius: 6px;')
                message_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            else:  # inserted
                if sender == 'error':
                    bubble.setStyleSheet('background-color: #ff5555; color: white; padding: 10px; border-radius: 6px;')
                    message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bubble_layout.addWidget(message_label)
        bubble.setLayout(bubble_layout)
        self.chat_display.addWidget(bubble)
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def handle_ai_response(self, response):
        self.chat_sessions[self.current_session].append(f'AI: {response}')
        self.display_message(response, 'ai')
        self.loader_label.hide()
        self.progress_bar.hide()
        self.save_sessions()

    def update_history(self):
        self.history_list.blockSignals(True)
        self.history_list.clear()
        for session in self.chat_sessions:
            item = QListWidgetItem(session)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
            self.history_list.addItem(item)
        self.history_list.blockSignals(False)

    def rename_session(self, item):
        old_name = item.text()
        dialog = QDialog(self)
        dialog.setWindowTitle('Rename or Delete Session')
        layout = QVBoxLayout(dialog)
        input_label = QLabel('Enter new name:')
        input_field = QLineEdit(old_name)
        layout.addWidget(input_label)
        layout.addWidget(input_field)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        delete_button = QPushButton('Delete Session')
        button_box.addButton(delete_button, QDialogButtonBox.ButtonRole.ActionRole)
        layout.addWidget(button_box)

        def on_delete():
            confirm = QMessageBox.question(self, 'Delete Session', f'Are you sure you want to delete the session \'{old_name}\'?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                if old_name in self.chat_sessions:
                    del self.chat_sessions[old_name]
                if self.current_session == old_name:
                    self.current_session = None
                    self.clear_screen()
                matched_items = self.history_list.findItems(old_name, Qt.MatchFlag.MatchExactly)
                if matched_items:
                    self.history_list.takeItem(self.history_list.row(matched_items[0]))
                self.save_sessions()
                self.update_history()
                dialog.accept()
        delete_button.clicked.connect(on_delete)

        def on_accept():
            new_name = input_field.text().strip()
            if new_name and new_name!= old_name:
                if new_name in self.chat_sessions:
                    QMessageBox.warning(self, 'Duplicate Name', 'A session with this name already exists.')
                    return
                self.chat_sessions[new_name] = self.chat_sessions.pop(old_name)
                matched_items = self.history_list.findItems(old_name, Qt.MatchFlag.MatchExactly)
                if matched_items:
                    matched_items[0].setText(new_name)
                if self.current_session == old_name:
                    self.current_session = new_name
                self.save_sessions()
                self.update_history()
            dialog.accept()
        button_box.accepted.connect(on_accept)
        button_box.rejected.connect(dialog.reject)
        dialog.exec()

    def load_session(self, session_item):
        session_name = session_item.text()
        self.current_session = session_name
        self.clear_screen()
        for message in self.chat_sessions.get(session_name, []):
            sender, text = message.split(': ', 1) if ': ' in message else ('error', message)
            self.display_message(text, sender)

    def clear_screen(self):
        for i in reversed(range(self.chat_display.count())):
            widget = self.chat_display.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        self.clear_button.show()

    def clear_everything(self):
        for i in reversed(range(self.chat_display.count())):
            self.chat_display.itemAt(i).widget().deleteLater()
            self.load_sessions()
            self.update_history()
            clear_conversation_history()
        self.watermark = QLabel('Nectar-X', self)
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watermark.setStyleSheet('color: rgba(255, 255, 255, 0.07); font-size: 50px; font-weight: bold;')
        self.chat_display.addWidget(self.watermark)

class MessageWorker(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, message):
        super().__init__()
        self.message = message

    def run(self):
        try:
            import socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect(('127.0.0.1', 5005))
                client.send(self.message.encode('utf-8'))
                reply = client.recv(4096).decode('utf-8')
                self.finished.emit(reply)
        except Exception as e:
            self.error.emit(str(e))

class EmittingStream(QObject):
    text_written = pyqtSignal(str)

    def write(self, text):
        self.text_written.emit(str(text))

    def flush(self):
        return
from PyQt6.QtCore import QObject, pyqtSignal

class SignalEmitter(QObject):
    auto_run = pyqtSignal()
    stop = pyqtSignal()

class ClickableLabel1(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.default_style = '\n            background-color: #000000;\n            color: #ffffff;\n            padding: 10px 15px;\n            border-radius: 10px;\n            font-size: 13px;\n        '
        self.hover_style = '\n            background-color: #ffffff;\n            color: #000000;\n            padding: 10px 15px;\n            border-radius: 10px;\n            font-size: 13px;\n        '
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
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class AppState:
    loaded_model_path = ''
from functools import partial

class Engine_Holder(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_model_watcher()
        self.setWindowTitle('K47B-LS5')
        self.settings1 = QSettings('NectarX', 'Modelpath')
        self.signals = SignalEmitter()
        self.signals.auto_run.connect(self.auto_run)
        self.signals.stop.connect(self.terminate)
        self.loaded_model_path = ''
        self.executable_path = ''
        self.process = None
        self.llm_server_thread = None
        self.llm_instance = None
        self.conversation_history = []
        AppState.loaded_model_path = self.loaded_model_path
        self.init_ui()

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'ICON', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

    def init_ui(self):
        import qtawesome as qta
        main_layout = QHBoxLayout()
        from PyQt6.QtWidgets import QSizePolicy
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(12)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        icon_path51 = self.find_icon('ICON\\menu\\net.png')
        icon_path52 = self.find_icon('ICON\\menu\\chat2.png')
        icon_path53 = self.find_icon('ICON\\menu\\sett.png')
        icons = {'Load': QIcon(icon_path51), 'Code': QIcon(icon_path52), 'Settings': QIcon(icon_path53)}
        for i, name in enumerate(['Load', 'Code', 'Settings']):
            btn = QPushButton()
            btn.setIcon(icons[name])
            btn.setIconSize(QSize(24, 24))
            btn.setToolTip(name)
            btn.setFixedSize(44, 44)
            btn.setStyleSheet('\n                QPushButton {\n                    background-color: 1e1e1e ;\n                    border-radius: 10px;\n                }\n                QPushButton:hover {\n                    background-color: #000000;\n                }\n                QPushButton:pressed {\n                    background-color: #000000;\n                }\n            ')
            btn.clicked.connect(lambda _, idx=i: self.card_layout.setCurrentIndex(idx))
            sidebar_layout.addWidget(btn)
        sidebar_layout.addStretch(1)
        self.stop_server_button = QPushButton()
        self.stop_server_button.setIcon(qta.icon('fa5s.power-off', color='black'))
        self.stop_server_button.setToolTip('Stop')
        self.stop_server_button.setIconSize(QSize(20, 20))
        self.stop_server_button.setFixedSize(44, 44)
        self.stop_server_button.setStyleSheet('\n            QPushButton {\n                background-color: #1e1e1e ;\n                border-radius: 8px;\n            }\n            QPushButton:hover {\n                background-color: #ffffff;\n            }\n        ')
        self.stop_server_button.clicked.connect(self.terminate)
        sidebar_layout.addWidget(self.stop_server_button)
        sidebar_widget = QWidget()
        sidebar_widget.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sidebar_widget.setFixedHeight(400)
        sidebar_widget.setStyleSheet('border-radius: 10px; background-color: #1e1e1e')
        sidebar_widget.setLayout(sidebar_layout)
        sidebar_widget.setFixedWidth(64)
        self.card_layout = QStackedLayout()
        self.page_load = self.Engine()
        self.page_code = self.create_code_page()
        self.page_settings = self.create_settings_page()
        self.card_layout.addWidget(self.page_load)
        self.card_layout.addWidget(self.page_code)
        self.card_layout.addWidget(self.page_settings)
        content_widget = QWidget()
        content_widget.setLayout(self.card_layout)
        main_layout.addWidget(sidebar_widget)
        main_layout.addWidget(content_widget)
        self.setLayout(main_layout)

    def Engine(self):
        page = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        model_loader_frame = QFrame()
        model_loader_layout = QVBoxLayout(model_loader_frame)
        model_loader_layout.setContentsMargins(0, 0, 0, 0)
        model_loader_layout.setSpacing(8)
        self.label_model_path = ClickableLabel1('Click to load Model')
        self.label_model_path.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_model_path.setWordWrap(True)
        self.label_model_path.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_model_path.clicked.connect(self.load_model)
        self.label_model_path.setStyleSheet('\n            QLabel {\n                background-color: #000000;\n                border-radius: 8px;\n                padding: 10px;\n                font-size: 14px;\n                color: #dddddd;\n            }\n            \n        ')
        self.combo_model_list = QComboBox()
        self.combo_model_list.addItem('Select Model to Load')
        self.combo_model_list.setStyleSheet('\n            QComboBox {\n                background-color: transparent;\n                border: 1px solid #444;\n                border-radius: 8px;\n                padding: 8px 35px 8px 12px;\n                font-size: 13px;\n                color: #ffffff;\n            }\n\n            QComboBox:hover {\n                border: 1px solid #6c6c6c;\n            }\n\n            QComboBox::drop-down {\n                subcontrol-origin: padding;\n                subcontrol-position: top right;\n                width: 28px;\n                border-left: 1px solid #444;\n                border-top-right-radius: 8px;\n                border-bottom-right-radius: 8px;\n                background-color: #ffffff;\n            }\n\n            QComboBox::down-arrow {\n                image: url(\"background/down-arrow.svg\");  /* Replace this with your icon */\n                width: 12px;\n                height: 12px;\n            }\n\n            QComboBox QAbstractItemView {\n                background-color: #ffffff;\n                color: #000000;\n                border: 1px solid #333;\n                selection-background-color: #1b1b1b;\n                padding: 6px;\n                outline: 0;\n            }\n        ')
        self.combo_model_list.hide()
        model_loader_layout.addWidget(self.label_model_path)
        model_loader_layout.addWidget(self.combo_model_list)
        layout.addWidget(model_loader_frame)
        self.output_area = QPlainTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet('\n            QPlainTextEdit {\n                background-color: transparent;\n                color: #e8e8e8;\n                padding: 12px;\n                border-radius: 10px;\n                font-family: Consolas, monospace;\n                font-size: 13px;\n            }\n        ')
        layout.addWidget(self.output_area)
        self.stdout_stream = EmittingStream()
        self.stdout_stream.text_written.connect(self.append_output)
        sys.stdout = self.stdout_stream
        sys.stderr = self.stdout_stream
        page.setLayout(layout)
        return page

    def append_output(self, text):
        self.output_area.appendPlainText(text.rstrip())

    def create_code_page(self):
        page = Code_Space()
        return page

    def create_group(self, title: str, options: list):
        """\n        Create a group box with combo boxes based on options.\n        options = [(\"Label Text\", [Option1, Option2, ...])]\n        """  # inserted
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

    def get_group_value(self, group_title: str, label_text: str):
        """\n        Retrieves the current selected value from a group combo box.\n        """  # inserted
        return self.group_controls[group_title][label_text].currentText()

    def create_settings_page(self):
        from PyQt6.QtCore import QSettings
        self.set_light_theme()
        self.settings = QSettings('Zashirion', 'Nectar')
        page = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        sliders_layout = QFormLayout()
        sliders_layout.setSpacing(15)

        def add_slider(key, name, slider, label, min_val, max_val, default_val, formatter=str):
            slider.setOrientation(Qt.Orientation.Horizontal)
            slider.setRange(min_val, max_val)
            start_val = int(self.settings.value(key, default_val))
            slider.setValue(start_val)
            label.setText(formatter(start_val))
            label.setMinimumWidth(40)
            slider.valueChanged.connect(lambda val: (label.setText(formatter(val)), self.settings.setValue(key, val)))
            h_layout = QHBoxLayout()
            h_layout.setSpacing(12)
            h_layout.addWidget(slider)
            h_layout.addWidget(label)
            container = QWidget()
            container.setStyleSheet('background-color: #ffffff; color: #000000;')
            container.setLayout(h_layout)
            sliders_layout.addRow(f'{name}:', container)
        title_label = QLabel('<h3>⚙️ Settings</h3>')
        title_label.setFixedHeight(50)
        title_label.setStyleSheet('\n            QLabel {\n                background-color: #ffffff;\n                font-size: 18px;\n                font-weight: bold;\n                color: #000000;\n                padding: 8px 16px;\n                border-radius: 8px;\n            }\n        ')
        spacer = QLabel('')
        spacer.setFixedHeight(0)
        sliders_layout.addRow(title_label)
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
        add_slider('thread_num', 'Threads', self.thread_num, self.thread_num_label, 2, 32, 4)
        self.gpu_layer_label = QLabel()
        self.gpu_layer = QSlider()
        add_slider('gpu_layer', 'GPU Layers', self.gpu_layer, self.gpu_layer_label, 2, 32, 4)
        self.temperature_label = QLabel()
        self.temperature = QSlider()
        add_slider('temperature', 'Temperature', self.temperature, self.temperature_label, 0, 100, 70, lambda v: f'{v / 100:.2f}')
        self.chat_template_group = self.create_group('Chat Template', [('Select Template', ['chatml', 'llama-2', 'mistral-instruct', 'zephyr', 'openchat'])])
        combo = self.group_controls['Chat Template']['Select Template']
        saved_template = QSettings('Nectar-X', 'UserPreferences').value('chat_template', 'chatml')
        index = combo.findText(saved_template)
        if index >= 0:
            combo.setCurrentIndex(index)
        combo.currentTextChanged.connect(lambda value: QSettings('Nectar-X', 'UserPreferences').setValue('chat_template', value))
        sidebar = QVBoxLayout()
        sidebar.setSpacing(10)
        sidebar.setContentsMargins(15, 15, 15, 15)

        def add_checkbox(key, text, default_checked):
            checkbox = QCheckBox(text)
            checked = self.settings.value(key, 'true' if default_checked else 'false') == 'true'
            checkbox.setChecked(checked)
            checkbox.setStyleSheet('\n                QCheckBox {\n                    font-size: 13px;\n                    font-weight: 500;\n                    spacing: 10px;\n                }\n                QCheckBox::indicator {\n                    width: 16px;\n                    height: 16px;\n                }\n            ')
            checkbox.stateChanged.connect(lambda state: self.settings.setValue(key, checkbox.isChecked()))
            sidebar.addWidget(checkbox)
            return checkbox
        self.use_mlock = add_checkbox('use_mlock', 'Use Memory Lock (mlock)', False)
        self.use_verbose = add_checkbox('use_verbose', 'Enable Verbose Logging', False)
        self.use_numa = add_checkbox('use_numa', 'Enable NUMA', True)
        self.use_mmap = add_checkbox('use_mmap', 'Enable Memory Map', True)
        self.use_mmap_mmap = add_checkbox('use_mmap_backend', 'Use mmap backend', True)
        sidebar_frame = QFrame()
        sidebar_frame.setLayout(sidebar)
        sidebar_frame.setStyleSheet('\n            QFrame {\n                background-color: #f8f9fa;\n                border: 1px solid #ccc;\n                border-radius: 10px;\n            }\n        ')
        info_card = QFrame()
        info_card.setStyleSheet('\n            QFrame {\n                background-color: #ffffff;\n                border: 1px solid #ddd;\n                border-radius: 12px;\n                padding: 16px;\n            }\n            QLabel {\n                color: #333;\n                font-size: 13px;\n            }\n        ')
        info_layout = QVBoxLayout()
        info_layout.setSpacing(8)

        def get_llama_version():
            try:
                import llama_cpp
                return llama_cpp.__version__
            except Exception:
                return 'Unavailable'

        def get_runtime_mode():
            try:
                import llama_cpp.llama_cpp as cpp
                info = cpp.llama_print_system_info()
                info = info.decode() if isinstance(info, bytes) else str(info)
                if 'CUDA' in info:
                    return 'GPU (CUDA)'
                if 'Metal' in info:
                    return 'GPU (Metal)'
                if 'ROCm' in info:
                    return 'GPU (ROCm)'
                if 'OpenBLAS' in info or 'AVX' in info:
                    return 'CPU (Optimized)'
                return 'CPU'
            except Exception:
                return 'Unknown'
        engine_type = QLabel('Engine: Zashir K47B-LS5')
        llama_version = QLabel(f'LLAMA.cpp Version: {get_llama_version()}')
        runtime_mode = QLabel(f'Runtime Mode: {get_runtime_mode()}')
        self.build_flags_label = QLabel('Build Flags: Not Available')
        info_layout.addWidget(engine_type)
        info_layout.addWidget(llama_version)
        info_layout.addWidget(runtime_mode)
        info_layout.addWidget(self.build_flags_label)
        info_card.setLayout(info_layout)
        right_panel = QVBoxLayout()
        right_panel.setSpacing(12)
        right_panel.addLayout(sliders_layout)
        right_panel.addWidget(info_card)
        right_panel.addWidget(self.chat_template_group)
        right_panel.addStretch()
        main_layout.addWidget(sidebar_frame)
        main_layout.addLayout(right_panel)
        page.setLayout(main_layout)
        return page

    def update_build_flags_label(self, llm_instance):
        if hasattr(self, 'build_flags_label'):
            flags = self.get_build_flags(llm_instance)
            self.build_flags_label.setText(f'Build Flags: {flags}')

    def set_light_theme(self):
        """Set light (Chrome-like) theme for the application."""  # inserted
        light_stylesheet = '\n                            QCheckBox {\n                                    spacing: 8px;\n                                    border-radius: 10px;\n                                    background-color: #ffffff;\n                                    font-size: 14px;\n                                    color: #000000;\n                                    padding: 5px;\n                            }\n                            QLabel{\n                                border-radius: 5px;\n                                background-color: #1b1b1b;\n                                padding: 10px;\n                            }\n                            QCheckBox::indicator {\n                                    width: 18px;\n                                    height: 18px;\n                                    border-radius: 4px;\n                                    background: #444;\n                                    border: 1px solid #888;\n                            }\n\n                            QCheckBox::indicator:checked {\n                                    background-color: #ffb700;\n                                    border: 1px solid #ffb700;\n                            }\n\n                            QCheckBox::indicator:unchecked {\n                                    background-color: #222;\n                                    border: 1px solid #666;\n                            }\n\n                            QCheckBox:hover {\n                                    color: #00bfff;\n                            }\n                            QSlider::groove:horizontal {\n                                            height: 6px;\n                                            background: #353535;\n                                            margin: 2px 0;\n                                            border-radius: 3px;\n                            }\n                            QSlider::handle:horizontal {\n                                            background: #1E90FF;\n                                            width: 14px;\n                                            height: 14px;\n                                            margin: -4px 0;\n                                            border-radius: 7px;\n                            }\n                            QLineEdit, QTextEdit, QPlainTextEdit {\n                                            background-color: #2a2c31;\n                                            color: #ffffff;\n                                            border: none;\n                                            padding: 5px;\n                                            border-radius: 10px;\n                            }\n                            QListWidget {\n                                            background-color: #3c3f41;\n                                            color: #d3d3d3;\n                                            border: 1px solid #444444;\n                            }\n                            QGroupBox {\n                                            background-color: #ffffff;\n                                            color: #000000;\n                                            margin: 5px;\n                                            padding: 10px;\n                            }\n                            QGroupBox::title {\n                                subcontrol-origin: margin;\n                                subcontrol-position: top center;  /* can be left, right, center */\n                                padding: 0 10px;\n                                color: #000000;\n                                font-size: 16px;\n                                font-weight: bold;\n                                background-color: #ffffff;\n                                border-radius: 6px;\n                            }\n                            QFormLayout {\n                                            background-color: #2b2b2b;\n                                            color: #d3d3d3;\n                            }\n\n                            /* Vertical Scrollbar */\n                            QScrollBar:vertical {\n                                background: transparent;\n                                width: 8px;\n                                margin: 0px;\n                                border: none;\n                            }\n\n                            QScrollBar::handle:vertical {\n                                background: rgba(0, 0, 0, 0.2);\n                                min-height: 20px;\n                                border-radius: 4px;\n                            }\n\n                            QScrollBar::handle:vertical:hover {\n                                background: rgba(0, 0, 0, 0.4);\n                            }\n\n                            QScrollBar::add-line:vertical,\n                            QScrollBar::sub-line:vertical,\n                            QScrollBar::add-page:vertical,\n                            QScrollBar::sub-page:vertical {\n                                background: none;\n                                height: 0px;\n                                border: none;\n                            }\n\n                            /* Horizontal Scrollbar */\n                            QScrollBar:horizontal {\n                                background: transparent;\n                                height: 8px;\n                                margin: 0px;\n                                border: none;\n                            }\n\n                            QScrollBar::handle:horizontal {\n                                background: rgba(0, 0, 0, 0.2);\n                                min-width: 20px;\n                                border-radius: 4px;\n                            }\n\n                            QScrollBar::handle:horizontal:hover {\n                                background: rgba(0, 0, 0, 0.4);\n                            }\n\n                            QScrollBar::add-line:horizontal,\n                            QScrollBar::sub-line:horizontal,\n                            QScrollBar::add-page:horizontal,\n                            QScrollBar::sub-page:horizontal {\n                                background: none;\n                                width: 0px;\n                                border: none;\n                            }\n\n                            '
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

    def setup_model_watcher(self):
        """Initializes the folder watcher for NectarHub."""  # inserted
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
        else:  # inserted
            return None

    def ensure_nectarhub_folder(self):
        program_files = os.environ.get('ProgramFiles', 'C:\\Program Files')
        nectarhub_path = os.path.join(program_files, 'NectarHub')
        try:
            if not os.path.exists(nectarhub_path):
                import ctypes
                if ctypes.windll.shell32.IsUserAnAdmin():
                    os.makedirs(nectarhub_path, exist_ok=True)
                else:  # inserted
                    QMessageBox.warning(self, 'Administrator Required', 'You need administrator privileges to create a folder in Program Files.')
                    return
            return nectarhub_path
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Could not create/access \'NectarHub\' folder:\n{str(e)}')
            return None

    def load_model(self):
        """Scans for GGUF models in NectarHub and populates the combo box."""  # inserted
        nectarhub_path = self.ensure_nectarhub_folder()
        if not nectarhub_path:
            return
        gguf_models = []
        try:
            for root, _, files in os.walk(nectarhub_path):
                for file in files:
                    if file.lower().endswith('.gguf'):
                        full_path = os.path.join(root, file)
                        gguf_models.append((file, full_path))
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error while scanning for models:\n{str(e)}')
            return
        self.combo_model_list.blockSignals(True)
        self.combo_model_list.clear()
        self.combo_model_list.addItem('Select Model to Load')
        for display_name, full_path in gguf_models:
            self.combo_model_list.addItem(display_name, full_path)
        self.combo_model_list.addItem('Load External Model', 'custom_path')
        self.combo_model_list.blockSignals(False)
        self.combo_model_list.show()
        try:
            self.combo_model_list.currentIndexChanged.disconnect()
        except TypeError:
            pass
        self.combo_model_list.currentIndexChanged.connect(self.model_selected)

    def model_selected(self, index: int):
        path = self.combo_model_list.itemData(index)
        if path == 'custom_path':
            file_path, _ = QFileDialog.getOpenFileName(self, 'Select GGUF Model', '', 'GGUF Files (*.gguf);;All Files (*)')
            if file_path:
                self.loaded_model_path = file_path
                self.settings1.setValue('models/last_used_path', self.loaded_model_path)
                self.label_model_path.setText(os.path.basename(file_path))
                self.start_server()
            else:  # inserted
                self.combo_model_list.setCurrentIndex(0)
        else:  # inserted
            if path and isinstance(path, str):
                self.loaded_model_path = path
                self.settings1.setValue('models/last_used_path', path)
                self.label_model_path.setText(os.path.basename(path))
                self.start_server()
        self.combo_model_list.hide()

    def auto_run(self):
        """Reloads the last used model from QSettings if it exists."""  # inserted
        last_path = self.settings1.value('models/last_used_path', '')
        if last_path and os.path.exists(last_path):
            self.loaded_model_path = last_path
            self.label_model_path.setText(os.path.basename(last_path))
            self.start_server()
        else:  # inserted
            QMessageBox.information(self, 'Auto Run', 'No previously loaded model found or file no longer exists.')

    def start_server(self):
        if not self.loaded_model_path:
            QMessageBox.warning(self, 'Error', 'Please load a GGUF model first.')
            return
        if self.llm_server_thread is not None and self.llm_server_thread.is_alive():
            QMessageBox.information(self, 'Engine', 'Engine is already running.')
            return
        self.llm_server_thread = threading.Thread(target=self.start_llm_server, daemon=True)
        self.llm_server_thread.start()

    def show_notification(self, message, bg_color='#000000', text_color='#ffffff', duration=10000):
        QTimer.singleShot(0, lambda: FloatingNotification(self, message, duration, bg_color, text_color))

    def start_llm_server(self):
        if Llama is None:
            self.show_notification('llama-cpp-python is not installed.')
            QMessageBox.information(self, 'llama-cpp-python', 'llama-cpp-python is not installed.')
            return
        try:
            ctx_value = self.context_size.value()
            thread_value = self.thread_num.value()
            gpu_layer_amount = self.gpu_layer.value()
            use_mem_lock = self.use_mlock.isChecked()
            use_verbose = self.use_verbose.isChecked()
            use_numa = self.use_numa.isChecked()
            use_mmap_activate = self.use_mmap.isChecked()
            use_mmap_active = self.use_mmap_mmap.isChecked()
            btx_value = self.batch_size.value()
            chat_format_selected = self.get_group_value('Chat Template', 'Select Template')
            self.llm_instance = Llama(model_path=self.loaded_model_path, n_ctx=ctx_value, chat_format=chat_format_selected, n_threads=thread_value, n_gpu_layers=gpu_layer_amount, use_mlock=use_mem_lock, verbose=use_verbose, numa=use_numa, mmap=use_mmap_activate, use_mmap=use_mmap_active, n_batch=btx_value)
            self.update_build_flags_label(self.llm_instance)
            self.conversation_history = []
            import socket
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(('127.0.0.1', 5005))
            self.server.listen(5)
            self.show_notification('Engine Running')
            if ctx_value > 8192:
                self.show_notification('⚠️ Warning: Very high context size. This may use a lot of RAM and slow down your system.')
            else:  # inserted
                if ctx_value > 4096:
                    self.show_notification('ℹ️ Note: This is a fairly high context size. Make sure your system has enough memory.')
                else:  # inserted
                    if ctx_value < 512:
                        self.show_notification('❌ Error: Context size too low. Minimum supported is 512 tokens.', bg_color='#8b0000')
                    else:  # inserted
                        if ctx_value == 512:
                            self.show_notification('⚠️ Warning: Minimum context size selected. Responses may be very short or cut off.')
                        else:  # inserted
                            if ctx_value == 4096:
                                self.show_notification('✅ Recommended: Recommended context size 4096 selected.')
                            else:  # inserted
                                self.show_notification(f'✔️ Context size set to {ctx_value} tokens.')
            while True:  # inserted
                client, _ = self.server.accept()
                threading.Thread(target=self.handle_client, args=(client,), daemon=True).start()
        except Exception as e:
            self.show_notification(f'Engine error: {e}')

    def handle_client(self, client_socket):
        try:
            data = client_socket.recv(4096).decode('utf-8')
            if data.startswith('LOAD_MODEL::'):
                client_socket.send(b'OK')
                return
            self.conversation_history.append({'role': 'user', 'content': data})
            self.conversation_history.append({'role': 'system', 'content': ' '})
            result = self.llm_instance.create_chat_completion(self.conversation_history, max_tokens=self.max_tokens.value(), temperature=self.temperature.value() / 100)
            reply = result['choices'][0]['message']['content'].strip()
            self.conversation_history.append({'role': 'assistant', 'content': reply})
            client_socket.send(reply.encode('utf-8'))
        except Exception as e:
            client_socket.send(f'Error: {e}'.encode('utf-8'))
        finally:  # inserted
            pass  # postinserted
        client_socket.close()
        client_socket.close()

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

    def run_model(self):
        if not self.loaded_model_path:
            QMessageBox.warning(self, 'Error', 'Please load a GGUF model first.')
            return
        try:
            import socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect(('127.0.0.1', 5005))
                command = f'LOAD_MODEL::{self.loaded_model_path}'
                client.send(command.encode('utf-8'))
                ack = client.recv(1024)
            if b'OK' in ack:
                QMessageBox.information(self, 'Model Loaded', 'Model loaded')
            else:  # inserted
                QMessageBox.critical(self, 'Error', 'failed to load model.')
        except Exception as e:
            QMessageBox.critical(self, 'Connection Error', str(e))

    def terminate(self):
        """Terminate the server and clean up resources."""  # inserted
        if self.llm_server_thread:
            self.server.close()
            self.loaded_model_path = None
            self.label_model_path.setText('No model selected')
            self.llm_server_thread.join()
            self.llm_instance = None
            self.output_area.clear()
            self.llm_server_thread = None
        FloatingNotification(self, '🚀 Engine Stopped')
ACCESS_TOKEN = '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'
token = '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'

class RepoSearchThread(QThread):
    search_complete = pyqtSignal(list)
    search_failed = pyqtSignal(str)

    def __init__(self, query):
        super().__init__()
        self.query = query

    def run(self):
        url = f'https://huggingface.co/api/models?search={self.query}&full=1'
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            repos = response.json()
            if not repos:
                self.search_failed.emit('No repositories found for the search query.')
                return
            results = []

            def fetch_info(repo):
                repo_id = repo.get('id', 'Unknown')
                tags = repo.get('tags') or repo.get('cardData', {}).get('tags', [])
                tags_str = ', '.join(tags) if tags else 'None'
                info = self.get_model_info(repo_id)
                downloads = info.get('downloads', 'N/A')
                return {'id': repo_id, 'description': f'Tags: {tags_str}', 'downloads': downloads}
            from concurrent.futures import ThreadPoolExecutor, as_completed
            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = [executor.submit(fetch_info, repo) for repo in repos]
                for future in as_completed(futures):
                    try:
                        results.append(future.result())
                    except Exception:
                        continue
            self.search_complete.emit(results)
        except Exception as e:
            self.search_failed.emit(f'Search failed: {str(e)}')

    def get_model_info(self, repo_id):
        url = f'https://huggingface.co/api/models/{repo_id}'
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception:
            return {}
import psutil

class FileListingThread(QThread):
    file_listing_complete = pyqtSignal(list)
    file_listing_failed = pyqtSignal(str)

    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id

    def run(self):
        url = f'https://huggingface.co/api/models/{self.repo_id}/tree/main'
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            files = response.json()
            total_ram = psutil.virtual_memory().total
            gguf_files = []
            for f in files:
                if f['path'].endswith('.gguf'):
                    size_bytes = f.get('size', 0)
                    too_large = size_bytes > total_ram if isinstance(size_bytes, (int, float)) else False
                    gguf_files.append({'path': f['path'], 'size': f'{round(size_bytes / 1073741824, 2)} GB' if isinstance(size_bytes, (int, float)) else 'Unknown', 'too_large': too_large})
            self.file_listing_complete.emit(gguf_files)
        except Exception as e:
            self.file_listing_failed.emit(f'Failed to list files in repository {self.repo_id}:\n{e}')

class DownloadThread23(QThread):
    progress_changed = pyqtSignal(int)
    download_complete = pyqtSignal(str)
    download_failed = pyqtSignal(str)

    def __init__(self, url, save_path):
        super().__init__()
        self.url = url
        self.save_path = save_path
        self._pause = False
        self._cancel = False

    def pause(self):
        self._pause = True

    def resume(self):
        self._pause = False

    def cancel(self):
        self._cancel = True

    def run(self):
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        try:
            with requests.get(self.url, headers=headers, stream=True) as r:
                r.raise_for_status()
                total = int(r.headers.get('Content-Length', 0))
                with open(self.save_path, 'wb') as f:
                    downloaded = 0
                    for chunk in r.iter_content(chunk_size=8192):
                        while self._pause:
                            self.msleep(100)
                        if self._cancel:
                            break
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total:
                                self.progress_changed.emit(int(downloaded / total * 100))
            if not self._cancel:
                self.download_complete.emit(self.save_path)
        except Exception as e:
            self.download_failed.emit(str(e))

class DownloadCard(QFrame):
    def __init__(self, file_name, save_path, delete_callback=None):
        super().__init__()
        self.file_name = file_name
        self.save_path = save_path
        self.delete_callback = delete_callback
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet('\n            QFrame {\n                background-color: #ffffff;\n                border: 1px solid #ddd;\n                border-radius: 12px;\n                padding: 12px;\n            }\n            QLabel {\n                color: #333;\n                font-size: 13px;\n            }\n            .setStyleSheet\n\t\t\t\tQScrollBar:vertical {\n\t\t\t\tbackground: transparent;\n\t\t\t\twidth: 8px;\n\t\t\t\tmargin: 0px;\n\t\t\t\tborder: none;\n\t\t\t}\n\n\t\t\tQScrollBar::handle:vertical {\n\t\t\t\tbackground: rgba(0, 0, 0, 0.2);\n\t\t\t\tmin-height: 20px;\n\t\t\t\tborder-radius: 4px;\n\t\t\t}\n\n\t\t\tQScrollBar::handle:vertical:hover {\n\t\t\t\tbackground: #ffffff;\n\t\t\t}\n\n\t\t\tQScrollBar::add-line:vertical,\n\t\t\tQScrollBar::sub-line:vertical,\n\t\t\tQScrollBar::add-page:vertical,\n\t\t\tQScrollBar::sub-page:vertical {\n\t\t\t\tbackground: none;\n\t\t\t\theight: 0px;\n\t\t\t\tborder: none;\n\t\t\t}\n\n\t\t\t/* Horizontal Scrollbar */\n\t\t\tQScrollBar:horizontal {\n\t\t\t\tbackground: transparent;\n\t\t\t\theight: 8px;\n\t\t\t\tmargin: 0px;\n\t\t\t\tborder: none;\n\t\t\t}\n\n\t\t\tQScrollBar::handle:horizontal {\n\t\t\t\tbackground: rgba(0, 0, 0, 0.2);\n\t\t\t\tmin-width: 20px;\n\t\t\t\tborder-radius: 4px;\n\t\t\t}\n\n\t\t\tQScrollBar::handle:horizontal:hover {\n\t\t\t\tbackground: rgba(0, 0, 0, 0.4);\n\t\t\t}\n\n\t\t\tQScrollBar::add-line:horizontal,\n\t\t\tQScrollBar::sub-line:horizontal,\n\t\t\tQScrollBar::add-page:horizontal,\n\t\t\tQScrollBar::sub-page:horizontal {\n\t\t\t\tbackground: none;\n\t\t\t\twidth: 0px;\n\t\t\t\tborder: none;\n\t\t\t} \n        ')
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(12, 12, 12, 12)
        self.label = QLabel(self.file_name)
        self.label.setFont(QFont('Segoe UI', 10, QFont.Bold))
        main_layout.addWidget(self.label)
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(6)
        self.progress = QProgressBar()
        self.progress.setMinimumWidth(180)
        self.progress.setFixedHeight(20)
        self.progress.setTextVisible(True)
        self.progress.setStyleSheet('\n            QProgressBar {\n                background-color: #eee;\n                border: 1px solid #ccc;\n                border-radius: 4px;\n                text-align: center;\n                color: #444;\n            }\n            QProgressBar::chunk {\n                background-color: #1b1b1b;\n                border-radius: 4px;\n            }\n        ')
        bottom_layout.addWidget(self.progress, stretch=2)
        icon_path0 = find_icon('ICON/menu/play.png')
        icon_path1 = find_icon('ICON/menu/pause.png')
        icon_path2 = find_icon('ICON/menu/cancel.png')
        icon_path3 = find_icon('ICON/menu/folder.png')
        icon_path4 = find_icon('ICON/menu/delete.png')
        self.resume_btn = self.create_icon_button(icon_path0, '#eee', '#bbb')
        self.resume_btn.hide()
        bottom_layout.addWidget(self.resume_btn)
        self.pause_btn = self.create_icon_button(icon_path1, '#eee', '#bbb')
        self.pause_btn.hide()
        bottom_layout.addWidget(self.pause_btn)
        self.cancel_btn = self.create_icon_button(icon_path2, '#fee', '#faa')
        self.cancel_btn.hide()
        bottom_layout.addWidget(self.cancel_btn)
        self.open_btn = self.create_icon_button(icon_path3, 'transparent', '#ddd')
        self.open_btn.setEnabled(False)
        self.open_btn.clicked.connect(self.open_file_location)
        bottom_layout.addWidget(self.open_btn)
        self.delete_btn = self.create_icon_button(icon_path4, 'transparent', '#ddd')
        self.delete_btn.clicked.connect(self.on_delete)
        self.delete_btn.setEnabled(False)
        bottom_layout.addWidget(self.delete_btn)
        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)

    def create_icon_button(self, icon_path, bg, hover):
        btn = QPushButton(QIcon(icon_path), '', self)
        btn.setFixedSize(24, 24)
        btn.setStyleSheet(f'\n            QPushButton {\n                background-color: {bg};\n                border: none;\n                border-radius: 6px;\n            }\n            QPushButton:hover {\n                background-color: {hover};\n            }\n        ')
        return btn

    def open_file_location(self):
        if os.path.exists(self.save_path):
            folder = os.path.dirname(self.save_path)
            QDesktopServices.openUrl(QUrl.fromLocalFile(folder))

    def on_delete(self):
        if self.delete_callback:
            self.delete_callback(self.file_name, self.save_path)

class DownloadsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NDM')
        self.setMinimumSize(600, 400)
        self.setStyleSheet('background-color: #121212; color: white;')
        icon_path = find_icon('background/NectarX.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:  # inserted
            self.setWindowIcon(QIcon('background/NectarX.png'))
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet('\n                                    QScrollBar:vertical {\n\t\t\t\t\t\t\t\t\tbackground: transparent;\n\t\t\t\t\t\t\t\t\twidth: 8px;\n\t\t\t\t\t\t\t\t\tmargin: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:vertical {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.2);\n\t\t\t\t\t\t\t\t\tmin-height: 20px;\n\t\t\t\t\t\t\t\t\tborder-radius: 4px;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:vertical:hover {\n\t\t\t\t\t\t\t\t\tbackground: #ffffff;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::add-line:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::sub-line:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::add-page:vertical,\n\t\t\t\t\t\t\t\tQScrollBar::sub-page:vertical {\n\t\t\t\t\t\t\t\t\tbackground: none;\n\t\t\t\t\t\t\t\t\theight: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\t/* Horizontal Scrollbar */\n\t\t\t\t\t\t\t\tQScrollBar:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: transparent;\n\t\t\t\t\t\t\t\t\theight: 8px;\n\t\t\t\t\t\t\t\t\tmargin: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.2);\n\t\t\t\t\t\t\t\t\tmin-width: 20px;\n\t\t\t\t\t\t\t\t\tborder-radius: 4px;\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::handle:horizontal:hover {\n\t\t\t\t\t\t\t\t\tbackground: rgba(0, 0, 0, 0.4);\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tQScrollBar::add-line:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::sub-line:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::add-page:horizontal,\n\t\t\t\t\t\t\t\tQScrollBar::sub-page:horizontal {\n\t\t\t\t\t\t\t\t\tbackground: none;\n\t\t\t\t\t\t\t\t\twidth: 0px;\n\t\t\t\t\t\t\t\t\tborder: none;\n\t\t\t\t\t\t\t\t} ')
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll_area)

    def add_download_card(self, card):
        self.scroll_layout.addWidget(card)
from PyQt6.QtCore import QTimer

class Gguf_Downloader(QWidget):
    def __init__(self):
        from PyQt6.QtCore import QSettings
        super().__init__()
        self.downloads_window = DownloadsWindow()
        self.download_folder = self.get_or_create_nectarhub_folder()
        os.makedirs(self.download_folder, exist_ok=True)
        self.settings = QSettings('NectarX', 'NDM (Nectar Download Manager)')
        self.completed_downloads = self.load_history()
        self.init_ui()
        self.display_hardware_info()
        self.restore_download_history()

    def get_or_create_nectarhub_folder(self):
        program_files = os.environ.get('ProgramFiles', 'C:\\Program Files')
        nectarhub_path = os.path.join(program_files, 'NectarHub')
        try:
            if not os.path.exists(nectarhub_path):
                import ctypes
                if ctypes.windll.shell32.IsUserAnAdmin():
                    os.makedirs(nectarhub_path, exist_ok=True)
                else:  # inserted
                    QMessageBox.warning(self, 'Admin Required', 'Administrator rights are required to create \'NectarHub\' in Program Files.')
                    return
            return nectarhub_path
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to create/access \'NectarHub\':\n{e}')
            return None

    def init_ui(self):
        self.setWindowTitle('Downloader')
        self.setStyleSheet('background-color: transparent; color: #FFFFFF;')
        main_layout = QVBoxLayout()
        main_layout.setSpacing(2)
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Search for models (e.g. llama, codellama)')
        self.search_input.returnPressed.connect(self.search_repositories)
        self.search_input.setStyleSheet('background-color: #1e1e1e; color: white; padding: 12px 20px; border-radius: 5px; font-size: 14px;')
        search_layout.addWidget(self.search_input)
        main_layout.addLayout(search_layout)
        self.text_output = QLabel('Output goes here')
        self.text_output.setTextFormat(Qt.TextFormat.RichText)
        self.text_output.setStyleSheet('background-color: transparent; color: white; padding: 5px;')
        main_layout.addWidget(self.text_output)
        toggle_layout = QHBoxLayout()
        toggle_layout.setSpacing(2)
        toggle_label = QLabel('GGUF Mode:')
        toggle_label.setStyleSheet('font-size: 14px; padding: 5px;')
        self.gguf_checkbox = AnimatedCheckBox()
        self.gguf_checkbox.stateChanged.connect(self.toggle_gguf_mode)
        toggle_layout.addWidget(toggle_label)
        toggle_layout.addWidget(self.gguf_checkbox)
        toggle_layout.addStretch()
        main_layout.addLayout(toggle_layout)
        self.repo_container_widget = QWidget()
        self.repo_container_layout = QVBoxLayout()
        self.repo_container_widget.setLayout(self.repo_container_layout)
        self.repo_scroll = QScrollArea()
        self.repo_scroll.setWidgetResizable(True)
        self.repo_scroll.setWidget(self.repo_container_widget)
        self.model_container_widget = QWidget()
        self.model_container_layout = QVBoxLayout()
        self.model_container_widget.setLayout(self.model_container_layout)
        self.model_scroll = QScrollArea()
        self.model_scroll.setWidgetResizable(True)
        self.model_scroll.setWidget(self.model_container_widget)
        repo_model_layout = QHBoxLayout()
        repo_model_layout.addWidget(self.repo_scroll)
        main_layout.addLayout(repo_model_layout)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        main_layout.addWidget(self.progress_bar)
        self.downloads_btn = QPushButton('Downloads')
        self.downloads_btn.clicked.connect(lambda: self.downloads_window.show())
        self.downloads_btn.setStyleSheet(' QPushButton { padding: 12px; background-color: #1b1b1b; color: white; border-radius: 5px;} QPushButton:hover { background-color: #ffffff; color: #000000;}')
        main_layout.addWidget(self.downloads_btn)
        self.status_label = QLabel('Note only select repositories that end in GGUF.')
        self.status_label.setStyleSheet('font-size: 14px; color: #B0B0B0;')
        main_layout.addWidget(self.status_label)
        self.status_label.show()
        self.setLayout(main_layout)

    def show_notification(self, message, bg_color='#000000', text_color='#ffffff', duration=10000):
        QTimer.singleShot(0, lambda: FloatingNotification(self, message, duration, bg_color, text_color))

    def toggle_gguf_mode(self):
        if self.gguf_checkbox.isChecked():
            self.settings.value('append_gguf', True, type=bool)
        else:  # inserted
            self.gguf_checkbox.stateChanged.connect(self.save_append_gguf_setting)

    def save_append_gguf_setting(self):
        self.settings.setValue('append_gguf', self.gguf_checkbox.isChecked())

    def display_hardware_info(self):
        result = get_llm_hardware_recommendation()
        self.text_output.setText(result.replace('\n', '<br>'))

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Download Folder')
        if folder:
            self.download_folder = folder

    def search_repositories(self):
        query = self.search_input.text().strip()
        if not query:
            QMessageBox.warning(self, 'Invalid Search', 'Please enter a search query.')
            return
        if self.gguf_checkbox.isChecked() and (not query.lower().endswith('gguf')):
            query = f'{query} gguf'
        self.repo_search_thread = RepoSearchThread(query)
        self.repo_search_thread.search_complete.connect(self.on_repositories_found)
        self.repo_search_thread.search_failed.connect(self.on_search_failed)
        self.repo_search_thread.start()
        self.status_label.show()
        self.status_label.setText('Searching repositories...')
        self.progress_bar.show()
        self.search_input.clear()

    def on_repositories_found(self, repo_list):
        for i in reversed(range(self.repo_container_layout.count())):
            widget = self.repo_container_layout.takeAt(i).widget()
            if widget:
                widget.deleteLater()
        for repo in repo_list:
            card = RepoCard(repo_id=repo['id'], description=repo.get('description', 'No description'), downloads=repo.get('downloads', 'N/A'))
            card.clicked.connect(self.on_repo_card_clicked)
            self.repo_container_layout.addWidget(card)
            self.progress_bar.hide()
            self.status_label.hide()

    def on_search_failed(self, error):
        self.status_label.hide()
        self.progress_bar.hide()
        QMessageBox.critical(self, 'Search Failed', error)

    def on_repo_card_clicked(self, repo_id):
        self.current_repo_id = repo_id
        self.status_label.show()
        self.status_label.setText(f'Listing .gguf files in {repo_id}...')
        self.progress_bar.show()
        self.file_listing_thread = FileListingThread(repo_id)
        self.file_listing_thread.file_listing_complete.connect(self.on_files_listed)
        self.file_listing_thread.file_listing_failed.connect(self.on_file_listing_failed)
        self.file_listing_thread.start()

    def on_files_listed(self, gguf_files):
        if hasattr(self, 'model_window'):
            self.model_window.close()

        def model_click_handler(file_path):
            self.on_model_card_clicked(file_path)
        self.model_window = ModelViewerWindow(self.current_repo_id, gguf_files, model_click_handler)
        self.model_window.show()
        self.status_label.hide()
        self.progress_bar.hide()
        for file in gguf_files:
            card = ModelCard(file['path'], file['size'])
            card.clicked.connect(self.on_model_card_clicked)
            self.model_container_layout.addWidget(card)
        self.status_label.hide()

    def on_file_listing_failed(self, error):
        QMessageBox.critical(self, 'Error', error)
        self.status_label.hide()
        self.progress_bar.hide()

    def on_model_card_clicked(self, file_path):
        try:
            repo_id = self.get_current_repo_id()
        except AttributeError as e:
            self.status_label.setText(str(e))
            return
        url = f'https://huggingface.co/{repo_id}/resolve/main/{file_path}'
        repo_folder = os.path.join(self.download_folder, self.current_repo_id.replace('/', '_'))
        os.makedirs(repo_folder, exist_ok=True)
        save_path = os.path.join(repo_folder, os.path.basename(file_path))
        card = DownloadCard(file_name=os.path.basename(file_path), save_path=save_path)
        self.downloads_window.add_download_card(card)
        self.model_window.hide()
        self.downloads_window.show()
        card.resume_btn.show()
        card.pause_btn.show()
        card.cancel_btn.show()
        download_thread = DownloadThread23(url, save_path)
        download_thread.progress_changed.connect(card.progress.setValue)

        def on_complete(path):
            card.open_btn.setEnabled(True)
            card.delete_btn.setEnabled(True)
            card.progress.setValue(100)
            QMessageBox.information(self, 'Download Complete', f'File saved to: {path}')
            self.completed_downloads.append({'file_name': card.file_name, 'save_path': card.save_path, 'timestamp': datetime.datetime.now().isoformat()})
            self.save_history()
            card.progress.hide()
            card.pause_btn.hide()
            card.cancel_btn.hide()
            card.resume_btn.hide()
            self.downloads_window.hide()

        def on_fail(error):
            card.label.setText(f'Failed: {error}')
            card.progress.setStyleSheet('QProgressBar::chunk { background-color: red; }')
        download_thread.download_complete.connect(on_complete)
        download_thread.download_failed.connect(on_fail)
        card.pause_btn.clicked.connect(lambda: download_thread.pause())
        card.resume_btn.clicked.connect(lambda: download_thread.resume())
        card.cancel_btn.clicked.connect(lambda: download_thread.cancel())
        download_thread.start()

    def delete_download_card(self, file_name, save_path):
        self.completed_downloads = [item for item in self.completed_downloads if item['file_name']!= file_name or item['save_path']!= save_path]
        self.save_history()
        layout = self.downloads_window.scroll_layout
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, DownloadCard) and widget.file_name == file_name and (widget.save_path == save_path):
                effect = QGraphicsOpacityEffect()
                widget.setGraphicsEffect(effect)
                anim = QPropertyAnimation(effect, b'opacity')
                anim.setDuration(500)
                anim.setStartValue(1.0)
                anim.setEndValue(0.0)
                anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

                def finalize():
                    layout.removeWidget(widget)
                    widget.setParent(None)
                    widget.deleteLater()
                    self.downloads_window.scroll_content.update()
                    self.downloads_window.scroll_area.update()
                    self.downloads_window.repaint()
                anim.finished.connect(finalize)
                anim.start()
                widget._animation = anim
                break

    def save_history(self):
        json_history = json.dumps(self.completed_downloads)
        self.settings.setValue('download_history', json_history)

    def load_history(self):
        raw = self.settings.value('download_history', '')
        if raw:
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                return []
        return []

    def restore_download_history(self):
        for item in self.completed_downloads:
            card = DownloadCard(file_name=item['file_name'], save_path=item['save_path'], delete_callback=self.delete_download_card)
            card.progress.setValue(100)
            card.progress.hide()
            card.open_btn.setEnabled(True)
            card.delete_btn.setEnabled(True)
            self.downloads_window.add_download_card(card)

    def get_current_repo_id(self):
        if hasattr(self, 'current_repo_id'):
            return self.current_repo_id
        raise AttributeError('No repo selected. Make sure a repo card was clicked before selecting a model.')
OWNER = 'headlessripper'
REPO = 'Nectar'
CURRENT_VERSION = 'v1.1'

class DownloadThread(QThread):
    """Separate thread to handle downloading."""
    progress_updated = pyqtSignal(int, int)
    download_complete = pyqtSignal(str)

    def __init__(self, download_url, local_filename):
        super().__init__()
        self.download_url = download_url
        self.local_filename = local_filename

    def run(self):
        import os
        import requests
        headers = {}
        file_exists = os.path.exists(self.local_filename)
        if file_exists:
            file_size = os.path.getsize(self.local_filename)
            headers['Range'] = f'bytes={file_size}-'
        else:  # inserted
            file_size = 0
        response = requests.get(self.download_url, headers=headers, stream=True)
        total_size = int(response.headers.get('content-length', 0)) + file_size
        downloaded_size = file_size
        with open(self.local_filename, 'ab') as file:
            for chunk in response.iter_content(chunk_size=1048576):
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    progress = int(downloaded_size / total_size * 100) if total_size > 0 else 0
                    self.progress_updated.emit(downloaded_size, total_size)
        self.download_complete.emit(self.local_filename)
from urllib.parse import urlparse
from PyQt6.QtGui import QIcon, QFont

class UpdatePrompt(QWidget):
    def __init__(self):
        super().__init__()
        self.is_dark_mode = True
        latest_version, download_url = get_latest_release()
        self.latest_version = latest_version
        self.download_url = download_url
        self.local_filename = os.path.basename(urlparse(self.download_url).path) if self.download_url else ''
        if self.latest_version == CURRENT_VERSION:
            self.init_ui(up_to_date=True)
        else:  # inserted
            self.init_ui(up_to_date=False)

    def init_ui(self, up_to_date=False):
        self.setWindowTitle('Update Available')
        self.setGeometry(600, 300, 400, 200)
        icon_path = self.find_icon('background/icon.png')
        self.setWindowIcon(QIcon(icon_path if icon_path else 'background/icon.png'))
        layout = QVBoxLayout()
        layout.setSpacing(2)
        self.progress_label = QLabel('🠗 Click \'Download\' to start', self)
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar = QProgressBar(self)
        self.progress_bar.hide()
        self.progress_bar.setFixedHeight(22)
        self.progress_bar.setStyleSheet('\n            QProgressBar {\n                background-color: transperent;\n                border-radius: 10px;\n                text-align: center;\n                font-weight: bold;\n                color: #ffffff;\n            }\n            QProgressBar::chunk {\n                background: qlineargradient(\n                    spread:pad, x1:0, y1:0, x2:1, y2:0,\n                    stop:0 #ff0000, stop:1 #000000\n                );\n                \n            }\n        ')
        button_style = '\n            QPushButton {\n                background-color: #000000;\n                color: #ffffff;\n                padding: 10px 18px;\n                border-radius: 8px;\n                font-weight: bold;\n                font-family: \'Segoe UI\';\n            }\n            QPushButton:hover {\n                background-color: #484848;\n                color: #000000;\n            }\n        '
        self.download_button = QPushButton('Download', self)
        self.download_button.setStyleSheet(button_style)
        self.download_button.clicked.connect(self.start_download)
        if up_to_date:
            self.progress_label.hide()
            self.download_button.hide()
            self.label = QLabel(f'<div align=\'center\'><span style=\'font-size:18pt; font-weight:600;\'>Software is <span style=\'color:#555000;\'>Up to Date!</span><br>Version: {CURRENT_VERSION}</span></div>')
        if not up_to_date:
            self.label = QLabel(f'<div align=\'center\'><span style=\'font-size:18pt; font-weight:600;\'>Software Update <br> New Version <span style=\'color:#555000;\'>{self.latest_version}</span> Available</span></div>')
        if not self.download_url:
            self.download_button.hide()
            self.progress_label.hide()
            self.download_button.setText('Download Unavailable')
            self.label = QLabel('<div align=\'center\'><span style=\'font-size:18pt; font-weight:600;\'>No Internet Connection</span></div>')
        self.label.setWordWrap(True)
        layout.addWidget(self.label)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.download_button)
        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.setStyleSheet(button_style)
        self.cancel_button.clicked.connect(self.close)
        self.cancel_button.hide()
        layout.addWidget(self.cancel_button)
        self.skip_button = QPushButton('⤫ Skip', self)
        self.skip_button.hide()
        self.skip_button.setFont(QFont('Arial', 8, QFont.Weight.Bold))
        self.skip_button.setStyleSheet(button_style)
        self.skip_button.clicked.connect(self.skip_update)
        layout.addWidget(self.skip_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        self.update_stylesheet()

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        return next((path for path in possible_paths if os.path.exists(path)), None)

    def skip_update(self):
        self.close()

    def start_download(self):
        self.progress_bar.show()
        self.cancel_button.show()
        self.download_button.setEnabled(False)
        self.download_button.hide()
        self.skip_button.hide()
        self.download_thread = DownloadThread(self.download_url, self.local_filename)
        self.download_thread.progress_updated.connect(self.update_progress)
        self.download_thread.download_complete.connect(self.download_finished)
        self.download_thread.start()

    def update_progress(self, current_size, total_size):
        progress = int(current_size / total_size * 100) if total_size else 0
        self.progress_bar.setValue(progress)
        self.progress_label.setText(f'Downloading... ({self.format_size(current_size)} / {self.format_size(total_size)})')

    def download_finished(self, filename):
        QMessageBox.information(self, 'Download Complete', f'Update downloaded: {filename}')
        self.download_button.show()
        self.prompt_install()

    def prompt_install(self):
        reply = QMessageBox.question(self, 'Install Update', 'Download complete! Do you want to install the update now?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
        if reply == QMessageBox.StandardButton.Yes:
            self.run_installer()
        else:  # inserted
            self.close()

    def run_installer(self):
        try:
            subprocess.run([self.local_filename, '/SILENT'], shell=True)
            QMessageBox.information(self, 'Installation Started', 'The update is being installed.')
            user_profile = os.getenv('USERPROFILE')
            if user_profile:
                app_exe_path = os.path.join('C:\\', 'Users', user_profile.split('\\')[(-1)], 'AppData', 'Local', 'Programs', 'Nectar', 'Nectar-Setup.exe')
                write_to_log(f'Nectar-Setup executable path: {app_exe_path}')
                if os.path.exists(app_exe_path):
                    os.startfile(app_exe_path)
                    QMessageBox.information(self, 'Restarting', 'Nectar-Setup.exe will restart.')
                else:  # inserted
                    QMessageBox.warning(self, 'Restart Failed', 'Could not find Nectar-Setup.exe to restart.')
            else:  # inserted
                QMessageBox.warning(self, 'Profile Path Error', 'Could not retrieve the user\'s profile path.')
        except Exception as e:
            QMessageBox.critical(self, 'Installation Failed', f'Error: {str(e)}')
        self.close()

    def format_size(self, size):
        if size < 1024:
            return f'{size} B'
        if size < 1048576:
            return f'{size / 1024:.2f} KB'
        if size < 1073741824:
            return f'{size / 1048576:.2f} MB'
        return f'{size / 1073741824:.2f} GB'

    def update_stylesheet(self):
        """Update the application stylesheet based on the current mode."""  # inserted
        if self.is_dark_mode:
            self.setStyleSheet(' \n                QWidget {\n                    background-color: #1e1e1e;\n                    color: #ffffff;\n                }\n                QPushButton {\n                    background-color: #000000;\n                    color: #ffffff;\n                    border: none;\n                    padding: 15px;\n                    border-radius: 10px;\n                }\n                QPushButton:hover {\n                    background-color: #484848;\n                    color: #000000;\n                }\n\n                QPushButton:pressed {\n                    background-color: #000000;\n                }\n            ')

def get_latest_release():
    """Fetch latest release details from GitHub API."""  # inserted
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/releases/latest'
    headers = {'Authorization': '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'}
    try:
        import requests
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        release_data = response.json()
        latest_version = release_data.get('tag_name')
        if release_data.get('assets'):
            download_url = release_data['assets'][0]['browser_download_url']
        else:  # inserted
            download_url = release_data.get('html_url')
        return (latest_version, download_url)
    except requests.exceptions.RequestException as e:
        try:
            write_to_log(f'Error fetching release data: {e}', file_path='logs/errors.log')
        except Exception:
            write_to_log(f'Logging failed, but error fetching release data: {e}', file_path='logs/errors.log')
        return (None, None)

class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Settings')
        self.resize(700, 600)
        self.setStyleSheet(self.get_stylesheet())
        self.settings = QSettings('Zashirion', 'Nectar')
        self.combo_boxes = {}
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        general_group = QGroupBox('General')
        general_layout = QVBoxLayout()
        for setting in [('Theme', ['Dark', 'Light', 'System']), ('Device', self.get_available_devices())]:
            general_layout.addLayout(self.create_setting(*setting))
        general_group.setLayout(general_layout)
        container_layout.addWidget(general_group)
        sys_group = QGroupBox('System')
        sys_layout = QVBoxLayout()
        system_info_widget = self.create_system_info_widget()
        sys_layout.addWidget(system_info_widget)
        sys_group.setLayout(sys_layout)
        container_layout.addWidget(sys_group)
        license_group = QGroupBox('License')
        license_layout = QVBoxLayout()
        system_info_widget = self.create_license_widget()
        license_layout.addWidget(system_info_widget)
        license_group.setLayout(license_layout)
        container_layout.addWidget(license_group)
        container_layout.addWidget(self.create_group('Model', [('Engine', ['Zashirions K47B-LS5'])]))
        container_layout.addWidget(self.create_group('LocalDocs', [('LocalDocs Enabled', ['True', 'False'])]))
        button_layout = QHBoxLayout()
        apply_btn = QPushButton('Apply')
        apply_btn.setStyleSheet(' QPushButton { padding: 12px; background-color: #1b1b1b; color: white; border-radius: 5px;} QPushButton:hover { background-color: #ffffff; color: #000000;}')
        reset_btn = QPushButton('Reset')
        reset_btn.setStyleSheet(' QPushButton { padding: 12px; background-color: #1b1b1b; color: white; border-radius: 5px;} QPushButton:hover { background-color: #ffffff; color: #000000;}')
        apply_btn.clicked.connect(self.save_settings)
        reset_btn.clicked.connect(self.reset_settings)
        button_layout.addStretch()
        button_layout.addWidget(apply_btn)
        button_layout.addWidget(reset_btn)
        container_layout.addLayout(button_layout)
        scroll_area.setWidget(container)
        main_layout.addWidget(scroll_area)

    def create_system_info_widget(self):
        info_layout = QVBoxLayout()
        info_layout.setSpacing(5)
        system_info = {'OS': platform.system(), 'Architecture': platform.machine(), 'Processor': get_cpu_info().get('brand_raw', 'Unknown'), 'Physical Cores': psutil.cpu_count(logical=False), 'Total Cores': psutil.cpu_count(logical=True), 'RAM': f'{round(psutil.virtual_memory().total / 1073741824, 2)} GB'}
        for key, value in system_info.items():
            label = QLabel(f'<b>{key}:</b> {value}')
            label.setStyleSheet('padding: 2px;')
            info_layout.addWidget(label)
        container = QWidget()
        container.setLayout(info_layout)
        return container

    def create_license_widget(self):
        info_layout = QVBoxLayout()
        info_layout.setSpacing(5)
        license_info = {'SOFTWARE OWNER': 'Zashirion inc', 'LICENSE KEY': 'CIRB-5002-NGWG-4132', 'DEVELOPER': 'Samuel Ikenna Great', 'CONTACT': 'Nategreat318@gmail.com'}
        for key, value in license_info.items():
            label = QLabel(f'<b>{key}:</b> {value}')
            label.setStyleSheet('padding: 2px;')
            info_layout.addWidget(label)
        container = QWidget()
        container.setLayout(info_layout)
        return container

    def get_available_devices(self):
        devices = ['CPU']
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            if gpus:
                devices.append('GPU')
        except Exception:
            try:
                import torch
                if torch.cuda.is_available():
                    devices.append('GPU')
            except ImportError:
                pass
        return devices

    def create_group(self, group_name, items):
        group = QGroupBox(group_name)
        layout = QVBoxLayout()
        for label_text, options in items:
            layout.addLayout(self.create_setting(label_text, options))
        group.setLayout(layout)
        return group

    def create_setting(self, label_text, options):
        layout = QHBoxLayout()
        layout.setSpacing(20)
        key = label_text.lower().replace(' ', '_')
        label = QLabel(label_text)
        label.setFixedWidth(180)
        combo = QComboBox()
        combo.addItems(options)
        combo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        saved_value = self.settings.value(key)
        if saved_value in options:
            combo.setCurrentText(saved_value)
        else:  # inserted
            combo.setCurrentIndex(0)
        self.combo_boxes[key] = combo
        layout.addWidget(label)
        layout.addWidget(combo)
        return layout

    def save_settings(self):
        for key, combo in self.combo_boxes.items():
            self.settings.setValue(key, combo.currentText())
            self.apply_selected_settings()
        QMessageBox.information(self, 'Settings', 'Settings saved.')

    def apply_selected_settings(self):
        theme = self.combo_boxes['theme'].currentText().lower()
        apply_theme(get_user_theme())
        if theme == 'light':
            apply_theme('light')
            set_user_theme('light')
        else:  # inserted
            if theme == 'dark':
                apply_theme('dark')
                set_user_theme('dark')
            else:  # inserted
                if theme == 'system':
                    apply_theme('system')
                    set_user_theme('system')

    def reset_settings(self):
        self.settings.clear()
        for key, combo in self.combo_boxes.items():
            combo.setCurrentIndex(0)
        QMessageBox.information(self, 'Settings', 'Settings reset to defaults.')

    def get_stylesheet(self):
        return '\n        QWidget {\n            background-color: transparent;\n            color: #f0f0f0;\n            font-family: Segoe UI, sans-serif;\n            font-size: 13px;\n        }\n\n        QGroupBox {\n            border: 1px solid #555;\n            border-radius: 10px;\n            margin-top: 10px;\n            padding: 10px;\n        }\n\n        QGroupBox:title {\n            subcontrol-origin: margin;\n            subcontrol-position: top left;\n            padding: 0 3px;\n            font-weight: bold;\n            font-size: 15px;\n            color: #9cdcfe;\n        }\n\n        QPushButton {\n            background-color: #000000;\n            border: 1px solid #555;\n            border-radius: 6px;\n            padding: 6px 14px;\n        }\n\n        QPushButton:hover {\n            background-color: #505050;\n            border: 1px solid #999;\n        }\n        \n        QComboBox {\n\t\t\tbackground-color: #1e1e1e;\n\t\t\tborder: 1px solid #444;\n\t\t\tborder-radius: 8px;\n\t\t\tpadding: 8px 35px 8px 12px;\n\t\t\tfont-size: 13px;\n\t\t\tcolor: #ffffff;\n\t\t}\n\n\t\tQComboBox:hover {\n\t\t\tborder: 1px solid #6c6c6c;\n\t\t}\n\n\t\tQComboBox::drop-down {\n\t\t\tsubcontrol-origin: padding;\n\t\t\tsubcontrol-position: top right;\n\t\t\twidth: 28px;\n\t\t\tborder-left: 1px solid #444;\n\t\t\tborder-top-right-radius: 8px;\n\t\t\tborder-bottom-right-radius: 8px;\n\t\t\tbackground-color: #2a2a2a;\n\t\t}\n\n\t\tQComboBox::down-arrow {\n\t\t\timage: url(\"background/down-arrow.svg\");  /* Replace this with your custom arrow icon or base64 */\n\t\t\twidth: 12px;\n\t\t\theight: 12px;\n\t\t}\n\n\t\tQComboBox QAbstractItemView {\n\t\t\tbackground-color: #1e1e1e;\n\t\t\tborder: 1px solid #333;\n\t\t\tselection-background-color: #2c2c2c;\n\t\t\tpadding: 6px;\n\t\t\toutline: 0;\n\t\t}\n        '

def set_light_theme2(self):
    """Set dark theme for the application."""  # inserted
    light_stylesheet = '\n\tQWidget {\n\t\tbackground-color: #262626;\n\t\tcolor: #ffffff;\n\t}\n    QTabWidget{\n        border-radius: 12px;\n        background-color: #1e1e1e;\n    }\n\tQLineEdit, QTextEdit, QPlainTextEdit {\n\t\tbackground-color: #2a2c31;\n\t\tcolor: #ffffff;\n\t\tborder: none;\n\t\tpadding: 5px;\n\t\tborder-radius: 10px;\n\t}\n\tQPushButton {\n\t\tbackground-color: #000000; \n\t\tcolor: white; \n\t\tfont-size: 16px; \n\t\tpadding: 10px; \n\t\tborder-radius: 5px;\n\t}\n\tQPushButton:hover {\n\t\tbackground-color: #f50000;\n\t}\n\tQPushButton:pressed {\n\t\tbackground-color: #FFFFFF;\n\t}\n\tQListWidget {\n\t\tbackground-color: #3c3f41;\n\t\tcolor: #d3d3d3;\n\t\tborder: 1px solid #444444;\n\t}\n\tQGroupBox {\n\t\tborder: 1px solid #444444;\n\t\tbackground-color: #2b2b2b;\n\t\tcolor: #d3d3d3;\n\t\tmargin: 5px;\n\t\tpadding: 10px;\n\t}\n\tQFormLayout {\n\t\tbackground-color: #2b2b2b;\n\t\tcolor: #d3d3d3;\n\t}\n    QPlainTextEdit{\n        background-color: #1e1e1e;\n    }\n    \n\t'
    self.setStyleSheet(light_stylesheet)

class PythonHighlighter(QSyntaxHighlighter):
    from PyQt6.QtGui import QTextCursor, QKeyEvent

    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []
        self.formats = self._init_formats()
        self._init_highlighting_rules()
        self.multi_line_string_format = self.formats['string']
        self.triple_single_quote = QRegularExpression('\'\'\'')
        self.triple_double_quote = QRegularExpression('\"\"\"')

    def keyPressEvent(self, event: QKeyEvent):
        import re
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            cursor = self.textCursor()
            cursor.select(QTextCursor.SelectionType.LineUnderCursor)
            line_text = cursor.selectedText()
            indentation = re.match('\\s*', line_text).group()
            increase_indent = re.search(':\\s*$', line_text)
            super().keyPressEvent(event)
            self.insertPlainText(indentation + ('    ' if increase_indent else ''))
        else:  # inserted
            super().keyPressEvent(event)

    def _init_formats(self):
        def fmt(color, italic=False, bold=False):
            _fmt = QTextCharFormat()
            _fmt.setForeground(QColor(color))
            if italic:
                _fmt.setFontItalic(True)
            if bold:
                _fmt.setFontWeight(QFont.Weight.Bold)
            return _fmt
        return {'keyword': fmt('#569CD6', bold=True), 'string': fmt('#D69D85'), 'comment': fmt('#6A9955', italic=True), 'number': fmt('#B5CEA8'), 'class': fmt('#4EC9B0', bold=True), 'function': fmt('#DCDCAA'), 'decorator': fmt('#FFFF00'), 'builtin': fmt('#4EC945', bold=True), 'bracket': fmt('#C586C0', bold=False), 'package': fmt('#C586C0', bold=False)}

    def _init_highlighting_rules(self):
        keywords = ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise','return', 'try', 'while', 'with', 'yield']
        builtins = ['abs', 'all', 'any', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range',
        bracket_chars = ['\\(', '\\)', '\\{', '\\}', '\\[', '\\]']
        self.keywords = set(keywords)
        for word in keywords:
            pattern = QRegularExpression(f'\\b{word}\\b')
            self.highlighting_rules.append((pattern, self.formats['keyword']))
        for word in builtins:
            pattern = QRegularExpression(f'\\b{word}\\b')
            self.highlighting_rules.append((pattern, self.formats['builtin']))
        for ch in bracket_chars:
            pattern = QRegularExpression(ch)
            self.highlighting_rules.append((pattern, self.formats['bracket']))
        self.highlighting_rules.append((QRegularExpression('#.*'), self.formats['comment']))
        self.highlighting_rules.append((QRegularExpression('\"[^\"\\\\]*(\\\\.[^\"\\\\]*)*\"'), self.formats['string']))
        self.highlighting_rules.append((QRegularExpression('\'[^\'\\\\]*(\\\\.[^\'\\\\]*)*\''), self.formats['string']))
        self.highlighting_rules.append((QRegularExpression('\\b\\d+(_\\d+)*(\\.\\d+(_\\d+)*)?([eE][-+]?\\d+)?\\b'), self.formats['number']))
        self.highlighting_rules.append((QRegularExpression('\\bclass\\s+(\\w+)'), self.formats['class']))
        self.highlighting_rules.append((QRegularExpression('\\bdef\\s+(\\w+)'), self.formats['function']))
        self.highlighting_rules.append((QRegularExpression('@\\w+'), self.formats['decorator']))
        self.package_import_pattern = QRegularExpression('\\b(?:import|from)\\s+([a-zA-Z_][\\w.]*)')

    def highlightBlock(self, text):
        for pattern, fmt in self.highlighting_rules:
            it = pattern.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)
        self.setCurrentBlockState(0)
        self._highlight_multiline(text, self.triple_single_quote, self.multi_line_string_format)
        self._highlight_multiline(text, self.triple_double_quote, self.multi_line_string_format)
        match_iter = self.package_import_pattern.globalMatch(text)
        while match_iter.hasNext():
            match = match_iter.next()
            captured_start = match.capturedStart(1)
            captured_length = match.capturedLength(1)
            self.setFormat(captured_start, captured_length, self.formats['package'])
        identifier_pattern = QRegularExpression('\\b[a-zA-Z_][a-zA-Z0-9_]*\\b')
        word_counts = {}
        matches = []
        it = identifier_pattern.globalMatch(text)
        while it.hasNext():
            match = it.next()
            word = match.captured()
            if word in self.keywords:
                continue
            word_counts[word] = word_counts.get(word, 0) + 1
            matches.append(match)
        for match in matches:
            word = match.captured()
            if word_counts[word] > 1:
                self.setFormat(match.capturedStart(), match.capturedLength(), self.formats['reference'])

    def _highlight_multiline(self, text, delimiter, fmt):
        start = 0
        add_length = 0
        if self.previousBlockState()!= 1:
            match = delimiter.match(text)
            if match.hasMatch():
                start = match.capturedStart()
                add_length = match.capturedLength()
                match = delimiter.match(text, start + add_length)
                if match.hasMatch():
                    end = match.capturedEnd()
                    self.setFormat(start, end - start, fmt)
                else:  # inserted
                    self.setCurrentBlockState(1)
                    self.setFormat(start, len(text) - start, fmt)
        else:  # inserted
            match = delimiter.match(text)
            if match.hasMatch():
                end = match.capturedEnd()
                self.setFormat(0, end, fmt)
                self.setCurrentBlockState(0)
            else:  # inserted
                self.setFormat(0, len(text), fmt)

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.code_editor = editor

    def sizeHint(self):
        return QSize(self.code_editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.code_editor.lineNumberAreaPaintEvent(event)

class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Consolas', 11))
        self.highlighter = PythonHighlighter(self.document())
        self.line_number_area = LineNumberArea(self)
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)
        self.update_line_number_area_width(0)
        self.highlight_current_line()
        keywords = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise','return', 'True', 'try', 'while', 'with', 'yield']
        self.completer = QCompleter(keywords)
        self.completer.setWidget(self)
        self.completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.activated.connect(self.insert_completion)

    def insert_completion(self, completion):
        tc = self.textCursor()
        extra = len(completion) - len(self.completer.completionPrefix())
        tc.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveMode.KeepAnchor, len(self.completer.completionPrefix()))
        tc.insertText(completion)
        self.setTextCursor(tc)

    def text_under_cursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.SelectionType.WordUnderCursor)
        return tc.selectedText()

    def keyPressEvent(self, event):
        if event.key() in [Qt.Key.Key_Enter, Qt.Key.Key_Return]:
            self.handle_auto_indent()
            return
        if event.key() == Qt.Key.Key_Tab:
            self.indent_selection()
            return
        if event.key() == Qt.Key.Key_Backtab:
            self.dedent_selection()
            return
        if self.completer.popup().isVisible() and event.key() in [Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Escape, Qt.Key.Key_Tab, Qt.Key.Key_Backtab]:
            event.ignore()
            return
        super().keyPressEvent(event)
        ctrl_or_shift = event.modifiers() & (Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.ShiftModifier)
        if ctrl_or_shift and event.text() == '':
            return
        eow = '~!@#$%^&*()+{}|:\"<>?,./;\'[]\\-='
        completion_prefix = self.text_under_cursor()
        if len(completion_prefix) > 0 and completion_prefix[(-1)] not in eow:
            if completion_prefix!= self.completer.completionPrefix():
                self.completer.setCompletionPrefix(completion_prefix)
                self.completer.popup().setCurrentIndex(self.completer.completionModel().index(0, 0))
            cr = self.cursorRect()
            cr.setWidth(self.completer.popup().sizeHintForColumn(0) + self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
        else:  # inserted
            self.completer.popup().hide()

    def handle_auto_indent(self):
        cursor = self.textCursor()
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.MoveOperation.StartOfBlock)
        cursor.select(QTextCursor.SelectionType.LineUnderCursor)
        line_text = cursor.selectedText()
        indentation = re.match('\\s*', line_text).group()
        dedent_keywords = ('return', 'pass', 'break', 'continue', 'raise', 'yield')
        cursor.movePosition(QTextCursor.MoveOperation.EndOfBlock)
        cursor.insertText('\n' + indentation)
        stripped = line_text.strip()
        if stripped.endswith(':'):
            cursor.insertText('    ')
        else:  # inserted
            if any((stripped.startswith(k) for k in dedent_keywords)) and len(indentation) >= 4:
                cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveMode.KeepAnchor, 4)
                if cursor.selectedText() == '    ':
                    cursor.removeSelectedText()
        cursor.endEditBlock()
        self.setTextCursor(cursor)

    def indent_selection(self):
        cursor = self.textCursor()
        if not cursor.hasSelection():
            cursor.insertText('    ')
            return
        start = cursor.selectionStart()
        end = cursor.selectionEnd()
        cursor.setPosition(start)
        while cursor.position() <= end:
            cursor.movePosition(QTextCursor.MoveOperation.StartOfLine)
            cursor.insertText('    ')
            if not cursor.movePosition(QTextCursor.MoveOperation.Down):
                break
            if cursor.position() > end:
                break

    def dedent_selection(self):
        cursor = self.textCursor()
        start = cursor.selectionStart()
        end = cursor.selectionEnd()
        cursor.setPosition(start)
        while cursor.position() <= end:
            cursor.movePosition(QTextCursor.MoveOperation.StartOfLine)
            cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, 4)
            if cursor.selectedText() == '    ':
                cursor.removeSelectedText()
            if not cursor.movePosition(QTextCursor.MoveOperation.Down):
                break
            if cursor.position() > end:
                break

    def line_number_area_width(self):
        digits = len(str(max(1, self.blockCount())))
        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height()))

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:  # inserted
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def highlight_current_line(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            lineColor = QColor('#1f1f1f')
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.Property.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QColor('#1e1e1e'))
        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())
        font = QFont('Consolas', 10)
        painter.setFont(font)
        painter.setPen(QColor('#858585'))
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.drawText(0, top, self.line_number_area.width() - 5, self.fontMetrics().height(), Qt.AlignmentFlag.AlignRight, number)
            block = block.next()
            top = bottom
            bottom = top + int(self.blockBoundingRect(block).height())
            blockNumber += 1

class TutorialDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Keyboard Shortcuts Tutorial')
        self.setModal(True)
        self.resize(350, 300)
        layout = QVBoxLayout(self)
        shortcuts_text = '\n        <b>Keyboard Shortcuts:</b><br><br>\n        Ctrl+R: Run Code<br>\n        Ctrl+I: Install Package<br>\n        Ctrl+N: New Tab<br>\n        Ctrl+O: Open File<br>\n        Ctrl+S: Save File<br>\n        Ctrl+D: Close Tab<br>\n        Ctrl+H: Tutorial\n        '
        label = QLabel(shortcuts_text)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        label.setWordWrap(True)
        self.checkbox = QCheckBox('Don\'t show this tutorial again')
        self.btn_ok = QPushButton('OK')
        layout.addWidget(label)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.btn_ok)
        self.btn_ok.clicked.connect(self.accept)

    def exec_and_save(self):
        settings = QSettings('YourCompany', 'YourApp')
        show_tutorial = settings.value('show_tutorial', True, type=bool)
        if show_tutorial and self.exec() == QDialog.DialogCode.Accepted:
            settings.setValue('show_tutorial', not self.checkbox.isChecked())

def maybe_show_tutorial(parent=None):
    dlg = TutorialDialog(parent)
    dlg.exec_and_save()
from PyQt6.QtCore import QThread, QObject, pyqtSignal

class Worker(QObject):
    finished = pyqtSignal(str)

    def __init__(self, code):
        super().__init__()
        self.code = code

    def run(self):
        import subprocess
        try:
            process = subprocess.Popen([sys.executable, '-c', self.code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output, _ = process.communicate()
            self.finished.emit(output)
        except Exception as e:
            self.finished.emit(f'Error: {e}')
from PyQt6.QtCore import QProcess

class Code_Space(QMainWindow):
    def __init__(self):
        super().__init__()
        set_light_theme2(self)
        self.setWindowTitle('Advanced Python IDE')
        self.setGeometry(100, 100, 800, 500)
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        console_widget = QWidget()
        console_layout = QVBoxLayout(console_widget)
        from PyQt6.QtCore import QProcess
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.read_stdout)
        self.process.readyReadStandardError.connect(self.read_stderr)
        self.process.finished.connect(self.process_finished)
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setStyleSheet('background-color: transparent; color: #ffffff;')
        self.console_output.setFont(QFont('Consolas', 10))
        self.console_input = QLineEdit()
        self.console_input.setPlaceholderText('Enter command and press Enter...')
        self.console_input.returnPressed.connect(self.handle_input)
        self.console_input.setStyleSheet('background-color: #1e1e1e; color: #ffffff; border-radius: 5px;')
        console_layout.addWidget(self.console_output)
        console_layout.addWidget(self.console_input)
        self.tabs.addTab(console_widget, 'Console')
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.cursor_label = QLabel('Line: 1 | Col: 1')
        self.status.addPermanentWidget(self.cursor_label)
        self.open_files = {}
        self.init_toolbar()
        self.create_new_tab()
        self.setup_shortcuts()
        self.setup_overlay()

    def handle_input(self):
        command = self.console_input.text().strip()
        if not command:
            return
        self.console_output.append(f'> {command}')
        self.console_input.clear()
        if self.process.state() == QProcess.ProcessState.Running:
            self.process.write((command + '\n').encode())
        else:  # inserted
            self.process.start('cmd.exe', ['/C', command])

    def setup_overlay(self):
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet('background-color: rgba(0, 0, 0, 180);')
        self.overlay.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.overlay.setVisible(True)
        overlay_layout = QVBoxLayout(self.overlay)
        overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        overlay_label = QLabel('🚧 Experimental Code Sand Box Ahead. Still in Development 🚧', self.overlay)
        overlay_label.setStyleSheet('\n            QLabel {\n                color: #ffffff;\n                font-size: 24px;\n                font-weight: bold;\n                background: transparent;\n            }\n        ')
        overlay_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        overlay_layout.addWidget(overlay_label)
        overlay_button = QPushButton('Click to Proceed')
        overlay_button.clicked.connect(lambda: self.last_func())
        overlay_button.setStyleSheet(' QPushButton { padding: 12px; background-color: #1b1b1b; color: white; border-radius: 5px;} QPushButton:hover { background-color: #ffffff; color: #000000;}')
        overlay_layout.addWidget(overlay_button)

    def resizeEvent(self, event):
        """Ensure overlay resizes with the main window."""  # inserted
        self.overlay.setGeometry(self.rect())
        super().resizeEvent(event)

    def last_func(self):
        self.overlay.setVisible(False)
        maybe_show_tutorial(self)

    def eventFilter(self, source, event):
        if source == self.console_input and event.type() == event.Type.KeyPress and (event.key() == Qt.Key.Key_Return) and (not event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
            command = self.console_input.toPlainText().strip()
            self.console_input.clear()
            self.execute_command(command)
            return True
        return super().eventFilter(source, event)

    def execute_command(self, command):
        if not command:
            return
        self.console_output.append(f'> {command}')
        try:
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            if result.stdout:
                self.console_output.append(result.stdout)
            if result.stderr:
                self.console_output.append(f'<span style=\'color:red\'>{result.stderr}</span>')
        except Exception as e:
            self.console_output.append(f'<span style=\'color:red\'>Error: {str(e)}</span>')

    def find_icon(self, icon_name):
        import os
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'ICON', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

    def init_toolbar(self):
        from PyQt6.QtGui import QIcon
        icon_path1 = self.find_icon('ICON\\menu\\run1.png')
        icon_path2 = self.find_icon('ICON\\menu\\install.png')
        icon_path3 = self.find_icon('ICON\\menu\\new1.png')
        icon_path4 = self.find_icon('ICON\\menu\\open1.png')
        icon_path5 = self.find_icon('ICON\\menu\\save1.png')
        icon_path6 = self.find_icon('ICON\\menu\\cancel1.png')
        run_icon = QIcon(icon_path1)
        run_action = QAction(run_icon, '', self)
        run_action.setToolTip('Run')
        run_action.triggered.connect(self.run_code)
        install_icon = QIcon(icon_path2)
        install_action = QAction(install_icon, '', self)
        install_action.setToolTip('Install Package')
        install_action.setShortcut(QKeySequence('Ctrl+I'))
        install_action.triggered.connect(self.install_package)
        new_icon = QIcon(icon_path3)
        new_action = QAction(new_icon, '', self)
        new_action.setToolTip('New Tab')
        new_action.setShortcut(QKeySequence('Ctrl+N'))
        new_action.triggered.connect(self.create_new_tab)
        open_icon = QIcon(icon_path4)
        open_action = QAction(open_icon, '', self)
        open_action.setToolTip('Open File')
        open_action.setShortcut(QKeySequence('Ctrl+O'))
        open_action.triggered.connect(self.open_file)
        save_icon = QIcon(icon_path5)
        save_action = QAction(save_icon, '', self)
        save_action.setToolTip('Save')
        save_action.setShortcut(QKeySequence('Ctrl+S'))
        save_action.triggered.connect(self.save_file)
        close_icon = QIcon(icon_path6)
        close_action = QAction(close_icon, '', self)
        close_action.setToolTip('Close Tab')
        close_action.setShortcut(QKeySequence('Ctrl+D'))
        close_action.triggered.connect(self.close_current_tab)

    def setup_shortcuts(self):
        from PyQt6.QtGui import QKeySequence, QShortcut
        QShortcut(QKeySequence('Ctrl+R'), self).activated.connect(self.run_code)
        QShortcut(QKeySequence('Ctrl+I'), self).activated.connect(self.install_package)
        QShortcut(QKeySequence('Ctrl+N'), self).activated.connect(self.create_new_tab)
        QShortcut(QKeySequence('Ctrl+O'), self).activated.connect(self.open_file)
        QShortcut(QKeySequence('Ctrl+S'), self).activated.connect(self.save_file)
        QShortcut(QKeySequence('Ctrl+D'), self).activated.connect(self.close_current_tab)
        QShortcut(QKeySequence('Ctrl+H'), self).activated.connect(lambda: maybe_show_tutorial(self))

    def current_editor(self):
        widget = self.tabs.currentWidget()
        if isinstance(widget, CodeEditor):
            return widget

    def create_new_tab(self):
        editor = CodeEditor()
        editor.cursorPositionChanged.connect(self.update_cursor_position)
        index = self.tabs.addTab(editor, 'Untitled')
        self.tabs.setCurrentIndex(index)
        self.open_files[index] = None

    def update_cursor_position(self):
        editor = self.current_editor()
        if editor:
            cursor = editor.textCursor()
            line = cursor.blockNumber() + 1
            col = cursor.positionInBlock() + 1
            self.cursor_label.setText(f'Line: {line} | Col: {col}')

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Python Files (*.py);;All Files (*)')
        if path:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    text = f.read()
                editor = CodeEditor()
                editor.setPlainText(text)
                editor.cursorPositionChanged.connect(self.update_cursor_position)
                index = self.tabs.addTab(editor, path.split('/')[(-1)])
                self.tabs.setCurrentIndex(index)
                self.open_files[index] = path
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Could not open file: {e}')

    def save_file(self):
        index = self.tabs.currentIndex()
        editor = self.current_editor()
        if editor:
            path = self.open_files.get(index)
            if not path:
                path, _ = QFileDialog.getSaveFileName(self, 'Save File As', '', 'Python Files (*.py);;All Files (*)')
                if not path:
                    return
                self.open_files[index] = path
                self.tabs.setTabText(index, path.split('/')[(-1)])
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(editor.toPlainText())
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Could not save file: {e}')

    def close_current_tab(self):
        index = self.tabs.currentIndex()
        if index > 0:
            self.tabs.removeTab(index)
            self.open_files.pop(index, None)

    def run_code(self):
        code = self.current_editor().toPlainText()
        self.thread = QThread()
        self.worker = Worker(code)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_run_finished)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.on_thread_finished)
        self.thread.start()

    def on_run_finished(self, output):
        if output.strip():
            self.console_output.setPlainText(output)
            self.tabs.setCurrentWidget(self.tabs.widget(0))
        else:  # inserted
            QMessageBox.information(self, 'Info', 'The script ran (possibly a GUI app with no output).')

    def on_thread_finished(self):
        self.thread = None
        self.worker = None

    def on_run_error(self, error_str):
        QMessageBox.critical(self, 'Execution Error', error_str)

    def install_package(self):
        package, ok = QInputDialog.getText(self, 'Install Package', 'Package name:')
        if ok and package:
            self.console_output.append(f'Installing package: {package}...')
            process = subprocess.Popen([sys.executable, '-m', 'pip', 'install', package], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output, _ = process.communicate()
            self.console_output.append(output)
            self.tabs.setCurrentWidget(self.console_output)

    def read_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.console_output.moveCursor(QTextCursor.MoveOperation.End)
        self.console_output.insertPlainText(output)
        self.console_output.moveCursor(QTextCursor.MoveOperation.End)

    def read_stderr(self):
        error = self.process.readAllStandardError().data().decode()
        self.console_output.moveCursor(QTextCursor.MoveOperation.End)
        self.console_output.insertHtml(f'<span style=\'color:red\'>{error}</span>')
        self.console_output.moveCursor(QTextCursor.MoveOperation.End)

    def process_finished(self, exit_code, exit_status):
        self.console_output.append(f'\n[Process finished with code {exit_code}]\n')

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

class Communicator(QObject):
    new_speech = pyqtSignal(str)
    new_stdout = pyqtSignal(str)
    new_stderr = pyqtSignal(str)

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
MAX_HISTORY = 20
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
    def __init__(self, title, url, zoom_key, url_key, parent_assets):
        super().__init__()
        self.parent_assets = parent_assets
        self.title = title
        self.url = url
        self.zoom_key = zoom_key
        self.url_key = url_key
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        header_layout = QHBoxLayout()
        self.label = QLabel(title)
        self.label.setStyleSheet('color: white; font-size: 14pt; font-weight: bold;')
        header_layout.addWidget(self.label)
        self.detach_button = QPushButton('Detach')
        self.detach_button.setFixedWidth(70)
        self.detach_button.clicked.connect(self.toggle_detach)
        header_layout.addWidget(self.detach_button)
        self.detach_button.setStyleSheet('\n            QPushButton {\n                background-color: #111111;\n                color: #ffffff;\n                border: 1px solid #444444;\n                border-radius: 6px;\n                padding: 6px 12px;\n                font-size: 12px;\n                font-weight: bold;\n                font-family: Consolas, monospace;\n            }\n            QPushButton:hover {\n                background-color: #222222;\n                border: 1px solid #666666;\n                color: cyan;\n            }\n            QPushButton:pressed {\n                background-color: #000000;\n                border: 1px solid #888888;\n            }\n        ')
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
        blocklist = ['doubleclick.net', 'google-analytics.com', 'googletagmanager.com', 'googlesyndication.com', 'googleadservices.com', 'adsafeprotected.com', 'adnxs.com', 'ads.yahoo.com', 'ads.twitter.com', 'ads.pubmatic.com', 'adform.net', 'adzerk.net', 'criteo.com', 'rubiconproject.com', 'scorecardresearch.com', 'quantserve.com', 'facebook.net', 'facebook.com/tr', 'connect.facebook.net', 'fbcdn.net', 'taboola.com', 'outbrain.com', 'moatads.com', 'zopim.com', 'hotjar.com', 'newrelic.com', 'optimizely.com', 'segment.com', 'tracking', 'track', 'ad.', '/ads?', '/ads/', 'pixel.', 'tracker.', 'log.doubleclick.net', 'pagead2.googlesyndication.com', 'bam.nr-data.net', 'cdn.heapanalytics.com']
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
        progress.setStyleSheet('\n            QProgressBar {\n                background-color: #1c1c1c;\n                border-radius: 4px;\n            }\n            QProgressBar::chunk {\n                background-color: #ffffff;\n                border-radius: 4px;\n            }\n        ')
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

class CircularProgressBar(QWidget):
    def __init__(self, diameter=60, thickness=8, value=0):
        super().__init__()
        self.diameter = diameter
        self.thickness = thickness
        self._value = value
        self.setFixedSize(diameter, diameter)

    def setValue(self, val):
        self._value = max(0, min(100, val))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = self.rect()
        center = rect.center()
        radius = self.diameter / 2 - self.thickness / 2
        painter.setPen(QPen(QColor('#2c2c2c'), self.thickness))
        painter.drawEllipse(center, radius, radius)
        angle = int(360 * self._value / 100)
        painter.setPen(QPen(QColor('#ffffff'), self.thickness))
        painter.drawArc(rect.adjusted(self.thickness / 2, self.thickness / 2, -self.thickness / 2, -self.thickness / 2), 1440, -angle * 16)
        painter.setPen(QColor('#dddddd'))
        painter.setFont(QFont('Segoe UI', 8, QFont.Weight.Normal))
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, f'{self._value}')

class StorageWorker(QObject):
    updated = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            try:
                usage = psutil.disk_usage('/')
                self.updated.emit(int(usage.percent))
            except Exception:
                self.updated.emit(0)
            QThread.msleep(1000)

    def stop(self):
        self.running = False

class QuickAppButton(QPushButton):
    def __init__(self, exe_path, icon=None, parent=None, delete_callback=None, icon_update_callback=None):
        super().__init__(parent)
        self.exe_path = exe_path
        self.setToolTip(os.path.basename(exe_path))
        self.setFixedSize(48, 48)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(parent.icon_button_stylesheet())
        self.delete_callback = delete_callback
        self.icon_update_callback = icon_update_callback
        self.setIcon(QIcon(icon or exe_path))
        self.setIconSize(QSize(32, 32))
        self.clicked.connect(self.launch_app)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        set_icon_action = menu.addAction('Set Icon')
        delete_action = menu.addAction('Delete')
        action = menu.exec(event.globalPos())
        if action == set_icon_action:
            self.show_icon_selector()
        else:  # inserted
            if action == delete_action and self.delete_callback:
                self.delete_callback(self)

    def show_icon_selector(self):
        icon_dir = find_icon('default_icons')
        icon_files = [f for f in os.listdir(icon_dir) if f.endswith(('.png', '.ico'))]
        menu = QMenu('Choose Icon', self)
        for file in icon_files:
            icon_path = os.path.join(icon_dir, file)
            icon = QIcon(icon_path)
            action = QAction(icon, file, self)
            action.triggered.connect(lambda _, p=icon_path: self.set_custom_icon(p))
            menu.addAction(action)
        menu.exec(QCursor.pos())

    def set_custom_icon(self, icon_path):
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(32, 32))
        if self.icon_update_callback:
            self.icon_update_callback(self.exe_path, icon_path)

    def launch_app(self):
        os.startfile(self.exe_path)

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
            painter.drawEllipse(x - circle['radius'] / 2, y - circle['radius'] / 2, circle['radius'], circle['radius'])

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

class Assets(QWidget):
    def __init__(self, max_apps=30):
        super().__init__()
        self.setWindowTitle('Nectar-X-Studio Hub')
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)
        self.setGeometry(400, 100, 700, 550)
        self.search_history = self.load_history()
        self.setup_ui()
        self.setup_autocomplete()
        self.ai = WindowsAutomationAI()
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
        self.search_input.setPlaceholderText('Win-X Search')
        self.search_input.setTextMargins(30, 0, 0, 0)
        self.icon_button = QToolButton(self.search_input)
        self.icon_button.setIcon(QIcon('background/NectarX.png'))
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
        btn_chrome = create_quick_button(find_icon('background/chrome.png'), lambda: self.launch_app('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
        btn_explorer = create_quick_button(find_icon('background/explore.png'), lambda: self.launch_app('explorer.exe'))
        btn_settings = create_quick_button(find_icon('background/settings.png'), lambda: self.launch_app('start ms-settings:'))
        storage_frame = QFrame()
        storage_frame.setStyleSheet('\n                background-color: #000000; \n                border-radius: 6px;\n                ')
        storage_frame.setFixedSize(48, 48)
        storage_layout = QHBoxLayout()
        storage_layout.setContentsMargins(0, 0, 0, 0)
        storage_frame.setLayout(storage_layout)
        self.storage_circular = CircularProgressBar(diameter=38, thickness=2)
        self.storage_circular.setToolTip('Storage')
        storage_layout.addWidget(self.storage_circular)
        self.time_label = QLabel()
        self.time_label.setStyleSheet('\n            color: white;\n            font-size: 13px;\n            font-family: Consolas, monospace;\n            background-color: #000000;\n            padding: 4px 8px;\n            border-radius: 6px;\n        ')
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setFixedHeight(48)
        self.time_label.setFixedWidth(140)
        btn_chrome.setToolTip('Chrome')
        btn_explorer.setToolTip('Explorer')
        btn_settings.setToolTip('Settings')
        quick_access_layout.addWidget(btn_chrome)
        quick_access_layout.addWidget(btn_explorer)
        quick_access_layout.addWidget(btn_settings)
        quick_access_layout.addWidget(self.time_label)
        quick_access_layout.addWidget(storage_frame)
        self.quick_access_layout = quick_access_layout
        self.load_custom_apps()
        btn_add = QPushButton('+')
        btn_add.setFixedSize(48, 48)
        btn_add.setContentsMargins(0, 0, 0, 0)
        btn_add.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_add.setStyleSheet('\n            QPushButton {\n                background-color: #000000;\n                color: white;\n                font-size: 24px;\n                border: 2px solid #000000;\n                border-radius: 8px;\n            }\n            QPushButton:hover {\n                background-color: #3a3a3a;\n            }\n            QToolTip {\n                background-color: #000000;\n                color: white;\n                border: 1px solid #444;\n                padding: 6px;\n                font-size: 12px;\n                font-family: Consolas, monospace;\n                border-radius: 4px;\n            }\n        ')
        btn_add.setToolTip('Add App')
        btn_add.clicked.connect(self.choose_app_to_add)
        quick_access_layout.addWidget(btn_add)
        main_layout.addLayout(quick_access_layout)
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)
        self.update_time()
        self.storage_thread = QThread()
        self.storage_worker = StorageWorker()
        self.storage_worker.moveToThread(self.storage_thread)
        self.storage_worker.updated.connect(self.update_storage)
        self.storage_thread.started.connect(self.storage_worker.run)
        self.storage_thread.start()
        from PyQt6.QtWebEngineWidgets import QWebEngineView
        from PyQt6.QtWebEngineCore import QWebEngineProfile
        interceptor = BlockTrackerInterceptor()
        sys.stderr = open(os.devnull, 'w')
        os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--disable-features=InterestCohortAPI,TrackingProtection --disable-3d-apis --disable-webgl --disable-notifications --disable-background-networking --disable-sync --disable-logging --disable-domain-reliability --disable-default-apps --disable-webrtc--enable-features=\"DnsOverHttps\" --dns-over-https-mode=secure --dns-over-https-templates=https://cloudflare-dns.com/dns-query'
        os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '0.0.0.0:9222'
        os.environ['QTWEBENGINE_DICTIONARIES_PATH'] = os.path.join(os.getcwd(), 'dummy_dictionaries')
        os.makedirs('dummy_dictionaries', exist_ok=True)
        QWebEngineProfile.defaultProfile().setHttpUserAgent('Chrome/125.0.6422.112')
        self.settings = QSettings('NectarX', 'NewsPrefence')
        persistent_profile_path = os.path.join(os.getcwd(), 'web_profile')
        os.makedirs(persistent_profile_path, exist_ok=True)
        self.web_profile = QWebEngineProfile('Default', self)
        self.web_profile.setPersistentStoragePath(persistent_profile_path)
        self.web_profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)
        self.web_profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.DiskHttpCache)
        self.web_profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.MemoryHttpCache)
        self.web_profile.setHttpUserAgent(self.web_profile.httpUserAgent() + ' Referrer-Policy: no-referrer')
        self.web_profile.setUrlRequestInterceptor(interceptor)
        self.web_profile.setHttpCacheMaximumSize(0)
        self.web_profile.setCachePath(persistent_profile_path)
        self.web_profile.setHttpUserAgent('Mozilla/5.0AppleWebKit/537.36Chrome/125.0.6422.112')
        last_url = self.settings.value('news/last_url', 'https://www.bbc.com/')
        zoom_level = float(self.settings.value('news/zoom', 1.0))
        news_container = QWidget()
        news_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        news_layout = QVBoxLayout(news_container)
        news_layout.setSpacing(20)

        def create_quick_button(icon_path, callback):
            btn = QPushButton()
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(32, 32))
            btn.setFixedSize(48, 48)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(self.icon_button_stylesheet())
            btn.clicked.connect(callback)
            return btn
        btn_hide = create_quick_button(find_icon('background/main.png'), self.run_hide)
        btn_mini = create_quick_button(find_icon('background/mini.png'), self.mini)
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
        btn_hide.setToolTip('Home')
        search_layout.addWidget(btn_hide)
        btn_mini.setToolTip('Staged')
        search_layout.addWidget(btn_mini)
        news_layout.addLayout(search_layout)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(StatusBar())
        news_layout.addLayout(layout)

        def create_news_row(left_title, left_url, left_keys, right_title, right_url, right_keys):
            row_layout = QHBoxLayout()
            row_layout.setSpacing(15)
            left_col = QVBoxLayout()
            self.add_news_section(left_col, left_title, left_url, *left_keys)
            row_layout.addLayout(left_col)
            right_col = QVBoxLayout()
            self.add_news_section(right_col, right_title, right_url, *right_keys)
            row_layout.addLayout(right_col)
            news_layout.addLayout(row_layout)
        create_news_row('BBC News', 'https://www.bbc.com/', ('bbc_zoom', 'bbc_url'), 'Al Jazeera', 'https://www.aljazeera.com/', ('aljazeera_zoom', 'aljazeera_url'))
        self.youtube_detachable = DetachableWebView('YouTube Hub', 'https://www.youtube.com/results?search_query=news', 'yt_zoom', 'yt_url', self)
        news_layout.addWidget(self.youtube_detachable)
        self.ground_detachable = DetachableWebView('Ground News', 'https://ground.news/', 'ground_zoom', 'ground_url', self)
        news_layout.addWidget(self.ground_detachable)
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
        icon_path32 = find_icon('background/NectarX.png')
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path32), self)
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

    def update_time(self):
        from datetime import datetime
        current_time = datetime.now().strftime('%A %I:%M %p<br>\n%d %B %Y')
        self.time_label.setText(current_time)

    def check_server(self):
        service_port = 5005
        is_active = self.ping('127.0.0.1', service_port)
        self.dot.set_active(is_active)

    def ping(self, host, port, timeout=0.5):
        if port == 0:
            return False
        pkt = IP(dst=host) / TCP(dport=port, flags='S')
        resp = sr1(pkt, timeout=timeout, verbose=0)
        if resp is None:
            return False
        if resp.haslayer(TCP):
            tcp_layer = resp.getlayer(TCP)
            if tcp_layer.flags == 18:
                rst_pkt = IP(dst=host) / TCP(dport=port, flags='R', seq=tcp_layer.ack)
                send(rst_pkt, verbose=0)
                return True
            if tcp_layer.flags == 20:
                return False
        return False

    def run_hide(self):
        self.hide()
        if hasattr(self, 'tray_icon'):
            self.tray_icon.showMessage('Running in Background', 'The application is minimized to the system tray.', QSystemTrayIcon.MessageIcon.Information, 3000)
            Studio_Nectar.show()

    def mini(self):
        background_widget.show()
        self.hide()

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
        user_command = self.search_bar.text()
        if user_command.lower() == 'clear':
            self.search_bar.clear()
        else:  # inserted
            if user_command:
                self.overlay.setVisible(True)
                self.worker = CommandWorker(self.ai, user_command)
                self.worker.result_signal.connect(self.on_result_received)
                self.worker.start()
                self.search_bar.clear()

    def on_result_received(self, result):
        if result == 'No output from command.':
            tooltip_text = 'Retry'
        else:  # inserted
            tooltip_text = f'{result}'
            self.overlay.setVisible(False)
        icon_path101 = find_icon('NectarX.ico')
        tooltip_text = f'<img src=\"{icon_path101}\" width=\"32\" height=\"32\" style=\"vertical-align:middle; margin-right:30px;\"> <span style=\"font-size:20px; margin-left:30px; font-weight:bold; display:inline-block; text-align:center; width:100%; \">Nectar-X</span> <br> {result}'
        tooltip = PersistentTooltip(tooltip_text, self)
        global_pos = self.search_bar.mapToGlobal(QPoint(0, -tooltip.height()))
        tooltip.show_for_duration(global_pos, duration_ms=300000)

    def update_storage(self, percent_used):
        self.storage_circular.setValue(percent_used)

    def add_quick_app_button(self, exe_path, custom_icon=None):
        self.quick_buttons = []
        btn = QuickAppButton(exe_path, icon=custom_icon, parent=self, delete_callback=self.delete_quick_app_button, icon_update_callback=self.update_app_icon)
        self.quick_access_layout.addWidget(btn)
        self.quick_buttons.append(btn)

    def delete_quick_app_button(self, btn):
        settings = QSettings('NectarX', 'ButtonPrefence')
        exe_path = btn.exe_path
        self.quick_access_layout.removeWidget(btn)
        btn.deleteLater()
        if btn in self.quick_buttons:
            self.quick_buttons.remove(btn)
        apps = settings.value('custom_apps', [])
        icons = settings.value('custom_icons', {}) or {}
        if exe_path in apps:
            apps.remove(exe_path)
        if exe_path in icons:
            del icons[exe_path]
        settings.setValue('custom_apps', apps)
        settings.setValue('custom_icons', icons)

    def save_custom_app(self, exe_path, icon_path=None):
        settings = QSettings('NectarX', 'ButtonPrefence')
        apps = settings.value('custom_apps', [])
        if exe_path not in apps:
            apps.append(exe_path)
            settings.setValue('custom_apps', apps)
        if icon_path:
            icons = settings.value('custom_icons', {}) or {}
            icons[exe_path] = icon_path
            settings.setValue('custom_icons', icons)

    def choose_app_to_add(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter('Applications (*.exe)')
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                exe_path = selected_files[0]
                self.add_quick_app_button(exe_path)
                self.save_custom_app(exe_path)

    def load_custom_apps(self):
        settings = QSettings('NectarX', 'ButtonPrefence')
        apps = settings.value('custom_apps', [])
        icons = settings.value('custom_icons', {}) or {}
        for exe in apps:
            if os.path.exists(exe):
                icon = icons.get(exe)
                self.add_quick_app_button(exe, custom_icon=icon)

    def update_app_icon(self, exe_path, icon_path):
        settings = QSettings('NectarX', 'ButtonPrefence')
        icons = settings.value('custom_icons', {}) or {}
        icons[exe_path] = icon_path
        settings.setValue('custom_icons', icons)

    def add_news_section(self, layout, title, default_url, zoom_key, url_key, min_height=300):
        label = QLabel(f'{title}')
        label.setStyleSheet('color: white; font-size: 14pt; font-weight: bold;')
        layout.addWidget(label)
        web_view = QWebEngineView(self.web_profile)
        from PyQt6.QtWebEngineCore import QWebEngineSettings
        self.web_profile.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        web_view.setStyleSheet('\n            QWebEngineView {\n                border-radius: 8px;\n                \n            }\n        ')
        web_view.setMinimumHeight(min_height)
        last_url = self.settings.value(f'news/{url_key}', default_url)
        zoom_level = float(self.settings.value(f'news/{zoom_key}', 1.0))
        web_view.setZoomFactor(zoom_level)
        web_view.load(QUrl(last_url))
        web_view.urlChanged.connect(lambda url: self.settings.setValue(f'news/{url_key}', url.toString()))
        web_view.page().zoomFactorChanged.connect(lambda z: self.settings.setValue(f'news/{zoom_key}', z))
        layout.addWidget(web_view)

    def icon_button_stylesheet(self):
        return '\n            QWidget{\n                background-color: #000000;\n            }\n            QPushButton {\n                border: none;\n                background-color: #000000;\n                border-radius: 8px;\n            }\n            QPushButton:hover {\n                background-color: #3a3a3a;\n                border-radius: 8px;\n            }\n            QPushButton:pressed {\n                background-color: #000000;\n            }\n            QToolTip {\n                background-color: #000000;\n                color: white;\n                border: 1px solid #444;\n                padding: 6px;\n                font-size: 12px;\n                font-family: Consolas, monospace;\n                border-radius: 4px;\n            }\n        '

    def launch_app(self, exe_path):
        self.threadpool.start(RunnableTask(self._launch_app_threaded, exe_path))

    def _launch_app_threaded(self, exe_path):
        try:
            if exe_path.startswith('start '):
                subprocess.Popen(exe_path, shell=True)
            else:  # inserted
                subprocess.Popen(exe_path)
        except Exception as e:
            write_to_log('Launch error:', e)

    def launch_callback(self, success, error=None):
        if not success:
            QMessageBox.critical(self, 'Launch Failed', f'Failed to launch app:\n{error}')

    def closeEvent(self, event):
        event.ignore()
        self.hide()

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
            write_to_log(f'Web suggestion error: {e}')
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
        self.show_search_options(query)

    def show_search_options(self, query):
        menu = QMenu(self)
        menu.setStyleSheet('\n            QMenu {\n                background-color: #121212;\n                color: white;\n                border: 1px solid #333;\n                padding: 6px;\n                font-size: 13px;\n            }\n            QMenu::item:selected {\n                background-color: #1a1a1a;\n                color: cyan;\n            }\n        ')
        win_action = QAction('Search with Windows', self)
        web_action = QAction('Search with Qwant (Web)', self)
        win_action.triggered.connect(lambda: self.perform_windows_search(query))
        web_action.triggered.connect(lambda: self.perform_qwant_search(query))
        menu.addAction(win_action)
        menu.addAction(web_action)
        menu.exec(self.search_input.mapToGlobal(self.search_input.rect().bottomLeft()))

    def perform_windows_search(self, query):
        import pyautogui
        import time
        pyautogui.press('win')
        time.sleep(0.3)
        pyautogui.write(query, interval=0.05)
        self.search_input.clear()

    def perform_qwant_search(self, query):
        import webview
        icon_path_new = find_icon('background/NectarX.png')
        window = webview.create_window(title='Nectar-X-Search', url=f'https://www.google.com/search?q={query}', width=600, height=400, resizable=True, confirm_close=True)
        webview.start(gui='edgechromium')
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
            write_to_log('Error saving history:', e)
from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QGuiApplication

class PersistentTooltip(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet('\n            QLabel {\n                background-color: #1e1e1e;\n                color: #ffffff;\n                border: 1px solid gray;\n                padding: 8px;\n                border-radius: 10px;\n                font-size: 14px;\n            }\n        ')
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

class BackgroundWidget(QWidget):
    """A small floating widget for background mode."""

    def __init__(self, ai, parent=None):
        super().__init__(parent)
        self.ai = ai
        self.parent = parent
        self.setWindowTitle('Background Mode')
        self.setFixedSize(300, 50)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet('background: transparent;')
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = screen_geometry.width() - self.width() - 180
        y = 213
        self.move(x, y)
        icon_path32 = find_icon('background/NectarX.png')
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path32), self)
        tray_menu = QMenu()
        restore_action = QAction('Restore', self)
        restore_action.triggered.connect(self.show)
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(QApplication.quit)
        tray_menu.addAction(restore_action)
        tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Ask Nectar-X')
        self.input_field.setStyleSheet('\n            QLineEdit {\n                background-color: #1e1e1e;\n                color: #ffffff;\n                border-radius: 6px;\n                padding: 6px 10px;\n                font-size: 14px;\n            }\n            QLineEdit:focus {\n                color: #ffffff;\n                background-color: #1b1b1b;\n            }\n        ')
        self.input_field.setFixedHeight(40)
        self.input_field.returnPressed.connect(self.execute_command)
        icon_path1 = self.find_icon('ICON\\menu\\play.png')
        self.speech_mode_button = QPushButton('')
        self.speech_mode_button.setFixedSize(36, 36)
        self.speech_mode_button.setStyleSheet('\n            QPushButton {\n                padding: 12px;\n                background-color: #ffffff;\n                color: black;\n                border-radius: 6px;\n            }\n            QPushButton:hover {\n\t\t\t\tbackground-color: #e6e6e6;\n\t\t\t}\n\t\t\tQPushButton:pressed {\n\t\t\t\tbackground-color: #d0d0d0;\n\t\t\t}\n        ')
        self.speech_mode_button.clicked.connect(self.run_speech_mode)
        self.loader = Loader()
        self.loader.setFixedSize(30, 36)
        self.loader.setVisible(False)
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(8)
        layout.addWidget(self.loader)
        layout.addWidget(self.input_field)
        layout.addWidget(self.speech_mode_button)
        self.setLayout(layout)
        self._dragging = False
        self._drag_start_pos = QPoint()
        self.input_field.installEventFilter(self)

    def run_speech_mode(self):
        import webbrowser
        webbrowser.open('http://127.0.0.1:9010')

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'ICON', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

    def execute_command(self):
        user_command = self.input_field.text().strip()
        if user_command.lower() == 'exit':
            self.hide()
            self.input_field.clear()
            asset.show()
        else:  # inserted
            if user_command:
                self.loader.setVisible(True)
                self.input_field.setEnabled(False)
                self.worker = CommandWorker(self.ai, user_command)
                self.worker.result_signal.connect(self.handle_command_result)
                self.worker.start()

    def handle_command_result(self, result):
        self.loader.setVisible(False)
        self.input_field.setEnabled(True)
        self.input_field.setText('')
        icon_path101 = find_icon('NectarX.ico')
        tooltip_text = f'<img src=\"{icon_path101}\" width=\"32\" height=\"32\" style=\"vertical-align:middle; margin-right:30px;\"> <span style=\"font-size:20px; margin-left:30px; font-weight:bold; display:inline-block; text-align:center; width:100%; \">Nectar-X</span> <br> {result}'
        tooltip = PersistentTooltip(tooltip_text, self)
        global_pos = self.input_field.mapToGlobal(QPoint(0, -tooltip.height()))
        tooltip.show_for_duration(global_pos, duration_ms=300000)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._dragging = True
            self._drag_start_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._dragging:
            self.move(event.globalPosition().toPoint() - self._drag_start_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._dragging = False
            event.accept()

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
            self._dragging = True
            self._drag_start_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            return True
        if event.type() == QEvent.Type.MouseMove and self._dragging:
            self.move(event.globalPosition().toPoint() - self._drag_start_pos)
            return True
        if event.type() == QEvent.Type.MouseButtonRelease and event.button() == Qt.MouseButton.LeftButton:
            self._dragging = False
            return True
        return super().eventFilter(source, event)
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QTimer, QElapsedTimer
from PyQt6.QtGui import QPainter, QColor, QBrush
import math

class Loader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Speech Simulation Loader')
        self.setFixedSize(100, 100)
        self.setStyleSheet('background-color: #ffffff; color: #E0E0E0; padding: 10px; border-radius: 5px;')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.max_radius = 10
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
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        center_x = self.width() / 2
        center_y = self.height() / 2
        for circle in self.circles:
            x = center_x + math.cos(math.radians(circle['angle'])) * 10
            y = center_y + math.sin(math.radians(circle['angle'])) * 10
            painter.setPen(Qt.PenStyle.NoPen)
            color = QColor(255, 0, 0)
            color.setAlpha(180)
            painter.setBrush(QBrush(color))
            painter.drawEllipse(int(x - circle['radius'] / 2), int(y - circle['radius'] / 2), int(circle['radius']), int(circle['radius']))

    def update_loader(self):
        elapsed_time = self.time.elapsed()
        for circle in self.circles:
            fluctuation = math.sin(elapsed_time / 1000 * 2 * math.pi)
            circle['radius'] = self.min_radius + fluctuation * (self.max_radius - self.min_radius)
            circle['radius'] = max(self.min_radius, min(circle['radius'], self.max_radius))
            circle['angle'] = (circle['angle'] + 3) % 360
        self.update()

class WindowsAutomationAI(QObject):
    response_ready = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.mode = 'chat'

    def show_notification(self, message, bg_color='#000000', text_color='#ffffff', duration=10000):
        QTimer.singleShot(0, lambda: FloatingNotification(self, message, duration, bg_color, text_color))

    def set_mode(self, mode):
        if mode in ['automation', 'chat', 'search']:
            self.mode = mode
            self.show_notification(f'[Mode] Switched to: {self.mode}')

    def get_interpretation(self, user_command):
        import logging
        try:
            if self.mode == 'automation':
                system_message = {'role': 'system', 'content': 'You are a Windows automation AI. Your job is to convert natural language user requests into valid Windows commands. Only output the command — no explanations.\nHere are some example conversions to guide you (do not repeat them, just use them as a pattern):\n\nUser: open taskmanager\nCommand: taskmgr\n\nUser: Increase volume by 30%\nCommand: nircmd.exe changesysvolume 8192\n\nUser: Switch to the next tab in Chrome\nCommand: nircmd.exe sendkeypress ctrl+tab\n\nFeel free to interpret the user\'s request as needed to find the most accurate Windows command.'}
                user_message = {'role': 'user', 'content': f'My request: {user_command}'}
            else:  # inserted
                system_message = {'role': 'system', 'content': 'You are a helpful AI assistant named Alpha. Respond naturally and helpfully.'}
                user_message = {'role': 'user', 'content': user_command}
            question = f"{system_message['content']} {user_message['content']}"
            reply = send_to_AlphaLLM(question)
            content = reply.strip()
            history.append({'role': 'assistant', 'content': content})
            save_history()
            if self.mode == 'automation':
                command = content.lower().strip().replace('`', '')
                if command.startswith('the') or not command or any((w in command for w in ['based', 'invalid', 'error'])):
                    return
                return command.split('\n')[0].strip()
            return content
        except Exception as e:
            write_to_log(f'LLM Error: {e}', file_path='logs/errors.log')
            return f'An error occurred: {e}'

    def cli_search(self, user_command):
        """\n        Safely performs a search command\n        """  # inserted
        if self.mode!= 'search':
            return 'Search mode is not active.'
        query = user_command.strip()
        if not query:
            return 'Please enter a valid command.'
        if query.lower() in ['exit', 'quit']:
            return 'Exiting search.'
        try:
            search_engine = 'google'
            if search_engine == 'google':
                search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            else:  # inserted
                if search_engine == 'bing':
                    search_url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"
                else:  # inserted
                    if search_engine == 'duckduckgo':
                        search_url = f"https://duckduckgo.com/?q={query.replace(' ', '+')}"
                    else:  # inserted
                        self.show_notification(f'Unsupported search engine: {search_engine}')
                        return
            webbrowser.open(search_url)
            self.show_notification(f'Opened {search_engine.title()} search for: {query}')
        except Exception as e:
            self.show_notification(f'Failed to open browser: {str(e)}')

    def execute_command(self, user_command):
        user_command = user_command.lower().strip()
        if user_command == 'chat':
            self.set_mode('chat')
            return 'Switched to Chat Mode.'
        if user_command == 'auto':
            self.set_mode('automation')
            return 'Switched to Automation Tool Mode.'
        if user_command == 'search':
            self.set_mode('search')
            return 'Switched to Search Mode.'
        if user_command == 'delete':
            clear_conversation_history()
            return 'Deleted conversation history.'
        result = self.get_interpretation(user_command)
        request = self.cli_search(user_command)
        if self.mode == 'automation':
            if result:
                try:
                    process = subprocess.run(result, shell=True, capture_output=True, text=True)
                    output = process.stdout.strip() or process.stderr.strip()
                    return output if output else 'Command executed with no output.'
                except Exception as e:
                    return f'Execution error: {e}'
            else:  # inserted
                return 'Could not interpret a valid Windows command.'
        else:  # inserted
            if self.mode == 'search':
                return request or 'Failed to send search request.'
            return result or 'Failed to get a response.'

class CommandWorker(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self, ai, user_command):
        super().__init__()
        self.ai = ai
        self.user_command = user_command

    def run(self):
        feedback = self.ai.execute_command(self.user_command)
        self.result_signal.emit(feedback)

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script\'s directory."""  # inserted
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'ICON', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None
import socket

class Broadcast(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('🧠 AlphaLLM Broadcast Engine')
        self.resize(640, 520)
        self.broadcast_enabled = False
        self.server_running = False
        self.server_socket = None
        self.broadcast_base_ip = '127.0.0.1'
        self.broadcast_port = 8012
        self.init_ui()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet(self.futuristic_style())
        self.animate_window()
        self.start_broadcast_server()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(14)
        self.target_display = QLabel(f'📡 API Target: {self.broadcast_base_ip}:{self.broadcast_port}')
        layout.addWidget(self.target_display)
        btns = QHBoxLayout()
        self.toggle_button = QPushButton('Start Engine')
        self.toggle_button.clicked.connect(self.toggle_engine)
        btns.addWidget(self.toggle_button)
        layout.addLayout(btns)
        layout.addWidget(QLabel('📦 Packet Log:'))
        self.packet_log = QTextEdit()
        self.packet_log.setReadOnly(True)
        layout.addWidget(self.packet_log)
        self.setLayout(layout)

    def toggle_engine(self):
        if not self.server_running:
            self.server_running = True
            self.start_broadcast_server()
            self.toggle_button.setText('Stop Engine')
            self.log_packet('[Engine] Broadcast server started.')
        else:  # inserted
            self.stop_broadcast_server()
            self.toggle_button.setText('Start Engine')
            self.log_packet('[Engine] Broadcast server stopped.')

    def start_broadcast_server(self):
        def server_thread():
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(('127.0.0.1', self.broadcast_port))
            self.server_socket.listen(5)
            self.log_packet(f'[Relay] Listening on 127.0.0.1:{self.broadcast_port}...')
            while self.server_running:
                try:
                    self.server_socket.settimeout(5)
                    client_socket, addr = self.server_socket.accept()
                    incoming_data = client_socket.recv(4096).decode('utf-8')
                    self.log_packet(f'[Incoming] From {addr[0]}:{addr[1]} -> {incoming_data}')
                    alpha_response = send_to_AlphaLLM(incoming_data)
                    self.log_packet(f'[Forwarded] Response from AlphaLLM: {alpha_response}')
                    client_socket.send(alpha_response.encode('utf-8'))
                    client_socket.close()
                except socket.timeout:
                    continue
                except Exception as e:
                    self.log_packet(f'[Error] Server exception: {e}')
                    break
            self.log_packet('[Server] Listener stopped.')
        threading.Thread(target=server_thread, daemon=True).start()

    def log_packet(self, message):
        self.packet_log.append(f'{message}')

    def stop_broadcast_server(self):
        self.server_running = False
        if self.server_socket:
            try:
                self.server_socket.close()
                self.server_socket = None
            except Exception as e:
                self.log_packet(f'[Error] Could not close socket: {e}')

    def animate_window(self):
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        geo = self.geometry()
        self.animation.setStartValue(QRect(geo.x(), geo.y() + 30, geo.width(), geo.height()))
        self.animation.setEndValue(geo)
        self.animation.start()

    def futuristic_style(self):
        return '\n        QWidget {\n            background: rgba(18, 18, 18, 200);\n            border-radius: 20px;\n            color: #ffffff;\n            font-family: \'Segoe UI\', sans-serif;\n        }\n        QLineEdit, QTextEdit {\n            background: rgba(40, 40, 40, 180);\n            color: #ffffff;\n            border: 1px solid #ffffff;\n            border-radius: 10px;\n            padding: 10px;\n        }\n        QPushButton {\n            background-color: #ffffff;\n            border: none;\n            border-radius: 10px;\n            padding: 10px;\n            color: #000000;\n            font-weight: bold;\n        }\n        QPushButton:hover {\n            background-color: #000000;\n            color: white;\n        }\n        QPushButton:pressed {\n            background-color: #1e1e1e;\n        }\n        QTextEdit {\n            font-family: Consolas, monospace;\n            font-size: 13px;\n        }\n        QLabel {\n            background-color: transparent;\n            color: #ffffff;\n        }\n        '
colors = {'bg': '#121212', 'panel': '#1e1e1e', 'text': '#e5e5e5', 'subtext': '#aaaaaa', 'accent': '#0db9d7', 'input': '#2b2b2b', 'border': '#303030', 'hover': '#1a1a1a'}

class NetworkSecurityUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('🛡 Network Security Console')
        self.setStyleSheet(f"background-color: {colors['bg']}; color: {colors['text']}; font-family: \'Segoe UI\';")
        self.setFont(QFont('Segoe UI', 10))
        self.auto_refresh_enabled = False
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.auto_refresh_update)
        self.init_ui()
        self.init_tray()
        self.init_timer()
        icon_path = self.find_icon('background/icon.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:  # inserted
            self.setWindowIcon(QIcon('background/icon.png'))

    def find_icon(self, icon_name):
        import os
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'ICON', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

    def init_ui(self):
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet('QScrollArea { border: none; }')
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)
        grid = QGridLayout()
        grid.setSpacing(15)
        grid.addWidget(self.create_button('🔎 Show Established Connections', self.show_established), 0, 0)
        grid.addWidget(self.create_button('🎧 Show Listening Ports', self.show_listening), 0, 1)
        layout.addLayout(grid)
        layout.addWidget(self.create_group('Remote Connection Control', self.remote_connection_controls()))
        layout.addWidget(self.create_group('Kill Listening Port', self.kill_port_controls()))
        self.textbox = QTextEdit()
        self.textbox.setReadOnly(True)
        self.textbox.setStyleSheet(f"\n            background-color: {colors['input']};\n            border: 1px solid {colors['border']};\n            padding: 10px;\n            font-family: Consolas;\n            color: {colors['text']};\n            border-radius: 10px;\n        ")
        layout.addWidget(self.textbox)
        self.logBox = QPlainTextEdit()
        self.logBox.setReadOnly(True)
        self.logBox.setFixedHeight(120)
        self.logBox.setStyleSheet(f"\n            background-color: {colors['panel']};\n            color: {colors['subtext']};\n            border: 1px solid {colors['border']};\n            border-radius: 10px;\n            padding: 8px;\n        ")
        layout.addWidget(QLabel('🔍 Activity Log:'))
        layout.addWidget(self.logBox)
        self.toggle_btn = self.create_button('🔄 Auto-Refresh: OFF', self.toggle_auto_refresh)
        layout.addWidget(self.toggle_btn)
        scroll_area.setWidget(container)
        outer_layout.addWidget(scroll_area)

    def create_button(self, label, callback, height=42):
        btn = QPushButton(label)
        btn.setMinimumHeight(height)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setToolTip(label)
        btn.setStyleSheet(f"\n            QPushButton {\n                background-color: {colors['panel']};\n                border: 1px solid {colors['border']};\n                border-radius: 8px;\n                color: {colors['text']};\n                padding: 6px 14px;\n                font-weight: 600;\n            }\n            QPushButton:hover {\n                background-color: {colors['hover']};\n            }\n            QPushButton:pressed {\n                background-color: {colors['accent']};\n                color: black;\n            }\n        ")
        btn.clicked.connect(callback)
        return btn

    def create_group(self, title, layout_widget):
        group = QGroupBox(title)
        group.setStyleSheet(f"\n            QGroupBox {\n                border: 1px solid {colors['border']};\n                border-radius: 10px;\n                margin-top: 16px;\n                font-weight: bold;\n                font-size: 14px;\n            }\n            QGroupBox:title {\n                subcontrol-origin: margin;\n                subcontrol-position: top left;\n                padding: 0 6px;\n                color: {colors['accent']};\n            }\n        ")
        group.setLayout(layout_widget)
        return group

    def toggle_auto_refresh(self):
        self.auto_refresh_enabled = not self.auto_refresh_enabled
        if self.auto_refresh_enabled:
            self.refresh_timer.start(5000)
            self.toggle_btn.setText('🔄 Auto-Refresh: ON')
            self.textbox.setText('🔄 Auto-Refresh Enabled.')
        else:  # inserted
            self.refresh_timer.stop()
            self.toggle_btn.setText('🔄 Auto-Refresh: OFF')
            self.textbox.setText('⏹ Auto-Refresh Disabled.')

    def auto_refresh_update(self):
        self.show_established()

    def remote_connection_controls(self):
        layout = QGridLayout()
        self.remote_ip = self.styled_input('Enter remote IP')
        self.remote_port = self.styled_input('Enter port')
        layout.addWidget(QLabel('Remote IP:'), 0, 0)
        layout.addWidget(self.remote_ip, 0, 1)
        layout.addWidget(QLabel('Remote Port:'), 1, 0)
        layout.addWidget(self.remote_port, 1, 1)
        layout.addWidget(self.create_button('🚫 Kill Connection', self.kill_connection), 0, 2, 2, 1)
        return layout

    def kill_port_controls(self):
        layout = QHBoxLayout()
        self.kill_port = self.styled_input('Port to kill')
        layout.addWidget(QLabel('Port:'))
        layout.addWidget(self.kill_port)
        layout.addWidget(self.create_button('⚡ Kill Port', self.kill_port_fn))
        return layout

    def styled_input(self, placeholder=''):
        box = QLineEdit()
        box.setPlaceholderText(placeholder)
        box.setStyleSheet(f"\n            QLineEdit {\n                background-color: {colors['input']};\n                border: 1px solid {colors['border']};\n                border-radius: 6px;\n                padding: 6px;\n                color: {colors['text']};\n            }\n            QLineEdit:focus {\n                border: 1px solid {colors['accent']};\n            }\n        ")
        return box

    def log_action(self, message):
        from PyQt6.QtCore import Qt, QTimer, QDateTime
        timestamp = QDateTime.currentDateTime().toString('HH:mm:ss')
        self.logBox.appendPlainText(f'[{timestamp}] {message}')

    def init_tray(self):
        self.tray_icon = QSystemTrayIcon(QIcon('background/tray.png'), self)
        self.tray_icon.setToolTip('Network Security Console')
        menu = QMenu()
        show_action = QAction('Show')
        quit_action = QAction('Exit')
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(QApplication.quit)
        menu.addAction(show_action)
        menu.addAction(quit_action)
        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage('Minimized', 'Network Security Console is still running in the tray.')

    def init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_refresh)
        self.timer.start(5000)

    def auto_refresh(self):
        if self.auto_refresh_enabled:
            self.show_established()

    def show_established(self):
        result = subprocess.run('netstat -an', capture_output=True, text=True, shell=True)
        lines = [line for line in result.stdout.splitlines() if 'ESTABLISHED' in line]
        output = '\n'.join(lines) if lines else 'No established connections found.'
        self.textbox.setText(output)
        self.log_action('Refreshed established connections.')

    def show_listening(self):
        result = subprocess.run('netstat -an', capture_output=True, text=True, shell=True)
        lines = [line for line in result.stdout.splitlines() if 'LISTENING' in line]
        output = '\n'.join(lines) if lines else 'No listening ports found.'
        self.textbox.setText(output)
        self.log_action('Refreshed listening ports.')

    def kill_connection(self):
        ip = self.remote_ip.text().strip()
        port = self.remote_port.text().strip()
        if ip and port:
            try:
                for conn in psutil.net_connections(kind='tcp'):
                    if conn.raddr and conn.raddr.ip == ip and (conn.raddr.port == int(port)) and (conn.status == 'ESTABLISHED'):
                        psutil.Process(conn.pid).terminate()
                        self.textbox.setText(f'✔ Terminated connection PID {conn.pid}')
                        self.log_action(f'Terminated connection to {ip}:{port}')
                        return
                else:  # inserted
                    self.textbox.setText(f'✖ No matching established connection found for {ip}:{port}')
                    self.log_action(f'No match to kill for {ip}:{port}')
            except Exception as e:
                self.textbox.setText(f'✖ Error: {e}')
                self.log_action(f'Error: {e}')
        else:  # inserted
            self.textbox.setText('⚠ Please enter both IP and Port.')
            self.log_action('Missing IP or Port for connection kill.')

    def kill_port_fn(self):
        port = self.kill_port.text().strip()
        if port:
            result = subprocess.run('netstat -aon', capture_output=True, text=True, shell=True)
            for line in result.stdout.splitlines():
                if f':{port} ' in line and 'LISTENING' in line:
                    pid = int(line.strip().split()[(-1)])
                    try:
                        psutil.Process(pid).terminate()
                        self.textbox.setText(f'✔ Killed process PID {pid} listening on port {port}')
                        self.log_action(f'Killed PID {pid} on port {port}')
                        return
                    except Exception as e:
                        self.textbox.setText(f'✖ Failed to kill process: {e}')
                        self.log_action(f'Error killing port {port}: {e}')
                        return
            else:  # inserted
                self.textbox.setText(f'✖ No process found listening on port {port}')
                self.log_action(f'No listener found on port {port}')
        else:  # inserted
            self.textbox.setText('⚠ Please enter a port number.')
            self.log_action('Missing port input for kill.')

class CodeViewer(QWidget):
    def __init__(self, code_text: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle('API')
        layout = QVBoxLayout(self)
        label = QLabel('Python Code:')
        label.setStyleSheet('color: #aaa; font-weight: bold;')
        layout.addWidget(label)
        self.code_edit = QTextEdit()
        self.code_edit.setReadOnly(True)
        self.code_edit.setFont(QFont('Courier New', 10))
        self.code_edit.setStyleSheet('\n            QTextEdit {\n                background-color: #1e1e1e;\n                color: #dcdcdc;\n                border: 1px solid #444;\n                border-radius: 8px;\n                padding: 12px;\n            }\n        ')
        self.code_edit.setText(code_text)
        layout.addWidget(self.code_edit)
        button_layout = QHBoxLayout()
        copy_button = QPushButton('Copy Code')
        copy_button.clicked.connect(self.copy_code)
        button_layout.addStretch()
        button_layout.addWidget(copy_button)
        layout.addLayout(button_layout)

    def copy_code(self):
        from PyQt6.QtGui import QFont, QGuiApplication
        QGuiApplication.clipboard().setText(self.code_edit.toPlainText())
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, QPropertyAnimation, pyqtProperty, QEasingCurve, Qt, QVariantAnimation
from PyQt6.QtGui import QColor, QPainter, QBrush, QPalette
from PyQt6.QtCore import pyqtProperty, QEasingCurve, QPropertyAnimation, QVariantAnimation, Qt
from PyQt6.QtGui import QColor, QPainter, QBrush
from PyQt6.QtWidgets import QLabel

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
        tooltip_text = f'<img src=\"{icon_path101}\" width=\"32\" height=\"32\" style=\"vertical-align:middle; margin-right:30px;\"> <span style=\"font-size:20px; margin-left:30px; font-weight:bold; display:inline-block; text-align:center; width:100%;\">Nectar-X</span> <br> {result}'
        threading.Thread(target=tts_and_playback, args=(result,), daemon=True).start()
        tooltip = PersistentTooltip(tooltip_text, self)
        global_pos = self.output.mapToGlobal(QPoint(0, -tooltip.height()))
        tooltip.show_for_duration(global_pos, duration_ms=300000)

    def closeEvent(self, event):
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()
        event.accept()

class Main(QMainWindow):
    def __init__(self):
        from PyQt6.QtGui import QIcon
        super().__init__()
        self.setWindowTitle('Nectar-X-Studio')
        self.setGeometry(100, 100, 1200, 630)
        self.setStyleSheet(self.get_styles())
        icon_path = self.find_icon('background/NectarX.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:  # inserted
            self.setWindowIcon(QIcon('background/NectarX.png'))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QHBoxLayout()
        self.central_widget.setLayout(main_layout)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        self.primary_panel = QWidget()
        self.primary_panel.setFixedWidth(80)
        self.primary_panel.setStyleSheet('background-color: #484848; border-radius: 8px; padding: 8px;')
        self.primary_panel_layout = QVBoxLayout()
        self.primary_panel_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        button_style = '\n                QPushButton {\n                    background-color: #ffffff;\n                    color: white;\n                    font-size: 16px;\n                    border-radius: 8px;\n                    padding: 10px;\n                    margin: 5px;\n                }\n                QPushButton:hover {\n                    background-color: #3f3f3f;\n                    color: black;\n                }\n                QPushButton[selected=\"true\"] {\n                    background-color: #3f3f3f;\n                    color: black;\n                }\n                '
        icon_path1 = self.find_icon('ICON\\menu\\settings.png')
        icon_path2 = self.find_icon('ICON\\menu\\chat.png')
        icon_path5 = self.find_icon('ICON\\menu\\home.png')
        icon_path6 = self.find_icon('ICON\\menu\\llm.png')
        icon_path7 = self.find_icon('ICON\\menu\\test.png')
        icon_path8 = self.find_icon('ICON\\menu\\download.png')
        icon_path9 = self.find_icon('ICON\\menu\\update.png')
        self.buttons = {'Home': QPushButton(), 'Chat': QPushButton(), 'Broadcast': QPushButton(), 'Test Lab': QPushButton(), 'Model Downloader': QPushButton(), 'Update': QPushButton()}
        self.buttons['Home'].setIcon(QIcon(icon_path5))
        self.buttons['Chat'].setIcon(QIcon(icon_path2))
        self.buttons['Broadcast'].setIcon(QIcon(icon_path6))
        self.buttons['Test Lab'].setIcon(QIcon(icon_path7))
        self.buttons['Model Downloader'].setIcon(QIcon(icon_path8))
        self.buttons['Update'].setIcon(QIcon(icon_path9))
        self.buttons['Home'].setToolTip('Home')
        self.buttons['Chat'].setToolTip('Chat')
        self.buttons['Broadcast'].setToolTip('Server')
        self.buttons['Test Lab'].setToolTip('Lab')
        self.buttons['Model Downloader'].setToolTip('Download')
        self.buttons['Update'].setToolTip('Update')
        for btn in self.buttons.values():
            btn.setFixedHeight(50)
            btn.setIconSize(QSize(24, 24))
            btn.setStyleSheet(button_style)
            self.primary_panel_layout.addWidget(btn)
        self.primary_panel_layout.addStretch()
        self.dot = AnimatedDot()
        self.dot.setFixedSize(50, 50)
        self.dot.setToolTip('Online Model Status')
        self.primary_panel_layout.addWidget(self.dot, alignment=Qt.AlignmentFlag.AlignCenter)
        self.settings = QPushButton()
        self.settings.setIcon(QIcon(icon_path1))
        self.settings.setFixedHeight(50)
        self.settings.setStyleSheet(button_style)
        self.settings.clicked.connect(self.settings_menu)
        self.settings.setToolTip('Settings')
        self.primary_panel_layout.addWidget(self.settings)
        self.primary_panel.setLayout(self.primary_panel_layout)
        self.toggle_button = QPushButton('')
        self.toggle_button.setFixedSize(50, 50)
        self.toggle_button.setToolTip('Minimal Mode')
        self.toggle_button.setStyleSheet('QPushButton {background-color: #1E1E1E; color: white; border: none; font-size: 24px; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}')
        self.toggle_button.clicked.connect(self.toggle_sidebar)
        self.content_area = QStackedWidget()
        self.content_area.setStyleSheet('background-color: transparent; border: none; border-radius: 8px;')
        raw_pages = {'': DisplayImage(), 'Home': Home(), 'Chat': Chat(), 'Broadcast': Broadcast(), 'Test Lab': Engine_Holder(), 'Model Downloader': Gguf_Downloader(), 'Update': UpdatePrompt(), 'Settings': Settings(), 'Docs': Home1(), 'Dev': NetworkSecurityUI()}
        for key in raw_pages:
            write_to_log(f'Loaded page: {key}', file_path='logs/app.log')
        self.pages = {}
        for name, widget in raw_pages.items():
            from PyQt6.QtWidgets import QScrollArea
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setStyleSheet('\n                                QScrollBar:vertical {\n                                background: transparent;\n                                width: 8px;\n                                margin: 0px;\n                                border: none;\n                            }\n\n                            QScrollBar::handle:vertical {\n                                background: #ffffff;\n                                min-height: 20px;\n                                border-radius: 4px;\n                            }\n\n                            QScrollBar::handle:vertical:hover {\n                                background: #1b1b1b;\n                            }\n\n                            QScrollBar::add-line:vertical,\n                            QScrollBar::sub-line:vertical,\n                            QScrollBar::add-page:vertical,\n                            QScrollBar::sub-page:vertical {\n                                background: none;\n                                height: 0px;\n                                border: none;\n                            }\n\n                            /* Horizontal Scrollbar */\n                            QScrollBar:horizontal {\n                                background: transparent;\n                                height: 8px;\n                                margin: 0px;\n                                border: none;\n                            }\n\n                            QScrollBar::handle:horizontal {\n                                background: rgba(0, 0, 0, 0.2);\n                                min-width: 20px;\n                                border-radius: 4px;\n                            }\n\n                            QScrollBar::handle:horizontal:hover {\n                                background: rgba(0, 0, 0, 0.4);\n                            }\n\n                            QScrollBar::add-line:horizontal,\n                            QScrollBar::sub-line:horizontal,\n                            QScrollBar::add-page:horizontal,\n                            QScrollBar::sub-page:horizontal {\n                                background: none;\n                                width: 0px;\n                                border: none;\n                            } ')
            scroll_area.setWidget(widget)
            self.content_area.addWidget(scroll_area)
            self.pages[name] = scroll_area
        for name, btn in self.buttons.items():
            btn.clicked.connect(lambda _, n=name: self.load_tool_and_highlight(n))
        splitter.addWidget(self.primary_panel)
        splitter.addWidget(self.content_area)
        main_layout.addWidget(splitter)
        main_layout.addWidget(self.toggle_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.timeout.connect(self.show_inactivity_screen)
        self.inactivity_timer.start(3600000)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_server)
        self.timer.start(3000)
        self.check_server()
        self.setMouseTracking(True)
        self.installEventFilter(self)

    def on_dot_clicked(self):
        self.engine = Engine_Holder()
        self.engine.signals.auto_run.emit()

    def check_server(self):
        service_port = 5005
        is_active = self.ping('127.0.0.1', service_port)
        self.dot.set_active(is_active)

    def ping(self, host, port, timeout=0.5):
        if port == 0:
            return False
        pkt = IP(dst=host) / TCP(dport=port, flags='S')
        resp = sr1(pkt, timeout=timeout, verbose=0)
        if resp is None:
            return False
        if resp.haslayer(TCP):
            tcp_layer = resp.getlayer(TCP)
            if tcp_layer.flags == 18:
                rst_pkt = IP(dst=host) / TCP(dport=port, flags='R', seq=tcp_layer.ack)
                send(rst_pkt, verbose=0)
                return True
            if tcp_layer.flags == 20:
                return False
        return False

    def load_tool_and_highlight(self, name):
        self.highlight_selected_button(name)
        self.load_tool(name)

    def highlight_selected_button(self, selected_name):
        for name, btn in self.buttons.items():
            if name == selected_name:
                btn.setProperty('selected', 'true')
            else:  # inserted
                btn.setProperty('selected', 'false')
            btn.style().unpolish(btn)
            btn.style().polish(btn)
        self.settings.setProperty('selected', selected_name == 'Settings')
        self.settings.style().unpolish(self.settings)
        self.settings.style().polish(self.settings)

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'ICON', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

    def load_tool(self, tool_name):
        self.content_area.setCurrentWidget(self.pages[tool_name])

    def show_inactivity_screen(self):
        self.content_area.setCurrentWidget(self.pages[''])

    def get_styles(self):
        return '\n                            QPushButton:hover {\n                                            background-color: #007ACC;\n                            }\n                            QPushButton:pressed {\n                                            background-color: #005F9E;\n                            }\n                            '

    def eventFilter(self, source, event):
        from PyQt6.QtCore import QEvent
        if event.type() in [QEvent.Type.KeyPress, QEvent.Type.MouseMove]:
            self.inactivity_timer.start(3600000)
        return super().eventFilter(source, event)

    def toggle_sidebar(self):
        asset.show()
        self.hide()
        self.load_tool_and_highlight('')

    def settings_menu(self):
        self.load_tool_and_highlight('Settings')
code = 'def send_to_API(question): \n\timport socket\n\ttry:\n\t\tclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n\t\tclient.connect((\'127.0.0.1\', 8012))\n\t\tclient.send(question.encode(\'utf-8\'))\n\t\tresponse = client.recv(4096)\n\t\tclient.close()\n\t\treturn response.decode(\'utf-8\')\n\texcept (socket.error, socket.timeout) as e:\n\t\treturn f\"[Error] Could not connect to AlphaLLM: {e}\"\n\t'
conversation_history = load_conversation_history()
history = load_history()
from PyQt6.QtCore import QSharedMemory, QSystemSemaphore

def main():
    global background_widget  # inserted
    global Studio_Nectar  # inserted
    global viewer  # inserted
    global asset  # inserted
    shared_memory = QSharedMemory('Nectar-X-Studio')
    if not shared_memory.create(1):
        write_to_log('Another instance is already running.')
        return
    app = QApplication(sys.argv)
    entry = SplashScreen()
    entry.show_splash()
    apply_theme(get_user_theme())
    ai = WindowsAutomationAI()
    background_widget = BackgroundWidget(ai)
    viewer = CodeViewer(code)
    viewer.resize(700, 400)
    asset = Assets()
    Studio_Nectar = Main()
    sys.exit(app.exec())
if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
