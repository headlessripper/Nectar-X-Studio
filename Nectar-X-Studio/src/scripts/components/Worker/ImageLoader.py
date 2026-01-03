
from PyQt6.QtCore import (
    pyqtSignal, QObject, QRunnable
)
from PyQt6.QtGui import (
    QPixmap, QImage
)

import requests
from scripts.components.Utility.write_to_log import write_to_log

# Worker signals
class WorkerSignals(QObject):
    image_loaded = pyqtSignal(QPixmap)

# Background worker to fetch image
class ImageLoader(QRunnable):
    def __init__(self, url, callback):
        super().__init__()
        self.url = url
        self.signals = WorkerSignals()
        self.signals.image_loaded.connect(callback)

    def run(self):
        try:
            response = requests.get(self.url, timeout=5)
            image = QImage.fromData(response.content)
            pix = QPixmap.fromImage(image)
            self.signals.image_loaded.emit(pix)
        except Exception as e:
            write_to_log(f"Error loading {e}")