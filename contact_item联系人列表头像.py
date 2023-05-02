from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QBrush, QColor, QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLabel, QWidget


class ContactItem(QWidget):
    def __init__(self, name, avatar_path):
        super().__init__()

        self.name = name
        self.avatar_path = avatar_path
        self.layout = QHBoxLayout()  # 定义成员变量

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        # 创建头像标签
        self.avatar_label = QLabel()
        self.avatar_label.setCursor(Qt.PointingHandCursor)  # 设置鼠标指针为手形
        #self.avatar_label.mousePressEvent = self.choose_avatar  # 设置鼠标单击事件处理程序
        layout.addWidget(self.avatar_label)

        # 创建圆形头像
        pixmap = QPixmap(self.avatar_path)
        pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 检查图片格式
        if self.avatar_path.endswith(".gif"):
            # 如果是GIF格式，创建QMovie并设置为头像标签的内容
            movie = QMovie(self.avatar_path)
            movie.setScaledSize(QSize(64, 64))
            self.avatar_label.setMovie(movie)
            movie.start()
        else:
            # 如果是静态图，直接将Pixmap设置为头像标签的内容
            self.avatar_label.setPixmap(pixmap)

        # 为头像设置圆角矩形遮罩
        mask = QPixmap(64, 64)
        mask.fill(Qt.transparent)
        painter = QPainter(mask)
        painter.setBrush(QBrush(QColor("white")))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(QRect(0, 0, 64, 64), 32, 32)
        painter.end()

        self.avatar_label.setMask(mask.createMaskFromColor(Qt.transparent))

        # 联系人名称
        name_label = QLabel(self.name)
        layout.addWidget(name_label)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        self.setLayout(layout)

    def choose_avatar(self, avatar_path):
        """
        使用提供的 avatar_path 更改头像。
        """
        self.avatar_path = avatar_path
        pixmap = QPixmap(self.avatar_path)
        pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if self.avatar_path.endswith(".gif"):
            movie = QMovie(self.avatar_path)
            movie.setScaledSize(QSize(64, 64))
            self.avatar_label.setMovie(movie)
            movie.start()
        else:
            self.avatar_label.setPixmap(pixmap)

        # 为新头像设置圆角矩形遮罩
        mask = QPixmap(64, 64)
        mask.fill(Qt.transparent)
        painter = QPainter(mask)
        painter.setBrush(QBrush(QColor("white")))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(QRect(0, 0, 64, 64), 32, 32)
        painter.end()
        self.avatar_label.setMask(mask.createMaskFromColor(Qt.transparent))

        # 联系人名称
        name_label = QLabel(self.name)
        layout.addWidget(name_label)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        self.setLayout(layout)
