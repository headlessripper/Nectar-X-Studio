import asyncio
import struct
import pyotp
import uvicorn
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
import subprocess
import platform
import socket
import psutil
import shutil
import re
import requests
import time
import math
from urllib.parse import urlparse
from urllib.request import urlopen
from datetime import datetime
import datetime
import base64
import json
import xml.etree.ElementTree as ET
import warnings
import threading
import tempfile
import os, sys
 
try:
    from llama_cpp import Llama
except Exception:
    Llama = None

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import uuid, hashlib, psutil

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QLineEdit, QGridLayout, QMessageBox,
    QTextEdit, QCheckBox, QHBoxLayout, QFrame, QFileDialog, QInputDialog,
    QPlainTextEdit, QStackedWidget, QStackedLayout, QFormLayout,
    QSlider, QScrollArea, QGraphicsOpacityEffect, QListWidgetItem, QComboBox, QGroupBox,
    QTabWidget, QCompleter, QMenu,
    QDialogButtonBox, QDialog, QSystemTrayIcon
)
from PyQt6.QtCore import (
    Qt, QTimer, QThread, pyqtSignal, QElapsedTimer,
    QObject, QSize, QPropertyAnimation, QEvent,
    QFileSystemWatcher, QStringListModel, QPoint, QUrl, QEasingCurve, QVariantAnimation, QRect,
    pyqtProperty, pyqtSlot, QRunnable, QThreadPool
)
from PyQt6.QtGui import (
    QIcon, QFont, QPixmap, QPainter, QPainterPath, QDesktopServices, QShortcut,
    QColor, QSyntaxHighlighter, QAction,
    QPen, QKeySequence, QGuiApplication, QCursor, QBrush, QImage, QClipboard
)
from PyQt6.QtWebEngineWidgets import QWebEngineView

from concurrent.futures import ThreadPoolExecutor, as_completed
from PyQt6.QtCore import QThread, pyqtSignal
import psutil

from PIL import Image

import logging

from PyQt6.QtCore import QSettings
from winotify import Notification, audio
import pickle
import markdown
import feedparser
import torch
import re
from datetime import datetime
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
from concurrent.futures import ThreadPoolExecutor, as_completed

class Notify(QWidget):
    def __init__(self, message, duration=3000, parent=None):
        if parent is None or not parent.isVisible():
            parent = QApplication.activeWindow()  # Fallback
        super().__init__(parent, flags=Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WA_DeleteOnClose, True)  # Auto-delete on clos
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