import socket

from PyQt6.QtCore import (
    QThread, pyqtSignal, pyqtProperty, pyqtSlot
)

AUTH_KEY = "NEC-892657"

class StreamClientWorker(QThread):
    chunk_received = pyqtSignal(str)    # partial text
    finished_response = pyqtSignal(str) # full text or final

    def __init__(self, prompt: str, parent=None):
        super().__init__(parent)
        self.prompt = prompt
        self._stop = False

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", 5005))

            payload = f"{AUTH_KEY} {self.prompt}".encode("utf-8")
            s.sendall(payload)

            buffer = b""

            while not self._stop:
                data = s.recv(1024)
                if not data:
                    break

                buffer += data

                if b"<<END_OF_RESPONSE>>" in buffer:
                    break

                chunk = data.decode("utf-8", errors="ignore")
                self.chunk_received.emit(chunk)

        except Exception as e:
            self.finished_response.emit(f"Error: {e}")
        finally:
            s.close()
            self.finished_response.emit("")  # signal completion only

    def stop(self):
        self._stop = True