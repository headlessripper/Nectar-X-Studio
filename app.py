"""
\nLicense Key: CIRB-5002-NGWG-4132
\nUnique Numerical Signature: 4153318607422408869
\nSeriel No: D51CD0192107E1E6F03746B510264E29
\n
"""

global _logger_initialized  # inserted
Encoded_License_Details = 'eyJsaWNlbnNvciI6ICJaYXNoaXJpb24gaW5jIiwgImxpY2Vuc2Vfa2V5IjogIkNJUkItNTAwMi1OR1dHLTQxMzIiLCAiZXhwaXJhdGlvbl9kYXRlIjogIjIwMjctMTItMjMifQ=='
import asyncio
import pyotp
import uvicorn
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QSharedMemory, QSystemSemaphore
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSplashScreen, QLabel
from PyQt6.QtCore import Qt, QTimer, QSharedMemory
from PyQt6.QtCore import Qt, QTimer, QElapsedTimer
from PyQt6.QtGui import QPainter, QColor, QBrush
import math
from urllib.parse import urlparse
import socket
import pygame
import sys
import os
import subprocess
import platform
import urllib.request
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import subprocess
import platform
import psutil
import shutil
import os
import re
import os
import requests
import shutil
import subprocess
import sys
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar, QLabel
import os
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGraphicsOpacityEffect
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtWebEngineWidgets import QWebEngineView
import time
from PyQt6.QtGui import QCursor
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
import os
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QLabel, QMessageBox, QProgressBar, QHBoxLayout, QFormLayout,
    QSpinBox, QDoubleSpinBox, QFileDialog, QScrollArea, QComboBox
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PIL import Image
from PIL.ImageQt import ImageQt
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
import sys
import time
QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)
import threading
try:
    from llama_cpp import Llama
except ImportError:
    Llama = None
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QFont, QGuiApplication
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, QPropertyAnimation, pyqtProperty, QEasingCurve, Qt, QVariantAnimation
from PyQt6.QtGui import QColor, QPainter, QBrush, QPalette
from PyQt6.QtCore import pyqtProperty, QEasingCurve, QPropertyAnimation, QVariantAnimation, Qt
from PyQt6.QtGui import QColor, QPainter, QBrush
from PyQt6.QtWidgets import QLabel
import os
import json
import os, json, threading
from PyQt6.QtCore import pyqtSignal, QObject
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from urllib.request import urlopen
from PyQt6.QtGui import QPixmap, QImage
import sys
import os
import threading
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

# ----------------------------
# Find a free port
# ----------------------------
def find_free_port():
    """Find a free local port to use for the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


# ----------------------------
# Silent HTTP Server with Download Support
# ----------------------------
class SilentHandler(SimpleHTTPRequestHandler):
    """Custom HTTP handler that allows file downloads and hides logs."""

    def end_headers(self):
        # Add CORS headers for JupyterLite compatibility
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def log_message(self, format, *args):
        # Suppress log output
        pass

    def do_GET(self):
        """Handle file download requests."""
        if self.path.startswith("/download/"):
            filepath = self.path[len("/download/"):]
            if os.path.isfile(filepath):
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream")
                self.send_header(
                    "Content-Disposition",
                    f'attachment; filename="{os.path.basename(filepath)}"'
                )
                self.end_headers()
                with open(filepath, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File not found.")
        else:
            super().do_GET()

    def guess_type(self, path):
        """Force download for unknown file types (like .ipynb, .txt, .csv)."""
        base, ext = os.path.splitext(path)
        if ext not in ('.html', '.js', '.css', '.png', '.jpg', '.gif'):
            return 'application/octet-stream'
        return super().guess_type(path)


class HTTPServerThread(threading.Thread):
    """Run a local HTTP server silently in a separate thread."""
    def __init__(self, directory, port):
        super().__init__(daemon=True)
        self.directory = directory
        self.port = port
        self.httpd = None

    def run(self):
        os.chdir(self.directory)
        self.httpd = HTTPServer(("localhost", self.port), SilentHandler)
        self.httpd.serve_forever()

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()

def find_notebook(icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'Notebook', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:  # inserted
            return None

from pathlib import Path

output_dir = Path(find_notebook("Notebook"))
if not output_dir.exists():
    print(f"❌ Directory not found: {output_dir}")
    sys.exit(1)

port = find_free_port()
server_thread = HTTPServerThread(str(output_dir), port)
server_thread.start()

# Give the server time to start
time.sleep(2)

# --- Determine correct entry file (lab/index.html or index.html) ---
index_path = output_dir / "lab" / "index.html"
if not index_path.exists():
    index_path = output_dir / "index.html"

class GoogleAuthWorker(QObject):
    finished = pyqtSignal(dict)
    failed = pyqtSignal(str)

    def __init__(self, client_secret_path, scopes):
        super().__init__()
        self.client_secret_path = client_secret_path
        self.scopes = scopes

    def run(self):
        try:
            flow = InstalledAppFlow.from_client_secrets_file(self.client_secret_path, self.scopes)
            creds = flow.run_local_server(port=0)
            service = build("oauth2", "v2", credentials=creds)
            profile = service.userinfo().get().execute()
            self.finished.emit(profile)
        except Exception as e:
            self.failed.emit(str(e))


class GoogleAuthHelper:
    SCOPES = [
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
    ]

    def __init__(self, settings):
        self.settings = settings
        self.client_secret_file = os.path.join(os.path.dirname(__file__), "oauth", "client_secret.json")

    def save_profile(self, profile: dict):
        """Save Google account data."""
        self.settings.setValue("google/name", profile.get("name", ""))
        self.settings.setValue("google/email", profile.get("email", ""))
        self.settings.setValue("google/picture", profile.get("picture", ""))
        self.settings.setValue("google/authorized", True)

    def load_picture(self):
        """Return QPixmap of the saved profile picture."""
        url = self.settings.value("google/picture", "")
        if not url:
            return None
        try:
            data = urlopen(url).read()
            image = QImage()
            image.loadFromData(data)
            return QPixmap(image)
        except Exception:
            return None

    def is_authenticated(self):
        return self.settings.value("google/authorized", False, type=bool)

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

_logger_lock = threading.Lock()
_logger_initialized = False

def setup_logger(log_file_path='logs/Debug.log'):
    global _logger_initialized
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
                logging.basicConfig(
                    filename=log_file_path,
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    encoding='utf-8'
                )
            except Exception:
                logging.basicConfig(
                    filename=log_file_path,
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )

            logging.raiseExceptions = False
            logging.debug('Logger initialized successfully.')
            _logger_initialized = True

        except Exception as e:
            print(f"Logger initialization failed: {e}")
            _logger_initialized = True

# Initialize logger
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
light_theme = """
QMainWindow {
    background-color: #E7DB74;
    color: black;
}
"""

dark_theme = """
QMainWindow {
    background-color: #221a0f;
    color: #ffffff;
}
"""

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
    settings = QSettings('Zashirion', 'UserPreferences')
    return settings.value('theme', 'dark')

def set_user_theme(theme):
    settings = QSettings('Zashirion', 'UserPreferences')
    settings.setValue('theme', theme)

def set_dark_theme1(self):
    """Set dark theme for the application."""  # inserted
    dark_stylesheet = """
        QWidget {
            background-color: #463019;
            color: #ffffff;
        }
        """

    self.setStyleSheet(dark_stylesheet)

def set_light_theme(self):
    """Set dark theme for the application."""  # inserted
    light_stylesheet = """
        QWidget {
            background-color: transparent;
            color: #f50000;
        }

        QLineEdit, QTextEdit, QPlainTextEdit {
            background-color: #2a2c31;
            color: #ffffff;
            border: none;
            padding: 5px;
            border-radius: 10px;
        }

        QPushButton {
            background-color: #000000;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #f50000;
        }

        QPushButton:pressed {
            background-color: #FFFFFF;
        }

        QListWidget {
            background-color: #3c3f41;
            color: #d3d3d3;
            border: 1px solid #444444;
        }

        QGroupBox {
            border: 1px solid #444444;
            background-color: #2b2b2b;
            color: #d3d3d3;
            margin: 5px;
            padding: 10px;
        }

        QFormLayout {
            background-color: #2b2b2b;
            color: #d3d3d3;
        }
        """

    self.setStyleSheet(light_stylesheet)

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
        self.card_frame.setStyleSheet("""
            QWidget {
                background-color: #1b1b1b;
                border-radius: 12px;
                padding: 16px;
                margin: 8px;
            }

            QFrame {
                background-color: #000000;
                border: 1px solid transparent;
                border-radius: 12px;
                padding: 16px;
            }

            QLabel {
                color: #333;
                font-size: 13px;
            }

            QWidget:hover {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            """)

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
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {base_color};
                border-radius: 12px;
                padding: 15px;
                margin: 8px;
            }}
            QWidget:hover {{
                background-color: {hover_color};
            }}
        """)

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
        scroll.setStyleSheet("""
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
        self.setStyleSheet("""
            QCheckBox {
                spacing: 10px;
            }

            QCheckBox::indicator {
                width: 40px;
                height: 20px;
                border-radius: 10px;
                background: transparent;
            }
            """)

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
        self.overlay_text.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 18px;
                background-color: rgba(0, 0, 0, 120);
                border-radius: 8px;
                padding: 6px 12px;
            }
            """)

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
        self.setStyleSheet("""
            QWidget {
                background-color: transparent;
                color: white;
                font-size: 14px;
                border-radius: 8px;
                padding: 10px;
            }

            QLineEdit {
                background-color: #000000;
                color: #ffffff;
                border-radius: 6px;
                padding: 10px;
                border: 1px solid None;
            }

            QLineEdit:hover {
                border: 1px solid None;
                background-color: #111111;
            }

            QPushButton {
                padding: 12px;
                background-color: #000000;
                color: white;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #242424;
                color: #ffffff;
            }

            QLabel {
                color: #e0e0e0;
            }

            QFrame {
                background-color: transparent;
                border-radius: 8px;
                padding: 10px;
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

        # --- Layout setup ---
        main_layout = QHBoxLayout(self)

        # Left: Sidebar / History
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(8)

        title = QLabel('Chat History')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet('font-size: 20x; font-weight: bold; color: #dddddd; padding: 5px;')
        sidebar_layout.addWidget(title)

        from PyQt6.QtWidgets import QListWidget
        self.history_list = QListWidget()
        self.history_list.setSpacing(4)
        self.history_list.setEditTriggers(QListWidget.EditTrigger.DoubleClicked)
        self.history_list.itemDoubleClicked.connect(self.rename_session)
        self.history_list.setToolTip('Double Click to Rename or Delete Session.')
        self.history_list.setStyleSheet("""
            QListWidget {
                background-color: transparent;
                border-radius: 6px;
                padding: 5px;
            }

            QListWidget::item {
                background-color: #000000;
                padding: 8px;
                color: #ffffff;
                border-radius: 6px;
            }

            QListWidget::item:selected {
                background-color: #242424;
                border-radius: 6px;
            }

            QListWidget::item:hover {
                background-color: #1b1b1b;
                border-radius: 6px;
            }
            """)

        self.history_list.itemClicked.connect(self.load_session)
        sidebar_layout.addWidget(self.history_list)

        new_chat_button = QPushButton('+ New Chat')
        new_chat_button.clicked.connect(self.create_new_session)
        sidebar_layout.addWidget(new_chat_button)

        sidebar = QWidget()
        sidebar.setLayout(sidebar_layout)
        sidebar.setFixedWidth(320)

        # Right: Chat area
        chat_area_layout = QVBoxLayout()
        chat_area_layout.setContentsMargins(10, 10, 10, 10)
        chat_area_layout.setSpacing(8)

        # Scrollable chat display
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.chat_container = QWidget()
        self.chat_display = QVBoxLayout(self.chat_container)
        self.chat_display.setSpacing(12)
        self.scroll_area.setWidget(self.chat_container)
        chat_area_layout.addWidget(self.scroll_area)

        # Watermark
        self.watermark = QLabel("Nectar-X-Studio")
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watermark.setStyleSheet("color: #000000; font-size: 42px; font-weight: bold;")
        self.chat_display.addWidget(self.watermark)

        # Loading + progress
        self.loader_label = QLabel("Thinking...")
        self.loader_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loader_label.hide()
        chat_area_layout.addWidget(self.loader_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: transparent;
                border: 1px solid transparent;
                border-radius: 4px;
                text-align: center;
                color: #444444;
                font-weight: bold;
            }

            QProgressBar::chunk {
                background-color: #1b1b1b;
                border-radius: 4px;
            }
            """)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        chat_area_layout.addWidget(self.progress_bar)

        # Input section
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message...")
        self.input_field.returnPressed.connect(self.send_message)
        input_layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setToolTip("Send your message")
        input_layout.addWidget(self.send_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_everything)
        input_layout.addWidget(self.clear_button)

        chat_area_layout.addLayout(input_layout)

        main_layout.addWidget(sidebar)
        main_layout.addLayout(chat_area_layout)

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
        self.clear_button.show()
        self.watermark = QLabel('Nectar-X-Studio', self)
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watermark.setStyleSheet('color: rgba(0, 0, 0, 1); font-size: 50px; font-weight: bold;')
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
            bubble.setStyleSheet('background-color: #000000; color: white; padding: 10px; border-radius: 6px;')
            message_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        else:  # inserted
            if sender == 'ai':
                bubble.setStyleSheet('background-color: #ffffff; color: black; padding: 10px; border-radius: 6px;')
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
        dialog.setStyleSheet("""
            QDialog {
                background-color: #000000;
                border-radius: 10px;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #1e1e1e;
                color: #ffffff;
                border: 1px solid #ffffff;
                border-radius: 5px;
                padding: 4px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #000000;
                color: white;
                border-radius: 5px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #000111;
            }
            QPushButton:pressed {
                background-color: #000000;
            }
            QDialogButtonBox QPushButton {
                min-width: 100px;
            }
        """)
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
            confirm = QMessageBox(self)
            confirm.setWindowTitle('Delete Session')
            confirm.setText(f"Are you sure you want to delete the session '{old_name}'?")
            confirm.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirm.setDefaultButton(QMessageBox.StandardButton.No)

            # Apply custom styling
            confirm.setStyleSheet("""
                QMessageBox {
                    background-color: #000000;
                    border-radius: 10px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton {
                    background-color: #000000;
                    color: white;
                    border-radius: 5px;
                    padding: 6px 12px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #000111;
                }
                QPushButton:pressed {
                    background-color: #000000;
                }
            """)

            result = confirm.exec()
            if result == QMessageBox.StandardButton.Yes:
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
            if new_name and new_name != old_name:
                if new_name in self.chat_sessions:
                    # Styled warning message box
                    warning = QMessageBox(self)
                    warning.setWindowTitle('Duplicate Name')
                    warning.setText('A session with this name already exists.')
                    warning.setIcon(QMessageBox.Icon.Warning)
                    warning.setStandardButtons(QMessageBox.StandardButton.Ok)
                    
                    # Apply custom styling
                    warning.setStyleSheet("""
                        QMessageBox {
                            background-color: #000000;
                            border-radius: 10px;
                        }
                        QLabel {
                            color: #ffffff;
                            font-size: 14px;
                            font-weight: bold;
                        }
                        QPushButton {
                            background-color: #000000;
                            color: white;
                            border-radius: 5px;
                            padding: 6px 12px;
                            min-width: 80px;
                        }
                        QPushButton:hover {
                            background-color: #000111;
                        }
                        QPushButton:pressed {
                            background-color: #000000;
                        }
                    """)
                    warning.exec()
                    return
                
                # Rename session
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
        self.watermark = QLabel('Nectar-X-Studio', self)
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watermark.setStyleSheet('color: rgba(0, 0, 0, 1); font-size: 50px; font-weight: bold;')
        self.chat_display.addWidget(self.watermark)

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

PYTHON_VERSION = "3.12"

class DownloadThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, url, output_file):
        super().__init__()
        self.url = url
        self.output_file = output_file

    def run(self):
        try:
            with urllib.request.urlopen(self.url) as response:
                total_size = int(response.getheader('Content-Length').strip())
                downloaded = 0
                chunk_size = 8192
                with open(self.output_file, 'wb') as f:
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)
                        percent = int(downloaded * 100 / total_size)
                        self.progress.emit(percent)
            self.finished.emit(self.output_file)
        except Exception as e:
            self.error.emit(str(e))


class PythonInstaller(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nectar-X-Studio - Python Installer")
        self.setStyleSheet("""
            QWidget { background-color: #000000; color: #cccccc; }
            QLabel#title { font-size: 22px; font-weight: bold; }
            QLabel#status { font-size: 16px; }
            QProgressBar { height: 25px; text-align: center; }
            QPushButton { font-size: 14px; padding: 10px; }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)
        self.setLayout(layout)

        self.title_label = QLabel("Nectar-X-Studio Installer")
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        self.status_label = QLabel("Checking Python installation...")
        self.status_label.setObjectName("status")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: transparent;
                border: 1px solid #444444;
                border-radius: 4px;
                text-align: center;
                color: #dddddd;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background-color: #1b1b1b;
                border-radius: 4px;
            }
        """)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.install_button = QPushButton("Download and Install Python")
        self.install_button.setEnabled(False)
        self.install_button.clicked.connect(self.start_install)
        layout.addWidget(self.install_button)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(sys.exit)
        layout.addWidget(self.quit_button)

        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.check_python()

    # 🔧 Check if Python is installed and update UI
    def check_python(self):
        if self.is_python_installed():
            self.status_label.setText("✅ Python is already installed on this system.")
            self.progress_bar.hide()
            self.install_button.hide()
        else:
            self.status_label.setText("❌ Python is not installed on this system.")
            self.install_button.setEnabled(True)
            self.progress_bar.show()

    def is_python_installed(self):
        try:
            # Check for python3 first
            subprocess.run(["python3", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except Exception:
            # Then try 'python' (Windows often uses that)
            try:
                subprocess.run(["python", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return True
            except Exception:
                return False

    def start_install(self):
        self.install_button.setEnabled(False)
        self.status_label.setText("Preparing to install Python...")
        system = platform.system()
        if system == "Windows":
            self.install_windows()
        elif system == "Linux":
            self.install_linux()
        elif system == "Darwin":
            self.install_mac()
        else:
            self.status_label.setText(f"{system} is not supported.")
            self.install_button.setEnabled(True)

    # ------------------- WINDOWS -------------------
    def install_windows(self):
        arch = platform.architecture()[0]
        url = (
            f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-amd64.exe"
            if arch == "64bit"
            else f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}.exe"
        )
        installer_file = os.path.join(os.getcwd(), "python_installer.exe")
        self.status_label.setText("Downloading Python installer...")
        self.download_thread = DownloadThread(url, installer_file)
        self.download_thread.progress.connect(self.progress_bar.setValue)
        self.download_thread.finished.connect(lambda f: self.run_windows_installer(f))
        self.download_thread.error.connect(lambda e: self.status_label.setText(f"Download Error: {e}"))
        self.download_thread.start()

    def run_windows_installer(self, installer_file):
        try:
            self.status_label.setText("Installing Python...")
            subprocess.run([installer_file, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
            self.status_label.setText("✅ Python installed successfully!")
            self.progress_bar.setValue(100)
        except Exception as e:
            self.status_label.setText(f"Installation Failed: {e}")
            self.install_button.setEnabled(True)

    # ------------------- LINUX -------------------
    def install_linux(self):
        distro = self.get_linux_distro()
        self.status_label.setText(f"Installing Python {PYTHON_VERSION} on {distro}...")
        try:
            if distro in ["ubuntu", "debian"]:
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", f"python3.{PYTHON_VERSION.split('.')[1]}"], check=True)
            elif distro in ["fedora"]:
                subprocess.run(["sudo", "dnf", "install", "-y", f"python3.{PYTHON_VERSION.split('.')[1]}"], check=True)
            elif distro in ["centos", "rhel"]:
                subprocess.run(["sudo", "yum", "install", "-y", f"python3.{PYTHON_VERSION.split('.')[1]}"], check=True)
            elif distro in ["opensuse"]:
                subprocess.run(["sudo", "zypper", "install", "-y", f"python3.{PYTHON_VERSION.split('.')[1]}"], check=True)
            else:
                self.status_label.setText(f"⚠️ Please install Python {PYTHON_VERSION} manually for {distro}.")
                self.install_button.setEnabled(True)
                return
            self.status_label.setText("✅ Python installed successfully!")
            self.progress_bar.setValue(100)
        except Exception as e:
            self.status_label.setText(f"Installation Failed: {e}")
            self.install_button.setEnabled(True)

    def get_linux_distro(self):
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("ID="):
                        return line.strip().split("=")[1].strip('"').lower()
        except Exception:
            pass
        return "unknown"

    # ------------------- MAC -------------------
    def install_mac(self):
        url = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-macos11.pkg"
        installer_file = os.path.join(os.getcwd(), "python_installer.pkg")
        self.status_label.setText("Downloading Python for macOS...")
        self.download_thread = DownloadThread(url, installer_file)
        self.download_thread.progress.connect(self.progress_bar.setValue)
        self.download_thread.finished.connect(lambda f: self.run_mac_installer(f))
        self.download_thread.error.connect(lambda e: self.status_label.setText(f"Download Error: {e}"))
        self.download_thread.start()

    def run_mac_installer(self, installer_file):
        try:
            self.status_label.setText("Installing Python...")
            subprocess.run(["sudo", "installer", "-pkg", installer_file, "-target", "/"], check=True)
            self.status_label.setText("✅ Python installed successfully!")
            self.progress_bar.setValue(100)
        except Exception as e:
            self.status_label.setText(f"Installation Failed: {e}")
            self.install_button.setEnabled(True)

class Engine_Holder(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_model_watcher()
        self.setWindowTitle('Engine - Nectar-X-Studio')
        self.settings1 = QSettings('Zashirion', 'Modelpath')
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
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'menu', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
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
        icon_path51 = self.find_icon('menu/net.png')
        icon_path52 = self.find_icon('menu/chat2.png')
        icon_path53 = self.find_icon('menu/sett.png')
        icons = {'Load': QIcon(icon_path51), 'Code': QIcon(icon_path52), 'Settings': QIcon(icon_path53)}
        for i, name in enumerate(['Load', 'Code', 'Settings']):
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
                """)

            btn.clicked.connect(lambda _, idx=i: self.card_layout.setCurrentIndex(idx))
            sidebar_layout.addWidget(btn)
        sidebar_layout.addStretch(1)
        self.stop_server_button = QPushButton()
        self.stop_server_button.setIcon(qta.icon('fa5s.power-off', color='black'))
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
                background-color: #000000;  /* dark background */
                color: #FFFFFF;             /* white text */
                border: 1px solid transparent;  /* light gray border */
                padding: 5px;
                border-radius: 5px;
                font-size: 12pt;
                font-family: Arial;
            }
            """)

        self.stop_server_button.clicked.connect(self.terminate)
        sidebar_layout.addWidget(self.stop_server_button)
        sidebar_widget = QWidget()
        sidebar_widget.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sidebar_widget.setFixedHeight(400)
        sidebar_widget.setStyleSheet('border-radius: 10px; background-color: #000000')
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
        self.label_model_path.setStyleSheet("""
            QLabel {
                background-color: #000000;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                color: #dddddd;
            }
            """)

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

            QComboBox::down-arrow {
                image: url("background/down-arrow.svg");  /* Replace this with your icon */
                width: 12px;
                height: 12px;
            }

            QComboBox QAbstractItemView {
                background-color: #000000;
                color: #000000;
                border: 1px solid #333;
                selection-background-color: #1b1b1b;
                padding: 6px;
                outline: 0;
            }
            """)

        self.combo_model_list.hide()
        model_loader_layout.addWidget(self.label_model_path)
        model_loader_layout.addWidget(self.combo_model_list)
        layout.addWidget(model_loader_frame)
        
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
        page = PythonInstaller()
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

    def get_group_value(self, group_title: str, label_text: str):
        """
        Retrieve the currently selected value from a group combo box.
        """
        return self.group_controls[group_title][label_text].currentText()

    def create_settings_page(self):
        from PyQt6.QtCore import QSettings
        self.set_light_theme()
        self.settings = QSettings('Zashirion', 'Nectar_File')
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
        saved_template = QSettings('Zashirion', 'Nectar-X-Studio').value('chat_template', 'chatml')
        index = combo.findText(saved_template)
        if index >= 0:
            combo.setCurrentIndex(index)
        combo.currentTextChanged.connect(lambda value: QSettings('Zashirion', 'Nectar-X-Studio').setValue('chat_template', value))
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
        self.use_numa = add_checkbox('use_numa', 'Enable NUMA', True)
        self.use_mmap = add_checkbox('use_mmap', 'Enable Memory Map', True)
        self.use_mmap_mmap = add_checkbox('use_mmap_backend', 'Use mmap backend', True)
        sidebar_frame = QFrame()
        sidebar_frame.setLayout(sidebar)
        sidebar_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border: 1px solid #ccc;
                border-radius: 10px;
            }
            """)

        info_card = QFrame()
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
        light_stylesheet = """
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
                background-color: #1b1b1b;
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
        try:
            nectarhub_path = None
            log_message = ""

            # -------- WINDOWS --------
            if sys.platform.startswith("win"):
                import ctypes
                program_files = os.environ.get("ProgramFiles", r"C:\Program Files")
                nectarhub_path = os.path.join(program_files, "NectarHub")

                try:
                    is_admin = bool(ctypes.windll.shell32.IsUserAnAdmin())
                except Exception:
                    is_admin = False

                if not os.path.exists(nectarhub_path):
                    if is_admin:
                        os.makedirs(nectarhub_path, exist_ok=True)
                        log_message += f"[INFO] Created NectarHub in Program Files: {nectarhub_path}\n"
                    else:
                        home_dir = os.path.expanduser("~")
                        nectarhub_path = os.path.join(home_dir, "NectarHub")
                        os.makedirs(nectarhub_path, exist_ok=True)
                        log_message += f"[WARNING] No admin rights, created NectarHub in user directory: {nectarhub_path}\n"
                        QMessageBox.information(
                            self,
                            "Notice",
                            f"Created NectarHub in user directory instead of Program Files:\n{nectarhub_path}"
                        )

            # -------- LINUX / MACOS --------
            else:
                home_dir = os.path.expanduser("~")
                if sys.platform == "darwin":
                    nectarhub_path = os.path.join(home_dir, "NectarHub")
                else:
                    nectarhub_path = os.path.join(home_dir, ".NectarHub")

                os.makedirs(nectarhub_path, exist_ok=True)
                log_message += f"[INFO] Ensured NectarHub folder at: {nectarhub_path}\n"

            # -------- LOGGING --------
            log_file = os.path.join(nectarhub_path, "log.txt")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {log_message}")

            if not os.path.isdir(nectarhub_path):
                raise OSError(f"Could not create/access folder at: {nectarhub_path}")

            return nectarhub_path

        except Exception as e:
            try:
                home_dir = os.path.expanduser("~")
                fallback_log = os.path.join(home_dir, "NectarHub_error.log")
                with open(fallback_log, "a", encoding="utf-8") as f:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"[{timestamp}] [ERROR] {str(e)}\n")
            except Exception:
                pass

            QMessageBox.critical(
                self,
                "Error",
                f"Could not create/access 'NectarHub' folder:\n{str(e)}"
            )
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
            self.llm_instance = Llama(
                model_path=self.loaded_model_path, n_ctx=ctx_value, chat_format=chat_format_selected,
                n_threads=thread_value, n_gpu_layers=gpu_layer_amount,
                use_mlock=use_mem_lock, verbose=use_verbose, numa=use_numa,
                mmap=use_mmap_activate, use_mmap=use_mmap_active, n_batch=btx_value
            )
            self.update_build_flags_label(self.llm_instance)
            self.conversation_history = []

            import socket
            self.server_running = True  # <── add this flag
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind(('127.0.0.1', 5005))
            self.server.listen(5)
            self.show_notification('Engine Running')

            while self.server_running:
                try:
                    client, _ = self.server.accept()
                except OSError:
                    break  # server closed, exit loop safely
                threading.Thread(target=self.handle_client, args=(client,), daemon=True).start()

        except Exception as e:
            self.show_notification(f'Engine error: {e}')

    def handle_client(self, client_socket):
        try:
            data = client_socket.recv(4096).decode('utf-8').strip()
            if not data:
                client_socket.send(b'No data received')
                return

            if data.startswith('LOAD_MODEL::'):
                self.conversation_history.append({'role': 'user', 'content': data})
                client_socket.send(b'OK')
                return

            # Append user's message
            self.conversation_history.append({'role': 'user', 'content': data})

            # Generate response
            result = self.llm_instance.create_chat_completion(
                self.conversation_history,
                max_tokens=self.max_tokens.value(),
                temperature=self.temperature.value() / 100
            )

            reply = result['choices'][0]['message']['content'].strip()

            # Append assistant's reply
            self.conversation_history.append({'role': 'assistant', 'content': reply})

            # Send reply to client
            client_socket.send(reply.encode('utf-8'))

        except Exception as e:
            error_message = f'Error: {e}'
            client_socket.send(error_message.encode('utf-8'))

        finally:
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
            self.show_notification('🚀 Engine Stopped')
        except Exception as e:
            self.show_notification(f'❌ Error during termination: {e}')
        
ACCESS_TOKEN = 'ACCESS_TOKEN'
token = 'ACCESS_TOKEN'

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
        self.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 12px;
                padding: 12px;
            }

            QLabel {
                color: #333;
                font-size: 13px;
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
        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: #eeeeee;
                border: 1px solid #cccccc;
                border-radius: 4px;
                text-align: center;
                color: #444444;
                font-weight: bold;
            }

            QProgressBar::chunk {
                background-color: #1b1b1b;
                border-radius: 4px;
            }
            """)

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
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg};
                border: none;
                border-radius: 6px;
            }}
            QPushButton:hover {{
                background-color: {hover};
            }}
        """)

        return btn

    def open_file_location(self):
        if os.path.exists(self.save_path):
            folder = os.path.dirname(self.save_path)
            QDesktopServices.openUrl(QUrl.fromLocalFile(folder))
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("⚠️ File Not Found")
            msg.setText("The file path no longer exists.")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.setWindowModality(Qt.WindowModality.ApplicationModal)

            # Optional custom icon
            # msg.setWindowIcon(QIcon("icons/warning.png"))

            # Apply custom stylesheet
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #1e1e2f;
                    color: #f5f5f5;
                    font-family: 'Segoe UI';
                    font-size: 14px;
                    border-radius: 12px;
                }
                QLabel {
                    color: #ffcc00;
                    font-size: 14px;
                    padding: 6px;
                }
                QPushButton {
                    background-color: #ffcc00;
                    color: #1e1e2f;
                    font-weight: bold;
                    border: none;
                    border-radius: 8px;
                    padding: 6px 16px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #ffd633;
                }
                QPushButton:pressed {
                    background-color: #e6b800;
                }
            """)

            msg.exec()

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
        self.scroll_area.setStyleSheet("""
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
        self.settings = QSettings('Zashirion', 'NDM (Nectar Download Manager)')
        self.completed_downloads = self.load_history()
        self.init_ui()
        self.display_hardware_info()
        self.restore_download_history()

    import os
    import sys
    from PyQt6.QtWidgets import QMessageBox

    def get_or_create_nectarhub_folder(self):
        try:
            if sys.platform.startswith("win"):
                # Windows: Use Program Files
                program_files = os.environ.get('ProgramFiles', 'C:\\Program Files')
                nectarhub_path = os.path.join(program_files, 'NectarHub')

                # Check admin privileges on Windows
                import ctypes
                try:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin()
                except Exception:
                    is_admin = False

                if not os.path.exists(nectarhub_path):
                    if is_admin:
                        os.makedirs(nectarhub_path, exist_ok=True)
                    else:
                        QMessageBox.warning(self, 'Admin Required',
                                            "Administrator rights are required to create 'NectarHub' in Program Files.")
                        return None

            else:
                # Linux / macOS: Use home directory
                home_dir = os.path.expanduser("~")
                nectarhub_path = os.path.join(home_dir, '.NectarHub')  # hidden folder
                os.makedirs(nectarhub_path, exist_ok=True)

            return nectarhub_path

        except Exception as e:
            msg = QMessageBox(self)
            msg.setWindowTitle("❌ Error")
            msg.setText(f"Failed to create/access 'NectarHub':\n{e}")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #0b0b0b;
                    border: 1px solid #330000;
                    border-radius: 12px;
                }
                QMessageBox QLabel {
                    color: #ff5555;
                    font-size: 15px;
                    padding: 8px;
                    font-weight: 500;
                }
                QMessageBox QPushButton {
                    background-color: #1a1a1a;
                    color: #ff5555;
                    border: 1px solid #550000;
                    border-radius: 8px;
                    padding: 6px 16px;
                    font-weight: 600;
                }
                QMessageBox QPushButton:hover {
                    background-color: #220000;
                    border: 1px solid #770000;
                }
                QMessageBox QPushButton:pressed {
                    background-color: #330000;
                }
            """)
            msg.exec()
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
        self.search_input.setStyleSheet('background-color: #000000; color: white; padding: 12px 20px; border-radius: 5px; font-size: 14px;')
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
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: transparent;
                border: 1px solid transparent;
                border-radius: 4px;
                text-align: center;
                color: #444444;
                font-weight: bold;
            }

            QProgressBar::chunk {
                background-color: #ffffff;
                border-radius: 4px;
            }
            """)
        self.progress_bar.hide()
        main_layout.addWidget(self.progress_bar)
        self.downloads_btn = QPushButton('Downloads')
        self.downloads_btn.clicked.connect(lambda: self.downloads_window.show())
        self.downloads_btn.setStyleSheet(' QPushButton { padding: 12px; background-color: #000000; color: white; border-radius: 5px;} QPushButton:hover { background-color: #ffffff; color: #000000;}')
        main_layout.addWidget(self.downloads_btn)
        self.status_label = QLabel('Note only select repositories that end in GGUF.')
        self.status_label.setStyleSheet('font-size: 14px; color: #ffffff;')
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
            # Styled warning message box
            warning = QMessageBox(self)
            warning.setWindowTitle('Invalid Search')
            warning.setText('Please enter a search query.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok)

            # Apply custom styling
            warning.setStyleSheet("""
                QMessageBox {
                    background-color: #000000;
                    border-radius: 10px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton {
                    background-color: #000000;
                    color: white;
                    border-radius: 5px;
                    padding: 6px 12px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #ffffff;
                    color: black;
                }
                QPushButton:pressed {
                    background-color: #000000;
                }
            """)
            warning.exec()
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
        
        # Styled critical message box
        critical = QMessageBox(self)
        critical.setWindowTitle('Search Failed')
        critical.setText(error)
        critical.setIcon(QMessageBox.Icon.Critical)
        critical.setStandardButtons(QMessageBox.StandardButton.Ok)

        # Apply custom dark-themed styling
        critical.setStyleSheet("""
                QMessageBox {
                    background-color: #000000;
                    border-radius: 10px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton {
                    background-color: #000000;
                    color: white;
                    border-radius: 5px;
                    padding: 6px 12px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #ffffff;
                    color: black;
                }
                QPushButton:pressed {
                    background-color: #000000;
                }
            """)
        critical.exec()

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
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("❌ Error")
        msg.setText(error)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Optional: custom icon
        # msg.setWindowIcon(QIcon("icons/error.png"))

        # Apply custom stylesheet
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #2b2b2b;
                color: #ff4d4d;
                font-family: 'Segoe UI';
                font-size: 14px;
                border-radius: 12px;
            }
            QLabel {
                color: #ff4d4d;
                font-size: 14px;
                padding: 6px;
            }
            QPushButton {
                background-color: #ff4d4d;
                color: #ffffff;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 6px 16px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #ff6666;
            }
            QPushButton:pressed {
                background-color: #e60000;
            }
        """)

        msg.exec()
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
            msg = QMessageBox(self)
            msg.setWindowTitle("✅ Download Complete")
            msg.setText(f"File saved to:\n{path}")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #0e0e0e;
                    border: 1px solid #333;
                    border-radius: 12px;
                }
                QMessageBox QLabel {
                    color: #e0e0e0;
                    font-size: 15px;
                    padding: 8px;
                    font-weight: 500;
                }
                QMessageBox QPushButton {
                    background-color: #1b1b1b;
                    color: #e0e0e0;
                    border: 1px solid #444;
                    border-radius: 8px;
                    padding: 6px 16px;
                    font-weight: 600;
                }
                QMessageBox QPushButton:hover {
                    background-color: #222;
                    border: 1px solid #666;
                }
                QMessageBox QPushButton:pressed {
                    background-color: #333;
                }
            """)
            msg.exec()
            
            from datetime import datetime

            self.completed_downloads.append({
                'file_name': card.file_name,
                'save_path': card.save_path,
                'timestamp': datetime.now().isoformat()
            })
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
REPO = 'Nectar-X-Studio'
CURRENT_VERSION = 'v1.2'

# ----------------- THREADS -----------------
class ReleaseCheckThread(QThread):
    result_ready = pyqtSignal(object, object)  # latest_version, download_url

    def run(self):
        url = f'https://api.github.com/repos/{OWNER}/{REPO}/releases/latest'
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            latest_version = data.get('tag_name', None)
            if data.get('assets'):
                download_url = data['assets'][0]['browser_download_url']
            else:
                download_url = data.get('html_url', None)
            self.result_ready.emit(latest_version, download_url)
        except Exception as e:
            self.result_ready.emit(None, None)


class DownloadThread(QThread):
    progress_updated = pyqtSignal(int, int)
    download_complete = pyqtSignal(str)
    download_failed = pyqtSignal(str)

    def __init__(self, url, local_filename):
        super().__init__()
        self.url = url
        self.local_filename = local_filename

    def run(self):
        try:
            headers = {}
            downloaded_size = 0
            if os.path.exists(self.local_filename):
                downloaded_size = os.path.getsize(self.local_filename)
                headers['Range'] = f'bytes={downloaded_size}-'

            response = requests.get(self.url, headers=headers, stream=True, timeout=15)
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0)) + downloaded_size

            with open(self.local_filename, 'ab') as f:
                for chunk in response.iter_content(chunk_size=1024*1024):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        self.progress_updated.emit(downloaded_size, total_size)
            self.download_complete.emit(self.local_filename)
        except Exception as e:
            self.download_failed.emit(str(e))

# ----------------- MAIN UI -----------------
class UpdatePrompt(QWidget):
    def __init__(self):
        super().__init__()

        self.latest_version = None
        self.download_url = None
        self.local_filename = None

        # -------- Create layout and widgets ONCE --------
        self.setWindowTitle("Update Checker")
        self.setGeometry(600, 300, 400, 200)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("", self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: transparent;
                border: 1px solid transparent;
                border-radius: 4px;
                text-align: center;
                color: #444444;
                font-weight: bold;
            }

            QProgressBar::chunk {
                background-color: #ffffff;
                border-radius: 4px;
            }
            """)
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.hide()
        self.layout.addWidget(self.progress_bar)

        self.download_button = QPushButton("Download", self)
        self.download_button.setStyleSheet("""
            QPushButton {
                padding: 10px;
                font-size: 14px;
                background-color: #000000;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #ffffff;
                color: black;
            }
        """)
        self.download_button.clicked.connect(self.start_download)
        self.download_button.hide()
        self.layout.addWidget(self.download_button)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.close)
        self.layout.addWidget(self.cancel_button)

        # -------- Initial state --------
        self.set_state("checking")
        self.check_release()

    # -------- State handler --------
    def set_state(self, state):
        self.progress_bar.hide()
        self.download_button.hide()
        self.cancel_button.hide()
        self.label.setText("")

        if state == "checking":
            self.label.setText("Checking for updates...")
        elif state == "up_to_date":
            self.label.setText(f"<div align=\'center\'><span style=\'font-size:18pt; font-weight:600;\'>Software is <span style=\'color:#555000;\'>Up to Date!</span><br>Version: {CURRENT_VERSION}</span></div>")
        elif state == "update_available":
            self.label.setText(f"<div align=\'center\'><span style=\'font-size:18pt; font-weight:600;\'>Software Update <br> New Version <span style=\'color:#555000;\'>{self.latest_version}</span> Available</span></div>")
            self.download_button.show()
        elif state == "downloading":
            self.progress_bar.show()
        elif state == "failed":
            self.label.setText("<div align=\'center\'><span style=\'font-size:18pt; font-weight:600;\'>No Internet Connection</span></div>")

    # -------- Release check --------
    def check_release(self):
        self.release_thread = ReleaseCheckThread()
        self.release_thread.result_ready.connect(self.handle_release_result)
        self.release_thread.start()

    def handle_release_result(self, latest_version, download_url):
        if latest_version is None:
            self.set_state("failed")
            return

        self.latest_version = latest_version
        self.download_url = download_url
        self.local_filename = os.path.basename(urlparse(download_url).path) if download_url else None

        if self.latest_version == CURRENT_VERSION:
            self.set_state("up_to_date")
        else:
            self.set_state("update_available")

    # -------- Download logic --------
    def start_download(self):
        if not self.download_url:
            QMessageBox.warning(self, "Error", "No download URL available")
            return

        self.set_state("downloading")
        self.download_button.setEnabled(False)
        self.download_thread = DownloadThread(self.download_url, self.local_filename)
        self.download_thread.progress_updated.connect(self.update_progress)
        self.download_thread.download_complete.connect(self.download_finished)
        self.download_thread.download_failed.connect(self.download_failed)
        self.download_thread.start()

    def update_progress(self, current, total):
        self.progress_bar.setValue(int(current / total * 100))
        self.label.setText(f"Downloading... {current / 1024 / 1024:.2f} MB / {total / 1024 / 1024:.2f} MB")

    def download_finished(self, filename):
        QMessageBox.information(self, "Download Complete", f"Downloaded to {filename}")
        self.run_installer(filename)

    def download_failed(self, error):
        QMessageBox.critical(self, "Download Failed", error)
        self.download_button.setEnabled(True)

    def run_installer(self, path):
        try:
            subprocess.run([path, "/SILENT"], shell=True)
            QMessageBox.information(self, "Installer", "Installer launched!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.resize(720, 600)
        self.settings = QSettings("Zashirion", "Nectar_File")
        self.combo_boxes = {}
        self.setStyleSheet(self.get_stylesheet())
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        container_layout.setSpacing(20)

        # --- General Settings ---
        general_group = QGroupBox("General")
        general_layout = QVBoxLayout()
        for label, options in [
            ("Theme", ["Dark", "Light", "System"]),
            ("Device", self.get_available_devices())
        ]:
            general_layout.addLayout(self.create_setting(label, options))
        general_group.setLayout(general_layout)
        container_layout.addWidget(general_group)

        # --- System Info ---
        sys_group = QGroupBox("System")
        sys_layout = QVBoxLayout()
        sys_layout.addWidget(self.create_system_info_widget())
        sys_group.setLayout(sys_layout)
        container_layout.addWidget(sys_group)

        # --- License Info ---
        license_group = QGroupBox("License")
        license_layout = QVBoxLayout()
        license_layout.addWidget(self.create_license_widget())
        license_group.setLayout(license_layout)
        container_layout.addWidget(license_group)

        # --- Model & LocalDocs ---
        container_layout.addWidget(self.create_group("Model", [("Engine", ["Zashirion K47B-LS5"])]))
        container_layout.addWidget(self.create_group("LocalDocs", [("LocalDocs Enabled", ["True", "False"])]))

        # --- Buttons ---
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        apply_btn = QPushButton("Apply")
        reset_btn = QPushButton("Reset")
        apply_btn.clicked.connect(self.save_settings)
        reset_btn.clicked.connect(self.reset_settings)
        button_layout.addWidget(apply_btn)
        button_layout.addWidget(reset_btn)
        container_layout.addLayout(button_layout)

        scroll_area.setWidget(container)
        main_layout.addWidget(scroll_area)

    # --------------------- Core UI Components --------------------- #
    def create_setting(self, label_text, options):
        layout = QHBoxLayout()
        layout.setSpacing(15)

        key = label_text.lower().replace(" ", "_")
        label = QLabel(label_text)
        label.setFixedWidth(150)

        combo = QComboBox()
        combo.addItems(options)
        combo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        saved_value = self.settings.value(key)
        if saved_value in options:
            combo.setCurrentText(saved_value)
        self.combo_boxes[key] = combo

        layout.addWidget(label)
        layout.addWidget(combo)
        return layout

    def create_group(self, name, items):
        group = QGroupBox(name)
        layout = QVBoxLayout()
        for label, options in items:
            layout.addLayout(self.create_setting(label, options))
        group.setLayout(layout)
        return group

    def create_system_info_widget(self):
        info_layout = QVBoxLayout()
        info_layout.setSpacing(5)
        info = {
            "OS": platform.system(),
            "Architecture": platform.machine(),
            "Processor": get_cpu_info().get("brand_raw", "Unknown"),
            "Physical Cores": psutil.cpu_count(logical=False),
            "Total Cores": psutil.cpu_count(logical=True),
            "RAM": f"{round(psutil.virtual_memory().total / 1073741824, 2)} GB"
        }
        for k, v in info.items():
            lbl = QLabel(f"<b>{k}:</b> {v}")
            lbl.setStyleSheet("padding: 2px;")
            info_layout.addWidget(lbl)
        container = QWidget()
        container.setLayout(info_layout)
        return container

    def create_license_widget(self):
        info_layout = QVBoxLayout()
        info_layout.setSpacing(5)
        license_info = {
            "SOFTWARE OWNER": "Zashirion Inc",
            "LICENSE KEY": "CIRB-5002-NGWG-4132",
            "DEVELOPER": "Samuel Ikenna Great",
            "CONTACT": "Nategreat318@gmail.com"
        }
        for k, v in license_info.items():
            lbl = QLabel(f"<b>{k}:</b> {v}")
            lbl.setStyleSheet("padding: 2px;")
            info_layout.addWidget(lbl)
        container = QWidget()
        container.setLayout(info_layout)
        return container

    # --------------------- Device Detection --------------------- #
    def get_available_devices(self):
        devices = ["CPU"]
        try:
            import GPUtil
            if GPUtil.getGPUs():
                devices.append("GPU")
        except Exception:
            try:
                import torch
                if torch.cuda.is_available():
                    devices.append("GPU")
            except ImportError:
                pass
        return devices

    # --------------------- Settings Actions --------------------- #
    def save_settings(self):
        for key, combo in self.combo_boxes.items():
            self.settings.setValue(key, combo.currentText())
        self.apply_selected_settings()

        # Create a styled QMessageBox
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Settings")
        msg_box.setText("Settings saved.")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        # Apply custom stylesheet
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #000000;
                color: #ffffff;
                font-family: Segoe UI, sans-serif;
                font-size: 13px;
                border-radius: 10px;
            }
            QMessageBox QLabel {
                color: #ffffff;
            }
            QMessageBox QPushButton {
                background-color: #2c2c2c;
                color: #ffffff;
                border: 1px solid #444;
                border-radius: 6px;
                padding: 6px 12px;
                min-width: 80px;
            }
            QMessageBox QPushButton:hover {
                background-color: #505050;
            }
        """)

        msg_box.exec()

    def apply_selected_settings(self):
        theme = self.combo_boxes.get("theme").currentText().lower()
        apply_theme(theme)
        set_user_theme(theme)

    def reset_settings(self):
        self.settings.clear()
        for combo in self.combo_boxes.values():
            combo.setCurrentIndex(0)
        QMessageBox.information(self, "Settings", "Settings reset to defaults.")

    # --------------------- Modern Styles --------------------- #
    def get_stylesheet(self):
        return """
        QWidget {
            background-color: transparent;
            color: #ffffff;
            font-family: Segoe UI, sans-serif;
            font-size: 13px;
        }
        QGroupBox {
            border: 1px solid #000000;
            border-radius: 10px;
            margin-top: 10px;
            padding: 10px;
        }
        QGroupBox:title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            font-weight: bold;
            font-size: 15px;
            color: #ffffff;
        }
        QPushButton {
            background-color: #000000;
            color: #fff;
            border: none;
            border-radius: 8px;
            padding: 10px 18px;
        }
        QPushButton:hover {
            background-color: #fff;
            color: #000000;
        }
        QComboBox {
            background-color: #000000;
            color: #ffffff;
            border: 1px solid None;
            border-radius: 8px;
            padding: 6px 12px;
        }
        QComboBox:hover {
            border: 1px solid #ffffff;
        }
        QComboBox QAbstractItemView {
            background-color: #000000;
            color: #ffffff;
            selection-background-color: transparent;
            padding: 5px;
        }
        QComboBox::drop-down {
            border: none;
        }
        QComboBox::down-arrow {
            image: url("background/down-arrow.svg");
            width: 12px;
            height: 12px;
        }
        QLabel {
            color: #ffffff;
        }
        """

def set_light_theme2(self):
    """Set dark theme for the application."""  # inserted
    light_stylesheet = """
        QWidget {
            background-color: transparent;
            color: #ffffff;
        }

        QTabWidget {
            border-radius: 12px;
            background-color: transparent;
        }

        QLineEdit, QTextEdit, QPlainTextEdit {
            background-color: transparent;
            color: #ffffff;
            border: none;
            padding: 5px;
            border-radius: 10px;
        }

        QPushButton {
            background-color: #000000;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #f50000;
        }

        QPushButton:pressed {
            background-color: #ffffff;
        }

        QListWidget {
            background-color: transparent;
            color: #d3d3d3;
            border: 1px solid #444444;
        }

        QGroupBox {
            border: 1px solid #444444;
            background-color: transparent;
            color: #d3d3d3;
            margin: 5px;
            padding: 10px;
        }

        QFormLayout {
            background-color: transparent;
            color: #d3d3d3;
        }

        QPlainTextEdit {
            background-color: transparent;
        }
        """

    self.setStyleSheet(light_stylesheet)

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
        self.text_label.setStyleSheet("""
            QLabel {
                color: #f0f0f0;
            }
            """)

        layout.addWidget(self.text_label)
        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background-color: #1b1b1b;
                border: 2px solid #1b1b1b;
                border-radius: 8px;
            }
            """)

    def show_tooltip(self, position):
        self.move(position)
        self.show()


HISTORY_FILE = 'search_history.json'

def find_icon(icon_name):
    """Attempts to find the icon in and out of the script\'s directory."""  # inserted
    script_dir = os.path.dirname(os.path.realpath(__file__))
    possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    else:  # inserted
        return None

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

class Broadcast(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('🧠 AlphaLLM Broadcast Engine')
        self.resize(700, 600)

        # Local TCP server
        self.server_running = False
        self.server_socket = None
        self.broadcast_port = 8012
        self.broadcast_base_ip = '127.0.0.1'

        # FastAPI server
        self.fastapi_app = FastAPI()
        self.fastapi_host = '0.0.0.0'
        self.fastapi_port = 8000
        self.fastapi_running = False
        self.websockets = []

        self.init_ui()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet(self.futuristic_style())
        self.animate_window()
        self.setup_fastapi_routes()

    # --------------------------- UI ---------------------------
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Target display
        self.target_display = QLabel(f'📡 Local Engine: {self.broadcast_base_ip}:{self.broadcast_port}')
        layout.addWidget(self.target_display)

        # FastAPI host/port
        fastapi_layout = QHBoxLayout()
        self.host_input = QLineEdit(self.fastapi_host)
        self.host_input.setPlaceholderText('FastAPI Host')
        self.port_input = QLineEdit(str(self.fastapi_port))
        self.port_input.setPlaceholderText('FastAPI Port')
        self.fastapi_button = QPushButton("Start FastAPI")
        self.fastapi_button.clicked.connect(self.toggle_fastapi)
        fastapi_layout.addWidget(self.host_input)
        fastapi_layout.addWidget(self.port_input)
        fastapi_layout.addWidget(self.fastapi_button)
        layout.addLayout(fastapi_layout)

        # Token for authentication
        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Access Token (Optional)")
        layout.addWidget(self.token_input)

        # Broadcast engine toggle
        self.toggle_button = QPushButton('Start Local Engine')
        self.toggle_button.clicked.connect(self.toggle_engine)
        layout.addWidget(self.toggle_button)

        # FastAPI dynamic route configuration
        self.api_config_layout = QVBoxLayout()
        self.api_config_layout.addWidget(QLabel("📡 FastAPI Route Configuration"))
        route_layout = QHBoxLayout()
        self.route_input = QLineEdit("/predict")
        self.route_input.setPlaceholderText("Route Path")
        self.method_input = QComboBox()
        self.method_input.addItems(["GET", "POST", "WebSocket"])

        self.add_route_btn = QPushButton("Add Route")
        self.add_route_btn.clicked.connect(self.add_fastapi_route)
        self.viewer_btn = QPushButton("View API")
        self.viewer_btn.clicked.connect(self.Api_view)
        route_layout.addWidget(self.route_input)
        route_layout.addWidget(self.method_input)
        route_layout.addWidget(self.add_route_btn)
        route_layout.addWidget(self.viewer_btn)
        self.api_config_layout.addLayout(route_layout)
        layout.addLayout(self.api_config_layout)

        # Packet log
        layout.addWidget(QLabel('📦 Packet Log:'))
        self.packet_log = QTextEdit()
        self.packet_log.setReadOnly(True)
        layout.addWidget(self.packet_log)

        self.setLayout(layout)

    def Api_view(self):
        if viewer is not None:
            viewer.show()

    # --------------------------- Local TCP Engine ---------------------------
    def toggle_engine(self):
        if not self.server_running:
            self.server_running = True
            threading.Thread(target=self.start_broadcast_server, daemon=True).start()
            self.toggle_button.setText('Stop Local Engine')
            self.log_packet('[Engine] Local broadcast server started.')
        else:
            self.server_running = False
            self.stop_broadcast_server()
            self.toggle_button.setText('Start Local Engine')
            self.log_packet('[Engine] Local broadcast server stopped.')

    def start_broadcast_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.broadcast_base_ip, self.broadcast_port))
        self.server_socket.listen(5)
        self.log_packet(f'[Relay] Listening on {self.broadcast_base_ip}:{self.broadcast_port}...')
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
                # Broadcast to FastAPI WebSocket clients
                if self.fastapi_running:
                    asyncio.run(self.broadcast_fastapi(alpha_response))
            except socket.timeout:
                continue
            except Exception as e:
                self.log_packet(f'[Error] Server exception: {e}')
                break
        self.log_packet('[Server] Listener stopped.')

    def stop_broadcast_server(self):
        if self.server_socket:
            try:
                self.server_socket.close()
                self.server_socket = None
            except Exception as e:
                self.log_packet(f'[Error] Could not close socket: {e}')

    # --------------------------- FastAPI ---------------------------
    def toggle_fastapi(self):
        if not self.fastapi_running:
            self.fastapi_host = self.host_input.text()
            self.fastapi_port = int(self.port_input.text())
            threading.Thread(target=self.run_fastapi, daemon=True).start()
            self.fastapi_running = True
            self.fastapi_button.setText('Stop FastAPI')
            self.log_packet(f'[FastAPI] Started at {self.fastapi_host}:{self.fastapi_port}')
        else:
            self.fastapi_running = False
            self.fastapi_button.setText('Start FastAPI')
            self.log_packet('[FastAPI] Stopped (restart required).')

    def setup_fastapi_routes(self):
        self.fastapi_app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"]
        )

    def add_fastapi_route(self):
        path = self.route_input.text()
        method = self.method_input.currentText()
        token = self.token_input.text()

        if not path.startswith("/"):
            path = "/" + path

        if method in ["GET", "POST"]:
            async def api_endpoint(request: Request):
                # Optional token authentication
                if token:
                    auth = request.headers.get("Authorization")
                    if auth != f"Bearer {token}":
                        return JSONResponse(status_code=401, content={"error": "Unauthorized"})

                if method == "GET":
                    data = request.query_params.get("data", "")
                else:
                    data_json = await request.json()
                    data = data_json.get("data", "")
                response = send_to_AlphaLLM(data)
                # Broadcast to WebSocket clients
                if self.fastapi_running:
                    await self.broadcast_fastapi(response)
                return {"response": response}

            self.fastapi_app.add_api_route(path, api_endpoint, methods=[method])
            self.log_packet(f"[FastAPI] Added {method} route: {path}")

        elif method == "WebSocket":
            async def websocket_endpoint(websocket: WebSocket):
                await websocket.accept()
                self.websockets.append(websocket)
                self.log_packet(f'[FastAPI] WS Client connected: {websocket.client}')
                try:
                    while True:
                        data = await websocket.receive_text()
                        response = send_to_AlphaLLM(data)
                        await websocket.send_text(response)
                        self.log_packet(f'[FastAPI] WS Received: {data}, Sent: {response}')
                except Exception as e:
                    self.log_packet(f'[FastAPI] WS error: {e}')
                finally:
                    self.websockets.remove(websocket)
                    self.log_packet(f'[FastAPI] WS Client disconnected: {websocket.client}')

            self.fastapi_app.add_api_websocket_route(path, websocket_endpoint)
            self.log_packet(f"[FastAPI] Added WebSocket route: {path}")

    async def broadcast_fastapi(self, message):
        for ws in self.websockets:
            try:
                await ws.send_text(message)
            except Exception as e:
                self.log_packet(f'[FastAPI] Broadcast failed: {e}')

    import uvicorn

    def run_fastapi(self):
        log_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(levelprefix)s %(message)s",
                    "use_colors": False  # <-- disable colors here
                },
            },
            "handlers": {
                "default": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": sys.stdout,
                },
            },
            "loggers": {
                "uvicorn": {"handlers": ["default"], "level": "INFO"},
                "uvicorn.error": {"level": "INFO"},
                "uvicorn.access": {"handlers": ["default"], "level": "INFO"},
            },
        }

        uvicorn.run(
            self.fastapi_app,
            host=self.fastapi_host,
            port=self.fastapi_port,
            log_config=log_config,
        )

    # --------------------------- Logging & UI ---------------------------
    def log_packet(self, message):
        self.packet_log.append(f'{message}')

    def animate_window(self):
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        geo = self.geometry()
        self.animation.setStartValue(QRect(geo.x(), geo.y() + 30, geo.width(), geo.height()))
        self.animation.setEndValue(geo)
        self.animation.start()

    def futuristic_style(self):
        return '''
            QWidget {
                background-color: rgba(18, 18, 18, 200);
                border-radius: 20px;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
            }
            QLineEdit, QTextEdit {
                background-color: transparent;
                color: #ffffff;
                border: 1px solid #ffffff;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton {
                background-color: #ffffff;
                border: none;
                border-radius: 10px;
                padding: 10px;
                color: #000000;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #000000;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #1e1e1e;
            }
            QTextEdit {
                font-family: Consolas, monospace;
                font-size: 13px;
            }
            QLabel {
                background-color: transparent;
                color: #ffffff;
            }
        '''

class CodeViewer(QWidget):
    def __init__(self, code_blocks, parent=None):
        super().__init__(parent)
        self.setWindowTitle('API VIEW')
        self.setMinimumSize(700, 500)
        apply_theme(get_user_theme())
        self.setStyleSheet("background-color: #000000; color: #e0e0e0;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea { border: none; }
            QScrollBar:vertical {
                background: #1e1e1e;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #ffffff;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line, QScrollBar::sub-line { height: 0; }
        """)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(15)

        for block in code_blocks:
            title = block.get("title", "Python Code")
            code_text = block.get("code", "")

            block_frame = QFrame()
            block_frame.setFrameShape(QFrame.Shape.StyledPanel)
            block_frame.setStyleSheet("""
                QFrame {
                    background-color: transparent;
                    border-radius: 10px;
                    padding: 12px;
                    border: 1px solid #ffffff;
                }
            """)
            block_layout = QVBoxLayout(block_frame)
            block_layout.setSpacing(8)

            # Title label
            label = QLabel(title)
            label.setStyleSheet('color: #ffffff; font-weight: 600; font-size: 14px;')
            block_layout.addWidget(label)

            # Code editor
            code_edit = QTextEdit()
            code_edit.setReadOnly(True)
            code_edit.setFont(QFont('Courier New', 11))
            code_edit.setText(code_text)
            code_edit.setFixedHeight(150)
            code_edit.setStyleSheet('''
                QTextEdit {
                    background-color: transparent;
                    color: #ffffff;
                    border: 1px solid #ffffff;
                    border-radius: 6px;
                    padding: 10px;
                    font-family: Courier, monospace;
                    font-size: 18px;
                    selection-background-color: #555555;
                }
            ''')
            block_layout.addWidget(code_edit)

            # Buttons: Copy & Expand
            button_layout = QHBoxLayout()
            button_layout.addStretch()

            copy_button = QPushButton('Copy Code')
            copy_button.setCursor(Qt.CursorShape.PointingHandCursor)
            copy_button.setStyleSheet("""
                QPushButton {
                    background-color: #000000;
                    color: #ffffff;
                    font-weight: bold;
                    padding: 5px 12px;
                    border-radius: 6px;
                }
                QPushButton:hover { background-color: #ffffff; color: #000000; }
                QPushButton:pressed { background-color: #777777; }
            """)
            copy_button.clicked.connect(lambda _, ce=code_edit: self.copy_code(ce))
            button_layout.addWidget(copy_button)

            expand_button = QPushButton('Expand')
            expand_button.setCursor(Qt.CursorShape.PointingHandCursor)
            expand_button.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    color: #000000;
                    font-weight: bold;
                    padding: 5px 12px;
                    border-radius: 6px;
                }
                QPushButton:hover { background-color: #000000; color: #ffffff; }
                QPushButton:pressed { background-color: #777777; }
            """)
            expand_button.clicked.connect(lambda _, text=code_text, title=title: self.expand_code(text, title))
            button_layout.addWidget(expand_button)

            block_layout.addLayout(button_layout)
            scroll_layout.addWidget(block_frame)

        scroll_layout.addStretch()
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

    def copy_code(self, code_edit):
        QGuiApplication.clipboard().setText(code_edit.toPlainText())

    def expand_code(self, code_text, title):
        dialog = QDialog(self)
        dialog.setWindowTitle(f"{title} - Full Code")
        dialog.setMinimumSize(800, 600)
        dialog.setStyleSheet("background-color: #121212; color: #e0e0e0;")

        dlg_layout = QVBoxLayout(dialog)
        code_area = QTextEdit()
        code_area.setReadOnly(True)
        code_area.setFont(QFont('Courier New', 11))
        code_area.setText(code_text)
        code_area.setStyleSheet('''
            QTextEdit {
                background-color: #121212;
                color: #e0e0e0;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 10px;
                font-family: Courier, monospace;
                font-size: 12px;
                selection-background-color: #555555;
            }
        ''')
        dlg_layout.addWidget(code_area)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        dlg_layout.addWidget(buttons)

        dialog.exec()

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
            f'display:inline-block; text-align:center; width:100%;">Nectar-X</span>'
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

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel,
    QFrame, QToolButton, QTabWidget, QFileDialog
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEngineDownloadRequest
from PyQt6.QtCore import Qt, QTimer, QUrl, QSettings
from PyQt6.QtGui import QIcon
import urllib.request
import os

class PersistentWebBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persistent Web Browser")
        self.resize(1400, 800)
        self.setStyleSheet("background-color: #000000; color: white;")

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # --- Persistent Profile ---
        self.profile = QWebEngineProfile.defaultProfile()
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)
        self.profile.setPersistentStoragePath(os.path.join(os.getcwd(), "persistent_profile"))
        self.profile.downloadRequested.connect(self.handle_download)

        # Load settings
        self.settings = QSettings("Zashirion", "PersistentBrowser")

        # --- Main content ---
        self.main_frame = QFrame()
        main_layout = QVBoxLayout(self.main_frame)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # --- Navigation bar ---
        nav_bar = QFrame()
        nav_bar.setFixedHeight(60)
        nav_bar.setStyleSheet("background-color: transparent;")
        nav_layout = QHBoxLayout(nav_bar)
        nav_layout.setContentsMargins(5, 5, 5, 5)
        import qtawesome as qta

        self.back_btn = QPushButton()
        self.back_btn.setIcon(qta.icon("fa5s.arrow-left", color="white"))
        self.back_btn.setToolTip("Back")

        # Forward button
        self.forward_btn = QPushButton()
        self.forward_btn.setIcon(qta.icon("fa5s.arrow-right", color="white"))
        self.forward_btn.setToolTip("Forward")

        # Reload button
        self.reload_btn = QPushButton()
        self.reload_btn.setIcon(qta.icon("fa5s.sync", color="white"))
        self.reload_btn.setToolTip("Reload")

        # Home button
        self.home_btn = QPushButton()
        self.home_btn.setIcon(qta.icon("fa5s.home", color="white"))
        self.home_btn.setToolTip("Home")

        # New Tab button
        self.new_tab_btn = QPushButton()
        self.new_tab_btn.setIcon(qta.icon("fa5s.plus", color="white"))
        self.new_tab_btn.setToolTip("New Tab")

        for btn in [self.back_btn, self.forward_btn, self.reload_btn, self.home_btn, self.new_tab_btn]:
            btn.setFixedSize(40, 40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #000000;
                    color: white;
                    border-radius: 5px;
                    padding: 5px 10px;
                }
                QPushButton:hover {
                    background-color: #ffffff;
                    color: black;
                }
            """)
            nav_layout.addWidget(btn)

        self.search_input = QLineEdit()
        self.search_input.setFixedHeight(40)
        self.search_input.setPlaceholderText("Search Qwant...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #2b2b2b;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        nav_layout.addWidget(self.search_input)
        main_layout.addWidget(nav_bar)

        # --- Tabs ---
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_nav_buttons)
        main_layout.addWidget(self.tabs)
        self.layout.addWidget(self.main_frame)

        # --- Connections ---
        self.back_btn.clicked.connect(self.go_back)
        self.forward_btn.clicked.connect(self.go_forward)
        self.reload_btn.clicked.connect(self.reload_page)
        self.home_btn.clicked.connect(self.go_home)
        self.new_tab_btn.clicked.connect(lambda: self.add_new_tab())
        self.search_input.returnPressed.connect(self.do_search)

        # Start with Qwant
        self.add_new_tab("https://www.qwant.com/", "Qwant")

    # --- Tabs ---
    def add_new_tab(self, url="https://www.qwant.com/", label="New Tab"):
        web_view = QWebEngineView()
        # Use default QWebEngineView page. The global profile was configured
        # above (persistent cookies/storage) and should be used by the engine.
        # Some PyQt6 builds don't expose QWebEnginePage to Python, so avoid
        # creating pages explicitly to maintain compatibility.
        pass
        if self.check_internet():
            web_view.load(QUrl(url))
        else:
            web_view.setHtml("<h2 style='color:white;text-align:center;margin-top:20px;'>No Internet Connection</h2>")
        i = self.tabs.addTab(web_view, label)
        self.tabs.setCurrentIndex(i)
        web_view.titleChanged.connect(lambda title, tab=web_view: self.update_tab_title(tab, title))
        web_view.loadFinished.connect(lambda ok, view=web_view: self.inject_user_info(view))

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def update_tab_title(self, web_view, title):
        index = self.tabs.indexOf(web_view)
        if index != -1:
            self.tabs.setTabText(index, title)

    # --- Navigation buttons update ---
    def update_nav_buttons(self, index=None):
        view = self.current_web_view()
        if view:
            self.back_btn.setEnabled(view.history().canGoBack())
            self.forward_btn.setEnabled(view.history().canGoForward())

    # --- Navigation ---
    def current_web_view(self):
        return self.tabs.currentWidget()

    def go_back(self):
        view = self.current_web_view()
        if view:
            view.back()

    def go_forward(self):
        view = self.current_web_view()
        if view:
            view.forward()

    def reload_page(self):
        view = self.current_web_view()
        if view and self.check_internet():
            view.reload()
        elif view:
            view.setHtml("<h2 style='color:white;text-align:center;margin-top:20px;'>No Internet Connection</h2>")

    def go_home(self):
        view = self.current_web_view()
        if view:
            self.load_url("https://www.qwant.com/", view)

    def do_search(self, query=None):
        if query is None:
            query = self.search_input.text().strip()
        if not query:
            return
        url = f"https://www.qwant.com/?q={query}"
        view = self.current_web_view()
        if view:
            self.load_url(url, view)

    def load_url(self, url, view):
        if self.check_internet():
            view.load(QUrl(url))
        else:
            view.setHtml("<h2 style='color:white;text-align:center;margin-top:20px;'>No Internet Connection</h2>")

    # --- Internet check ---
    def check_internet(self, url='http://www.google.com', timeout=3):
        try:
            urllib.request.urlopen(url, timeout=timeout)
            return True
        except:
            return False

    # --- Google Account ---
    def update_account_info(self):
        try:
            main_window = self.window()
            if hasattr(main_window, "get_google_account_info"):
                account_info = main_window.get_google_account_info()
                if account_info:
                    name = account_info.get("name", "Unknown")
                    email = account_info.get("email", "")
                    self.account_label.setText(f"{name}")
                    self.settings.setValue("user_name", name)
                    self.settings.setValue("user_email", email)
                else:
                    self.account_label.setText("Not logged in")
            else:
                self.account_label.setText("No account info")
        except Exception as e:
            print("Error retrieving account info:", e)
            self.account_label.setText("Not logged in")

    def inject_user_info(self, web_view):
        name = self.settings.value("user_name", "")
        email = self.settings.value("user_email", "")
        if name and email:
            script = f"""
                window.__google_user__ = {{
                    name: "{name}",
                    email: "{email}"
                }};
                console.log("Injected Google account:", window.__google_user__);
            """
            web_view.page().runJavaScript(script)

    # --- File download support ---
    def handle_download(self, download):
        path, _ = QFileDialog.getSaveFileName(self, "Save File As", download.path())
        if path:
            download.setPath(path)
            download.accept()

# ------------------- THREAD FOR IMAGE GENERATION -------------------
class ImageGenerator(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(object)
    error = pyqtSignal(str)
    eta_signal = pyqtSignal(float)

    def __init__(self, pipe, prompt, steps, guidance, width, height):
        super().__init__()
        self.pipe = pipe
        self.prompt = prompt
        self.steps = steps
        self.guidance = guidance
        self.width = width
        self.height = height
        self.stop_flag = False
        self.start_time = None

    def run(self):
        try:
            self.start_time = time.time()

            def callback(step, timestep, latents):
                if self.stop_flag:
                    raise KeyboardInterrupt
                progress_percent = int((step + 1) / self.steps * 100)
                elapsed = time.time() - self.start_time
                avg_step_time = elapsed / (step + 1)
                eta = max((self.steps - (step + 1)) * avg_step_time, 0)
                self.progress.emit(progress_percent)
                self.eta_signal.emit(eta)

            negative_prompt = (
                "low quality, blurry, bad anatomy, bad hands, deformed, cartoon, sketch, "
                "text, logo, watermark, signature, poorly drawn, overexposed, underexposed, "
                "grain, noise, jpeg artifacts, pixelated, distorted, unrealistic, "
                "extra limbs, mutated, cropped, bad proportions, ugly, glitch, "
                "bad lighting, unnatural colors, oversaturated, under-saturated, "
                "tiling, poorly rendered, low-res, oversharpened, over-processed"
            )

            image = self.pipe(
                self.prompt,
                negative_prompt=negative_prompt,
                height=self.height,
                width=self.width,
                num_inference_steps=self.steps,
                guidance_scale=self.guidance,
                callback=callback,
                callback_steps=1,
                output_type="pil"
            ).images[0]

            self.finished.emit(image)

        except KeyboardInterrupt:
            self.error.emit("⛔ Generation stopped by user.")
        except Exception as e:
            self.error.emit(str(e))

# ------------------- MAIN APP -------------------
class StableDiffusionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stable Diffusion – Professional Edition")
        self.setGeometry(100, 100, 900, 950)

        self.pipe = None
        self.thread = None
        self.current_image = None  # store full-resolution image

        self.init_ui()
        os.makedirs("outputs", exist_ok=True)  # folder to save images

    def init_ui(self):
        layout = QVBoxLayout()

        # --- Model selection ---
        model_layout = QHBoxLayout()
        self.model_combo = QComboBox()
        self.model_combo.addItems([
            "Select Model...",
            "stable-diffusion-v1-5",
            "dreamlike-photoreal-2.0"
        ])

        # Styling for dark modern theme
        self.model_combo.setStyleSheet("""
            QComboBox {
                background-color: #000000;
                color: white;
                padding: 8px 12px;
                border: 2px solid None;
                border-radius: 8px;
                font-size: 14px;
                min-width: 180px;
            }
            QComboBox:hover {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid None;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left: 1px solid #555;
                border-radius: 0px 8px 8px 0px;
                background-color: #000000;
            }
            QComboBox::down-arrow {
                image: url("background/down-arrow.svg");  /* optional custom arrow icon */
                width: 14px;
                height: 14px;
            }
            QComboBox QAbstractItemView {
                background-color: #000000;
                color: white;
                selection-background-color: #4CAF50;
                selection-color: black;
                border-radius: 8px;
                padding: 5px;
                outline: 0;
            }
        """)

        self.model_path_input = QLineEdit()
        self.model_path_input.setPlaceholderText("Or browse custom model path...")
        self.model_path_input.setReadOnly(True)
        self.model_path_input.setStyleSheet("background-color: #000000;")
        self.model_path_input.setFixedHeight(38)

        self.browse_button = QPushButton("Browse")
        self.browse_button.setFixedHeight(38)
        self.browse_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ffffff;
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
        """)

        self.device_combo = QComboBox()
        self.device_combo.addItems(["CPU", "GPU"])

        # Styling for dark modern theme
        self.device_combo.setStyleSheet("""
            QComboBox {
                background-color: #000000;
                color: white;
                padding: 8px 12px;
                border: 2px solid None;
                border-radius: 8px;
                font-size: 14px;
                min-width: 100px;
            }
            QComboBox:hover {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid None;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left: 1px solid #555;
                border-radius: 0px 8px 8px 0px;
                background-color: #000000;
            }
            QComboBox::down-arrow {
                image: url("background/down-arrow.svg");   /* optional custom arrow icon */
                width: 14px;
                height: 14px;
            }
            QComboBox QAbstractItemView {
                background-color: #000000;
                color: white;
                selection-background-color: #4CAF50;
                selection-color: black;
                border-radius: 8px;
                padding: 5px;
                outline: 0;
            }
        """)

        self.load_model_button = QPushButton("Load Model")
        self.load_model_button.setFixedHeight(38)
        self.load_model_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ffffff;
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
        """)
        model_layout.addWidget(self.model_combo)
        model_layout.addWidget(self.model_path_input)
        model_layout.addWidget(self.browse_button)
        device_label = QLabel("Device:")
        device_label.setStyleSheet("""
            QLabel {
                background-color: #ffffff;      /* Dark background */
                color: #000000;               /* White text */
                font-size: 14px;              /* Medium font size */
                padding: 4px 0;               /* Small vertical padding */
            }
        """)
        device_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        # Add to layout
        model_layout.addWidget(device_label)
        model_layout.addWidget(self.device_combo)
        model_layout.addWidget(self.load_model_button)
        layout.addLayout(model_layout)

        # --- Settings ---
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setHorizontalSpacing(15)
        form_layout.setVerticalSpacing(10)

        # Steps SpinBox
        self.steps_spin = QSpinBox()
        self.steps_spin.setRange(5, 100)
        self.steps_spin.setValue(30)
        self.steps_spin.setStyleSheet("""
            QLabel {
                    Background-color: #ffffff;
                    color: #000000;
                    font-size: 14px;
                    font-weight: bold;
                    padding: 2px 0;
                }
            QSpinBox {
                background-color: #000000;
                color: white;
                border: 2px solid None;
                border-radius: 8px;
                padding: 5px 10px;
                font-size: 14px;
            }
            QSpinBox:focus {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid None;
            }
            QSpinBox::up-button {
                subcontrol-origin: border;
                subcontrol-position: top right;
                width: 18px;
                background-color: #ffffff;
                border-left: 1px solid #555;
                border-top-right-radius: 6px;
            }
            QSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: bottom right;
                width: 18px;
                background-color: #ffffff;
                border-left: 1px solid #555;
                border-bottom-right-radius: 6px;
            }
            QSpinBox::up-button:hover,
            QSpinBox::down-button:hover {
                background-color: #1e1e1e;        /* Green hover effect */
            }
            QSpinBox::up-arrow, QDoubleSpinBox::down-arrow {
                width: 10px;
                height: 10px;
            }
            
        """)

        # Guidance DoubleSpinBox
        self.guidance_spin = QDoubleSpinBox()
        self.guidance_spin.setRange(1.0, 20.0)
        self.guidance_spin.setSingleStep(0.5)
        self.guidance_spin.setValue(8.5)
        self.guidance_spin.setStyleSheet("""
            QDoubleSpinBox {
                background-color: #000000;        /* Dark background */
                color: #ffffff;                   /* White text */
                border: 2px solid None;           /* Subtle border */
                border-radius: 8px;               /* Rounded corners */
                padding: 5px 10px;                /* Inner padding */
                font-size: 14px;                  /* Readable text */
                min-width: 100px;
            }
            QDoubleSpinBox:hover {
                background-color: #ffffff;        /* Dark background */
                color: #000000; 
                border: 2px solid None;        /* Green hover accent */
            }
            QDoubleSpinBox:focus {
                border: 2px solid None;        /* Focus highlight */
            }
            QDoubleSpinBox::up-button {
                subcontrol-origin: border;
                subcontrol-position: top right;
                width: 18px;
                background-color: #ffffff;
                border-left: 1px solid #555;
                border-top-right-radius: 6px;
            }
            QDoubleSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: bottom right;
                width: 18px;
                background-color: #ffffff;
                border-left: 1px solid #555;
                border-bottom-right-radius: 6px;
            }
            QDoubleSpinBox::up-button:hover,
            QDoubleSpinBox::down-button:hover {
                background-color: #1e1e1e;        /* Green hover effect */
            }
            QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {
                width: 10px;
                height: 10px;
            }
        """)

        # Width SpinBox
        self.width_spin = QSpinBox()
        self.width_spin.setRange(128, 2048)
        self.width_spin.setValue(360)
        self.width_spin.setStyleSheet(self.steps_spin.styleSheet())

        # Height SpinBox
        self.height_spin = QSpinBox()
        self.height_spin.setRange(128, 2048)
        self.height_spin.setValue(360)
        self.height_spin.setStyleSheet(self.steps_spin.styleSheet())

        # Labels styling
        for label_text in ["Steps:", "Guidance:", "Width:", "Height:"]:
            label = QLabel(label_text)
            label.setStyleSheet("""
                QLabel {
                    Background-color: #ffffff;
                    color: #000000;
                    font-size: 14px;
                    font-weight: bold;
                    padding: 2px 0;
                }
            """)

        # Add rows to form layout
        form_layout.addRow(QLabel("Steps:"), self.steps_spin)
        form_layout.addRow(QLabel("Guidance:"), self.guidance_spin)
        form_layout.addRow(QLabel("Width:"), self.width_spin)
        form_layout.addRow(QLabel("Height:"), self.height_spin)

        layout.addLayout(form_layout)

        # --- Prompt input ---
        prompt_layout = QHBoxLayout()
        self.prompt_input = QLineEdit()
        self.prompt_input.setFixedHeight(38)
        self.prompt_input.setPlaceholderText("Describe your image...")
        self.prompt_input.setStyleSheet("""
            QLineEdit {
                background-color: #000000;
                color: white;
                padding: 10px;
                border: 2px solid None;
                border-radius: 8px;
                font-size: 14px;
            }
            QLineEdit:focus {
                background-color: #1e1e1e;
                color: white;
                border: 2px solid None;
            }
        """)
        self.generate_button = QPushButton("Generate Image")
        self.generate_button.setFixedHeight(38)
        self.generate_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ffffff;
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
        """)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setFixedHeight(38)
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ffffff;
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
        """)
        self.save_button = QPushButton("Save Image")
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ffffff;
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
        """)
        self.cancel_button.setEnabled(False)
        self.save_button.setEnabled(False)
        prompt_layout.addWidget(self.prompt_input)
        prompt_layout.addWidget(self.generate_button)
        prompt_layout.addWidget(self.cancel_button)
        prompt_layout.addWidget(self.save_button)
        layout.addLayout(prompt_layout)

        # --- Status and progress ---
        self.status_label = QLabel("   Model not loaded.")
        self.status_label.setFixedHeight(30)
        self.status_label.setStyleSheet("background-color: #ffffff; color: #000000;")
        layout.addWidget(self.status_label)
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: transparent;
                border: 1px solid transparent;
                border-radius: 4px;
                text-align: center;
                color: #444444;
                font-weight: bold;
            }

            QProgressBar::chunk {
                background-color: #1b1b1b;
                border-radius: 4px;
            }
            """)
        layout.addWidget(self.progress_bar)
        self.eta_label = QLabel("ETA: --")
        self.eta_label.setFixedHeight(30)
        self.eta_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.eta_label.setStyleSheet("background-color: #ffffff; color: #000000;")
        layout.addWidget(self.eta_label)

        # --- Image display ---
        self.scroll_area = QScrollArea()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.image_label)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)

        # --- Connections ---
        self.browse_button.clicked.connect(self.browse_model)
        self.load_model_button.clicked.connect(self.load_model)
        self.generate_button.clicked.connect(self.generate_image)
        self.cancel_button.clicked.connect(self.cancel_generation)
        self.save_button.clicked.connect(self.save_image)
        self.model_combo.currentIndexChanged.connect(self.model_selection_changed)

    # ------------------- FUNCTIONS -------------------
    def model_selection_changed(self):
        selected = self.model_combo.currentText()
        if selected != "Select Model...":
            self.model_path_input.setText(selected)

    def browse_model(self):
        path = QFileDialog.getExistingDirectory(self, "Select Model Directory")
        if path:
            self.model_path_input.setText(path)

    def load_model(self):
        path = self.model_path_input.text().strip()
        if not path:
            QMessageBox.warning(self, "Error", "Please select a model path.")
            return

        device = self.device_combo.currentText().lower()
        device_type = "cuda" if device == "gpu" and torch.cuda.is_available() else "cpu"
        self.status_label.setText(f"   Loading model on {device_type.upper()}...")
        QApplication.processEvents()

        try:
            self.pipe = StableDiffusionPipeline.from_pretrained(
                path,
                torch_dtype=torch.float16 if device_type == "cuda" else torch.float32
            )
            self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(self.pipe.scheduler.config)
            self.pipe = self.pipe.to(device_type)
            self.pipe.enable_attention_slicing()
            self.pipe.enable_vae_slicing()
            self.status_label.setText(f"   Model loaded successfully on {device_type.upper()}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            self.status_label.setText("   Failed to load model.")

    def generate_image(self):
        if not self.pipe:
            QMessageBox.warning(self, "Error", "Model is not loaded.")
            return
        prompt = self.prompt_input.text().strip()
        if not prompt:
            QMessageBox.warning(self, "Error", "Please enter a prompt.")
            return

        self.status_label.setText("   Generating image...")
        self.progress_bar.setValue(0)
        self.eta_label.setText("ETA: calculating...")
        self.generate_button.setEnabled(False)
        self.cancel_button.setEnabled(True)
        self.save_button.setEnabled(False)

        steps = self.steps_spin.value()
        guidance = self.guidance_spin.value()
        width = self.width_spin.value()
        height = self.height_spin.value()

        self.thread = ImageGenerator(self.pipe, prompt, steps, guidance, width, height)
        self.thread.progress.connect(self.progress_bar.setValue)
        self.thread.finished.connect(self.display_image)
        self.thread.error.connect(self.show_error)
        self.thread.eta_signal.connect(self.update_eta)
        self.thread.start()

    def cancel_generation(self):
        if self.thread and self.thread.isRunning():
            self.thread.stop_flag = True
            self.cancel_button.setEnabled(False)
            self.status_label.setText("Stopping generation...")

    def display_image(self, image: Image.Image):
        self.current_image = image  # store full-res image
        qt_image = ImageQt(image)
        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(pixmap)
        self.status_label.setText("Image generated successfully!")
        self.progress_bar.setValue(100)
        self.eta_label.setText("ETA: done")
        self.generate_button.setEnabled(True)
        self.cancel_button.setEnabled(False)
        self.save_button.setEnabled(True)

        # Automatically save
        self.save_image(auto=True)

    def save_image(self, auto=False):
        if self.current_image:
            if auto:
                filename = datetime.now().strftime("outputs/image_%Y%m%d_%H%M%S.png")
            else:
                filename, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png)")
                if not filename:
                    return
            self.current_image.save(filename)
            if not auto:
                QMessageBox.information(self, "Saved", f"Image saved to {filename}")

    def update_eta(self, eta):
        self.eta_label.setText(f"ETA: {eta:.1f}s")

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)
        self.status_label.setText("Error generating image.")
        self.progress_bar.setValue(0)
        self.eta_label.setText("ETA: --")
        self.generate_button.setEnabled(True)
        self.cancel_button.setEnabled(False)
        self.save_button.setEnabled(False)

# ----------------------------
# PyQt6 Main Window with Download Handling
# ----------------------------
class Code(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setWindowTitle("JupyterLab Viewer")
        self.setGeometry(100, 100, 1200, 850)

        # --- Central Layout ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # --- Web View ---
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        # --- Enable automatic file download handling ---
        profile = QWebEngineProfile.defaultProfile()
        profile.downloadRequested.connect(self.on_download_requested)

        # --- Load the given URL ---
        self.web_view.load(QUrl(url))

    def on_download_requested(self, download):
        """Handle file downloads triggered inside JupyterLite."""
        # Ask user where to save the file
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File As", download.downloadFileName())
        if save_path:
            download.setPath(save_path)
            download.accept()
            print(f"📥 Download started: {save_path}")
        else:
            download.cancel()
            print("⚠️ Download canceled.")

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nectar-X-Studio")
        self.setGeometry(100, 100, 1200, 630)
        self.setStyleSheet(self.get_styles())
        # Idle detection timer
        #self.idle_timer = QTimer(self)
        #self.idle_timer.setInterval(5 * 60 * 1000)  # 5 minutes
        #self.idle_timer.timeout.connect(self.on_idle_timeout)
        #self.idle_timer.start()

        # Install event filter on main window and all child widgets
        #self.install_event_filter_recursive(self)

        self.settings = QSettings("Zashirion", "Nectar-X-Studio")
        self.auth_methods = ["Click to choose an option","Password", "PIN", "Pattern", "2FA (Authenticator)"]
        self.pattern_sequence = []

        self.init_ui()
        self.init_services()
        self.google_auth = GoogleAuthHelper(self.settings)
        self.load_google_account()


    # ------------------------------------------------------------
    # UI Initialization
    # ------------------------------------------------------------

    def init_ui(self):
        # Window icon
        self.setWindowIcon(QIcon(self.find_icon('background/NectarX.png') or 'background/NectarX.png'))

        # Layout setup
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QHBoxLayout(self.central_widget)
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Sidebar and content
        self.primary_panel = self.build_primary_panel()
        self.content_area = self.build_content_area()

        splitter.addWidget(self.primary_panel)
        splitter.addWidget(self.content_area)
        main_layout.addWidget(splitter)

        # Minimal mode toggle button
        self.toggle_button = self.build_toggle_button()
        main_layout.addWidget(self.toggle_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Timers
        self.setup_timers()

        # Mouse tracking
        self.setMouseTracking(True)
        self.installEventFilter(self)

        self.Auth()
        self.check_existing_user()

    # ------------------------------------------------------------
    # Build Components
    # ------------------------------------------------------------
    def build_primary_panel(self):
        panel = QWidget()
        panel.setFixedWidth(80)
        panel.setStyleSheet('background-color: transparent; border-radius: 8px; padding: 8px;')

        layout = QVBoxLayout(panel)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        button_style = """
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #3f3f3f;
                color: #000000;
            }
            QPushButton[selected="true"] {
                background-color: #3f3f3f;
                color: #000000;
            }
            QToolTip {
                background-color: #000000;  /* dark background */
                color: #FFFFFF;             /* white text */
                border: 1px solid transparent;  /* light gray border */
                padding: 5px;
                border-radius: 5px;
                font-size: 12pt;
                font-family: Arial;
            }
        """

        icons = {
            "Chat": "menu/chat.png",
            "Broadcast": "menu/broadcast.png",
            "Test Lab": "menu/sys.png",
            "Model Downloader": "menu/download.png",
            "Update": "menu/update.png",
            "Settings": "menu/settings.png",
        }

        # --- Create Buttons ---
        self.buttons = {}
        for name, icon_path in icons.items():
            btn = QPushButton()
            btn.setFixedHeight(50)
            btn.setIcon(QIcon(self.find_icon(icon_path)))
            btn.setIconSize(QSize(24, 24))
            btn.setStyleSheet(button_style)
            btn.setToolTip(name)
            self.buttons[name] = btn

        # Add top navigation buttons
        for name in ["Chat", "Broadcast", "Test Lab", "Model Downloader", "Update"]:
            layout.addWidget(self.buttons[name])

        layout.addStretch()  # Push rest to bottom

        # Google profile picture circle
        self.google_profile_label = QLabel()
        self.google_profile_label.setFixedSize(60, 60)
        # Set the hover effect in the stylesheet
        self.google_profile_label.setStyleSheet("""
            QLabel {
                border-radius: 8px;
                background-color: #000000;
                color: #ffffff;
                font-size: 24px;
            }
            QLabel:hover {
                background-color: #1a1a1a; /* lighter black on hover */
            }
            QToolTip {
                background-color: #000000;  /* dark background */
                color: #FFFFFF;             /* white text */
                border: 1px solid transparent;  /* light gray border */
                padding: 5px;
                border-radius: 5px;
                font-size: 12pt;
                font-family: Arial;
            }
        """)

        # Set the cursor programmatically
        self.google_profile_label.setCursor(Qt.CursorShape.PointingHandCursor)

        
        layout.addWidget(self.google_profile_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Animated dot (status indicator)
        self.dot = AnimatedDot()
        self.dot.setFixedSize(50, 50)
        self.dot.setToolTip("Online Model Status")
        self.dot.setStyleSheet("""
            QToolTip {
                background-color: #000000;  /* dark background */
                color: #FFFFFF;             /* white text */
                border: 1px solid transparent;  /* light gray border */
                padding: 5px;
                border-radius: 5px;
                font-size: 12pt;
                font-family: Arial;
            }
        """)
        layout.addWidget(self.dot, alignment=Qt.AlignmentFlag.AlignCenter)

        # Settings button at the very bottom
        settings_btn = self.buttons["Settings"]
        settings_btn.clicked.connect(self.settings_menu)
        layout.addWidget(settings_btn)

        # Connect navigation buttons
        for name in ["Chat", "Broadcast", "Test Lab", "Model Downloader", "Update"]:
            self.buttons[name].clicked.connect(lambda _, n=name: self.load_tool_and_highlight(n))

        return panel

    def build_toggle_button(self):
        toggle = QPushButton("")
        toggle.setFixedSize(50, 50)
        toggle.setToolTip("Minimal Mode")

        # 🔹 Specify your custom icon path here
        icon_path = self.find_icon("menu/menu.png")
        toggle.setIcon(QIcon(icon_path))
        toggle.setIconSize(toggle.size() * 0.6)  # Adjust icon size as needed

        toggle.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: white;
                border: none;
                font-size: 24px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #242424;
                color: #ffffff;
            }
            QToolTip {
                background-color: #000000;  /* dark background */
                color: #FFFFFF;             /* white text */
                border: 1px solid transparent;  /* light gray border */
                padding: 5px;
                border-radius: 5px;
                font-size: 12pt;
                font-family: Arial;
            }
        """)

        toggle.clicked.connect(self.toggle_sidebar)
        return toggle

    def build_content_area(self):
        area = QStackedWidget()
        area.setStyleSheet('background-color: transparent; border: none; border-radius: 8px;')

        # Base pages
        raw_pages = {
            "": DisplayImage(),
            "Chat": Chat(),
            "Broadcast": Broadcast(),
            "Test Lab": Engine_Holder(),
            "Model Downloader": Gguf_Downloader(),
            "Update": UpdatePrompt(),
            "Settings": Settings(),
            "Browser": PersistentWebBrowser(),
            "ImageStudio": StableDiffusionApp(),
            "CodeLab": Code(f"http://localhost:{port}/{index_path.relative_to(output_dir).as_posix()}")
        }

        self.pages = {}
        for name, widget in raw_pages.items():
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setWidget(widget)
            scroll.setStyleSheet(self.scrollbar_style())
            area.addWidget(scroll)
            self.pages[name] = scroll
            write_to_log(f"Loaded page: {name}", file_path="logs/app.log")

        return area

    # ------------------------------------------------------------
    # Initialization and Timers
    # ------------------------------------------------------------
    # Recursive installation of event filters
    def install_event_filter_recursive(self, widget):
        widget.installEventFilter(self)
        for child in widget.findChildren(QWidget):
            child.installEventFilter(self)

    # Event filter to track user activity
    def eventFilter(self, source, event):
        if event.type() in (
            QEvent.Type.MouseMove,
            QEvent.Type.KeyPress,
            QEvent.Type.MouseButtonPress,
            QEvent.Type.MouseButtonRelease,
            QEvent.Type.Wheel,
            QEvent.Type.FocusIn
        ):
            self.reset_idle_timer()
        return super().eventFilter(source, event)

    # Reset timer on user activity
    def reset_idle_timer(self):
        if self.idle_timer.isActive():
            self.idle_timer.stop()
        self.idle_timer.start()

    # Called after 5 minutes of inactivity
    def on_idle_timeout(self):
        self.init_ui()

    def init_services(self):
        global viewer
        viewer = CodeViewer(codes)
        viewer.resize(700, 400)

    def setup_timers(self):
        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.timeout.connect(self.show_inactivity_screen)
        self.inactivity_timer.start(3600000)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_server)
        self.timer.start(3000)
        self.check_server()

    # ------------------------------------------------------------
    # Core Logic
    # ------------------------------------------------------------
    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        for path in [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, "menu", icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))
        ]:
            if os.path.exists(path):
                return path
        return None

    def check_server(self):
        is_active = self.ping("127.0.0.1", 5005)
        self.dot.set_active(is_active)

    def ping(self, host, port, timeout=0.5):
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

    def load_tool_and_highlight(self, name):
        self.highlight_selected_button(name)
        self.load_tool(name)

    def highlight_selected_button(self, selected_name):
        for name, btn in self.buttons.items():
            btn.setProperty("selected", "true" if name == selected_name else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

    def load_tool(self, tool_name):
        if tool_name in self.pages:
            self.content_area.setCurrentWidget(self.pages[tool_name])

    def show_inactivity_screen(self):
        self.content_area.setCurrentWidget(self.pages[""])

    def eventFilter(self, source, event):
        if event.type() in [QEvent.Type.KeyPress, QEvent.Type.MouseMove]:
            self.inactivity_timer.start(3600000)
        return super().eventFilter(source, event)

    def toggle_sidebar(self):
        # Create a dropdown menu
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: #000000;
                border: 1px solid #444;
                padding: 8px;
                border-radius: 8px;
            }
            QMenu::item {
                color: #ffffff;
                padding: 6px 14px;
                border-radius: 6px;
            }
            QMenu::item:selected {
                background-color: #1e1e1e;
                color: white;
            }
        """)

        # --- Add menu actions ---
        image_studio_action = QAction("Image Studio", self)
        browser_action = QAction("Browser", self)
        code_lab_action = QAction("Code Lab", self)

        menu.addAction(image_studio_action)
        menu.addAction(browser_action)
        menu.addSeparator()
        menu.addAction(code_lab_action)
        menu.addSeparator()

        # --- Connect actions to navigation ---
        image_studio_action.triggered.connect(lambda: Studio_Nectar.load_tool_and_highlight('ImageStudio'))
        browser_action.triggered.connect(lambda: Studio_Nectar.load_tool_and_highlight('Browser'))
        code_lab_action.triggered.connect(lambda: Studio_Nectar.load_tool_and_highlight('CodeLab'))

        # --- Show menu at cursor position ---
        menu.exec(QCursor.pos())

    def settings_menu(self):
        self.load_tool_and_highlight("Settings")

    from PyQt6.QtGui import QPixmap, QPainter, QPainterPath
    from PyQt6.QtCore import Qt

    def load_google_account(self):
        """Load saved Google profile (if any)."""
        if self.google_auth.is_authenticated():
            pixmap = self.google_auth.load_picture()
            if pixmap:
                # 🔵 Make the pixmap circular
                size = 55  # diameter of profile image
                rounded_pixmap = QPixmap(size, size)
                rounded_pixmap.fill(Qt.GlobalColor.transparent)

                painter = QPainter(rounded_pixmap)
                painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                path = QPainterPath()
                path.addEllipse(0, 0, size, size)
                painter.setClipPath(path)
                scaled_pixmap = pixmap.scaled(size, size)
                painter.drawPixmap(0, 0, scaled_pixmap)
                painter.end()

                self.google_profile_label.setPixmap(rounded_pixmap)
                self.google_profile_label.setFixedSize(size, size)
                self.google_profile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # <-- Center the image
                # Set the hover effect in the stylesheet
                self.google_profile_label.setStyleSheet("""
                    QLabel {
                        border-radius: 8px;
                        background-color: #000000;
                        color: #ffffff;
                        font-size: 24px;
                    }
                    QLabel:hover {
                        background-color: #1a1a1a; /* lighter black on hover */
                    }
                    QToolTip {
                background-color: #000000;  /* dark background */
                color: #FFFFFF;             /* white text */
                border: 1px solid transparent;  /* light gray border */
                padding: 5px;
                border-radius: 5px;
                font-size: 12pt;
                font-family: Arial;
            }
                """)

                # Set the cursor programmatically
                self.google_profile_label.setCursor(Qt.CursorShape.PointingHandCursor)

            else:
                self.google_profile_label.setText("👤")

            self.google_profile_label.setToolTip(self.settings.value("google/name", ""))
            self.google_profile_label.mousePressEvent = lambda e: self.show_google_menu(e)
        else:
            self.google_profile_label.setText(" ")
            self.google_profile_label.setToolTip("Click to sign in with Google")
            self.google_profile_label.mousePressEvent = lambda e: self.connect_google_account_threaded()

    def connect_google_account_threaded(self):
        """Start Google OAuth in background thread (non-blocking)."""
        self.google_profile_label.setText(" ")

        worker = GoogleAuthWorker(
            self.google_auth.client_secret_file,
            self.google_auth.SCOPES
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
        self.load_google_account()


    def on_google_auth_fail(self, error):
        """Handle failed login."""
        QMessageBox.critical(self, "Google Sign-In Failed", error)
        self.google_profile_label.setText(" ")


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
        self.google_profile_label.setText(" ")
        self.google_profile_label.setToolTip("Click to sign in with Google")
        self.google_profile_label.mousePressEvent = lambda e: self.connect_google_account_threaded()
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

    # ------------------------------------------------------------
    # Styles
    # ------------------------------------------------------------
    def get_styles(self):
        return """
            QPushButton:hover {
                background-color: #007ACC;
            }
            QPushButton:pressed {
                background-color: #005F9E;
            }
        """

    def scrollbar_style(self):
        return """
            QScrollBar:vertical {
                background: transparent;
                width: 8px;
                border: none;
            }
            QScrollBar::handle:vertical {
                background: #ffffff;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: #1b1b1b;
            }
            QScrollBar:horizontal {
                background: transparent;
                height: 8px;
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
        """
    
    # ------------------------------------------------------------
    # Lock Screen / Authentication
    # --------------------------------------------------
    
    def Auth(self):
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet('background-color: rgba(0, 0, 0, 180);')
        self.overlay.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.overlay.setVisible(True)
        overlay_layout = QVBoxLayout(self.overlay)
        overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.profile_label = QLabel()
        self.profile_label.setFixedSize(80, 80)
        self.profile_label.setStyleSheet("""
            QLabel {
                border-radius: 40px;
                background-color: #2a2a2a;
                border: 2px solid #333;
            }
        """)
        overlay_layout.addWidget(self.profile_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.overlay_label = QLabel(' ', self.overlay)
        self.overlay_label.setWordWrap(False)
        self.overlay_label.setStyleSheet('\n            QLabel {\n                color: #ffffff;\n                font-size: 24px;\n                font-weight: bold;\n                background: transparent;\n            }\n        ')
        self.overlay_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        overlay_layout.addWidget(self.overlay_label)

        self.method_selector = QComboBox()
        self.method_selector.addItems(self.auth_methods)
        self.method_selector.setStyleSheet("""
            QComboBox {
                background: #000000;
                border-radius: 6px;
                padding: 8px;
                font-size: 16px;
                color: #ffffff;
            }

            QComboBox:hover {
                background: #ffffff;  
                color: #000000;
            }

            QComboBox::drop-down {
                border: none;
                background: #000000; 
                border-radius: 6px;
                width: 25px;
            }
                                           
            QComboBox::down-arrow {
                image: url("background/down-arrow.svg");  /* Replace this with your icon */
                width: 12px;
                height: 12px;
            }

            QComboBox QAbstractItemView {
                background-color: #000000;
                color: white;
                selection-background-color: #000111;
                selection-color: #ffffff;
            }
        """)

        self.method_selector.currentTextChanged.connect(self.update_input_method)
        self.method_selector.setFixedWidth(228)
        overlay_layout.addWidget(self.method_selector, alignment=Qt.AlignmentFlag.AlignCenter)

        self.input_field = QLineEdit()
        self.input_field.setFixedWidth(250)
        self.input_field.setPlaceholderText("Enter your credential here")
        self.input_field.setStyleSheet("""
            QLineEdit {
                background: #000000;
                border-radius: 8px;
                padding: 6px;
                font-size: 16px;
                color: #ffffff;
            }
        """)
        overlay_layout.addWidget(self.input_field, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Pattern grid
        self.pattern_grid = QWidget()
        self.pattern_layout = QGridLayout(self.pattern_grid)
        self.pattern_layout.setSpacing(15)

        # Give the grid a border radius and modern dark background
        self.pattern_grid.setStyleSheet("""
            QWidget#pattern_grid {
                background-color: transparent;
                border-radius: 10px;
                border: 1px solid transparent;
                padding: 15px;
            }
        """)
        self.pattern_grid.setObjectName("pattern_grid")

        self.pattern_buttons = {}
        for i in range(4):
            for j in range(4):
                btn = QPushButton("")
                btn.setFixedSize(60, 60)
                btn.setStyleSheet(""" 
                                  
                    QWidget { 
                    background: transparent; 
                    } 
                    QPushButton { 
                    background: #000000; 
                    border-radius: 30px; 
                    } 
                    QPushButton:hover { 
                    background: #1b1b1b; 
                    } 
                """)
                btn.clicked.connect(lambda _, n=i*4+j+1: self.pattern_click(n))
                self.pattern_layout.addWidget(btn, i, j)
                self.pattern_buttons[i*4+j+1] = btn

        overlay_layout.addWidget(self.pattern_grid, alignment=Qt.AlignmentFlag.AlignCenter)
        self.pattern_grid.hide()

        self.submit_btn = QPushButton("Enter")
        self.submit_btn.setFixedWidth(180)
        self.submit_btn.setStyleSheet(' QPushButton { padding: 12px; background-color: #000000; color: white; border-radius: 5px;} QPushButton:hover { background-color: #ffffff; color: #000000;}')
        self.submit_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.submit_btn.clicked.connect(self.handle_submit)
        overlay_layout.addWidget(self.submit_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def resizeEvent(self, event):
        """Ensure overlay resizes with the main window."""  # inserted
        self.overlay.setGeometry(self.rect())
        super().resizeEvent(event)

    def clear_pattern(self):
        """Resets the pattern sequence and restores button styles."""
        self.pattern_sequence = []
        for btn in self.pattern_buttons.values():
            btn.setStyleSheet("""
                QPushButton {
                    background: #444444;
                    border-radius: 30px;
                }
                QPushButton:hover {
                    background: #007ACC;
                }
            """)

    def check_existing_user(self):
        settings1 = QSettings("Zashirion", "Nectar-X-Studio")

        if not settings1.contains("auth_method"):
            self.overlay_label.setText("🚧 Welcome! Create a login method. 🚧")
            return

        # --- Retrieve method ---
        method = settings1.value("auth_method")

        # --- Retrieve Google Info ---
        settings1.beginGroup("google")
        name1 = settings1.value("name", "User")
        picture_url = settings1.value("picture", "")
        settings1.endGroup()

        # --- Display text --- #{name1}
        self.overlay_label.setText(f"🚧 Enter your {method} to unlock. 🚧")

        # --- Display Profile Picture (if QLabel named self.profile_label exists) ---
        if hasattr(self, "profile_label"):
            pixmap = None
            try:
                if picture_url.startswith("http"):
                    # Download image from URL
                    response = requests.get(picture_url)
                    from io import BytesIO
                    image_data = BytesIO(response.content)
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data.read())
                else:
                    # Load from local file path
                    pixmap = QPixmap(picture_url)

                if not pixmap.isNull():
                    # Make the image round
                    size = 80
                    rounded = QPixmap(size, size)
                    rounded.fill(Qt.GlobalColor.transparent)

                    painter = QPainter(rounded)
                    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                    path = QPainterPath()
                    path.addEllipse(0, 0, size, size)
                    painter.setClipPath(path)
                    painter.drawPixmap(0, 0, pixmap.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation))
                    painter.end()

                    self.profile_label.setPixmap(rounded)
                    self.profile_label.setFixedSize(size, size)
            except Exception as e:
                print("Error loading profile picture:", e)

        # --- Lock method selector ---
        self.method_selector.setCurrentText(method)
        self.method_selector.setEnabled(False)
        self.update_input_method(method)

    def update_input_method(self, method):
        self.input_field.hide()
        self.pattern_grid.hide()
        self.input_field.clear()
        self.pattern_sequence = []

        if method in ["Password", "PIN"]:
            self.input_field.show()
            self.input_field.setEchoMode(QLineEdit.EchoMode.Password)
        elif method == "Pattern":
            self.pattern_grid.show()
        elif method == "2FA (Authenticator)":
            self.input_field.show()
            self.input_field.setEchoMode(QLineEdit.EchoMode.Normal)

    def pattern_click(self, number):
        self.pattern_sequence.append(str(number))
        self.pattern_buttons[number].setStyleSheet("""
            QPushButton {
                background: #ffffff;
                border-radius: 30px;
            }
        """)

    def handle_submit(self):
        method = self.method_selector.currentText()
        if not self.settings.contains("auth_method"):
            if method == "Pattern":
                if not self.pattern_sequence:
                    QMessageBox.warning(self, "Error", "Enter a pattern!")
                    return
                self.settings.setValue("credential", "".join(self.pattern_sequence))
            elif method == "2FA (Authenticator)":
                secret = pyotp.random_base32()
                self.settings.setValue("2fa_secret", secret)
                QMessageBox.information(self, "2FA Setup",
                                        f"Your 2FA secret: {secret}\nAdd it to Google Authenticator")
            else:
                credential = self.input_field.text().strip()
                if not credential:
                    QMessageBox.warning(self, "Error", "Enter valid credential!")
                    return
                self.settings.setValue("credential", credential)
            self.settings.setValue("auth_method", method)
            QMessageBox.information(self, "Success", "Login credentials saved!")
            self.overlay.setVisible(False)
        else:
            stored_method = self.settings.value("auth_method")
            if stored_method != method:
                QMessageBox.warning(self, "Error", "Wrong login method selected!")
                return

            if method == "Pattern":
                if "".join(self.pattern_sequence) == self.settings.value("credential"):
                    self.accept_login()
                else:
                    QMessageBox.warning(self, "Error", "Invalid pattern!")
                    self.clear_pattern()
            elif method == "2FA (Authenticator)":
                totp = pyotp.TOTP(self.settings.value("2fa_secret"))
                if totp.verify(self.input_field.text().strip()):
                    self.accept_login()
                else:
                    QMessageBox.warning(self, "Error", "Invalid 2FA code!")
            else:
                if self.input_field.text().strip() == self.settings.value("credential"):
                    self.accept_login()
                else:
                    QMessageBox.warning(self, "Error", "Invalid credential!")

    def accept_login(self):
        #QMessageBox.information(self, "Success", "Login successful!")
        self.overlay.setVisible(False)

codes = [
        {"title": "GET Example", "code": """import requests\nurl = "http://127.0.0.1:8000/predict"\nparams = {"data": "Hello AlphaLLM"}\nresponse = requests.get(url, params=params)\nprint(response.json())"""},
        {"title": "POST Example", "code": """import requests\nurl = "http://127.0.0.1:8000/predict"\npayload = {"data": "Hello AlphaLLM"}\nresponse = requests.post(url, json=payload)\nprint(response.json())"""},
        {"title": "WebSocket Example", "code": """import asyncio\nimport websockets\nasync def send_data():\n    url = "ws://127.0.0.1:8000/ws_predict"\n    async with websockets.connect(url) as ws:\n        await ws.send("Hello AlphaLLM")\n        response = await ws.recv()\n        print(response)\nasyncio.run(send_data())"""},
        {"title": "Integration in App", "code": """
            import requests

            # Replace with your actual token
            ACCESS_TOKEN = "AccessToken"

            def query_alpha_llm(data: str):
                url = "http://127.0.0.1:8000/predict"
                headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
                try:
                    # Send data as query parameter (server uses GET)
                    response = requests.get(url, params={"data": data}, headers=headers)
                    return response.json().get("response", "No response received")
                except requests.exceptions.RequestException as e:
                    return f"Error: {e}"

            def chat_terminal():
                print("Alpha LLM Terminal Chat (type 'exit' to quit)")
                while True:
                    user_input = input("You: ").strip()
                    if user_input.lower() == "exit":
                        print("Exiting chat...")
                        break
                    response = query_alpha_llm(user_input)
                    print(f"Alpha: {response}\n")

            if __name__ == "__main__":
                chat_terminal()
        """}
    ]

conversation_history = load_conversation_history()
history = load_history()


# ----------------- SINGLE INSTANCE CHECK -----------------
def check_single_instance():
    shared_memory = QSharedMemory('Nectar-X-Studio')
    if not shared_memory.create(1):
        write_to_log('Another instance is already running.')
        return False
    return True

Studio_Nectar = None  # define 
viewer = None

# ----------------- STARTUP -----------------
def main():
    if not check_single_instance():
        return

    app = QApplication(sys.argv)

    # Apply user theme
    apply_theme(get_user_theme())
    global Studio_Nectar

    # Initialize main window
    Studio_Nectar = Main()
    Studio_Nectar.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
