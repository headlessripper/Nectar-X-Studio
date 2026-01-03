import sys
import os
import requests

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QMessageBox, QHBoxLayout
)
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer, QPointF
from PyQt6.QtGui import QPainter, QPen, QColor, QFont, QConicalGradient, QIcon

GITHUB_EXE_URL = 'https://huggingface.co/Zashiron/Nectar-X-Studio/resolve/main/Nectar-X-Studio.exe?download=true'
HOME_DIR = os.path.expanduser('~')
EXE_PATH = os.path.join(HOME_DIR, 'Nectar-X-Studio.exe')


def find_icon(icon_name: str) -> str | None:
    """Attempts to find the icon in and around the script's directory."""
    script_dir = os.path.dirname(os.path.realpath(__file__))
    possible_paths = [
        os.path.join(script_dir, icon_name),
        os.path.join(script_dir, 'Model-Icon', icon_name),
        os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None


class CircularProgress(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0
        self._animation_value = 0
        self.setFixedSize(160, 160)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(15)

    def setValue(self, value: int):
        self.value = max(0, min(100, int(value)))

    def update_animation(self):
        # Simple easing towards target value
        if self._animation_value < self.value:
            self._animation_value += 1
            self.update()
        elif self._animation_value > self.value:
            self._animation_value -= 1
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = self.rect().adjusted(10, 10, -10, -10)

        # Background circle
        pen_bg = QPen(QColor(240, 240, 240), 14)
        pen_bg.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen_bg)
        painter.drawEllipse(rect)

        # Gradient arc
        gradient = QConicalGradient()
        gradient.setCenter(QPointF(rect.center().x(), rect.center().y()))
        gradient.setAngle(-90)
        gradient.setColorAt(0.0, QColor(85, 170, 255))
        gradient.setColorAt(0.5, QColor(0, 255, 255))
        gradient.setColorAt(1.0, QColor(85, 170, 255))

        pen_fg = QPen()
        pen_fg.setBrush(gradient)
        pen_fg.setWidth(14)
        pen_fg.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen_fg)

        angle = int(360 * (self._animation_value / 100.0))
        painter.drawArc(rect, -90 * 16, -angle * 16)

        # Glow
        pen_glow = QPen(QColor(85, 170, 255, 60), 20)
        pen_glow.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen_glow)
        painter.drawArc(rect, -90 * 16, -angle * 16)

        # Text
        painter.setPen(QColor(50, 50, 50))
        painter.setFont(QFont('Segoe UI', 18, QFont.Weight.Bold))
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, f'{self._animation_value}%')

        painter.end()


class DownloadWorker(QThread):
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    finished = pyqtSignal(str)   # emits EXE_PATH
    error = pyqtSignal(str)
    bytes_downloaded = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self._stop = False

    def stop(self):
        self._stop = True

    def run(self):
        try:
            self.status.emit('Preparing download...')
            mode = 'wb'
            headers = {}
            downloaded = 0

            if os.path.exists(EXE_PATH):
                downloaded = os.path.getsize(EXE_PATH)
                headers = {'Range': f'bytes={downloaded}-'}
                mode = 'ab'
                self.status.emit(f'Resuming download from {downloaded} bytes...')

            response = requests.get(GITHUB_EXE_URL, stream=True, headers=headers, timeout=15)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0)) + downloaded
            self.status.emit('Downloading executable...')

            with open(EXE_PATH, mode) as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if self._stop:
                        self.status.emit('Download stopped')
                        return

                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            percent = int((downloaded / total_size) * 100)
                        else:
                            percent = 0
                        self.progress.emit(percent)
                        self.bytes_downloaded.emit(downloaded, total_size)

            self.status.emit('Download completed.')
            self.finished.emit(EXE_PATH)

        except Exception as e:
            self.error.emit(str(e))


class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(' ')
        self.setWindowIcon(QIcon(find_icon('background/NectarX.png') or 'background/NectarX.png'))
        self.setWindowFlags(Qt.WindowType.Dialog)
        self.setFixedSize(450, 350)
        self.setStyleSheet("""
            QWidget { background-color: #f5f5f7; }
            QLabel { color: #333; }
            QPushButton {
                background-color: #55aaff;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #00ccff; }
            QPushButton:pressed { background-color: #0099cc; }
        """)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title = QLabel('Nectar-X-Studio 🔻')
        self.title.setStyleSheet("font-size:18px; font-weight:bold;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title)

        self.status = QLabel('Idle')
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status)

        self.progress = CircularProgress()
        layout.addWidget(self.progress, alignment=Qt.AlignmentFlag.AlignCenter)

        side_layout = QHBoxLayout()
        side_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Start button
        icon_path_start = find_icon('Model-Icon/forward.png')
        self.button_start = QPushButton()
        if icon_path_start:
            self.button_start.setIcon(QIcon(icon_path_start))
        self.button_start.setFixedSize(50, 50)
        self.button_start.setStyleSheet("""
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
        self.button_start.clicked.connect(self.start_download)
        side_layout.addWidget(self.button_start)

        # Stop button
        icon_path_stop = find_icon('Model-Icon/close.png')
        self.button_stop = QPushButton()
        self.button_stop.setEnabled(False)
        if icon_path_stop:
            self.button_stop.setIcon(QIcon(icon_path_stop))
        self.button_stop.setFixedSize(50, 50)
        self.button_stop.setStyleSheet("""
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
        self.button_stop.clicked.connect(self.stop_download)
        side_layout.addWidget(self.button_stop)

        layout.addLayout(side_layout)

        self.worker: DownloadWorker | None = None

    def start_download(self):
        self.button_start.setEnabled(False)
        self.button_stop.setEnabled(True)
        self.progress.setValue(0)
        self.status.setText('Starting...')
        self.setWindowTitle('Nectar-X-Studio Downloader')

        self.worker = DownloadWorker()
        self.worker.progress.connect(self.progress.setValue)
        self.worker.status.connect(self.status.setText)
        self.worker.bytes_downloaded.connect(self.update_window_title)
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.on_error)
        self.worker.start()

    def stop_download(self):
        if self.worker:
            self.worker.stop()
            self.status.setText('Stopping download...')
            self.button_start.setEnabled(True)
            self.button_stop.setEnabled(False)

    def update_window_title(self, downloaded: int, total: int):
        def format_bytes(b: int) -> str:
            if b >= 1_000_000_000:
                return f'{b / 1_000_000_000:.2f} GB'
            if b >= 1_000_000:
                return f'{b / 1_000_000:.2f} MB'
            if b >= 1_000:
                return f'{b / 1_000:.2f} KB'
            return f'{b} B'

        self.setWindowTitle(f'Downloading: {format_bytes(downloaded)} / {format_bytes(total)}')

    def on_finished(self, exe_path: str):
        self.button_stop.setEnabled(False)
        self.status.setText('Completed successfully!')
        self.setWindowTitle('Enjoy')

        QMessageBox.information(self, 'Done', f'Executable downloaded to:\n{exe_path}')

        # Ask user if they want to run it
        reply = QMessageBox.question(
            self,
            'Run Installer',
            'Do you want to run the downloaded executable now?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                os.startfile(exe_path)  # Windows only
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to run executable:\n{e}')

        self.button_start.setEnabled(True)

    def on_error(self, msg: str):
        self.button_stop.setEnabled(False)
        QMessageBox.critical(self, 'Error', msg)
        self.status.setText('Failed')
        self.setWindowTitle('Error')
        self.button_start.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownloaderApp()
    window.show()
    sys.exit(app.exec())
