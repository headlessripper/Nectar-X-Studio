import os, socket, base64
from urllib.parse import urlparse
from urllib.request import urlopen
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from PyQt6.QtCore import (
    pyqtSignal, QObject, QThread
)
from PyQt6.QtGui import QPixmap, QImage

from winotify import Notification, audio
import pickle

from scripts.components.Service.find_icon import find_icon
from scripts.components.Utility.write_to_log import write_to_log
from scripts.SYS_Config.Config import POLL_INTERVAL_MS
from email import message_from_bytes

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