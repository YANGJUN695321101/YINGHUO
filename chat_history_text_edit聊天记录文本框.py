from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QSizePolicy


class ChatHistoryTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(ChatHistoryTextEdit, self).__init__(parent)
        self.setReadOnly(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def add_message(self, message, is_sender):
        if is_sender:
            html_message = self.sender_message_to_html(message)
        else:
            html_message = self.receiver_message_to_html(message)

        self.append(html_message)

    def sender_message_to_html(self, message):
        return f"""
            <div style="
                background-color: #DCF8C6;
                max-width: 60%;
                padding: 8px;
                border-radius: 8px;
                margin-bottom: 8px;
                margin-left: auto;
            ">
                {message}
            </div>
        """

    def receiver_message_to_html(self, message):
        return f"""
            <div style="
                background-color: #FFFFFF;
                max-width: 60%;
                padding: 8px;
                border-radius: 8px;
                margin-bottom: 8px;
                margin-right: auto;
            ">
                {message}
            </div>
        """


def add_messages():
    history_text_edit.add_message("你好，你好吗？", is_sender=True)
    history_text_edit.add_message("我很好，谢谢！", is_sender=False)

app = QApplication([])
window = QMainWindow()
central_widget = QWidget()
layout = QVBoxLayout(central_widget)
history_text_edit = ChatHistoryTextEdit()
layout.addWidget(history_text_edit)
window.setCentralWidget(central_widget)
window.show()

# 使用 QTimer 来在事件循环开始后添加消息
timer = QTimer()
timer.timeout.connect(add_messages)
timer.setSingleShot(True)
timer.start(0)

app.exec_()
