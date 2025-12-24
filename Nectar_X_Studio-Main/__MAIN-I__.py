"""
-----BEGIN NEW CERTIFICATE REQUEST-----
MIIEwTCCAqkCAQAwfDELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWEx
ETAPBgNVBAcTCHNhbiBqb3NlMREwDwYDVQQLEwhTb2Z0d2FyZTERMA8GA1UEChMI
WmFzaGlyb24xHzAdBgNVBAMTFnphc2hpcm9uLmluY0BnbWFpbC5jb20wggIiMA0G
CSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDXqITZ11upATVV5yigIKp6rWaiqYJA
jdgFhC6KEOnyIw34qrMBfu+GsrEMIB3fKzbVeBNxIRN1OBUgT8gMEnUBhqfQorIO
ZwcYCS95lYBIyU0vzVfHV4T3ovKn9EnNB+ojvb5EzYmBiwc9eZ6hd3RuoS4NopdG
wN6nv/x1PsqPUTvnzJWciDsL4/kmoAeoteJXptdgyAHobz5CYSounZyQ4KpLNfbf
t6+kKJVF+oocXEVbpMujrBP0MLJvE+o4mM6J+o0H90BcnKlHFAqdkGZPHaupiBub
XjSjVXVHOQVsML1f2kjysykJkBUBPhHMoRZpwA097WBiNDDMck9/O5I+1T9zMA5v
p8iIzsre4fSW8IpWR8VzI8sh1dW1jm37jlPE0p9YrySfHsM4ax3IzlEUT3lJw5yI
lYc6dQBVNYpCboa1OzK603f9MDcDyVprUh8toLbhwmUWrTy6wWlNemPTq9N/2dDK
yUulBWe7SKch4303R+W2kWp6zYfeO4NSFg1XprhdlOGhpk1QQfy5cFDcbaxyuT4b
vxvFhb9iLJlSCwAWgmsQkAHfchVof1bWynZ42Je/lG2hsI2k6sepdX9RYRkLXHxu
dsVy5/j2ajaEdkAEUAHwSR3XHFcf91zwXU9A0UeFnHU5pUXpoK/hSo/wWdbUHt9E
R8S5yXT9AkQbsQIDAQABoAAwDQYJKoZIhvcNAQEFBQADggIBAAv08Po6CYdlxTbU
JVG/VUj1qJOo6tZI8R9vc1OEl07qfOdCKPKNxber/lavxIz6t62+tzlK+/n4db2s
s73NiSaCDNXoV0oXePEuVsa4lLTRZlrEGV9vEOyQF7sp+baXYO7c4RHaAP0ILQ3Z
6ZYGDgFuMsHR2QbHzxcprTr93e0N2muu5Lcy3MWKWR/LP3MNmp5/JslGct7450rp
5H2J2VDSrr294Tqs9jo10MeJ6d46P90SVnWaIZa5nz2wyaZ6P5rGFrDU4mZUf1nI
U1PaysnJ17NA3rAYhbVtzMidl9MJoZQjirPJcBH4BbC5viwPb9XYPqaWLVDmvmPI
ptASBo61T7ATsAExJg2QCw/ZXjcTukQps5/g8SLZa60iw+iGeVOHEyjahUytPPvP
o+BaB76LSEuwg0Ag9Dzh9HFMlBXVzkgYea/pMt8hpocxRoyU0+iNeB24pkFexJNm
UyY3IjXjI4d7r1csM2infY/EoE/rd/cM4lJuNEOCEoLXyIrNgheYnB8syzuZlJ7O
dlONy02TzzsB6WyNrMy5PiyRms4gO3642JLWqdCiaA0dK3jcVVcKvlRq266cD8fs
9qySy9ALf5ditWsS0NSwnhSJpMBX33HDBzn4X7v2vsWhJiasSNg+vztBufe+KQJh
/yCrruLaBkPE4xi8ZyzFyAz/NCOv
-----END NEW CERTIFICATE REQUEST-----

"""

"""
\nLicense Key: DHVD-0877-DWRH-2865 
\nUnique Numerical Signature: 15684358866751936532
\nSeriel No: E729A9A903218C5C7EB22B3B13F9AE89
"""
#------------------------------------------------------------------------------
# Keys
#------------------------------------------------------------------------------

ACCESS_TOKEN = 'Hugging face API-KEY Here'
token = 'Hugging face API-KEY Here'
REFERENCE_IMAGE = 'background/NectarX.png'
OWNER = 'headlessripper'
REPO = 'Nectar-X-Studio'
CURRENT_VERSION = 'v1.4'
DEFAULT_SUGGESTIONS = ["Valorant", "CS:GO", "Minecraft"]
MAX_HISTORY = 10
POLL_INTERVAL_MS = 5000 
Encoded_License_Details = 'eyJsaWNlbnNvciI6ICJaYXNoaXJpb24gaW5jIiwgImxpY2Vuc2Vfa2V5IjogIkRIVkQtMDg3Ny1EV1JILTI4NjUiLCAiZXhwaXJhdGlvbl9kYXRlIjogIjIwMjYtMTItMjMifQ=='

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------

global _logger_initialized 
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
    QSpacerItem, QSizePolicy, QLineEdit, QGridLayout, QMessageBox,
    QTextEdit, QCheckBox, QHBoxLayout, QFrame, QFileDialog, QInputDialog,
    QPlainTextEdit, QSplitter, QStackedWidget, QStackedLayout, QFormLayout,
    QSlider, QScrollArea, QGraphicsOpacityEffect, QListWidgetItem, QComboBox, QGroupBox,
    QTabWidget, QCompleter, QMenu, QToolTip, QToolButton,
    QDialogButtonBox, QDialog
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
import SYS_PROMPTS.sys_msgs as sys_msgs
#import Nectar_Scripts.sys_msgs as sys_msgs
#import Nectar_Scripts.SYS_PROMPTS.sys_msgs as sys_msgs
import markdown
import feedparser
import torch
import re
from datetime import datetime
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
from concurrent.futures import ThreadPoolExecutor, as_completed

QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)

TRANSFORMER_MODEL_PATH = os.path.join(os.path.expanduser("~"), "all-MiniLM-L12-v2")

#-----------------------------------------------------------------------------
# Plug Directory
#-----------------------------------------------------------------------------
PLUGIN_DIR = os.path.join(os.path.expanduser("~"), ".Plugin", "plugins")
os.makedirs(PLUGIN_DIR, exist_ok=True)
MAX_COLUMNS = 3

#-----------------------------------------------------------------------------
# Logger Setup
#-----------------------------------------------------------------------------

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
            write_to_log(f"Logger initialization failed: {e}")
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

#--------------------------------------------------------------------------------
# License Unload
#--------------------------------------------------------------------------------

# ----------------- DEVICE BINDING / LICENSE CHECK -----------------
def get_device_id1():
    """Generate unique device identifier (cross-platform)."""
    node = uuid.getnode()
    sys_info = platform.system() + platform.release()
    base = f"{node}-{sys_info}"
    return hashlib.sha256(base.encode()).hexdigest()


def get_device_id():
    """
    Returns a unique, hashed device ID (hardware-locked).
    """
    node = uuid.getnode()
    sys_info = os.uname().sysname if hasattr(os, 'uname') else sys.platform
    base = f"{node}-{sys_info}"
    return hashlib.sha256(base.encode()).hexdigest()


def decode_license(encoded_license):
    """
    Decodes base64 license data into a Python dict.
    """
    try:
        decoded_json = base64.urlsafe_b64decode(encoded_license.encode()).decode()
        return json.loads(decoded_json)
    except Exception as e:
        write_to_log(f"License decoding failed: {e}")
        return None


def save_license_silently(license_data):
    """
    Saves decoded license details silently to ~/.nectar_license.
    """
    license_file = os.path.join(os.path.expanduser("~"), ".nectar_license")
    try:
        with open(license_file, "w") as f:
            json.dump(license_data, f)
        write_to_log("License details saved to .nectar_license")
    except Exception as e:
        write_to_log(f"Failed to save license: {e}")

def load_license_data():
    """
    Loads license details from ~/.nectar_license if present.
    """
    license_file = os.path.join(os.path.expanduser("~"), ".nectar_license")
    if not os.path.exists(license_file):
        return None
    try:
        with open(license_file, "r") as f:
            return json.load(f)
    except Exception as e:
        write_to_log(f"Failed to load license: {e}")
        return None

def is_license_expired(expiration_date):
    """
    Checks if the license has expired.
    """
    try:
        exp_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        return datetime.now().date() > exp_date
    except Exception:
        return True

def verify_license():
    """
    Verifies license validity, expiration, and device binding.
    Prompts for new encoded details if invalid or expired.
    """
    license_data = load_license_data()

    if not license_data:
        write_to_log("No local license found. Initializing new one.")
        decoded = decode_license(Encoded_License_Details)
        if decoded:
            save_license_silently(decoded)
            license_data = decoded
        else:
            QMessageBox.critical(None, "License Error", "Corrupted license data. Contact support.")
            return False
        
    if not all(k in license_data for k in ("licensor", "license_key", "expiration_date")):
        write_to_log("Invalid license structure.")
        QMessageBox.critical(None, "License Error", "Invalid license structure. Please reactivate.")
        return False

    # Expiration check
    if is_license_expired(license_data["expiration_date"]):
        QMessageBox.warning(None, "License Expired",
                            f"Your license expired on {license_data['expiration_date']}.\n"
                            "Please enter a new encoded license key to continue.")
        new_license, ok = QInputDialog.getText(None, "License Renewal", "Enter new encoded license:")
        if ok and new_license.strip():
            decoded_new = decode_license(new_license.strip())
            if decoded_new:
                save_license_silently(decoded_new)
                QMessageBox.information(None, "License Updated", "New license activated successfully.")
                return True
            else:
                QMessageBox.critical(None, "License Error", "Invalid encoded license entered.")
                return False
        else:
            write_to_log("User canceled license renewal.")
            return False

    device_id = get_device_id()
    local_hash = hashlib.sha256((license_data["license_key"] + device_id).encode()).hexdigest()

    write_to_log(f"License verified for {license_data['licensor']}, valid until {license_data['expiration_date']}.")
    write_to_log(f"Device ID hash: {local_hash}")

    return True

verify_license()

# ----------------- ANTI-INJECTION / ANTI-DEBUGGING -----------------
def detect_debugger_or_injection():
    blacklisted = [
        'x64dbg', 'ollydbg', 'cheatengine', 'wireshark', 
        'processhacker', 'ida', 'ghidra'
    ]
    try:
        for proc in psutil.process_iter(['name']):
            name = proc.info.get('name', '').lower()
            if any(bad in name for bad in blacklisted):
                write_to_log(f"Suspicious process detected: {name}")
                QMessageBox.warning(None, "Security Alert",
                                    f"Unauthorized debugger/injector detected: {name}\nExiting for safety.")
                sys.exit(1)
    except Exception as e:
        write_to_log(f"Process scan error: {e}")

# ----------------- SECURITY ENTRYPOINT -----------------
def run_security_checks():
    detect_debugger_or_injection()
    if not verify_license():
        sys.exit(1)

license_data = load_license_data()

#-----------------------------------------------------------------------------
# License Series
#-----------------------------------------------------------------------------
device_id = get_device_id()
local_hash = hashlib.sha256((license_data["license_key"] + device_id).encode()).hexdigest()

# License text (Zashiron License v1.2)
licenseagreement_info = f"""
Nectar-X-Studio Proprietary License 
(Zashiron License v1.2)
Copyright © 2025 Zashiron. All rights reserved.

1. Definitions
“Software” means the computer program known as Nectar-X-Studio (AI Studio),
which is currently locked to this device,  
Platform UUID(unique user identification) : {local_hash}.
including all executable code, source code, scripts, assets, documentation,
updates, and related materials provided by Zashiron.

“Licensee” (or “You”) means any person or legal entity authorized by Zashiron
to use the Software under this License.

“Use” means to install, execute, access, or otherwise interact with the Software.

2. Grant of License
Subject to the terms of this License, Zashiron grants You a non-exclusive,
non-transferable, revocable license to install and use one copy of the Software
for personal, educational, or approved commercial purposes.
All other rights are reserved by Zashiron.

3. Commercial Use
You may use the Software for commercial purposes only if you have obtained an
official commercial license or written authorization from Zashiron, and comply
with all fees and conditions. Unauthorized commercial use is strictly prohibited.

4. Restrictions
You may not:
- Copy, modify, or create derivative works of the Software.
- Distribute, sublicense, rent, lease, lend, or resell the Software.
- Circumvent or bypass licensing or activation mechanisms.
- Remove or alter any copyright or proprietary notices.
- Use the Software for illegal, unethical, or competing purposes.

5. Ownership
All rights, title, and interest in the Software remain the exclusive property of Zashiron.

6. Updates and Support
Zashiron may, at its discretion, provide updates, patches, or enhancements.
Such updates remain governed by this License.

7. Termination
This License is effective until terminated. Upon termination, You must cease use
and destroy all copies of the Software.

8. Disclaimer of Warranties
The Software is provided “AS IS”, without warranties of any kind, express or implied.

9. Limitation of Liability
In no event shall Zashiron be liable for any direct, indirect, incidental, or
consequential damages arising from use or inability to use the Software.

10. Governing Law
This License is governed by the laws of the Republic of South Africa.

11. Commercial Licensing Inquiries
For enterprise or commercial licensing:
Zashiron Licensing Department
Email: Zashiron.inc@gmail.com
Website: https://github.com/Zashiron

12. Acknowledgment
By installing or using the Software, You agree to be bound by this License.

13. Anti-Decompilation Clause
You expressly agree not to reverse engineer, decompile, disassemble, decrypt,
modify, or otherwise attempt to derive the source code or algorithms of the Software,
except where such activity is expressly permitted by law. Any unauthorized attempt
constitutes a material breach and may result in termination and legal action.

14. Data Privacy
Zashiron is committed to protecting your privacy. We do not collect or store any personal data without your consent. Any data collected during the use of the Software is used solely for the purpose of providing and improving the Software.
By using the Software, You acknowledge that You have read, understood, and agree to be bound by the terms of this License.
"""

# ---------- Get local IP ----------
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# ----------------------------
# Find a free port
# ----------------------------
def find_free_port():
    """Find a free local port to use for the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

class GoogleAuthHelper:
    SCOPES = [
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/gmail.readonly",
    ]

    def __init__(self, settings):
        self.settings = settings
        self.client_secret_file = os.path.join(os.path.dirname(__file__), "oauth", "client_secret.json")
        self.creds_file = os.path.join(os.path.dirname(__file__), "oauth", "creds.pkl")

    def save_profile(self, profile: dict):
        """Save Google account data."""
        self.settings.setValue("google/name", profile.get("name", ""))
        self.settings.setValue("google/email", profile.get("email", ""))
        self.settings.setValue("google/picture", profile.get("picture", ""))
        self.settings.setValue("google/authorized", True)

    def save_credentials(self, creds):
        """Save Google credentials to creds.pkl"""
        try:
            with open(self.creds_file, "wb") as f:
                pickle.dump(creds, f)
            write_to_log(f"✅ Credentials saved to {self.creds_file}")
        except Exception as e:
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="Error ⚠️",
                msg=f"Failed to save credentials: {e}",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()

    def load_credentials(self):
        """Load credentials from creds.pkl"""
        if os.path.exists(self.creds_file):
            try:
                with open(self.creds_file, "rb") as f:
                    creds = pickle.load(f)
                return creds
            except Exception as e:
                toast = Notification(
                app_id="Nectar-X-Studio",
                title="Error ⚠️",
                msg=f"Failed to load credentials: {e}",
                icon=find_icon('background/NectarX.png'),
                duration="short"
                )
                toast.set_audio(audio.SMS, loop=False)
                toast.show()
        return None

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

class GoogleAuthWorker(QObject):
    finished = pyqtSignal(dict)
    failed = pyqtSignal(str)

    def __init__(self, client_secret_path, scopes, helper: GoogleAuthHelper):
        super().__init__()
        self.client_secret_path = client_secret_path
        self.scopes = scopes
        self.helper = helper

    def run(self):
        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                self.client_secret_path,
                self.scopes
            )
            creds = flow.run_local_server(port=0)

            if creds:
                self.helper.save_credentials(creds)

            service = build("oauth2", "v2", credentials=creds)
            profile = service.userinfo().get().execute()

            self.helper.save_profile(profile)

            self.finished.emit(profile)
        except Exception as e:
            self.failed.emit(str(e))

from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

def send_gmail_message(service, to, subject, body):
    """Send an email via Gmail API."""
    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message_obj = {'raw': raw}
    message_sent = service.users().messages().send(userId='me', body=message_obj).execute()
    return message_sent

from googleapiclient.discovery import build
import base64
from email import message_from_bytes

def fetch_latest_messages(creds, sender="Zashiron.inc@gmail.com"):
    service = build('gmail', 'v1', credentials=creds)
    result = service.users().messages().list(userId='me', q=f"from:{sender}", maxResults=5).execute()
    messages = result.get('messages', [])
    fetched = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='raw').execute()
        raw = base64.urlsafe_b64decode(msg_data['raw'].encode())
        email_msg = message_from_bytes(raw)
        subject = email_msg['subject']
        body = ""
        if email_msg.is_multipart():
            for part in email_msg.get_payload():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = email_msg.get_payload(decode=True).decode()
        fetched.append({"subject": subject, "body": body})
    return fetched

def find_icon(icon_name):
    """Attempts to find the icon in and out of the script\'s directory.""" 
    script_dir = os.path.dirname(os.path.realpath(__file__))
    possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'background', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    else:
        return None
    
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
    else:
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
        else:
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
    else: 
        if 4 <= ram < 8:
            recommendation.append('Run small quantized models like 7B (Q4_0 or Q5_0) using CPU.')
        else: 
            if 8 <= ram < 16:
                recommendation.append('Run 7B models comfortably (Q4_0 to Q6_K).')
            else: 
                if 16 <= ram < 32:
                    recommendation.append('Run 13B (Q4/Q5), 7B full precision possible.')
                else:
                    if ram >= 32:
                        recommendation.append('Run 13B easily, 33B quantized models possible (Q4).')
    if gpu_vram >= 12:
        recommendation.append('Run 13B or even 33B models in GGUF on GPU.')
    else: 
        if 6 <= gpu_vram < 12:
            recommendation.append('Run 7B GGUF models on GPU (Q4 or Q5 quantization).')
        else: 
            if 0 < gpu_vram < 6:
                recommendation.append('Very limited GPU use CPU instead.')
            else: 
                recommendation.append('No GPU acceleration available; CPU-only inference recommended.')
    rec_text = '                '.join(recommendation)
    summary = f"\n    LLM Recommendation: With {ram} GB RAM and GPU: {info['gpu_name']} ({gpu_vram} GB VRAM)\n [ {rec_text} ]\n    "
    return summary

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

#--------------------------------------------------------------------------------
# Slide Image Loader
#--------------------------------------------------------------------------------
def load_image_from_url(url):
    try:
        response = requests.get(url, timeout=5)
        image = QImage.fromData(response.content)
        return QPixmap.fromImage(image)
    except Exception as e:
        write_to_log("Error loading image:", e)
        return QPixmap()

#--------------------------------------------------------------------------------
# Send Function
#--------------------------------------------------------------------------------

def send_to_AlphaLLM(question):
    import socket
    
    SERVER_ADDRESS = ('127.0.0.1', 5005)
    AUTH_KEY = ("NEC-892657")

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
        client.connect(SERVER_ADDRESS)

        secure_message = f"{AUTH_KEY} {question}"
        client.sendall(secure_message.encode('utf-8'))

        response = client.recv(8192).decode('utf-8').strip()
        client.close()

        return response

    except (socket.error, socket.timeout) as e:
        return f"[Error] Could not connect to AlphaLLM: {e}"

TAG_RE = re.compile(r"<.*?>")

def html_to_text(html: str) -> str:
    text = TAG_RE.sub("", html)
    text = text.replace("&nbsp;", " ")
    return text.strip()

from mdx_linkify.mdx_linkify import LinkifyExtension

SECTION_PATTERNS = {
    r"key findings": "## Key Findings",
    r"actionable steps": "## Actionable Steps",
    r"sources? & context": "## Sources & Context",
    r"analysis": "## Analysis",
    r"urls?": "## Urls",
}

def beautify_markdown(text: str) -> str:
    text = re.sub(
        r"(Key Findings)\s*(\d+\.)",
        r"\1\n\2",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(r"\s*##\s*", r"\n\n## ", text)

    raw_lines = text.splitlines()
    out = []

    for raw in raw_lines:
        line = raw.strip()
        if not line:
            continue

        lowered = line.lower()
        replaced = False

        for pat, heading in SECTION_PATTERNS.items():
            m = re.search(pat, lowered)
            if m:
                before = line[:m.start()].strip()
                after = line[m.end():].strip()

                if before:
                    out.append(before)

                out.append("")
                out.append(heading)
                out.append("")

                if after:
                    out.append(after)
                replaced = True
                break

        if replaced:
            continue

        line = re.sub(r"(?<!\n)(\d+\.\s+)", r"\n\1", line)

        for subline in line.split("\n"):
            subline = subline.strip()
            if not subline:
                continue
            out.append(subline)

    return "\n".join(out).strip()
    
WEB_RAG_SYSTEM_PROMPT = sys_msgs.assistant_msg  

DECISION_MODEL_PATH = os.path.join(os.path.expanduser("~"), "Decision-Model/decision-k2.gguf")
    
import json

router_llm = Llama(
    model_path=DECISION_MODEL_PATH,
    n_ctx=32768,
    n_threads=2,
    n_gpu_layers=-1,
    n_batch=3524,
    temperature=0.0,
    logits_all=False,
    verbose=False
)

# ---------------------------------------------------------------
# 🔎 QUERY GENERATOR
# ---------------------------------------------------------------
def query_generator(query):
    """Generate a search query based on the last user prompt."""
    sys_msg = sys_msgs.query_msg
    query_msg = f"CREATE A SEARCH QUERY FOR THIS PROMPT:\n{query}"

    response = router_llm.create_chat_completion(
        messages=[
            {"role": "system", "content": sys_msg},
            {"role": "user", "content": query_msg},
        ],
        max_tokens=50,
        stop=["\n"],
    )

    return response["choices"][0]["message"]["content"].strip()

def model_decides_web_rag(llm, query: str) -> bool:

    messages = [
        sys_msgs.ROUTER_SYSTEM_PROMPT,
        {"role": "user", "content": query}
    ]

    result = llm.create_chat_completion(
        messages,
        max_tokens=50,
        temperature=0.0  # deterministic
    )

    raw = result["choices"][0]["message"]["content"].strip()

    try:
        decision = json.loads(raw)
        return bool(decision.get("use_web", False))
    except Exception:
        # Safety fallback: don't web-search
        return False
    
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
        else:
            self._radius_anim.setDirection(QPropertyAnimation.Direction.Forward)
        self._radius_anim.start()

    def _reverse_opacity_animation(self):
        direction = self._opacity_anim.direction()
        if direction == QPropertyAnimation.Direction.Forward:
            self._opacity_anim.setDirection(QPropertyAnimation.Direction.Backward)
        else:
            self._opacity_anim.setDirection(QPropertyAnimation.Direction.Forward)
        self._opacity_anim.start()

    def set_active(self, is_active: bool):
        if is_active:
            self.setToolTip('Engine Status: ONLINE - Model Loaded.')
            
            self._color_anim.setDirection(QVariantAnimation.Direction.Forward)
            self._color_anim.start()
            self._radius_anim.setDirection(QPropertyAnimation.Direction.Forward)
            self._radius_anim.start()
            self._opacity_anim.setDirection(QPropertyAnimation.Direction.Forward)
            self._opacity_anim.start()
        else:
            self.setToolTip('Engine Status: OFFLINE - Please Loaded A Model, Click to Auto Run Last Loaded Model.')
           
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

    def closeEvent(self, event):
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()
        event.accept()

class SearchLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Search")
        self.setFixedHeight(36)
        self.setStyleSheet(
            "background: rgba(255,255,255,0.02); padding-left:12px; border-radius:10px; color:#bdbdbd;"
        )
    
        self.search_history = []
        self.typing_timer = QTimer()
        self.typing_timer.setSingleShot(True)
        self.typing_timer.setInterval(300)
        self.typing_timer.timeout.connect(self.fetch_web_suggestions)

        self.completer_model = QStringListModel()
        self.completer = QCompleter(self.completer_model, self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.setCompleter(self.completer)

        self.threadpool = QThreadPool.globalInstance()

        self.textChanged.connect(self.on_text_changed)
        self.returnPressed.connect(self.run_search_thread)

    def on_text_changed(self, text):
        if text.strip():
            self.typing_timer.start()

    def fetch_web_suggestions(self):
        self.typing_timer.stop()
        query = self.text().strip()
        if not query:
            return
        self.threadpool.start(RunnableTask(self._fetch_suggestions_threaded, query))

    def _fetch_suggestions_threaded(self, query):
        try:
            response = requests.get(
                'https://suggestqueries.google.com/complete/search',
                params={'client': 'firefox', 'q': query},
                timeout=2
            )
            suggestions = response.json()[1]
        except Exception as e:
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="Web suggestion Error",
                msg=f"Web suggestion Error: No Internet or {e}",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()
            suggestions = []

        # Merge web suggestions, history, and defaults
        combined = list(dict.fromkeys(suggestions + self.search_history + DEFAULT_SUGGESTIONS))
        self.completer_model.setStringList(combined)

    def run_search_thread(self):
        url_str = self.text().strip()
        if not url_str:
            return
        if url_str not in self.search_history:
            self.search_history.insert(0, url_str)
            self.search_history = self.search_history[:MAX_HISTORY]

        Notify("Coming Soon!", parent=self)

class Inform(QWidget):
    def __init__(self, message, duration=3000, parent=None):
        super().__init__(parent, flags=Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        self._drag_active = False
        self._drag_position = QPoint()

        self.label = QLabel(message, self)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #self.setMaximumWidth(400)
        #self.setMinimumWidth(200)
        self.label.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                color: red;
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
            screen = QApplication.primaryScreen().geometry()
            self.move(
                screen.center().x() - self.width() // 2,
                50
            )

        # Auto-close timer
        QTimer.singleShot(duration, self.close)
        self.show()

        self.label.installEventFilter(self)

    # Handle mouse events for dragging
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

    # Event filter to forward label events to the widget for dragging
    def eventFilter(self, source, event):
        if source == self.label:
            if event.type() == event.Type.MouseButtonPress:
                self.mousePressEvent(event)
                return True
            elif event.type() == event.Type.MouseMove:
                self.mouseMoveEvent(event)
                return True
            elif event.type() == event.Type.MouseButtonRelease:
                self.mouseReleaseEvent(event)
                return True
            elif event.type() == event.Type.MouseButtonDblClick:
                self.mouseDoubleClickEvent(event)
                return True
        return super().eventFilter(source, event)   

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

# ----------------- CUSTOM LOG VIEW WITH WATERMARK -----------------
class WatermarkedDeveloperContactView(QTextEdit):
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
        font = QFont("Consolas", 24, QFont.Weight.Bold)
        painter.setFont(font)

        # Calculate text position for perfect centering
        text_rect = self.rect()
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, self.watermark_text)
        painter.end()

# ----------------- CUSTOM WATERMARKED WIDGET -----------------
class WatermarkedBackgroundWidget(QWidget):
    def __init__(self, watermark_text="Nectar-X-Studio", parent=None):
        super().__init__(parent)
        self.watermark_text = watermark_text

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(12)

        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: black;
                font-size: 14px;
                border-radius: 8px;
                padding: 10px;
            }
        """)

    def paintEvent(self, event):
        """Draw watermark centered horizontally and vertically in the background."""
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Full red watermark
        painter.setPen(QColor("#eab676"))
        font = QFont("Consolas", 30, QFont.Weight.Bold)
        painter.setFont(font)

        text_rect = self.rect()
        painter.drawText(
            text_rect,
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter,
            self.watermark_text
        )
        painter.end()


#------------------------------------------------------------------------------
# Class Threads / Signal
#------------------------------------------------------------------------------

AUTH_KEY = "NEC-892657"

class StreamClientWorker(QThread):
    chunk_received = pyqtSignal(str)    # partial text
    finished_response = pyqtSignal(str) # full text or final

    def __init__(self, prompt: str, parent=None):
        super().__init__(parent)
        self.prompt = prompt
        self._stop = False

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", 5005))

            payload = f"{AUTH_KEY} {self.prompt}".encode("utf-8")
            s.sendall(payload)

            buffer = b""

            while not self._stop:
                data = s.recv(1024)
                if not data:
                    break

                buffer += data

                if b"<<END_OF_RESPONSE>>" in buffer:
                    break

                chunk = data.decode("utf-8", errors="ignore")
                self.chunk_received.emit(chunk)

        except Exception as e:
            self.finished_response.emit(f"Error: {e}")
        finally:
            s.close()
            self.finished_response.emit("")  # signal completion only

    def stop(self):
        self._stop = True

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

class RepoSearchThread(QThread):
    search_complete = pyqtSignal(list)
    search_failed = pyqtSignal(str)

    def __init__(self, query, limit=5):
        super().__init__()
        self.query = query
        self.limit = limit  # Number of repos to load at once
        self.offset = 0  # Starting offset for pagination

    def run(self):
        url = f'https://huggingface.co/api/models?search={self.query}&full=1&limit={self.limit}&start={self.offset}'
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            repos = response.json()
            if not repos:
                self.search_failed.emit('No repositories found for the search query.')
                return

            results = []

            # Fetch details for each repo concurrently
            def fetch_info(repo):
                repo_id = repo.get('id', 'Unknown')
                tags = repo.get('tags') or repo.get('cardData', {}).get('tags', [])
                tags_str = ', '.join(tags) if tags else 'None'
                info = self.get_model_info(repo_id)
                downloads = info.get('downloads', 'N/A')
                return {'id': repo_id, 'description': f'Tags: {tags_str}', 'downloads': downloads}

            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(fetch_info, repo) for repo in repos]
                for future in as_completed(futures):
                    try:
                        results.append(future.result())
                    except Exception:
                        continue

            self.offset += self.limit  # Update offset for the next batch
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

# Worker signals
class WorkerSignals(QObject):
    image_loaded = pyqtSignal(QPixmap)

# Background worker to fetch image
class ImageLoader(QRunnable):
    def __init__(self, url, callback):
        super().__init__()
        self.url = url
        self.signals = WorkerSignals()
        self.signals.image_loaded.connect(callback)

    def run(self):
        try:
            response = requests.get(self.url, timeout=5)
            image = QImage.fromData(response.content)
            pix = QPixmap.fromImage(image)
            self.signals.image_loaded.emit(pix)
        except Exception as e:
            write_to_log(f"Error loading {e}")

class RunnableTask(QRunnable):
    def __init__(self, fn, *args):
        super().__init__()
        self.fn = fn
        self.args = args

    def run(self):
        self.fn(*self.args)

import email.utils

class GmailPollingWorker(QThread):
    new_message = pyqtSignal(str, str, str)  # emits body, sender, timestamp
    error = pyqtSignal(str)

    def __init__(self, google_auth):
        super().__init__()
        self.google_auth = google_auth
        self.running = True
        self.last_message_id = None

    def run(self):
        while self.running:
            try:
                socket.create_connection(("www.google.com", 80), timeout=5)
            except OSError:
                self.error.emit("❌ No internet connection.")
                self.msleep(POLL_INTERVAL_MS)
                continue

            creds = self.google_auth.load_credentials()
            if not creds:
                self.error.emit("❌ Google credentials not found.")
                self.msleep(POLL_INTERVAL_MS)
                continue

            try:
                service = build('gmail', 'v1', credentials=creds)
                result = service.users().messages().list(
                    userId='me', q="from:Zashiron.inc@gmail.com", maxResults=5
                ).execute()
                messages = result.get('messages', [])

                # Sort messages by internalDate ascending
                messages.sort(key=lambda m: int(service.users().messages().get(userId='me', id=m['id']).execute()['internalDate']))

                for msg in messages:
                    msg_id = msg['id']
                    if self.last_message_id and msg_id <= self.last_message_id:
                        continue

                    msg_data = service.users().messages().get(userId='me', id=msg_id, format='raw').execute()
                    raw = base64.urlsafe_b64decode(msg_data['raw'].encode())
                    email_msg = message_from_bytes(raw)

                    # Extract body
                    body = ""
                    if email_msg.is_multipart():
                        for part in email_msg.get_payload():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        body = email_msg.get_payload(decode=True).decode()

                    # Clean body: remove quoted lines like "> hi"
                    lines = [line for line in body.splitlines() if not line.startswith(">")]
                    body_clean = "\n".join(lines).strip()

                    if body_clean:
                        # Extract timestamp
                        ts_tuple = email.utils.parsedate_tz(email_msg['Date'])
                        ts = email.utils.mktime_tz(ts_tuple)
                        timestamp_str = email.utils.formatdate(ts, localtime=True)

                        # Emit: body, sender, timestamp
                        self.new_message.emit(body_clean, "developer", timestamp_str)
                        self.last_message_id = msg_id

            except Exception as e:
                self.error.emit(f"❌ Error fetching replies: {str(e)}")

            self.msleep(POLL_INTERVAL_MS)

#--------------------------------------------------------------------------------
# Main App Logic
#--------------------------------------------------------------------------------

class Card(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('card')
        self.setStyleSheet('''
        QFrame#card {
            background: #151515;
            border-radius: 12px;
        }
        ''')

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
        if hasattr(self, "settings_widget") and self.settings_widget.isVisible():
            return

        # Create a small internal settings widget
        self.settings_widget = QWidget(self)
        self.settings_widget.setWindowTitle("  ")
        self.settings_widget.setFixedSize(300, 320)
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

        # Title
        title_label = QLabel("<h1>App Info</h1>")
        title_label.setFixedHeight(50)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # --- Info body---
        body = QLabel()
        body.setText(
            "<span style='font-size:13px; font-weight:600;'>Nectar-X-Studio</span><br>"
            "<span style='font-size:11px; color:#9ca3af;'>Edition</span> · "
            "<span style='font-size:11px; color:#e5e7eb;'>GPU Optimized</span><br><br>"

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
            "DEVELOPER": "Samuel Ikenna Great",
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

#--------------------------------------------------------------------------------
# Landing Page Class
#--------------------------------------------------------------------------------

class SlideshowCard(QWidget):
    def __init__(self, image_urls, title_text, interval=30000):
        super().__init__()
        self.setWindowOpacity(1.0)
        self.image_urls = image_urls
        self.index = 0
        self.pool = QThreadPool.globalInstance()

        self.setFixedSize(160, 100)
        self.setStyleSheet("background-color: #222; border-radius: 10px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label, 1)

        # Timer for slideshow
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_image)
        self.timer.start(interval)
        self.next_image()

    def next_image(self):
        url = self.image_urls[self.index % len(self.image_urls)]
        worker = ImageLoader(url, self.set_image)
        self.pool.start(worker)
        self.index += 1

    def set_image(self, pix):
        if not pix.isNull():
            self.image_label.setPixmap(pix.scaled(
                self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

class Landing(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(1.0)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28,28,28,28)
        layout.setSpacing(28)

        title = QLabel('Home')
        title.setStyleSheet('color:#ffffff;')
        title.setFont(QFont('Segoe UI', 26, QFont.Weight.Bold))
        layout.addWidget(title)

        # Latest Patch Notes small card
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

        patch_card = Card()
        patch_card.setFixedHeight(90)
        pc_layout = QHBoxLayout(patch_card)
        pc_layout.setContentsMargins(14,10,14,10)
        left_text = QVBoxLayout()
        h1 = QLabel(f'Nectar-X-Studio Patch\nNotes 12.09\nPlatform UUID: {local_hash}') # UUID (USER UNIQUE IDENTIFICATION)
        h1.setStyleSheet('color:#ffffff; font-weight:700;')
        date = QLabel('December 20, 2025')
        date.setStyleSheet('color:#ff6b6b;')
        left_text.addWidget(h1)
        left_text.addWidget(date)
        pc_layout.addLayout(left_text)
        pc_layout.addStretch()
        # small decorative image (use portion of REFERENCE_IMAGE scaled)
        pix = QPixmap(REFERENCE_IMAGE)
        if not pix.isNull():
            badge = QLabel()
            badge.setPixmap(pix.scaledToHeight(70, Qt.TransformationMode.SmoothTransformation))
            pc_layout.addWidget(badge)
        layout.addWidget(patch_card)

        # What's New large card
        big_card = Card()
        big_card.setMinimumHeight(260)
        bc_layout = QHBoxLayout(big_card)
        bc_layout.setContentsMargins(18,18,18,18)

        left = QVBoxLayout()
        tag = QLabel('')
        tag.setStyleSheet('color:#d9a82a; font-weight:700;')
        heading = QLabel("N\nE\nC\nT\nA\nR\n|\nX\n|\nS\nT\nU\nD\nI\nO")
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        heading.setStyleSheet('color:#ffffff; font-weight:800;')
        heading.setWordWrap(True)
        sub = QLabel("")
        sub.setStyleSheet('color:#bdbdbd;')
        left.addWidget(tag)
        left.addWidget(heading)
        left.addWidget(sub)
        left.addStretch()
        bc_layout.addLayout(left, 3)

        icon_path = find_icon('background/halfpic.jpg')

        # Right side image using the REFERENCE_IMAGE (cropped look with diagonal mask)
        right_img_label = QLabel()
        pix2 = QPixmap(icon_path)

        if not pix2.isNull():
            # crop a central area first
            w = pix2.width()
            h = pix2.height()
            cropped = pix2.copy(int(w * 0.3), int(h * 0.21), int(w * 0.6), int(h * 0.8))

            # Scale the image for display
            scaled = cropped.scaledToHeight(820, Qt.TransformationMode.SmoothTransformation)

            # Create a diagonal mask
            mask = QPixmap(scaled.size())
            mask.fill(Qt.GlobalColor.transparent)

            painter = QPainter(mask)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            path = QPainterPath()
            # Create diagonal cut from top-left to bottom-right
            path.moveTo(0, scaled.height() * 0.2)
            path.lineTo(scaled.width(), 0)
            path.lineTo(scaled.width(), scaled.height() * 0.8)
            path.lineTo(0, scaled.height())
            path.closeSubpath()

            painter.fillPath(path, Qt.GlobalColor.white)
            painter.end()

            # Apply mask to create the diagonal effect
            scaled.setMask(mask.createMaskFromColor(Qt.GlobalColor.transparent))

            # Assign final pixmap
            right_img_label.setPixmap(scaled)

        right_img_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        bc_layout.addWidget(right_img_label, 4)

        layout.addWidget(big_card)        
        
        container = QWidget()
        title2 = QLabel("Images")
        title2.setStyleSheet('color:#ffffff;')
        title2.setFont(QFont('Segoe UI', 18, QFont.Weight.Bold))
        hl = QHBoxLayout(container)

        # Example image sets (6 slideshows)
        image_sets = [
            [f"https://picsum.photos/seed/{i*10+j}/200/120" for j in range(5)]
            for i in range(6)
        ]

        for i, urls in enumerate(image_sets):
            thumb = SlideshowCard(urls, f'{i+1}')
            hl.addWidget(thumb)

        hl.addStretch()
        layout.addWidget(title2)
        layout.addWidget(container)
        layout.addStretch()

class MiniCircularLoader(QWidget):
    def __init__(self, size=36, thickness=4):
        super().__init__()
        self.angle = 90        
        self.arc_length = 40
        self.expand = True

        self.thickness = thickness
        self.setFixedSize(size, size)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(12)

    def animate(self):
        self.angle = (self.angle + 8) % 360

        if self.expand:
            self.arc_length += 6
            if self.arc_length >= 220:
                self.expand = False
        else:
            self.arc_length -= 6
            if self.arc_length <= 40:
                self.expand = True

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = self.rect().adjusted(
            self.thickness, self.thickness,
            -self.thickness, -self.thickness
        )

        pen = QPen(QColor(220, 40, 40), self.thickness)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)

        start_deg = self.angle - 90

        painter.drawArc(
            rect,
            int(start_deg * 16),        # startAngle
            int(self.arc_length * 16)   # spanAngle
        )

        painter.end()

#------------------------------------------------------------------------------
# Chat Page Class
#------------------------------------------------------------------------------

class Chat(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(1.0)
        self.sessions_file = 'chat_sessions.json'
        self.chat_sessions = {}
        self.current_session = None
        self.player = None
        self.audio_output = None
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
        color: white;
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
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Left: Collapsible Sidebar / History
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(10, 10, 10, 10)
        self.sidebar_layout.setSpacing(8)
        
        # Initial sidebar width (collapsed)
        self.sidebar.setFixedWidth(0)
        self.sidebar_is_visible = False

        # Sidebar content
        title = QLabel('Chat History')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet('font-size: 20px; font-weight: bold; color: #ffffff; padding: 5px; border-radius: 6px; background-color: #000000; ')
        self.sidebar_layout.addWidget(title)

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
        padding: 8px;
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
        self.history_list.itemClicked.connect(self.load_session)
        self.sidebar_layout.addWidget(self.history_list)

        self.sidebar_layout.addStretch()

        new_chat_button = QPushButton('+ New Chat')
        new_chat_button.clicked.connect(self.create_new_session)
        self.sidebar_layout.addWidget(new_chat_button)
        #self.sidebar_layout.addStretch()

        main_layout.addWidget(self.sidebar)

        # Right: Chat area (flexible)
        self.chat_area = QWidget()
        self.chat_area_layout = QVBoxLayout(self.chat_area)
        self.chat_area_layout.setContentsMargins(10, 10, 10, 10)
        self.chat_area_layout.setSpacing(8)

        # Scrollable chat display
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Fixed background (already has a layout inside WatermarkedBackgroundWidget)
        self.chat_container = WatermarkedBackgroundWidget("Nectar-X-Studio")
        container_layout = self.chat_container.layout  # <-- reuse existing layout
        container_layout.setContentsMargins(0, 0, 0, 0)

        # Scroll area (transparent, scrolls on top)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setStyleSheet("""
            QScrollArea { background: transparent; }
            QWidget { background: transparent; }
        """)

        # Scrolling content (messages)
        self.messages_widget = QWidget()
        self.chat_display = QVBoxLayout(self.messages_widget)
        self.chat_display.setSpacing(12)
        self.chat_display.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.messages_widget)

        # Add scroll area ON TOP of the watermark
        container_layout.addWidget(self.scroll_area)
        self.chat_area_layout.addWidget(self.chat_container)

        self.progress_bar = MiniCircularLoader()
        self.progress_bar.setFixedSize(50, 50)
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
        #self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()

        # Input section
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFixedHeight(50)
        self.input_field.setPlaceholderText("Type your message...")
        self.input_field.returnPressed.connect(self.send_message)
        self.input_field.setStyleSheet("""
        QLineEdit {
        background-color: #ffffff;
        color: #000000;
        border-radius: 6px;
        padding: 10px;
        border: 1px solid None;
        }

        QLineEdit:hover {
        border: 1px solid None;
        background-color: #efefef;
        }
        
        QLineEdit:disabled {
            background-color: #dddddd;
            color: #888888;
        }
        """)
        input_layout.addWidget(self.input_field)

        icon_path_send = find_icon("menu/up.png")
        self.send_button = QPushButton()
        self.send_button.setFixedSize(50, 50)
        self.send_button.setIcon(QIcon(icon_path_send))
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setStyleSheet("""
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
        QPushButton:disabled {
        background-color: #cccccc;
        }
        """)
        input_layout.addWidget(self.send_button)

        # Sidebar Toggle Button
        icon_path_toggle = find_icon("menu/menu.png") if not self.sidebar_is_visible else find_icon("menu/close.png")
        self.toggle_sidebar_button = QPushButton()
        self.toggle_sidebar_button.setFixedSize(50, 50)
        self.toggle_sidebar_button.clicked.connect(self.toggle_sidebar)
        self.toggle_sidebar_button.setStyleSheet("""
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
        input_layout.addWidget(self.toggle_sidebar_button)
        self.update_toggle_icon()

        icon_path_clear = find_icon("menu/close.png")
        self.clear_button = QPushButton()
        self.clear_button.setEnabled(False)
        self.clear_button.setFixedSize(50, 50)
        self.clear_button.setIcon(QIcon(icon_path_clear))
        self.clear_button.clicked.connect(self.clear_everything)
        self.clear_button.setStyleSheet("""
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
        input_layout.addWidget(self.clear_button)

        self.chat_area_layout.addLayout(input_layout)
        main_layout.addWidget(self.chat_area, 1)  # Chat area takes remaining space

        self.setLayout(main_layout)
        self.update_history()

    def scroll_to_bottom(self):
        """Scroll to bottom of chat"""
        QTimer.singleShot(100, lambda: self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        ))

    def toggle_sidebar(self):
        """Toggle sidebar visibility with smooth animation"""
        if self.sidebar_is_visible:
            # Collapse sidebar
            self.sidebar.setFixedWidth(0)
            self.sidebar_is_visible = False
        else:
            # Expand sidebar
            self.sidebar.setFixedWidth(320)
            self.sidebar_is_visible = True
        
        self.update_toggle_icon()
        self.chat_area_layout.update()  # Force layout update

    def update_toggle_icon(self):
        """Update toggle button icon based on sidebar state"""
        if self.sidebar_is_visible:
            # Show collapse icon
            icon_path = find_icon("menu/back.png")
        else:
            # Show expand icon
            icon_path = find_icon("menu/forward.png")  # or "menu/sidebar.png"
        
        if icon_path and os.path.exists(icon_path):
            self.toggle_sidebar_button.setIcon(QIcon(icon_path))
        else:
            # Fallback text
            self.toggle_sidebar_button.setText("☰" if not self.sidebar_is_visible else "✕")
            self.toggle_sidebar_button.setFont(QFont("Arial", 16))

    def load_session(self, session_item):
        session_name = session_item.text()
        if session_name not in self.chat_sessions:
            return

        self.current_session = session_name
        self.clear_screen()

        for entry in self.chat_sessions.get(session_name, []):
            # each entry looks like "You: hi" or "AI: something"
            if ": " in entry:
                prefix, text = entry.split(": ", 1)
                prefix = prefix.strip().lower()
                if prefix == "you":
                    sender = "user"
                elif prefix == "ai":
                    sender = "ai"
                else:
                    sender = "error"
            else:
                sender, text = "error", entry

            self.display_message(text, sender)

        # scroll to bottom
        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        )

    def create_new_session(self, session_name=None):
        from datetime import datetime
        if not session_name:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            session_name = f"Chat {timestamp}"
        
        # Ensure unique name
        counter = 1
        original_name = session_name
        while session_name in self.chat_sessions:
            session_name = f"{original_name} ({counter})"
            counter += 1
        
        self.current_session = session_name
        self.chat_sessions[session_name] = []
        self.clear_screen()
        self.update_history()
        self.save_sessions()

    def save_sessions(self):
        """Save chat sessions to JSON file"""
        try:
            os.makedirs('logs', exist_ok=True)  # Ensure logs dir exists
            with open(self.sessions_file, 'w', encoding='utf-8') as file:
                json.dump(self.chat_sessions, file, indent=4, ensure_ascii=False)
        except Exception as e:
            write_to_log(f'Error saving chat sessions: {e}', file_path='logs/errors.log')
            Notify(f"Error saving chat sessions: {e}", parent=self)

    def clear_screen(self):
        while self.chat_display.count():
            item = self.chat_display.takeAt(0)
            w = item.widget()
            if w is not None:
                w.deleteLater()
        self.progress_bar.hide()

    def append_to_session(self, message: str):
        """
        Append a message to the current session.
        Ensures there is always a valid session key.
        """
        # If no active session, create a default one
        if not self.current_session:
            self.current_session = "New Chat"
            # avoid overwriting existing "New Chat"
            base = self.current_session
            counter = 1
            while self.current_session in self.chat_sessions:
                self.current_session = f"{base} ({counter})"
                counter += 1

        # Ensure list exists for this session
        self.chat_sessions.setdefault(self.current_session, [])
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
        self.progress_bar.show()
        self.save_sessions()
        self.update_history()
        self.disable_input()

        # create an empty AI bubble to stream into
        ai_label = self.display_message("", 'ai', return_label=True)
        ai_label._plain_text = ""   # custom attribute to hold raw text

        # start streaming client
        self.stream_worker = StreamClientWorker(user_text, parent=self)

        def on_chunk(chunk: str, lbl=ai_label):
            if not chunk:
                return
            # accumulate plain text
            current_plain = getattr(lbl, "_plain_text", "")
            new_plain = current_plain + chunk
            lbl._plain_text = new_plain

            # beautify + markdown -> HTML
            pretty_md = beautify_markdown(new_plain)
            html = markdown.markdown(
                pretty_md,
                extensions=["extra", "sane_lists", "nl2br", LinkifyExtension()]
            )
            lbl.setText(html)
            lbl.setTextFormat(Qt.TextFormat.RichText)

            self.scroll_area.verticalScrollBar().setValue(
                self.scroll_area.verticalScrollBar().maximum()
            )

        def on_finished(final_text: str):
            # final_text is the same as lbl._plain_text (if server sends plain text)
            if self.current_session not in self.chat_sessions:
                self.chat_sessions[self.current_session] = []
            self.chat_sessions[self.current_session].append(f'AI: {final_text}')
            self.save_sessions()
            self.progress_bar.hide()
            self.enable_input()

        self.stream_worker.chunk_received.connect(on_chunk)
        self.stream_worker.finished_response.connect(on_finished)
        self.stream_worker.start()

    from PyQt6.QtGui import QPixmap

    def display_message(self, text, sender, return_label=False):
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(10, 10, 10, 10)
        row_layout.setSpacing(6)

        bubble = QFrame()
        bubble.setFixedWidth(600)
        bubble_layout = QVBoxLayout(bubble)
        bubble_layout.setContentsMargins(10, 10, 10, 10)

        message_label = QLabel()
        message_label.setWordWrap(True)
        #message_label.setOpenExternalLinks(False)
        message_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse |
            Qt.TextInteractionFlag.LinksAccessibleByMouse
        )

        message_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        message_label.setOpenExternalLinks(False)
        message_label.linkActivated.connect(self.handle_link_click)

        # Pre-process to clean/structure the Markdown
        message_label.setTextFormat(Qt.TextFormat.RichText)
        message_label.setText(markdown.markdown(text, extensions=["extra", "sane_lists", "nl2br"])
                            if text else "")
        bubble_layout.addWidget(message_label)

        html = markdown.markdown(text, extensions=["extra", "sane_lists", "nl2br"]) if text else ""
        message_label.setTextFormat(Qt.TextFormat.RichText)
        message_label.setText(html)
        bubble_layout.addWidget(message_label)

        # webview container (always second item in bubble_layout)
        webview_container = QWidget()
        webview_layout = QVBoxLayout(webview_container)
        webview_layout.setContentsMargins(0, 8, 0, 0)
        webview_layout.setSpacing(8)
        bubble_layout.addWidget(webview_container)

        # copy button row (bottom-right)
        copy_row = QHBoxLayout()
        copy_row.addStretch()
        
        icon_path_copy = find_icon("menu/copy.png")
        copy_btn = QPushButton()
        copy_btn.setFixedSize(24, 24)
        copy_btn.setToolTip("Copy")
        copy_btn.setIcon(QIcon(icon_path_copy))
        copy_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: #ffffff;
                color: #aaaaaa;
                font-size: 14px;
            }
            QPushButton:hover {
                color: #2d2d2d;
            }
        """)

        def do_copy(lbl):
            cb = QApplication.clipboard()
            Inform("Copied", parent=self)
            raw_html = lbl.text()                 # QLabel rich text
            plain = html_to_text(raw_html)        # strip tags
            cb.setText(plain, mode=QClipboard.Mode.Clipboard)

        copy_btn.clicked.connect(
            lambda *args, lbl=message_label: do_copy(lbl)
        )

        copy_row.addWidget(copy_btn)

        # Avatar/icon label
        icon_label = QLabel()
        icon_label.setStyleSheet("background-color: #000000")
        icon_label.setFixedSize(50, 50)

        if sender == 'user':
            bubble.setStyleSheet("""
                background-color: #424343;
                color: white;
                padding: 10px;
                border-radius: 6px;
            """)
            message_label.setAlignment(Qt.AlignmentFlag.AlignRight)

            # icon on RIGHT of bubble
            if (icon_path := find_icon("menu/user.png")):
                pix = QPixmap(icon_path).scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio,
                                                Qt.TransformationMode.SmoothTransformation)
                icon_label.setPixmap(pix)

            row_layout.addStretch()
            row_layout.addWidget(self.progress_bar)
            row_layout.addWidget(bubble)
            row_layout.addWidget(icon_label)

        elif sender == 'ai':
            bubble.setStyleSheet("""
                background-color: #2d2d2d;
                color: white;
                padding: 10px;
                border-radius: 6px;
            """)
            message_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

            # icon on LEFT of bubble
            if (icon_path := find_icon("menu/ai.png")):
                pix = QPixmap(icon_path).scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio,
                                                Qt.TransformationMode.SmoothTransformation)
                icon_label.setPixmap(pix)
            
            icon_path_continue = find_icon("menu/continue.png")
            continue_btn = QPushButton()
            continue_btn.setFixedSize(26, 26)
            continue_btn.setIcon(QIcon(icon_path_continue))
            continue_btn.setToolTip("Continue generating")
            continue_btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    background-color: #ffffff;
                    color: #aaaaaa;
                    font-size: 14px;
                }
                QPushButton:hover {
                    color: #2d2d2d;
                }
            """)

            continue_btn.clicked.connect(self.do_continue)
            copy_row.addWidget(continue_btn)

            row_layout.addWidget(icon_label)
            row_layout.addWidget(bubble)
            row_layout.addStretch()

        elif sender == 'error':
            bubble.setStyleSheet("""
                background-color: #ff5555;
                color: white;
                padding: 10px;
                border-radius: 6px;
            """)
            message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            row_layout.addStretch()
            row_layout.addWidget(bubble)
            row_layout.addStretch()

        bubble_layout.addLayout(copy_row)

        self.chat_display.addLayout(row_layout)

        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        )
        if return_label:
            return message_label

    def handle_link_click(self, url_str: str):
        box = QMessageBox(self)
        box.setWindowTitle("Open link")
        box.setText(f"How would you like to open this link?")
        #internal_btn = box.addButton("Internal Browser", QMessageBox.ButtonRole.AcceptRole)
        external_btn = box.addButton("External Browser", QMessageBox.ButtonRole.DestructiveRole)
        cancel_btn   = box.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
        box.exec()

        clicked = box.clickedButton()
        if clicked is cancel_btn:
            return

        if clicked is external_btn:
            QDesktopServices.openUrl(QUrl(url_str))
            return

        #if clicked is internal_btn:
        #    
        #    self.webview = WEBVIEW(url_str)
        #    self.webview.show()

    def do_continue(self):
        # This text will be visible in user bubble
        continue_text = "continue generating"

        # Show as user bubble + update session
        self.display_message(continue_text, 'user')
        if self.current_session is None:
            self.current_session = continue_text[:20]
            self.chat_sessions.setdefault(self.current_session, [])
        self.append_to_session(f'You: {continue_text}')
        self.save_sessions()
        self.update_history()
        self.disable_input()

        # Start streaming a new AI answer using SAME flow as send_message
        self.progress_bar.show()

        ai_label = self.display_message("", 'ai', return_label=True)
        ai_label._plain_text = ""

        self.stream_worker = StreamClientWorker(continue_text, parent=self)

        def on_chunk(chunk: str, lbl=ai_label):
            current_plain = getattr(lbl, "_plain_text", "")
            new_plain = current_plain + chunk
            lbl._plain_text = new_plain

            pretty_md = beautify_markdown(new_plain)
            html = markdown.markdown(
                pretty_md,
                extensions=["extra", "sane_lists", "nl2br", LinkifyExtension()]
            )
            lbl.setText(html)
            lbl.setTextFormat(Qt.TextFormat.RichText)
            self.scroll_area.verticalScrollBar().setValue(
                self.scroll_area.verticalScrollBar().maximum()
            )

        def on_finished(final_text: str):
            if self.current_session not in self.chat_sessions:
                self.chat_sessions[self.current_session] = []
            self.chat_sessions[self.current_session].append(f'AI: {final_text}')
            self.save_sessions()
            self.progress_bar.hide()
            self.enable_input()

        self.stream_worker.chunk_received.connect(on_chunk)
        self.stream_worker.finished_response.connect(on_finished)
        self.stream_worker.start()

    def disable_input(self):
        self.input_field.setEnabled(False)
        self.send_button.setEnabled(False)

    def enable_input(self):
        self.input_field.setEnabled(True)
        self.send_button.setEnabled(True)

    def update_history(self):
        """Update history list safely"""
        self.history_list.blockSignals(True)
        self.history_list.clear()
        
        # Use sorted keys for consistent order
        sorted_sessions = sorted(self.chat_sessions.keys())
        for session_name in sorted_sessions:
            item = QListWidgetItem(session_name)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
            self.history_list.addItem(item)
        
        # Highlight current session
        if self.current_session and self.current_session in self.chat_sessions:
            for i in range(self.history_list.count()):
                item = self.history_list.item(i)
                if item.text() == self.current_session:
                    self.history_list.setCurrentItem(item)
                    break
        
        self.history_list.blockSignals(False)

    def rename_session(self, item):
        old_name = item.text().strip()
        if not old_name:
            return

        dialog = QDialog(self)
        dialog.setWindowTitle('Rename or Delete Session')
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
            confirm.setStandardButtons(QMessageBox.StandardButton.Yes |
                                    QMessageBox.StandardButton.No)
            confirm.setDefaultButton(QMessageBox.StandardButton.No)
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

            if confirm.exec() == QMessageBox.StandardButton.Yes:
                if old_name in self.chat_sessions:
                    del self.chat_sessions[old_name]
                if self.current_session == old_name:
                    self.current_session = None
                    self.clear_screen()
                matched_items = self.history_list.findItems(
                    old_name, Qt.MatchFlag.MatchExactly
                )
                if matched_items:
                    self.history_list.takeItem(self.history_list.row(matched_items[0]))
                self.save_sessions()
                self.update_history()
                dialog.accept()

        delete_button.clicked.connect(on_delete)

        def on_accept():
            new_name = input_field.text().strip()
            if not new_name or new_name == old_name:
                dialog.reject()
                return

            if new_name in self.chat_sessions:
                warning = QMessageBox(self)
                warning.setWindowTitle('Duplicate Name')
                warning.setText('A session with this name already exists.')
                warning.setIcon(QMessageBox.Icon.Warning)
                warning.setStandardButtons(QMessageBox.StandardButton.Ok)
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

            # rename key in backing dict
            self.chat_sessions[new_name] = self.chat_sessions.pop(old_name)

            # update list item text
            item.setText(new_name)

            # keep current_session in sync
            if self.current_session == old_name:
                self.current_session = new_name

            self.save_sessions()
            self.update_history()
            dialog.accept()

        button_box.accepted.connect(on_accept)
        button_box.rejected.connect(dialog.reject)

        dialog.exec()

    def load_sessions(self):
        """Load chat sessions from JSON file"""
        if os.path.exists(self.sessions_file):
            try:
                with open(self.sessions_file, 'r', encoding='utf-8') as file:
                    self.chat_sessions = json.load(file)
            except Exception as e:
                write_to_log(f'Error loading chat sessions: {e}', file_path='logs/errors.log')
                self.chat_sessions = {}
                Notify(f"Error loading chat sessions: {e}", parent=self)
        else:
            self.chat_sessions = {}

    def clear_screen(self):
        """Remove all message widgets from the chat display."""
        while self.chat_display.count():
            item = self.chat_display.takeAt(0)
            w = item.widget()
            if w is not None:
                w.deleteLater()
            else:
                # if there is a nested layout (shouldn't be, but be safe)
                sub_layout = item.layout()
                if sub_layout is not None:
                    while sub_layout.count():
                        sub_item = sub_layout.takeAt(0)
                        sw = sub_item.widget()
                        if sw is not None:
                            sw.deleteLater()

    def clear_everything(self):
        """Clear display and reset to new chat state (keep scroll area/layout)."""
        self.clear_screen()
        self.current_session = None
        self.enable_input()
        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().minimum()
        )
        
#------------------------------------------------------------------------------------
# Broad Cast Class
#------------------------------------------------------------------------------------

class Broadcast(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(1.0)
        self.setWindowTitle('🧠 AlphaLLM Broadcast Engine')
        self.resize(700, 600)

        # Local TCP server
        self.server_running = False
        self.server_socket = None
        self.broadcast_port = 8012
        self.broadcast_base_ip = '127.0.0.1'

        # FastAPI server
        self.fastapi_app = FastAPI()
        self.fastapi_host = f'{get_local_ip()}'
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

        self.qrcode_btn = QPushButton("NectarChat")
        self.qrcode_btn.clicked.connect(self.generate_qr_code)

        route_layout.addWidget(self.route_input)
        route_layout.addWidget(self.method_input)
        route_layout.addWidget(self.add_route_btn)
        route_layout.addWidget(self.viewer_btn)
        route_layout.addWidget(self.qrcode_btn)
        self.api_config_layout.addLayout(route_layout)
        layout.addLayout(self.api_config_layout)

        # Packet log
        layout.addWidget(QLabel('📦 Packet Log:'))
        self.packet_log = QTextEdit()
        self.packet_log.setReadOnly(True)
        layout.addWidget(self.packet_log)

        self.setLayout(layout)

    def Api_view(self):
        import webbrowser
        url = "https://github.com/headlessripper/Nectar-X-Studio/wiki/Documentation"
        webbrowser.open(url)

    def generate_qr_code(self):
        import qrcode
        url = f"http://{self.fastapi_host}:{self.fastapi_port}"

        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")

        qr_path = "qrcode.png"
        img.save(qr_path)

        pixmap = QPixmap(qr_path)
        msg_box = QMessageBox()
        msg_box.setWindowTitle("NectarChat")
        msg_box.setWindowIcon(QIcon(find_icon('background/NectarX.png') or 'background/NectarX.png'))
        msg_box.setText("Please scan this QR code with NectarChat.")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setIconPixmap(pixmap)
        msg_box.exec()

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

#------------------------------------------------------------------------------------
# LLM Engine Class
#------------------------------------------------------------------------------------

import faiss

class RAGEngine:
    def __init__(self, model_path=TRANSFORMER_MODEL_PATH):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Embedding model not found: {model_path}")

        self.embedder = SentenceTransformer(model_path)
        self.index = None
        self.docs = []

    def add_documents(self, texts):
        embeddings = self.embedder.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        self.docs.extend(texts)

        if self.index is None:
            self.index = faiss.IndexFlatIP(embeddings.shape[1])  # cosine similarity

        self.index.add(embeddings)

    def retrieve(self, query, top_k=3):
        if self.index is None or not self.docs:
            return []

        q_emb = self.embedder.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        scores, indices = self.index.search(q_emb, top_k)
        return [self.docs[i] for i in indices[0] if i < len(self.docs)]

# ----------- Web RAG -----------

# FIXED: Safe GPU initialization with error handling + memory management
def load_embedding_model_safely(model_path):
    try:
        # Check CUDA availability and version
        if torch.cuda.is_available():
            write_to_log(f"CUDA available Posting: {torch.cuda.get_device_name(0)}")
            write_to_log(f"CUDA version Booting: {torch.version.cuda}")
        
            torch.cuda.empty_cache()  # Clear any existing cache
            torch.cuda.synchronize()  # Sync CUDA operations
        
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        write_to_log(f"Loading engine model on device: {device}")
        toast = Notification(
            app_id="Nectar-X-Studio",
            title="WebRAG Engine",
            msg=f"Loading engine model on device: {device}",
            icon=find_icon('background/NectarX.png'),
            duration="short"
        )
        toast.set_audio(audio.SMS, loop=False)
        toast.show()
        
        model = SentenceTransformer(model_path, device=device)
        
        # Warmup to catch CUDA issues early
        dummy_text = ["test"]
        model.encode(dummy_text, batch_size=1, show_progress_bar=False)
        write_to_log("Engine Model loaded and warmed up successfully!")
        toast = Notification(
            app_id="Nectar-X-Studio",
            title="WebRAG Engine",
            msg=f"Engine Model loaded and warmed up successfully!",
            icon=find_icon('background/NectarX.png'),
            duration="short"
        )
        toast.set_audio(audio.SMS, loop=False)
        toast.show()
        return model, device
        
    except Exception as e:
        write_to_log(f"GPU failed ({e}), falling back to CPU")
        toast = Notification(
            app_id="Nectar-X-Studio",
            title="WebRAG Engine",
            msg=f"GPU failed ({e}), falling back to CPU",
            icon=find_icon('background/NectarX.png'),
            duration="short"
        )
        toast.set_audio(audio.SMS, loop=False)
        toast.show()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        return SentenceTransformer(model_path, device='cpu'), 'cpu'

embedding_model, device = load_embedding_model_safely(TRANSFORMER_MODEL_PATH)

class WebRAG:
    def __init__(self, rag_engine, google_api_key="AIzaSyD4Au69N-YV36kXA3g1YQcD-n55jpFf6Y8", google_cse_id="117a05283b97b4f08"):
        self.rag_engine = rag_engine
        self.google_api_key = google_api_key
        self.google_cse_id = google_cse_id
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})

    def __del__(self):
        if hasattr(self, 'session'):
            self.session.close()
        torch.cuda.empty_cache()  # Clean GPU memory

    # ------------------ Google News search ------------------
    def google_news_search(self, query, when="1d", max_results=5):
        q = requests.utils.quote(query)
        url = f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)
        entries = feed.entries[:max_results]
        news_results = []
        for e in entries:
            news_results.append({
                "link": getattr(e, "link", ""),
                "title": getattr(e, "title", ""),
                "snippet": getattr(e, "summary", ""),
                "published": getattr(e, "published", "")
            })
        return news_results

    # ------------------ Google Search with Default Recency ------------------
    def google_search(self, query, max_results=5, recent="m1"):
        if not self.google_api_key or not self.google_cse_id:
            raise ValueError("Google API key and CSE ID are required for Google search.")
        search_results = []
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.google_api_key,
            "cx": self.google_cse_id,
            "q": query,
            "num": min(max_results, 10)
        }
        params["dateRestrict"] = recent
        response = self.session.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        for item in data.get("items", []):
            search_results.append({
                "link": item.get("link"),
                "snippet": item.get("snippet", ""),
                "displayLink": item.get("displayLink", "")
            })
        return search_results

    # ------------------ Concurrent Page Fetching ------------------
    def fetch_pages_concurrent(self, urls, max_workers=8, max_chars=4000):  # Reduced workers
        def fetch_single(url):
            try:
                resp = self.session.get(url, timeout=8)  # Reduced timeout
                resp.raise_for_status()
                soup = BeautifulSoup(resp.text, "html.parser")
                for tag in soup(["script", "style", "nav", "footer", "header"]):
                    tag.decompose()
                return " ".join(soup.stripped_strings)[:max_chars]
            except Exception:
                return ""
        
        if not urls:
            return []
        
        pages = [None] * len(urls)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_idx = {executor.submit(fetch_single, url): i for i, url in enumerate(urls)}
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                pages[idx] = future.result()
        return pages

    # ------------------ FIXED Validation with Safe GPU Encoding ------------------
    def validate_results(self, query, results):
        if not results:
            return []

        now = datetime.now()
        current_year = str(now.year)
        outdated_keywords = ["Snapdragon 8 Gen 2", "Snapdragon 8 Gen 3", "2023", "2022"]
        tech_domains = ["samsung.com", "gsmarena.com", "techradar.com", "91mobiles.com", "phonearena.com", "sammyfans.com"]

        # 1) Concurrently fetch pages
        urls = [r["link"] for r in results]
        page_texts = self.fetch_pages_concurrent(urls)

        # 2) Build texts + filter outdated
        texts = []
        valid_indices = []
        for i, r in enumerate(results):
            page_text = page_texts[i] or ""
            text = r["snippet"] + " " + page_text
            
            if any(keyword.lower() in text.lower() for keyword in outdated_keywords):
                continue
            
            texts.append(text)
            valid_indices.append(i)

        if not texts:
            return []

        # 3) SAFE GPU encode with error handling + smaller batch
        try:
            if device == 'cuda':
                torch.cuda.empty_cache()
            
            # Smaller batch_size for stability + normalize_embeddings=False
            text_embs = embedding_model.encode(
                texts, 
                batch_size=16,  # Reduced from 32
                show_progress_bar=False, 
                convert_to_tensor=True,
                normalize_embeddings=True
            )
            
            if device == 'cuda':
                torch.cuda.empty_cache()
                
        except RuntimeError as e:
            if "CUDA" in str(e):
                print(f"GPU encoding failed: {e}. Falling back to CPU.")
                torch.cuda.empty_cache()
                text_embs = embedding_model.encode(
                    texts, 
                    batch_size=8, 
                    device='cpu',
                    show_progress_bar=False, 
                    convert_to_tensor=False
                )
            else:
                raise

        # 4) Score with bonuses
        query_emb = embedding_model.encode(query, batch_size=1, show_progress_bar=False, convert_to_tensor=True)
        scored_results = []

        for j, text in enumerate(texts):
            i = valid_indices[j]
            score = util.cos_sim(query_emb, text_embs[j]).item()
            
            # Recency parsing
            date_matches = re.findall(r'\b(2025|2024|2023|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b', text, re.I)
            recency_bonus = 0
            if current_year in date_matches:
                recency_bonus += 3.0
            elif "2024" in date_matches:
                recency_bonus += 1.5
            elif any(month in date_matches for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
                recency_bonus += 1.0

            domain_bonus = 0.8 if any(domain in results[i].get("displayLink", "").lower() for domain in tech_domains) else 0

            total_score = score + recency_bonus + domain_bonus
            scored_results.append({
                "link": results[i]["link"],
                "snippet": results[i]["snippet"],
                "content": page_texts[i] or "",
                "score": total_score,
                "recency_bonus": recency_bonus,
                "domain_bonus": domain_bonus
            })

        scored_results.sort(key=lambda x: x["score"], reverse=True)
        return scored_results[:3]

    # ------------------ Add Web Docs to RAG ------------------
    def add_web_docs(self, query, num_results=5, recent="w1"):
        if not self.rag_engine:
            print("RAG engine not initialized")
            return

        try:
            search_results = self.google_search(query, num_results, recent)
        except Exception as e:
            print(f"Google web search failed: {e}")
            search_results = []

        try:
            news_results_raw = self.google_news_search(query, when="1d", max_results=num_results)
        except Exception as e:
            print(f"Google News search failed: {e}")
            news_results_raw = []

        news_results = [
            {
                "link": r["link"],
                "snippet": r.get("snippet", r.get("title", "")),
                "displayLink": r.get("link", "")
            }
            for r in news_results_raw
            if r.get("link")
        ]

        validated_web = self.validate_results(query, search_results)
        validated_news = self.validate_results(query, news_results)

        combined_validated = validated_web + validated_news
        if not combined_validated:
            # toast notification here
            return

        docs = []
        for result in combined_validated:
            combined_text = result["snippet"] + "\n\n" + result["content"]
            if combined_text.strip():
                docs.append(combined_text)

        if docs:
            self.rag_engine.add_documents(docs)
            top_score = combined_validated[0]["score"]
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="WebRAG Info",
                msg=f"Added {len(docs)} recent web/news documents (top score: {top_score:.1f})",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()
        else:
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="WebRAG Warning",
                msg="No recent/relevant documents found. Try different query.",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()

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

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [os.path.join(script_dir, icon_name), os.path.join(script_dir, 'menu', icon_name), os.path.abspath(os.path.join(script_dir, os.pardir, icon_name))]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        else:
            return None

    def init_ui(self):
        import qtawesome as qta
        main_layout = QHBoxLayout()
        from PyQt6.QtWidgets import QSizePolicy
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(12)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        icon_path51 = self.find_icon('menu/net.png')
        icon_path52 = self.find_icon('menu/AI.png')
        icon_path53 = self.find_icon('menu/sett.png')
        icon_path54 = self.find_icon('menu/plus.png')
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
                client_socket.send(b'No data received')
                return

            if not data.startswith(AUTH_KEY):
                client_socket.send(b"Unauthorized")
                return

            data = data[len(AUTH_KEY):].strip()

            if data.startswith('LOAD_MODEL::'):
                self.append_message('user', data)
                client_socket.send(b'OK')
                return

            # Store user's input
            self.append_message('user', data)

            # Retrieve all messages from RAM
            query = data  # from client
            conversation_list = self.read_all_messages()

            # Default system behavior
            conversation_list.insert(0, sys_msgs.NORMAL_SYSTEM_PROMPT)

            # RAG retrieval
            if hasattr(self, "rag_engine"):
                retrieved_docs = self.rag_engine.retrieve(data)
                # Include retrieved documents in conversation
                for doc in retrieved_docs:
                    conversation_list.append({"role": "system", "content": f"[Context] {doc}"})
                #Inform(f"Loading Model... Found context: {retrieved_docs}", parent=self)

            # 🤖 Ask model if web search is needed *before* generating query
            use_web = model_decides_web_rag(self.llm_instance, query)

            if use_web:
                # 🔎 Generate search query *only when needed*
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

                # Switch system prompt to elite web mode
                conversation_list.insert(0, WEB_RAG_SYSTEM_PROMPT)

                web_rag = WebRAG(self.rag_engine)

                # ALWAYS USE GENERATED SEARCH QUERY
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
                stream=True
            )

            full_reply = []
            for chunk in stream:
                delta = chunk["choices"][0]["delta"]
                if "content" in delta:
                    token = delta["content"]
                    full_reply.append(token)
                    # stream tokens for real-time UI
                    client_socket.send(token.encode("utf-8"))

            # join, encode, and send end marker
            reply = "".join(full_reply).strip()
            client_socket.sendall(b"\n<<END_OF_RESPONSE>>")  # End marker only at finish

            # Store response in memory
            self.append_message('assistant', reply)

        except Exception as e:
            client_socket.send(f"Error: {e}".encode('utf-8'))

        finally:
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

#------------------------------------------------------------------------------------
# Download Model Class
#------------------------------------------------------------------------------------

class RepoCard(QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, repo_id, description, downloads):
        super().__init__()
        self.setWindowOpacity(1.0)
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
        else:
            self.card_frame.setFixedWidth(965)

    def changeEvent(self, event):
        from PyQt6.QtCore import Qt, QEvent
        if event.type() == QEvent.Type.WindowStateChange:
            if self.isMaximized():
                self.card_frame.setFixedWidth(self.original_width + 100)
            else:
                self.card_frame.setFixedWidth(self.original_width)
        super().changeEvent(event)

class ModelCard(QWidget):
    clicked = pyqtSignal(str, bool)

    def __init__(self, model_name, model_size, too_large=False, parent=None):
        super().__init__(parent)
        self.setWindowOpacity(1.0)
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

class ModelViewerWindow(QWidget):
    def __init__(self, repo_id, files, on_model_click_callback):
        super().__init__()
        self.setWindowOpacity(1.0)
        self.setWindowTitle(f'{repo_id}')
        self.setMinimumSize(600, 400)
        self.setStyleSheet('background-color: #1e1e1e; color: white;')
        icon_path = find_icon('background/NectarX.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
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
        else:
            self.on_model_click_callback(model_path)

class ToggleButton(QCheckBox):
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
        """Update the circle position during animation."""
        self.circle_x = value
        self.update()

    def animate_slider(self, state):
        """Animate the toggle switch movement."""
        checked = state == Qt.Checked
        start_x = 2 if not checked else 22
        end_x = 22 if not checked else 2
        self.animation.stop()
        self.animation.setStartValue(start_x)
        self.animation.setEndValue(end_x)
        self.animation.start()

    def paintEvent(self, event):
        """Custom paint event for drawing the switch."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor('#ff0000') if self.isChecked() else QColor('#000000'))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, 40, 20, 10, 10)
        painter.setBrush(QColor('#fff'))
        painter.drawEllipse(self.circle_x, 2, 16, 16)
        painter.end()

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
        icon_path0 = find_icon('menu/play.png')
        icon_path1 = find_icon('menu/pause.png')
        icon_path2 = find_icon('menu/cancel.png')
        icon_path3 = find_icon('menu/folder.png')
        icon_path4 = find_icon('menu/delete.png')
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
            # msg.setWindowIcon(QIcon("icons/warning.png"))

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
        self.setWindowTitle('Nectar-X-Studio')
        self.setMinimumSize(600, 400)
        self.setWindowOpacity(1.0)
        self.setStyleSheet('background-color: #121212; color: white;')
        icon_path = find_icon('background/NectarX.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
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

class Downloader(QWidget):
    def __init__(self):
        from PyQt6.QtCore import QSettings
        super().__init__()
        self.downloads_window = DownloadsWindow()
        self.download_folder = self.get_or_create_nectarhub_folder()
        self.setWindowOpacity(1.0)
        os.makedirs(self.download_folder, exist_ok=True)
        self.settings = QSettings('Zashiron', 'NDM (Nectar Download Manager)')
        self.completed_downloads = self.load_history()
        # Initialization for search parameters
        self.offset = 0
        self.limit = 5
        self.search_query = ""
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
        self.gguf_checkbox = ToggleButton()
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
        self.repo_scroll.setStyleSheet("""
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
        self.repo_scroll.setWidget(self.repo_container_widget)

        self.model_container_widget = QWidget()
        self.model_container_layout = QVBoxLayout()
        self.model_container_widget.setLayout(self.model_container_layout)
        self.model_scroll = QScrollArea()
        self.model_scroll.setWidgetResizable(True)
        self.model_scroll.setStyleSheet("""
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

        # Connect scroll event for dynamic loading
        self.repo_scroll.verticalScrollBar().valueChanged.connect(self.check_scroll_position)

    def toggle_gguf_mode(self):
        if self.gguf_checkbox.isChecked():
            self.settings.value('append_gguf', True, type=bool)
        else:
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

        # Store the original query
        self.search_query = query

        self.offset = 0

        self.repo_search_thread = RepoSearchThread(query, limit=self.limit)
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

    def load_more_repositories(self):
        # Use the stored search query and increment the offset
        if not self.search_query:
            return  # No query stored, can't load more
        
        self.offset = 1

        self.repo_search_thread = RepoSearchThread(self.search_query, limit=self.limit)
        self.repo_search_thread.search_complete.connect(self.on_repositories_found1)
        self.repo_search_thread.search_failed.connect(self.on_search_failed)
        self.repo_search_thread.start()

        self.status_label.show()
        self.status_label.setText('Loading more repositories...')
        self.progress_bar.show()

    def on_repositories_found1(self, repo_list):
        
        for repo in repo_list:
            card = RepoCard(repo_id=repo['id'], description=repo.get('description', 'No description'), downloads=repo.get('downloads', 'N/A'))
            card.clicked.connect(self.on_repo_card_clicked1)
            self.repo_container_layout.addWidget(card)
            self.progress_bar.hide()
            self.status_label.hide()
    
    def on_repo_card_clicked1(self, repo_id):
        self.current_repo_id = repo_id
        self.progress_bar.show()
        self.file_listing_thread = FileListingThread(repo_id)
        self.file_listing_thread.file_listing_complete.connect(self.on_files_listed1)
        self.file_listing_thread.file_listing_failed.connect(self.on_file_listing_failed)
        self.file_listing_thread.start()

    def on_files_listed1(self, gguf_files):
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

    def check_scroll_position(self):
        scroll_bar = self.repo_scroll.verticalScrollBar()

        # Check if we're at the bottom of the scroll area
        if scroll_bar.value() == scroll_bar.maximum():
            self.load_more_repositories()

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

#------------------------------------------------------------------------------------
# Update
#------------------------------------------------------------------------------------

class Update(QWidget):
    def __init__(self):
        super().__init__()

        self.latest_version = None
        self.download_url = None
        self.local_filename = None
        self.setWindowOpacity(1.0)

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
                background-color: #2d2d2d;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #000000;
                color: white;
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

#------------------------------------------------------------------------------------
# Plugin Class
#------------------------------------------------------------------------------------

class Plugin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plugin Manager")
        self.resize(900, 600)
        self.setWindowOpacity(1.0)
        self.setStyleSheet("background-color: transparent; color: #ffffff; font-family: 'Segoe UI', sans-serif;")

        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane { border: 0; }
            QTabBar::tab {
                background: #ffffff; 
                color: #000000;
                padding: 12px 20px;       /* Top/Bottom padding 12px, Left/Right 20px */
                border-radius: 8px;
                margin-right: 10px; 
            }
            QTabBar::tab:selected {
                background: #000000;
                color: #ffffff;
            }
            QTabBar::tab:last {
                margin-right: 0;           /* Remove margin for the last tab */
            }
        """)
        self.installed_tab = QWidget()

        #self.installer_tab = QWidget()
        
        self.tab_widget.addTab(self.installed_tab, "Nectar-X-Plugins")

        #self.tab_widget.addTab(self.installer_tab, "Installer")


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

        # Installer tab
        #self.installer_layout = QVBoxLayout()
        #self.installer_tab.setLayout(self.installer_layout)
        #self.install_button = QPushButton("Install Plugin")
        #self.install_button.setCursor(Qt.CursorShape.PointingHandCursor)
        #self.install_button.setStyleSheet("""
        #    QPushButton {
        #        background-color: #000000;
        #        color: #ffffff;
        #        font-size: 16px;
        #        font-weight: bold;
        #        padding: 12px 12px;
        #        border-radius: 8px;
        #    }
        #    QPushButton:hover { background-color: #ffffff; color: #000000;}
        #    QPushButton:pressed { background-color: #1e1e1e; }
        #""")
        #self.install_button.clicked.connect(self.install_plugin)

        import webbrowser

       # Create the label
       # self.label = QLabel()
       # self.label.setFixedHeight(30)
       # self.label.setText(
       #     'To Download PluginStore Visit: <a href="#">PluginStore</a>'
       # )
       # self.label.setTextFormat(Qt.TextFormat.RichText)  # Enable HTML formatting
       # self.label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
       # self.label.setOpenExternalLinks(False)  # We'll handle manually
       # self.label.setStyleSheet("color: #ffffff;")  # Optional styling

        # Determine platform-specific URL
       # if platform.system().lower() == "linux":
       #     download_url = "https://github.com/headlessripper/PluginStore/releases/download/v3/Plugin-Store.zip"
       # else:  # Windows or others
       #     download_url = "https://github.com/headlessripper/PluginStore/releases/download/v6/Plugin-Store.zip"

        # Connect link click
       # self.label.linkActivated.connect(lambda _: webbrowser.open(download_url))

       # self.installer_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignTop)

       # self.installer_layout.addWidget(self.install_button, alignment=Qt.AlignmentFlag.AlignTop)

        # Installed tab
        self.installed_layout = QGridLayout()
        self.installed_layout.setSpacing(15)
        
        self.installed_scroll = QScrollArea()
        self.installed_scroll.setWidgetResizable(True)
        self.installed_scroll.setStyleSheet("QScrollArea { border: none; }")
        self.installed_widget = QWidget()
        self.installed_widget.setLayout(self.installed_layout)
        self.installed_scroll.setWidget(self.installed_widget)
        
        self.installed_tab_layout = QVBoxLayout()
        self.installed_tab.setLayout(self.installed_tab_layout)

        # Button row
        self.installed_tab_btn_layout = QHBoxLayout()
        self.installed_tab_layout.addLayout(self.installed_tab_btn_layout)

        # Scroll area
        self.installed_tab_layout.addWidget(self.installed_scroll)

        # Refresh button
        icon_path_refresh = find_icon("background/refresh.png")
        refresh_button = QPushButton()
        refresh_button.setIcon(QIcon(icon_path_refresh))
        refresh_button.setToolTip("Refresh page to get latest plugins.")
        refresh_button.setFixedSize(50, 50)
        refresh_button.setCursor(Qt.CursorShape.PointingHandCursor)
        refresh_button.clicked.connect(lambda: self.installed_tab_refresh())
        refresh_button.setStyleSheet("""
            QPushButton {
                border-radius: 12px;
                background-color: #1e1e1e;
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
        self.installed_tab_btn_layout.addWidget(refresh_button)

        self.plugin_buttons = []
        self.load_installed_plugins()

    def installed_tab_refresh(self):
        self.refresh_installed_plugins()

    def refresh_installed_plugins(self):
        if not os.path.exists(PLUGIN_DIR):
            return

        # Clear existing buttons first
        self.plugin_buttons = []

        for folder_name in os.listdir(PLUGIN_DIR):
            folder_path = os.path.join(PLUGIN_DIR, folder_name)
            if os.path.isdir(folder_path):
                manifest_path = self.find_file_recursive(folder_path, "manifest.json")
                if manifest_path:
                    with open(manifest_path, "r") as f:
                        manifest_data = json.load(f)
                    self.add_installed_plugin(manifest_data, folder_path, add_to_grid_only=True)

        # Refresh layout
        self.update_grid_layout()

    # --------------------- Load Existing Plugins ---------------------
    def load_installed_plugins(self):
        if not os.path.exists(PLUGIN_DIR):
            return
        for folder_name in os.listdir(PLUGIN_DIR):
            folder_path = os.path.join(PLUGIN_DIR, folder_name)
            if os.path.isdir(folder_path):
                manifest_path = self.find_file_recursive(folder_path, "manifest.json")
                if manifest_path:
                    with open(manifest_path, "r") as f:
                        manifest_data = json.load(f)
                    self.add_installed_plugin(manifest_data, folder_path, add_to_grid_only=True)

    # --------------------- File Utilities ---------------------
    def find_file_recursive(self, root_dir, filename):
        for root, dirs, files in os.walk(root_dir):
            if filename in files:
                return os.path.join(root, filename)
        return None

    def find_entry_point_recursive(self, root_dir, entry_point):
        base_name = os.path.basename(entry_point)
        for root, dirs, files in os.walk(root_dir):
            if base_name in files:
                return os.path.join(root, base_name)
        return None

    # --------------------- Plugin Button Management ---------------------
    def add_installed_plugin(self, manifest_data, plugin_path, add_to_grid_only=False):
        icon_path = os.path.join(plugin_path, manifest_data.get("icon", ""))
        if not os.path.exists(icon_path):
            icon_path = self.find_file_recursive(plugin_path, os.path.basename(manifest_data.get("icon", "")))

        button = QPushButton()
        button.setFixedSize(90, 90)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setStyleSheet("""
            QPushButton {
                border-radius: 12px;
                background-color: #1e1e1e;
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

        if icon_path and os.path.exists(icon_path):
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(64, 64))

        name = manifest_data.get("name", "Unnamed")
        description = manifest_data.get("description", "")
        button.setToolTip(f"<b>{name}</b><br>{description}")

        button.plugin_path = plugin_path
        button.entry_point = manifest_data.get("entry_point")
        button.enabled_state = True
        button.clicked.connect(lambda checked, b=button: self.run_plugin(b.plugin_path, b.entry_point))

        button.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        button.customContextMenuRequested.connect(lambda pos, b=button: self.show_context_menu(b, pos))

        self.plugin_buttons.append(button)
        self.update_grid_layout()

        if not add_to_grid_only:
            msg = QMessageBox(self)
            msg.setWindowTitle("Installed")
            msg.setText(f"Plugin '{name}' installed successfully!")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #1e1e1e;
                    color: #ffffff;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 14px;
                    border: 1px solid #444;
                    border-radius: 10px;
                    padding: 12px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: #28a745; /* green for success */
                    color: #ffffff;
                    border: none;
                    border-radius: 6px;
                    font-weight: bold;
                    padding: 6px 14px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #3cd65b;
                    color: #ffffff;
                }
                QPushButton:pressed {
                    background-color: #1e7e34;
                }
            """)
            msg.exec()


    def update_grid_layout(self):
        for i in reversed(range(self.installed_layout.count())):
            widget = self.installed_layout.itemAt(i).widget()
            if widget:
                self.installed_layout.removeWidget(widget)

        for idx, button in enumerate(self.plugin_buttons):
            row = idx // MAX_COLUMNS
            col = idx % MAX_COLUMNS
            self.installed_layout.addWidget(button, row, col)

    # --------------------- Context Menu ---------------------
    def show_context_menu(self, button, pos):
        menu = QMenu()
        uninstall_action = QAction("Uninstall Plugin")
        delete_action = QAction("Delete Button")
        disable_action = QAction("Disable Plugin" if button.enabled_state else "Enable Plugin")

        uninstall_action.triggered.connect(lambda: self.uninstall_plugin(button))
        delete_action.triggered.connect(lambda: self.delete_button(button))
        disable_action.triggered.connect(lambda: self.toggle_enable(button))

        menu.addAction(uninstall_action)
        menu.addAction(delete_action)
        menu.addAction(disable_action)
        menu.exec(button.mapToGlobal(pos))

    def uninstall_plugin(self, button):
        reply = QMessageBox(self)
        reply.setWindowTitle("Uninstall")
        reply.setText(f"Are you sure you want to uninstall '{button.toolTip()}'?")
        reply.setIcon(QMessageBox.Icon.Question)
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        reply.setStyleSheet("""
            QMessageBox {
                background-color: #1e1e1e;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                border: 1px solid #444;
                border-radius: 10px;
                padding: 12px;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QPushButton {
                background-color: #0db9d7; /* primary accent color */
                color: #000000;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                padding: 6px 14px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #00e0ff;
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #0099aa;
            }
        """)
        reply_result = reply.exec()

        # Kill any running plugin processes safely and wait for termination
        try:
            for proc in psutil.process_iter(['pid', 'name', 'exe']):
                try:
                    if proc.info['exe'] and proc.info['exe'].startswith(button.plugin_path):
                        proc.kill()
                        proc.wait(timeout=10)  # wait up to 10 seconds for process to exit
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                    pass  # ignore if process is gone or can't be killed
        except Exception as e:
            Notify(f"Error checking/killing plugin processes: {e}", parent=self)

        # Check the user's response correctly
        try:
            if reply_result == QMessageBox.StandardButton.Yes:
                if os.path.exists(button.plugin_path):
                    shutil.rmtree(button.plugin_path)
                self.plugin_buttons.remove(button)
                button.deleteLater()
                self.update_grid_layout()
                self.refresh_installed_plugins()
        except Exception as e:
            Notify(f"Failed to update UI: {e}", parent=self)

    def delete_button(self, button):
        self.plugin_buttons.remove(button)
        button.deleteLater()
        self.update_grid_layout()

    def toggle_enable(self, button):
        button.enabled_state = not button.enabled_state
        button.setEnabled(button.enabled_state)

    # --------------------- Run Plugin ---------------------
    def run_plugin(self, plugin_path, entry_point):
        if not entry_point:
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText("No entry point specified for this plugin")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #1e1e1e;
                    color: #ffffff;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 14px;
                    border: 1px solid #444;
                    border-radius: 10px;
                    padding: 12px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: #0db9d7;
                    color: #000000;
                    border: none;
                    border-radius: 6px;
                    font-weight: bold;
                    padding: 6px 14px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #00e0ff;
                    color: #000000;
                }
                QPushButton:pressed {
                    background-color: #0099aa;
                }
            """)
            msg.exec()

            return

        full_path = os.path.join(plugin_path, entry_point)
        if not os.path.exists(full_path):
            full_path = self.find_entry_point_recursive(plugin_path, entry_point)
            if not full_path:
                msg = QMessageBox(self)
                msg.setWindowTitle("Error")
                msg.setText(f"Entry point '{entry_point}' not found")
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: #1e1e1e;
                        color: #ffffff;
                        font-family: 'Segoe UI', sans-serif;
                        font-size: 14px;
                        border: 1px solid #444;
                        border-radius: 10px;
                        padding: 12px;
                    }
                    QLabel {
                        color: #ffffff;
                        font-size: 14px;
                    }
                    QPushButton {
                        background-color: #0db9d7;
                        color: #000000;
                        border: none;
                        border-radius: 6px;
                        font-weight: bold;
                        padding: 6px 14px;
                        min-width: 80px;
                    }
                    QPushButton:hover {
                        background-color: #00e0ff;
                        color: #000000;
                    }
                    QPushButton:pressed {
                        background-color: #0099aa;
                    }
                """)
                msg.exec()
                return

        if not sys.platform.startswith("win"):
            try:
                st = os.stat(full_path)
                os.chmod(full_path, st.st_mode | 0o111)
            except Exception as e:
                msg = QMessageBox(self)
                msg.setWindowTitle("Error")
                msg.setText(f"Failed to set executable permission: {e}")
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: #1e1e1e;
                        color: #ffffff;
                        font-family: 'Segoe UI', sans-serif;
                        font-size: 14px;
                        border: 1px solid #444;
                        border-radius: 10px;
                        padding: 12px;
                    }
                    QLabel {
                        color: #ffffff;
                        font-size: 14px;
                    }
                    QPushButton {
                        background-color: #0db9d7;
                        color: #000000;
                        border: none;
                        border-radius: 6px;
                        font-weight: bold;
                        padding: 6px 14px;
                        min-width: 80px;
                    }
                    QPushButton:hover {
                        background-color: #00e0ff;
                        color: #000000;
                    }
                    QPushButton:pressed {
                        background-color: #0099aa;
                    }
                """)
                msg.exec()

                return

        try:
            if sys.platform.startswith("win"):
                os.startfile(full_path)
            else:
                subprocess.Popen([full_path])
        except Exception as e:
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText(f"Failed to run plugin: {e}")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #1e1e1e;
                    color: #ffffff;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 14px;
                    border: 1px solid #444;
                    border-radius: 10px;
                    padding: 12px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: #0db9d7;
                    color: #000000;
                    border: none;
                    border-radius: 6px;
                    font-weight: bold;
                    padding: 6px 14px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #00e0ff;
                    color: #000000;
                }
                QPushButton:pressed {
                    background-color: #0099aa;
                }
            """)
            msg.exec()

#------------------------------------------------------------------------------------
# Main Window Class
# -----------------------------------------------------------------------------------        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nectar-X-Studio')
        #self.setWindowOpacity(0.95)
        self.setWindowIcon(QIcon(find_icon('background/NectarX.png') or 'background/NectarX.png'))
        self.setFixedSize(1480, 788)

        self.settings = QSettings("Zashiron", "Nectar-X-Studio")
        self.auth_methods = ["Click to choose an option","Password", "PIN", "Pattern", "2FA (Authenticator)"]
        self.pattern_sequence = []

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0,0,0,0)

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setFixedSize(1040, 788)
        self.pages = [Landing(), LLM_Engine(), Broadcast(), Downloader(), Update(), Plugin()]
        for p in self.pages:
            #p.setStyleSheet('color: #ffffff; font-size:22px; background:#0f0f0f;')
            self.stacked_widget.addWidget(p)

        left = LeftSidebar(self.stacked_widget)
        main_layout.addWidget(left)
        
        main_layout.addWidget(self.stacked_widget)

        right = RightPanel()
        main_layout.addWidget(right)

        self.setStyleSheet('''
            QMainWindow { background: #0d0d0d; }
            QLabel { color: #dcdcdc; font-family: "Segoe UI", Arial; }
            QScrollArea { background: transparent; }
        ''')

        # Authentication setup
        self.Auth()
        self.check_existing_user()

    # ------------------------------------------------------------
    # Lock Screen / Authentication
    # ------------------------------------------------------------
    
    def Auth(self):
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet('background-color: rgba(0, 0, 0, 180);')
        self.overlay.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.overlay.setVisible(True)
        overlay_layout = QVBoxLayout(self.overlay)
        overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.profile_label = QLabel()
        self.profile_label.setFixedSize(40, 40)
        self.profile_label.setStyleSheet("""
            QLabel {
                border-radius: 40px;
                background-color: transparent;
                border: transparent;
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
                                
            QComboBox QAbstractItemView {
                background-color: #000000;
                color: white;
                selection-background-color: #000111;
                selection-color: #ffffff;
            }
        """)

        from pathlib import Path
        down_arrow_icon = find_icon('background/down-arrow.svg')
        if down_arrow_icon:
            icon_path = Path(down_arrow_icon).as_posix()  # ensures forward slashes
            self.method_selector.setStyleSheet(f"""
                QComboBox::down-arrow  {{
                    image: url("{icon_path}");
                    subcontrol-position: right;
                    width: 12px;
                    height: 12px;
                }}
            """)
        else:
            Notify("Close icon not found!", parent=self)

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
                    background: #ffffff; 
                    border-radius: 30px; 
                    } 
                    QPushButton:hover { 
                    background: #2d2d2d; 
                    } 
                """)
                btn.clicked.connect(lambda _, n=i*4+j+1: self.pattern_click(n))
                self.pattern_layout.addWidget(btn, i, j)
                self.pattern_buttons[i*4+j+1] = btn

        overlay_layout.addWidget(self.pattern_grid, alignment=Qt.AlignmentFlag.AlignCenter)
        self.pattern_grid.hide()

        icon_path_login = find_icon("menu/down.png")
        self.submit_btn = QPushButton()
        self.submit_btn.setIcon(QIcon(icon_path_login))
        self.submit_btn.setFixedSize(50, 50)
        self.submit_btn.setStyleSheet(' QPushButton { padding: 12px; background-color: #ffffff; color: red; border-radius: 5px;} QPushButton:hover { background-color: #2e2e2e;}')
        self.submit_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.submit_btn.clicked.connect(self.handle_submit)
        overlay_layout.addWidget(self.submit_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def resizeEvent(self, event):
        if hasattr(self, "overlay") and self.overlay:
            self.overlay.setGeometry(self.rect())
        super().resizeEvent(event)

    def clear_pattern(self):
        """Resets the pattern sequence and restores button styles."""
        self.pattern_sequence = []
        for btn in self.pattern_buttons.values():
            btn.setStyleSheet("""
                QPushButton {
                    background: #ffffff;
                    border-radius: 30px;
                }
                QPushButton:hover {
                    background: #2d2d2d;
                }
            """)

    def check_existing_user(self):
        settings1 = QSettings("Zashiron", "Nectar-X-Studio")

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

        # --- Display text ---
        self.overlay_label.setText(f"🚧 Enter your {method} to unlock. 🚧")

        # --- Display Profile Picture ---
        if hasattr(self, "profile_label"):
            try:
                pixmap = None
                if picture_url and picture_url.startswith("http"):
                    # Download image from URL
                    import requests
                    from io import BytesIO
                    response = requests.get(picture_url)
                    image_data = BytesIO(response.content)
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data.read())

                # --- Ensure pixmap is valid ---
                if pixmap is None or pixmap.isNull():
                    write_to_log("Profile pixmap is null, using blank placeholder")
                    #Notify(f"Profile pixmap is null, using blank placeholder", parent=self)
                    pixmap = QPixmap(60, 60)
                    pixmap.fill(Qt.GlobalColor.black)

                # --- Size & padding ---
                size = 80
                padding = 12
                radius = 12

                # --- Scale pixmap ---
                scaled_pixmap = pixmap.scaled(
                    size - 2 * padding,
                    size - 2 * padding,
                    Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                    Qt.TransformationMode.SmoothTransformation
                )

                # --- Create rounded square background ---
                rounded = QPixmap(size, size)
                rounded.fill(Qt.GlobalColor.transparent)

                painter = QPainter(rounded)
                painter.setRenderHint(QPainter.RenderHint.Antialiasing)

                # --- Draw rounded background mask ---
                path = QPainterPath()
                path.addRoundedRect(padding, padding, size - 2 * padding, size - 2 * padding, radius, radius)
                painter.setClipPath(path)

                # --- Draw scaled pixmap ---
                painter.drawPixmap(padding, padding, scaled_pixmap)
                painter.end()

                # --- Apply to label ---
                self.profile_label.setPixmap(rounded)
                self.profile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.profile_label.setFixedSize(size, size)

                self.profile_label.setStyleSheet("""
                    QLabel {
                        border: transparent;
                        border-radius: 8px;
                        padding: 6px;
                        background: transparent;
                    }
                """)

            except Exception as e:
                write_to_log(f"Error loading profile picture: {e}")
                Notify(f"Error loading profile picture: {e}", parent=self)

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
                background: #2e2e2e;
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
                username = "Nectar-X-Studio"
                # Step 1: Generate the 2FA secret key
                totp = pyotp.TOTP(pyotp.random_base32())
                secret_key = totp.secret
                uri = totp.provisioning_uri(username, issuer_name="Zashiron")

                # Step 2: Generate the QR code from the URI
                import qrcode
                qr = qrcode.make(uri)
                qr = qr.convert('RGB')  # Ensure it's in RGB mode (needed for blending the icon)

                # Step 3: Load the icon and place it in the center of the QR code
                icon_path = self.find_icon('NectarX.png')
                icon = Image.open(icon_path)

                # Resize the icon
                icon_size = qr.size[0] // 5  # Resize icon to 1/5th of the QR code size
                icon = icon.resize((icon_size, icon_size))

                # Position the icon in the center
                qr_width, qr_height = qr.size
                icon_width, icon_height = icon.size
                position = ((qr_width - icon_width) // 2, (qr_height - icon_height) // 2)

                # Paste the icon on the QR code
                qr.paste(icon, position, icon.convert('RGBA'))

                # Step 4: Convert the QR code to QPixmap and display it in a QMessageBox
                qr_path = "/tmp/temp_qr_code.png"  # Temporary path to save the QR image
                qr.save(qr_path)

                pixmap = QPixmap(qr_path)
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Scan the QR Code")
                msg_box.setText("Please scan this QR code with your authenticator app.")
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setIconPixmap(pixmap)
                msg_box.exec()

                # Step 5: Save the 2FA secret key for the user
                self.settings.setValue("2fa_secret", secret_key)
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
                    #QMessageBox.warning(self, "Error", "Invalid pattern!")
                    Inform("Invalid Pattern Please try again", parent=self)
                    self.clear_pattern()
            elif method == "2FA (Authenticator)":
                self.input_field.show()
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
        self.clear_pattern()
        self.input_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    run_security_checks()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())