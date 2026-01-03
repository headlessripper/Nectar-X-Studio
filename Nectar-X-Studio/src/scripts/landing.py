
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout
from PyQt6.QtCore import Qt, QTimer, QThreadPool
from PyQt6.QtGui import QFont, QPixmap, QPainter, QPainterPath
import re

from scripts.components.Card import Card
from scripts.SYS_Config.Config import REFERENCE_IMAGE, load_license_data, verify_license, local_hash
from scripts.components.Service.find_icon import find_icon
from scripts.components.Worker.ImageLoader import ImageLoader

#--------------------------------------------------------------------------------
# Landing Page Class
#--------------------------------------------------------------------------------

class SlideshowCard(QWidget):
    def __init__(self, image_urls, title_text, interval=30000):
        super().__init__()
        self.setWindowOpacity(1.0)
        self.image_urls = image_urls
        self.index = 0
        self.pool = QThreadPool.globalInstance()

        self.setFixedSize(160, 100)
        self.setStyleSheet("background-color: #222; border-radius: 10px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label, 1)

        # Timer for slideshow
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_image)
        self.timer.start(interval)
        self.next_image()

    def next_image(self):
        url = self.image_urls[self.index % len(self.image_urls)]
        worker = ImageLoader(url, self.set_image)
        self.pool.start(worker)
        self.index += 1

    def set_image(self, pix):
        if not pix.isNull():
            self.image_label.setPixmap(pix.scaled(
                self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

class Landing(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(1.0)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28,28,28,28)
        layout.setSpacing(28)

        title = QLabel('Home')
        title.setStyleSheet('color:#ffffff;')
        title.setFont(QFont('Segoe UI', 26, QFont.Weight.Bold))
        layout.addWidget(title)

        # Latest Patch Notes small card
        license_data = load_license_data()
        if not license_data:
            # Try to verify or initialize license if none exists
            license_data = verify_license()
            if not license_data:
                license_data = {
                    "licensor": "Unknown",
                    "license_key": "Unavailable",
                    "expiration_date": "N/A"
                }

        patch_card = Card()
        patch_card.setFixedHeight(90)
        pc_layout = QHBoxLayout(patch_card)
        pc_layout.setContentsMargins(14,10,14,10)
        left_text = QVBoxLayout()
        h1 = QLabel(f'Nectar-X-Studio Patch\nNotes 12.09\nPlatform UUID: {local_hash}') # UUID (USER UNIQUE IDENTIFICATION)
        h1.setStyleSheet('color:#ffffff; font-weight:700;')
        date = QLabel('December 20, 2025')
        date.setStyleSheet('color:#ff6b6b;')
        left_text.addWidget(h1)
        left_text.addWidget(date)
        pc_layout.addLayout(left_text)
        pc_layout.addStretch()
        # small decorative image (use portion of REFERENCE_IMAGE scaled)
        pix = QPixmap(REFERENCE_IMAGE)
        if not pix.isNull():
            badge = QLabel()
            badge.setPixmap(pix.scaledToHeight(70, Qt.TransformationMode.SmoothTransformation))
            pc_layout.addWidget(badge)
        layout.addWidget(patch_card)

        # What's New large card
        big_card = Card()
        big_card.setMinimumHeight(260)
        bc_layout = QHBoxLayout(big_card)
        bc_layout.setContentsMargins(18,18,18,18)

        left = QVBoxLayout()
        tag = QLabel('')
        tag.setStyleSheet('color:#d9a82a; font-weight:700;')
        heading = QLabel("N\nE\nC\nT\nA\nR\n|\nX\n|\nS\nT\nU\nD\nI\nO")
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        heading.setStyleSheet('color:#ffffff; font-weight:800;')
        heading.setWordWrap(True)
        sub = QLabel("")
        sub.setStyleSheet('color:#bdbdbd;')
        left.addWidget(tag)
        left.addWidget(heading)
        left.addWidget(sub)
        left.addStretch()
        bc_layout.addLayout(left, 3)

        icon_path = find_icon('background/halfpic.jpg')

        # Right side image using the REFERENCE_IMAGE (cropped look with diagonal mask)
        right_img_label = QLabel()
        pix2 = QPixmap(icon_path)

        if not pix2.isNull():
            # crop a central area first
            w = pix2.width()
            h = pix2.height()
            cropped = pix2.copy(int(w * 0.3), int(h * 0.21), int(w * 0.6), int(h * 0.8))

            # Scale the image for display
            scaled = cropped.scaledToHeight(820, Qt.TransformationMode.SmoothTransformation)

            # Create a diagonal mask
            mask = QPixmap(scaled.size())
            mask.fill(Qt.GlobalColor.transparent)

            painter = QPainter(mask)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            path = QPainterPath()
            # Create diagonal cut from top-left to bottom-right
            path.moveTo(0, scaled.height() * 0.2)
            path.lineTo(scaled.width(), 0)
            path.lineTo(scaled.width(), scaled.height() * 0.8)
            path.lineTo(0, scaled.height())
            path.closeSubpath()

            painter.fillPath(path, Qt.GlobalColor.white)
            painter.end()

            # Apply mask to create the diagonal effect
            scaled.setMask(mask.createMaskFromColor(Qt.GlobalColor.transparent))

            # Assign final pixmap
            right_img_label.setPixmap(scaled)

        right_img_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        bc_layout.addWidget(right_img_label, 4)

        layout.addWidget(big_card)        
        
        container = QWidget()
        title2 = QLabel("Images")
        title2.setStyleSheet('color:#ffffff;')
        title2.setFont(QFont('Segoe UI', 18, QFont.Weight.Bold))
        hl = QHBoxLayout(container)

        # Example image sets (6 slideshows)
        image_sets = [
            [f"https://picsum.photos/seed/{i*10+j}/200/120" for j in range(5)]
            for i in range(6)
        ]

        for i, urls in enumerate(image_sets):
            thumb = SlideshowCard(urls, f'{i+1}')
            hl.addWidget(thumb)

        hl.addStretch()
        layout.addWidget(title2)
        layout.addWidget(container)
        layout.addStretch()