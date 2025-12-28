from PyQt6.QtWidgets import QFrame

class Card(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('card')
        self.setStyleSheet('''
        QFrame#card {
            background: #151515;
            border-radius: 12px;
        }
        ''')