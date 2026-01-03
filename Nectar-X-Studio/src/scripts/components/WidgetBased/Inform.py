
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