import sys
import os
import psutil
import requests
import json

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton, QLineEdit, QMessageBox, QCheckBox, QHBoxLayout, QFrame, QFileDialog, QScrollArea, QGraphicsOpacityEffect
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QPropertyAnimation, QUrl, QEasingCurve
from PyQt6.QtGui import QIcon, QFont, QPainter, QDesktopServices, QColor

from concurrent.futures import ThreadPoolExecutor, as_completed
from PyQt6.QtCore import QThread, pyqtSignal
import psutil
from concurrent.futures import ThreadPoolExecutor, as_completed

from scripts.SYS_Config.Config import ACCESS_TOKEN
from scripts.components.Service.find_icon import find_icon
from scripts.components.Service.get_llm_hardware_recommendation import get_llm_hardware_recommendation

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