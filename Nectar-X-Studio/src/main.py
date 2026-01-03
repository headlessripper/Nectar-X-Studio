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
# Imports
#------------------------------------------------------------------------------
import pyotp
import sys
import os
import requests
import base64

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
    QSizePolicy, QLineEdit, QGridLayout, QMessageBox,
    QHBoxLayout, QStackedWidget, QComboBox, QMenu, QSystemTrayIcon
)
from PyQt6.QtCore import (
    Qt
)
from PyQt6.QtGui import (
    QIcon, QPixmap, QPainter, QPainterPath,
    QAction, QImage
)

from PIL import Image

from PyQt6.QtCore import QSettings
from winotify import Notification, audio

from scripts.plugin import Plugin
from scripts.updater import Update
from scripts.downloader import Downloader
from scripts.broadcast import Broadcast
from scripts.landing import Landing
from scripts.rightpanel import RightPanel
from scripts.leftsidebar import LeftSidebar
from scripts.Engine.main import LLM_Engine

QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)

from scripts.components.Utility.write_to_log import write_to_log
from scripts.components.Service.find_icon import find_icon
from scripts.SYS_Config.Config import run_security_checks
from scripts.components.WidgetBased.Notify import Notify
from scripts.components.WidgetBased.Inform import Inform

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
    
#------------------------------------------------------------------------------------
# Main Window Class
# -----------------------------------------------------------------------------------        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nectar-X-Studio')
        #self.setWindowOpacity(0.95)
        self.setWindowFlags(
            Qt.WindowType.Window |
            Qt.WindowType.CustomizeWindowHint |
            Qt.WindowType.WindowTitleHint |
            Qt.WindowType.WindowCloseButtonHint
        )
        self.setWindowIcon(QIcon(find_icon('background/NectarX.png') or 'background/NectarX.png'))
        self.setFixedSize(1480, 788)

        self.settings = QSettings("Zashiron", "Nectar-X-Studio")
        self.auth_methods = ["Click to choose an option", "None", "Password", "PIN", "Pattern", "2FA (Authenticator)"]
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

        icon_path = find_icon('background/NectarX.png')
        if icon_path and os.path.exists(icon_path):
            self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)
            self.tray_icon.show()
        else:
            print("[INFO] Tray icon skipped (icon not found)")
        tray_menu = QMenu()

        restore_action = QAction('Restore', self)
        restore_action.triggered.connect(self.restore_state)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(QApplication.quit)

        tray_menu.addAction(restore_action)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.hide()

        # Authentication setup
        self.Auth()
        self.check_existing_user()

    def restore_state(self):
        self.show()
        self.tray_icon.hide()

    def closeEvent(self, event):

        if self.settings.value('append_close_action', True, type=bool):
            event.ignore()
            self.hide()
            self.tray_icon.show()
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="Tray Notification",
                msg=f"Application minimized to tray. Right-click the tray icon to restore.",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()
        else:
            event.accept()  # close normally

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

        # --- Retrieve method ---
        method = settings1.value("auth_method", "None")  # Default to None
    
        #if method == "None":
            #self.overlay.setVisible(False)  # Skip auth entirely
            #return
        
        if not settings1.contains("auth_method") or method == "Click to choose an option":
            self.overlay_label.setText("🚧 Welcome! Create a login method. 🚧")
            return

        # --- Retrieve Google Info ---
        settings1.beginGroup("google")
        name1 = settings1.value("name", "User")
        picture_url = settings1.value("picture", "")
        settings1.endGroup()

        # --- Display text ---
        if settings1.value("auth_method") == "None":
            self.overlay_label.setText(f"🚧 Welcome back, {name1} 🚧")
            self.method_selector.hide()
            self.input_field.hide()
        else:
            self.overlay_label.setText(f"🚧 Welcome back, {name1}! Enter your {method} to unlock. 🚧")

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
                    Notify(f"Not Logged In", parent=self)
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

        #if method == "None":
        #    return  # No input needed
    
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
        if method == "None":
            self.settings.setValue("auth_method", "None")
            self.settings.remove("credential")  # Clean up old credentials
            self.settings.remove("2fa_secret")
            #QMessageBox.information(self, "Success", "No security enabled - access granted!")
            self.accept_login()
            return
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
            if stored_method == "None":
                self.accept_login()  # Already no security
                return
            
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
    #app.setQuitOnLastWindowClosed(False)
    run_security_checks()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())