
from PyQt5.QtCore import QRect, QRectF, QSize, Qt
from PyQt5.QtGui import (QBrush, QColor, QIcon, QImage, QMovie, QPainter,
                         QPainterPath, QPixmap, QRegion)
from PyQt5.QtWidgets import (QAction, QFileDialog, QFrame, QGridLayout,
                             QHBoxLayout, QLabel, QLineEdit, QListWidget,
                             QMainWindow, QMenu, QPushButton, QScrollArea,
                             QScrollBar, QSizePolicy, QSpacerItem, QTextEdit,
                             QToolButton, QVBoxLayout, QWidget)

from modules.chat_history_text_edit聊天记录文本框 import ChatHistoryTextEdit
from modules.chat_input_text_edit发送按钮 import ChatInputTextEdit
from modules.contact_list右键菜单栏 import ContactList
from modules.custom_title_bar标题栏 import CustomTitleBar
from modules.fixed_contacts模拟联系人 import FixedContacts


def load_avatar(avatar_label, image_path, is_gif=False):
    print(f"正在加载头像: {image_path}")
    if is_gif:
        movie = QMovie(image_path)
        if not movie.isValid():
            print(f"头像加载失败: {image_path}")
            return
        movie.setScaledSize(QSize(40, 40))
        avatar_label.setMovie(movie)
        movie.start()
    else:
        image = QImage(image_path)
        if image.isNull():
            print(f"头像加载失败: {image_path}")
            return
        pixmap = QPixmap.fromImage(image)
        avatar_label.setPixmap(pixmap.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))



        
class Ui_MainWindow(QMainWindow):
    def create_context_menu(self):
        context_menu = QMenu()
        change_avatar_action = QAction("更换头像", self.contact_list)
        delete_chat_action = QAction("删除聊天", self.contact_list)
        context_menu.addAction(change_avatar_action)
        context_menu.addAction(delete_chat_action)

        # 信号连接到槽
        change_avatar_action.triggered.connect(self.change_avatar)
        delete_chat_action.triggered.connect(self.delete_chat)

        return context_menu

    def change_avatar(self):
        current_item = self.contact_list.currentItem()
        if not current_item:
            return

        new_avatar_path, _ = QFileDialog.getOpenFileName(self, "选择头像", "", "Images (*.png *.xpm *.jpg *.gif)")
        if not new_avatar_path:
            return

        # 更新联系人的头像
        contact = current_item.data(Qt.UserRole)
        contact.choose_avatar(new_avatar_path)  # 调用 choose_avatar 函数


        # 在此处添加 delete_chat 函数
    def delete_chat(self):
        current_item = self.contact_list.currentItem()
        if not current_item:
            return
    def show_context_menu(self, pos):
        context_menu = self.create_context_menu(self.contact_list)
        global_pos = self.contact_list.mapToGlobal(pos)
        current_item = self.contact_list.itemAt(pos)
        if current_item:
            action = context_menu.exec_(global_pos)
            if action and action.text() == "删除联系人":
                row = self.contact_list.row(current_item)
                self.contact_list.takeItem(row)


    def setupUi(self, MainWindow):
        self.contact_list = ContactList()
        self.contact_list = QListWidget()
        self.contact_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.contact_list.customContextMenuRequested.connect(self.show_context_menu)
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

        # central_widget = QWidget(MainWindow)
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
        load_avatar(user_avatar, r"D:\DESK\remHENKEAI\DEF.gif", is_gif=True)
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

        central_layout.addWidget(sidebar)  # 将侧边栏添加到中央布局

        # 联系人列表模块
        contact_list_layout = QVBoxLayout()

        search_and_add_layout = QHBoxLayout()  # 新增水平布局

        search_bar = QLineEdit()
        search_bar.setPlaceholderText("搜索联系人")
        search_bar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)  # 设置搜索框的尺寸策略

        search_and_add_layout.addWidget(search_bar)  # 将搜索栏添加到水平布局中

        add_friend_button = QPushButton("+")  # 更改按钮文本
        # 更改按钮文本为 "+"
        add_friend_button = QPushButton("+")
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

        # 聊天窗口模块
        chat_layout = QVBoxLayout()
        chat_history = ChatHistoryTextEdit()
        chat_history.setReadOnly(True)
        chat_layout.addWidget(chat_history)

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

        # 输入框
        input_area_and_button_layout = QHBoxLayout()
        input_area_and_button_layout.setContentsMargins(0, 0, 0, 0)
        input_area_and_button_layout.setSpacing(0)

        # 在此处将 chat_history 传递给 ChatInputTextEdit 类
        input_area = ChatInputTextEdit(chat_history)
        input_area.setPlaceholderText("输入聊天内容")
        input_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # 设置输入框的尺寸策略
        input_area_and_button_layout.addWidget(input_area)
        input_frame_layout.addLayout(input_area_and_button_layout)  # 将input_area_and_button_layout添加到input_frame_layout中
        input_area_layout.addWidget(input_frame)  # 将input

        chat_layout.addLayout(input_area_layout)  # Add input_area_layout to chat_layout
        central_layout.addLayout(chat_layout)  # Add chat_layout to central_layout

        # 消息通知模块
        notification_bar = QLabel("新消息通知")
        notification_bar.setAlignment(Qt.AlignCenter)
        notification_bar.setFrameShape(QFrame.Box)
        notification_bar.setFrameShadow(QFrame.Raised)
        notification_bar.setLineWidth(2)
        notification_bar.setFixedHeight(50)

        main_layout.addLayout(central_layout)

    
        
    
if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_()) 