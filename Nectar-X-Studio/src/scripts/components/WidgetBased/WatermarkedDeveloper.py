from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QFont, QPainter, QColor, 
)

# ----------------- CUSTOM LOG VIEW WITH WATERMARK -----------------
class WatermarkedDeveloperContactView(QTextEdit):
    def __init__(self, watermark_text="Nectar-X-Studio"):
        super().__init__()
        self.watermark_text = watermark_text
        self.setReadOnly(True)
        self.setStyleSheet("""
            QTextEdit {
                background-color: #000000;
                color: #ffffff;
                border: none;
                border-radius: 16px;
                padding: 8px;
            }
        """)

    def paintEvent(self, event):
        """Draw watermark centered in the widget background."""
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QColor(255, 255, 255, 30))  # Semi-transparent white
        font = QFont("Consolas", 24, QFont.Weight.Bold)
        painter.setFont(font)

        # Calculate text position for perfect centering
        text_rect = self.rect()
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, self.watermark_text)
        painter.end()