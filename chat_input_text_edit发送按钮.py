# chat_input_text_edit.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QTextEdit

class ChatInputTextEdit(QTextEdit):
    def __init__(self, chat_history, parent=None):
        super().__init__(parent)

        self.chat_history = chat_history

        self.send_button = QPushButton("发送", self)
        self.send_button.setFixedSize(40, 40)
        self.send_button.setGeometry(self.width() - 50, self.height() - 50, 40, 40)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 连接发送按钮的 clicked 信号到 send_message 方法
        self.send_button.clicked.connect(self.send_message)

    def resizeEvent(self, event):
        self.send_button.move(self.width() - 50, self.height() - 50)
        super().resizeEvent(event)

    def send_message(self):
        # 发送消息的逻辑
        message = self.toPlainText().strip()
        if message:
            self.chat_history.append(f'用户: {message}')
            self.clear()
