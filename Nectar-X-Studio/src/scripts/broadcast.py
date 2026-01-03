
import asyncio
import uvicorn
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sys
import socket

import threading
import sys
 

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox,
    QTextEdit, QHBoxLayout, QComboBox
)
from PyQt6.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve, QRect,
)
from PyQt6.QtGui import (
    QIcon, QPixmap
)

from scripts.components.Service.get_local_ip import get_local_ip
from scripts.components.Service.find_icon import find_icon
from scripts.components.Utility.send_to_AlphaLLM import send_to_AlphaLLM
from scripts.components.Service.find_free_port import find_free_port
#------------------------------------------------------------------------------------
# Broad Cast Class
#------------------------------------------------------------------------------------

class Broadcast(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(1.0)
        self.setWindowTitle('🧠 AlphaLLM Broadcast Engine')
        self.resize(700, 600)

        # Local TCP server
        self.server_running = False
        self.server_socket = None
        self.broadcast_port = 8012
        self.broadcast_base_ip = '127.0.0.1'

        # FastAPI server
        self.fastapi_app = FastAPI()
        self.fastapi_host = f'{get_local_ip()}'
        self.fastapi_port = f'{find_free_port()}'
        self.fastapi_running = False
        self.websockets = []

        self.init_ui()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet(self.futuristic_style())
        self.animate_window()
        self.setup_fastapi_routes()

    # --------------------------- UI ---------------------------
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)
        
        self.title1 = QLabel(f'<h1>Expose Local Usage:</h1>')
        layout.addWidget(self.title1)
        
        layout.addSpacing(10)

        # Target display
        self.target_display = QLabel(f'📡 Local Engine: {self.broadcast_base_ip}:{self.broadcast_port}')
        layout.addWidget(self.target_display)
        
        # Broadcast engine toggle
        self.toggle_button = QPushButton('Start Local Engine')
        self.toggle_button.clicked.connect(self.toggle_engine)
        layout.addWidget(self.toggle_button)
        
        layout.addSpacing(20)
        
        self.title2 = QLabel(f'<h1>Expose To Network:</h1>')
        layout.addWidget(self.title2)
        
        layout.addSpacing(10)

        # FastAPI host/port
        fastapi_layout = QHBoxLayout()
        self.host_input = QLineEdit(self.fastapi_host)
        self.host_input.setPlaceholderText('FastAPI Host')
        self.port_input = QLineEdit(str(self.fastapi_port))
        self.port_input.setPlaceholderText('FastAPI Port')
        self.fastapi_button = QPushButton("Start ")
        self.fastapi_button.clicked.connect(self.toggle_fastapi)
        fastapi_layout.addWidget(self.host_input)
        fastapi_layout.addWidget(self.port_input)
        fastapi_layout.addWidget(self.fastapi_button)
        layout.addLayout(fastapi_layout)

        # Token for authentication
        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Access Token (Optional)")
        layout.addWidget(self.token_input)

        # FastAPI dynamic route configuration
        self.api_config_layout = QVBoxLayout()
        self.api_config_layout.addWidget(QLabel("📡 Route Configuration"))
        route_layout = QHBoxLayout()
        self.route_input = QLineEdit("/predict")
        self.route_input.setPlaceholderText("Route Path")
        self.method_input = QComboBox()
        self.method_input.addItems(["GET", "POST", "WebSocket"])

        self.add_route_btn = QPushButton("Add Route")
        self.add_route_btn.clicked.connect(self.add_fastapi_route)
        self.viewer_btn = QPushButton("Docs")
        self.viewer_btn.clicked.connect(self.Api_view)

        self.qrcode_btn = QPushButton("NectarChat")
        self.qrcode_btn.clicked.connect(self.generate_qr_code)

        route_layout.addWidget(self.route_input)
        route_layout.addWidget(self.method_input)
        route_layout.addWidget(self.add_route_btn)
        route_layout.addWidget(self.viewer_btn)
        route_layout.addWidget(self.qrcode_btn)
        self.api_config_layout.addLayout(route_layout)
        layout.addLayout(self.api_config_layout)

        # Packet log
        layout.addWidget(QLabel('📦 Packet Log:'))
        self.packet_log = QTextEdit()
        self.packet_log.setReadOnly(True)
        layout.addWidget(self.packet_log)

        self.setLayout(layout)

    def Api_view(self):
        import webbrowser
        url = "https://github.com/headlessripper/Nectar-X-Studio/wiki/Documentation"
        webbrowser.open(url)

    def generate_qr_code(self):
        import qrcode
        url = f"http://{self.fastapi_host}:{self.fastapi_port}"

        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")

        qr_path = "qrcode.png"
        img.save(qr_path)

        pixmap = QPixmap(qr_path)
        msg_box = QMessageBox()
        msg_box.setWindowTitle("NectarChat")
        msg_box.setWindowIcon(QIcon(find_icon('background/NectarX.png') or 'background/NectarX.png'))
        msg_box.setText("Please scan this QR code with NectarChat.")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setIconPixmap(pixmap)
        msg_box.exec()

    # --------------------------- Local TCP Engine ---------------------------
    def toggle_engine(self):
        if not self.server_running:
            self.server_running = True
            threading.Thread(target=self.start_broadcast_server, daemon=True).start()
            self.toggle_button.setText('Stop Local Engine')
            self.log_packet('[Engine] Local broadcast server started.')
        else:
            self.server_running = False
            self.stop_broadcast_server()
            self.toggle_button.setText('Start Local Engine')
            self.log_packet('[Engine] Local broadcast server stopped.')

    def start_broadcast_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.broadcast_base_ip, self.broadcast_port))
        self.server_socket.listen(5)
        self.log_packet(f'[Relay] Listening on {self.broadcast_base_ip}:{self.broadcast_port}...')
        while self.server_running:
            try:
                self.server_socket.settimeout(5)
                client_socket, addr = self.server_socket.accept()
                incoming_data = client_socket.recv(4096).decode('utf-8')
                self.log_packet(f'[Incoming] From {addr[0]}:{addr[1]} -> {incoming_data}')
                alpha_response = send_to_AlphaLLM(incoming_data)
                self.log_packet(f'[Forwarded] Response from AlphaLLM: {alpha_response}')
                client_socket.send(alpha_response.encode('utf-8'))
                client_socket.close()
                # Broadcast to FastAPI WebSocket clients
                if self.fastapi_running:
                    asyncio.run(self.broadcast_fastapi(alpha_response))
            except socket.timeout:
                continue
            except Exception as e:
                self.log_packet(f'[Error] Server exception: {e}')
                break
        self.log_packet('[Server] Listener stopped.')

    def stop_broadcast_server(self):
        if self.server_socket:
            try:
                self.server_socket.close()
                self.server_socket = None
            except Exception as e:
                self.log_packet(f'[Error] Could not close socket: {e}')

    # --------------------------- FastAPI ---------------------------
    def toggle_fastapi(self):
        if not self.fastapi_running:
            self.fastapi_host = self.host_input.text()
            self.fastapi_port = int(self.port_input.text())
            threading.Thread(target=self.run_fastapi, daemon=True).start()
            self.fastapi_running = True
            self.fastapi_button.setText('Stop FastAPI')
            self.log_packet(f'[FastAPI] Started at {self.fastapi_host}:{self.fastapi_port}')
        else:
            self.fastapi_running = False
            self.fastapi_button.setText('Start FastAPI')
            self.log_packet('[FastAPI] Stopped (restart required).')

    def setup_fastapi_routes(self):
        self.fastapi_app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"]
        )

    def add_fastapi_route(self):
        path = self.route_input.text()
        method = self.method_input.currentText()
        token = self.token_input.text()

        if not path.startswith("/"):
            path = "/" + path

        if method in ["GET", "POST"]:
            async def api_endpoint(request: Request):
                # Optional token authentication
                if token:
                    auth = request.headers.get("Authorization")
                    if auth != f"Bearer {token}":
                        return JSONResponse(status_code=401, content={"error": "Unauthorized"})

                if method == "GET":
                    data = request.query_params.get("data", "")
                else:
                    data_json = await request.json()
                    data = data_json.get("data", "")
                response = send_to_AlphaLLM(data)
                # Broadcast to WebSocket clients
                if self.fastapi_running:
                    await self.broadcast_fastapi(response)
                return {"response": response}

            self.fastapi_app.add_api_route(path, api_endpoint, methods=[method])
            self.log_packet(f"[FastAPI] Added {method} route: {path}")

        elif method == "WebSocket":
            async def websocket_endpoint(websocket: WebSocket):
                await websocket.accept()
                self.websockets.append(websocket)
                self.log_packet(f'[FastAPI] WS Client connected: {websocket.client}')
                try:
                    while True:
                        data = await websocket.receive_text()
                        response = send_to_AlphaLLM(data)
                        await websocket.send_text(response)
                        self.log_packet(f'[FastAPI] WS Received: {data}, Sent: {response}')
                except Exception as e:
                    self.log_packet(f'[FastAPI] WS error: {e}')
                finally:
                    self.websockets.remove(websocket)
                    self.log_packet(f'[FastAPI] WS Client disconnected: {websocket.client}')

            self.fastapi_app.add_api_websocket_route(path, websocket_endpoint)
            self.log_packet(f"[FastAPI] Added WebSocket route: {path}")

    async def broadcast_fastapi(self, message):
        for ws in self.websockets:
            try:
                await ws.send_text(message)
            except Exception as e:
                self.log_packet(f'[FastAPI] Broadcast failed: {e}')

    import uvicorn

    def run_fastapi(self):
        log_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(levelprefix)s %(message)s",
                    "use_colors": False  # <-- disable colors here
                },
            },
            "handlers": {
                "default": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": sys.stdout,
                },
            },
            "loggers": {
                "uvicorn": {"handlers": ["default"], "level": "INFO"},
                "uvicorn.error": {"level": "INFO"},
                "uvicorn.access": {"handlers": ["default"], "level": "INFO"},
            },
        }

        uvicorn.run(
            self.fastapi_app,
            host=self.fastapi_host,
            port=self.fastapi_port,
            log_config=log_config,
        )

    # --------------------------- Logging & UI ---------------------------
    def log_packet(self, message):
        self.packet_log.append(f'{message}')

    def animate_window(self):
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        geo = self.geometry()
        self.animation.setStartValue(QRect(geo.x(), geo.y() + 30, geo.width(), geo.height()))
        self.animation.setEndValue(geo)
        self.animation.start()

    def futuristic_style(self):
        return '''
            QWidget {
                background-color: rgba(18, 18, 18, 200);
                border-radius: 20px;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
            }
            QLineEdit, QTextEdit {
                background-color: transparent;
                color: #ffffff;
                border: 1px solid #ffffff;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton {
                background-color: #ffffff;
                border: none;
                border-radius: 10px;
                padding: 10px;
                color: #000000;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #000000;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #1e1e1e;
            }
            QTextEdit {
                font-family: Consolas, monospace;
                font-size: 13px;
            }
            QLabel {
                background-color: transparent;
                color: #ffffff;
            }
        '''