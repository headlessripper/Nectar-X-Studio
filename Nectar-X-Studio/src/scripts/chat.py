import os
import re
import json
 

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QHBoxLayout, QFrame, QScrollArea, QListWidgetItem, QDialogButtonBox, QDialog
from PyQt6.QtCore import Qt, QTimer, QUrl
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPainter, QDesktopServices, QColor, QPen, QClipboard
import markdown

from scripts.components.Service.find_icon import find_icon
from scripts.components.Worker.Threads.StreamClient import StreamClientWorker
from scripts.components.Utility.write_to_log import write_to_log
from scripts.components.WidgetBased.WatermarkedBackground import WatermarkedBackgroundWidget
from scripts.components.WidgetBased.Notify import Notify
from scripts.components.WidgetBased.Inform import Inform

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