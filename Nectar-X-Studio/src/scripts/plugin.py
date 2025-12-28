import sys
import os
import subprocess
import psutil
import shutil
import json

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGridLayout, QMessageBox, QHBoxLayout, QTabWidget, QScrollArea, QMenu
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction
from scripts.SYS_Config.Config import PLUGIN_DIR
from scripts.SYS_Config.Config import MAX_COLUMNS
from scripts.components.Service.find_icon import find_icon
from scripts.components.WidgetBased.Notify import Notify

#------------------------------------------------------------------------------------
# Plugin Class
#------------------------------------------------------------------------------------

class Plugin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plugin Manager")
        self.resize(900, 600)
        self.setWindowOpacity(1.0)
        self.setStyleSheet("background-color: transparent; color: #ffffff; font-family: 'Segoe UI', sans-serif;")

        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane { border: 0; }
            QTabBar::tab {
                background: #ffffff; 
                color: #000000;
                padding: 12px 20px;       /* Top/Bottom padding 12px, Left/Right 20px */
                border-radius: 8px;
                margin-right: 10px; 
            }
            QTabBar::tab:selected {
                background: #000000;
                color: #ffffff;
            }
            QTabBar::tab:last {
                margin-right: 0;           /* Remove margin for the last tab */
            }
        """)
        self.installed_tab = QWidget()

        #self.installer_tab = QWidget()
        
        self.tab_widget.addTab(self.installed_tab, "Nectar-X-Plugins")

        #self.tab_widget.addTab(self.installer_tab, "Installer")


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

        # Installer tab
        #self.installer_layout = QVBoxLayout()
        #self.installer_tab.setLayout(self.installer_layout)
        #self.install_button = QPushButton("Install Plugin")
        #self.install_button.setCursor(Qt.CursorShape.PointingHandCursor)
        #self.install_button.setStyleSheet("""
        #    QPushButton {
        #        background-color: #000000;
        #        color: #ffffff;
        #        font-size: 16px;
        #        font-weight: bold;
        #        padding: 12px 12px;
        #        border-radius: 8px;
        #    }
        #    QPushButton:hover { background-color: #ffffff; color: #000000;}
        #    QPushButton:pressed { background-color: #1e1e1e; }
        #""")
        #self.install_button.clicked.connect(self.install_plugin)

        import webbrowser

       # Create the label
       # self.label = QLabel()
       # self.label.setFixedHeight(30)
       # self.label.setText(
       #     'To Download PluginStore Visit: <a href="#">PluginStore</a>'
       # )
       # self.label.setTextFormat(Qt.TextFormat.RichText)  # Enable HTML formatting
       # self.label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
       # self.label.setOpenExternalLinks(False)  # We'll handle manually
       # self.label.setStyleSheet("color: #ffffff;")  # Optional styling

        # Determine platform-specific URL
       # if platform.system().lower() == "linux":
       #     download_url = "https://github.com/headlessripper/PluginStore/releases/download/v3/Plugin-Store.zip"
       # else:  # Windows or others
       #     download_url = "https://github.com/headlessripper/PluginStore/releases/download/v6/Plugin-Store.zip"

        # Connect link click
       # self.label.linkActivated.connect(lambda _: webbrowser.open(download_url))

       # self.installer_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignTop)

       # self.installer_layout.addWidget(self.install_button, alignment=Qt.AlignmentFlag.AlignTop)

        # Installed tab
        self.installed_layout = QGridLayout()
        self.installed_layout.setSpacing(15)
        
        self.installed_scroll = QScrollArea()
        self.installed_scroll.setWidgetResizable(True)
        self.installed_scroll.setStyleSheet("QScrollArea { border: none; }")
        self.installed_widget = QWidget()
        self.installed_widget.setLayout(self.installed_layout)
        self.installed_scroll.setWidget(self.installed_widget)
        
        self.installed_tab_layout = QVBoxLayout()
        self.installed_tab.setLayout(self.installed_tab_layout)

        # Button row
        self.installed_tab_btn_layout = QHBoxLayout()
        self.installed_tab_layout.addLayout(self.installed_tab_btn_layout)

        # Scroll area
        self.installed_tab_layout.addWidget(self.installed_scroll)

        # Refresh button
        icon_path_refresh = find_icon("background/refresh.png")
        refresh_button = QPushButton()
        refresh_button.setIcon(QIcon(icon_path_refresh))
        refresh_button.setToolTip("Refresh page to get latest plugins.")
        refresh_button.setFixedSize(50, 50)
        refresh_button.setCursor(Qt.CursorShape.PointingHandCursor)
        refresh_button.clicked.connect(lambda: self.installed_tab_refresh())
        refresh_button.setStyleSheet("""
            QPushButton {
                border-radius: 12px;
                background-color: #1e1e1e;
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
        self.installed_tab_btn_layout.addWidget(refresh_button)

        self.plugin_buttons = []
        self.load_installed_plugins()

    def installed_tab_refresh(self):
        self.refresh_installed_plugins()

    def refresh_installed_plugins(self):
        if not os.path.exists(PLUGIN_DIR):
            return

        # Clear existing buttons first
        self.plugin_buttons = []

        for folder_name in os.listdir(PLUGIN_DIR):
            folder_path = os.path.join(PLUGIN_DIR, folder_name)
            if os.path.isdir(folder_path):
                manifest_path = self.find_file_recursive(folder_path, "manifest.json")
                if manifest_path:
                    with open(manifest_path, "r") as f:
                        manifest_data = json.load(f)
                    self.add_installed_plugin(manifest_data, folder_path, add_to_grid_only=True)

        # Refresh layout
        self.update_grid_layout()

    # --------------------- Load Existing Plugins ---------------------
    def load_installed_plugins(self):
        if not os.path.exists(PLUGIN_DIR):
            return
        for folder_name in os.listdir(PLUGIN_DIR):
            folder_path = os.path.join(PLUGIN_DIR, folder_name)
            if os.path.isdir(folder_path):
                manifest_path = self.find_file_recursive(folder_path, "manifest.json")
                if manifest_path:
                    with open(manifest_path, "r") as f:
                        manifest_data = json.load(f)
                    self.add_installed_plugin(manifest_data, folder_path, add_to_grid_only=True)

    # --------------------- File Utilities ---------------------
    def find_file_recursive(self, root_dir, filename):
        for root, dirs, files in os.walk(root_dir):
            if filename in files:
                return os.path.join(root, filename)
        return None

    def find_entry_point_recursive(self, root_dir, entry_point):
        base_name = os.path.basename(entry_point)
        for root, dirs, files in os.walk(root_dir):
            if base_name in files:
                return os.path.join(root, base_name)
        return None

    # --------------------- Plugin Button Management ---------------------
    def add_installed_plugin(self, manifest_data, plugin_path, add_to_grid_only=False):
        icon_path = os.path.join(plugin_path, manifest_data.get("icon", ""))
        if not os.path.exists(icon_path):
            icon_path = self.find_file_recursive(plugin_path, os.path.basename(manifest_data.get("icon", "")))

        button = QPushButton()
        button.setFixedSize(90, 90)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setStyleSheet("""
            QPushButton {
                border-radius: 12px;
                background-color: #1e1e1e;
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

        if icon_path and os.path.exists(icon_path):
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(64, 64))

        name = manifest_data.get("name", "Unnamed")
        description = manifest_data.get("description", "")
        button.setToolTip(f"<b>{name}</b><br>{description}")

        button.plugin_path = plugin_path
        button.entry_point = manifest_data.get("entry_point")
        button.enabled_state = True
        button.clicked.connect(lambda checked, b=button: self.run_plugin(b.plugin_path, b.entry_point))

        button.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        button.customContextMenuRequested.connect(lambda pos, b=button: self.show_context_menu(b, pos))

        self.plugin_buttons.append(button)
        self.update_grid_layout()

        if not add_to_grid_only:
            msg = QMessageBox(self)
            msg.setWindowTitle("Installed")
            msg.setText(f"Plugin '{name}' installed successfully!")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #1e1e1e;
                    color: #ffffff;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 14px;
                    border: 1px solid #444;
                    border-radius: 10px;
                    padding: 12px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: #28a745; /* green for success */
                    color: #ffffff;
                    border: none;
                    border-radius: 6px;
                    font-weight: bold;
                    padding: 6px 14px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #3cd65b;
                    color: #ffffff;
                }
                QPushButton:pressed {
                    background-color: #1e7e34;
                }
            """)
            msg.exec()


    def update_grid_layout(self):
        for i in reversed(range(self.installed_layout.count())):
            widget = self.installed_layout.itemAt(i).widget()
            if widget:
                self.installed_layout.removeWidget(widget)

        for idx, button in enumerate(self.plugin_buttons):
            row = idx // MAX_COLUMNS
            col = idx % MAX_COLUMNS
            self.installed_layout.addWidget(button, row, col)

    # --------------------- Context Menu ---------------------
    def show_context_menu(self, button, pos):
        menu = QMenu()
        uninstall_action = QAction("Uninstall Plugin")
        delete_action = QAction("Delete Button")
        disable_action = QAction("Disable Plugin" if button.enabled_state else "Enable Plugin")

        uninstall_action.triggered.connect(lambda: self.uninstall_plugin(button))
        delete_action.triggered.connect(lambda: self.delete_button(button))
        disable_action.triggered.connect(lambda: self.toggle_enable(button))

        menu.addAction(uninstall_action)
        menu.addAction(delete_action)
        menu.addAction(disable_action)
        menu.exec(button.mapToGlobal(pos))

    def uninstall_plugin(self, button):
        reply = QMessageBox(self)
        reply.setWindowTitle("Uninstall")
        reply.setText(f"Are you sure you want to uninstall '{button.toolTip()}'?")
        reply.setIcon(QMessageBox.Icon.Question)
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        reply.setStyleSheet("""
            QMessageBox {
                background-color: #1e1e1e;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                border: 1px solid #444;
                border-radius: 10px;
                padding: 12px;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QPushButton {
                background-color: #0db9d7; /* primary accent color */
                color: #000000;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                padding: 6px 14px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #00e0ff;
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #0099aa;
            }
        """)
        reply_result = reply.exec()

        # Kill any running plugin processes safely and wait for termination
        try:
            for proc in psutil.process_iter(['pid', 'name', 'exe']):
                try:
                    if proc.info['exe'] and proc.info['exe'].startswith(button.plugin_path):
                        proc.kill()
                        proc.wait(timeout=10)  # wait up to 10 seconds for process to exit
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                    pass  # ignore if process is gone or can't be killed
        except Exception as e:
            Notify(f"Error checking/killing plugin processes: {e}", parent=self)

        # Check the user's response correctly
        try:
            if reply_result == QMessageBox.StandardButton.Yes:
                if os.path.exists(button.plugin_path):
                    shutil.rmtree(button.plugin_path)
                self.plugin_buttons.remove(button)
                button.deleteLater()
                self.update_grid_layout()
                self.refresh_installed_plugins()
        except Exception as e:
            Notify(f"Failed to update UI: {e}", parent=self)

    def delete_button(self, button):
        self.plugin_buttons.remove(button)
        button.deleteLater()
        self.update_grid_layout()

    def toggle_enable(self, button):
        button.enabled_state = not button.enabled_state
        button.setEnabled(button.enabled_state)

    # --------------------- Run Plugin ---------------------
    def run_plugin(self, plugin_path, entry_point):
        if not entry_point:
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText("No entry point specified for this plugin")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #1e1e1e;
                    color: #ffffff;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 14px;
                    border: 1px solid #444;
                    border-radius: 10px;
                    padding: 12px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: #0db9d7;
                    color: #000000;
                    border: none;
                    border-radius: 6px;
                    font-weight: bold;
                    padding: 6px 14px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #00e0ff;
                    color: #000000;
                }
                QPushButton:pressed {
                    background-color: #0099aa;
                }
            """)
            msg.exec()

            return

        full_path = os.path.join(plugin_path, entry_point)
        if not os.path.exists(full_path):
            full_path = self.find_entry_point_recursive(plugin_path, entry_point)
            if not full_path:
                msg = QMessageBox(self)
                msg.setWindowTitle("Error")
                msg.setText(f"Entry point '{entry_point}' not found")
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: #1e1e1e;
                        color: #ffffff;
                        font-family: 'Segoe UI', sans-serif;
                        font-size: 14px;
                        border: 1px solid #444;
                        border-radius: 10px;
                        padding: 12px;
                    }
                    QLabel {
                        color: #ffffff;
                        font-size: 14px;
                    }
                    QPushButton {
                        background-color: #0db9d7;
                        color: #000000;
                        border: none;
                        border-radius: 6px;
                        font-weight: bold;
                        padding: 6px 14px;
                        min-width: 80px;
                    }
                    QPushButton:hover {
                        background-color: #00e0ff;
                        color: #000000;
                    }
                    QPushButton:pressed {
                        background-color: #0099aa;
                    }
                """)
                msg.exec()
                return

        if not sys.platform.startswith("win"):
            try:
                st = os.stat(full_path)
                os.chmod(full_path, st.st_mode | 0o111)
            except Exception as e:
                msg = QMessageBox(self)
                msg.setWindowTitle("Error")
                msg.setText(f"Failed to set executable permission: {e}")
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: #1e1e1e;
                        color: #ffffff;
                        font-family: 'Segoe UI', sans-serif;
                        font-size: 14px;
                        border: 1px solid #444;
                        border-radius: 10px;
                        padding: 12px;
                    }
                    QLabel {
                        color: #ffffff;
                        font-size: 14px;
                    }
                    QPushButton {
                        background-color: #0db9d7;
                        color: #000000;
                        border: none;
                        border-radius: 6px;
                        font-weight: bold;
                        padding: 6px 14px;
                        min-width: 80px;
                    }
                    QPushButton:hover {
                        background-color: #00e0ff;
                        color: #000000;
                    }
                    QPushButton:pressed {
                        background-color: #0099aa;
                    }
                """)
                msg.exec()

                return

        try:
            if sys.platform.startswith("win"):
                os.startfile(full_path)
            else:
                subprocess.Popen([full_path])
        except Exception as e:
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText(f"Failed to run plugin: {e}")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: #1e1e1e;
                    color: #ffffff;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 14px;
                    border: 1px solid #444;
                    border-radius: 10px;
                    padding: 12px;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: #0db9d7;
                    color: #000000;
                    border: none;
                    border-radius: 6px;
                    font-weight: bold;
                    padding: 6px 14px;
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #00e0ff;
                    color: #000000;
                }
                QPushButton:pressed {
                    background-color: #0099aa;
                }
            """)
            msg.exec()