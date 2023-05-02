from PyQt5.QtWidgets import QTextEdit, QPushButton
from PyQt5.QtCore import    Qt
class ChatInputTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.send_button = QPushButton("发送", self)
        self.send_button.setFixedSize(40, 40)
        self.send_button.setGeometry(self.width() - 50, self.height() - 50, 40, 40)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def resizeEvent(self, event):
        self.send_button.move(self.width() - 50, self.height() - 50)
        super().resizeEvent(event)