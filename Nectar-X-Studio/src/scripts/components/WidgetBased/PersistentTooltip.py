import re
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