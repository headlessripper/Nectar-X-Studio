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