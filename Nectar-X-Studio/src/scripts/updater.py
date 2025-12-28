
import os
import subprocess

from urllib.parse import urlparse
from urllib.request import urlopen
import os
 

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton, QMessageBox
)
from PyQt6.QtCore import (
    Qt
)

from scripts.components.Worker.Threads.UpdatorThreads import ReleaseCheckThread, DownloadThread
from scripts.SYS_Config.Config import CURRENT_VERSION

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