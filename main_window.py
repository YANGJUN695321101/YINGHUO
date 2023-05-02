
from PyQt5.QtCore import QRect, QRectF, QSize, Qt
from PyQt5.QtGui import (QBrush, QColor, QIcon, QImage, QPainter,
                         QPainterPath, QPixmap, QRegion)
from PyQt5.QtWidgets import (QAction, QFileDialog, QFrame, QGridLayout,
                             QHBoxLayout, QLabel, QLineEdit, QListWidget,
                             QMainWindow, QMenu, QPushButton,
                             QScrollArea, QScrollBar, QSizePolicy, QSpacerItem,
                             QTextEdit, QToolButton, QVBoxLayout, QWidget)

from modules.chat_input_text_edit发送按钮 import ChatInputTextEdit
from modules.custom_title_bar标题栏 import CustomTitleBar
from modules.fixed_contacts模拟联系人 import FixedContacts
from modules.chat_history_text_edit聊天记录文本框 import ChatHistoryTextEdit


def load_avatar(avatar_label, image_path):
    print(f"正在加载头像: {image_path}")
    image = QImage(image_path)
    if image.isNull():
        print(f"头像加载失败: {image_path}")
        return
    pixmap = QPixmap.fromImage(image)
    avatar_label.setPixmap(pixmap.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        

        
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
         # 主布局
        central_widget = QWidget(MainWindow)  # 将 central_widget 的定义移动到这里
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)  # 设置 main_layout 的边距为零


        # 设置窗口标题栏
        self.title_bar = CustomTitleBar(MainWindow)
        main_layout.addWidget(self.title_bar)
        MainWindow.setCentralWidget(central_widget)  # 将 central_widget 设置为主窗口的中央部件
        MainWindow.setMenuWidget(self.title_bar)  # 将 title_bar 设置为主窗口的菜单部件


        # 设置窗口无边框
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setMouseTracking(True)

        MainWindow.setWindowTitle("聊天应用")
        MainWindow.setGeometry(100, 100, 1300, 800)

        #central_widget = QWidget(MainWindow)
        central_layout = QHBoxLayout(central_widget)

        # 侧边栏模块
        sidebar_layout = QVBoxLayout()

        sidebar = QFrame()
        sidebar.setAutoFillBackground(True)
        sidebar_palette = sidebar.palette()
        sidebar_palette.setColor(sidebar.backgroundRole(), Qt.lightGray)
        sidebar.setPalette(sidebar_palette)
        sidebar.setLayout(sidebar_layout)
        # 侧边栏头像部分

        # 用户头像部分
        user_avatar = QLabel()
        load_avatar(user_avatar, "D:\\DESK\\remHENKEAI\\ABC.png")
        user_avatar.setFixedSize(40, 40)  # 设置头像的固定大小

        # 设置头像为圆形
        path = QPainterPath()
        path.addEllipse(QRectF(0, 0, 40, 40))
        region = QRegion(path.toFillPolygon().toPolygon())
        user_avatar.setMask(region)

        user_nickname = QLabel("用户昵称")
        user_nickname.setAlignment(Qt.AlignHCenter)  # 将昵称水平居中

        # 将用户头像和昵称添加到布局中
        sidebar_layout.addWidget(user_avatar, alignment=Qt.AlignHCenter)
        sidebar_layout.addWidget(user_nickname, alignment=Qt.AlignHCenter)

        sidebar_layout.addStretch(5)  # 添加自定义间距

        # AI 头像部分
        ai_avatar = QLabel()
        load_avatar(ai_avatar, "D:\\DESK\\remHENKEAI\\ABC.png")
        ai_avatar.setFixedSize(40, 40)  # 设置头像的固定大小

        # 设置头像为圆形
        path = QPainterPath()
        path.addEllipse(QRectF(0, 0, 40, 40))
        region = QRegion(path.toFillPolygon().toPolygon())
        ai_avatar.setMask(region)

        ai_nickname = QLabel("AI昵称")
        ai_nickname.setAlignment(Qt.AlignHCenter)  # 将昵称水平居中

        # 将AI头像和昵称添加到布局中
        sidebar_layout.addWidget(ai_avatar, alignment=Qt.AlignHCenter)
        sidebar_layout.addWidget(ai_nickname, alignment=Qt.AlignHCenter)
        sidebar_layout.addStretch(150)


        central_layout.addWidget(sidebar)  # 将侧边栏添加到中央布局

        # 联系人列表模块
        contact_list_layout = QVBoxLayout()

        search_and_add_layout = QHBoxLayout()  # 新增水平布局

        search_bar = QLineEdit()
        search_bar.setPlaceholderText("搜索联系人")
        search_bar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)  # 设置搜索框的尺寸策略

        search_and_add_layout.addWidget(search_bar)  # 将搜索栏添加到水平布局中

        add_friend_button = QPushButton("+")  # 更改按钮文本为 "+"
        add_friend_button.setFixedSize(20, 20)  # 设置按钮大小
        add_friend_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 设置添加按钮的尺寸策略

        # 创建弹出菜单
        add_friend_menu = QMenu()
        add_friend_action = QAction("添加好友", add_friend_button)
        new_ai_action = QAction("新建AI聊天机器人", add_friend_button)
        add_friend_menu.addAction(add_friend_action)
        add_friend_menu.addAction(new_ai_action)

        # 将弹出菜单连接到按钮
        add_friend_button.setMenu(add_friend_menu)

        search_and_add_layout.addWidget(add_friend_button)  # 将添加按钮添加到水平布局中

        contact_list_layout.addLayout(search_and_add_layout)  # 将水平布局添加到联系人列表布局中

        contact_list = QListWidget()
        contact_list.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)  # 设置联系人列表的尺寸策略
        contact_list_layout.addWidget(contact_list)
        # 添加固定联系人
        fixed_contacts = FixedContacts(contact_list)

        central_layout.addLayout(contact_list_layout)

        # 输入区域布局
        input_area_layout = QVBoxLayout()
        input_area_layout.setContentsMargins(0, 0, 0, 0)
        input_area_layout.setSpacing(0)
        # 输入区域
        input_frame = QFrame()
        input_frame.setFrameShape(QFrame.StyledPanel)
        input_frame.setFixedHeight(180)  # 设置输入框的高度
        input_frame_layout = QVBoxLayout(input_frame)
        input_frame_layout.setContentsMargins(5, 5, 5, 5)
        input_frame_layout.setSpacing(0)
        #   输入框
        input_area_and_button_layout = QHBoxLayout()
        input_area_and_button_layout.setContentsMargins(0, 0, 0, 0)
        input_area_and_button_layout.setSpacing(0)
        input_area = ChatInputTextEdit()
        input_area.setPlaceholderText("输入聊天内容")
        input_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # 设置输入框的尺寸策略
        input_area_and_button_layout.addWidget(input_area)
        input_frame_layout.addLayout(input_area_and_button_layout)  # 将input_area_and_button_layout添加到input_frame_layout中
        input_area_layout.addWidget(input_frame)  # 将input_frame添加到input_area_layout中
        # 聊天记录框
        chat_layout = QVBoxLayout()
        chat_history = ChatHistoryTextEdit()
        chat_history.setReadOnly(True)
        chat_history.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置聊天记录框的尺寸策略
        chat_layout.addWidget(chat_history)
        central_layout.addLayout(chat_layout)

        central_layout.addLayout(input_area_layout)  # 将 input_area_layout 添加到 central_layout 中




        

        # 消息通知模块
        notification_bar = QLabel("新消息通知")
        notification_bar.setAlignment(Qt.AlignCenter)
        notification_bar.setFrameShape(QFrame.Box)
        notification_bar.setFrameShadow(QFrame.Raised)
        notification_bar.setLineWidth(2)
        notification_bar.setFixedHeight(50)

        
       

        MainWindow.setCentralWidget(central_widget)
        
    
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
