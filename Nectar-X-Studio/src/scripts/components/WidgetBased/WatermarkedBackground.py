from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout
)
from PyQt6.QtCore import (
    Qt
)
from PyQt6.QtGui import (
    QFont, QPainter, QColor
)

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