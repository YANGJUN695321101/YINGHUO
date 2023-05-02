from PyQt5.QtCore import QRectF, QSize, Qt
from PyQt5.QtGui import (QBrush, QIcon, QImage, QPainter, QPainterPath,
                         QPixmap, QRegion)
from PyQt5.QtWidgets import (QAction, QFrame, QGridLayout, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QMainWindow, QMenu,
                             QPushButton, QScrollArea, QScrollBar, QSizePolicy,
                             QSpacerItem, QTextEdit, QToolButton, QVBoxLayout,
                             QWidget)
from modules.custom_title_bar import CustomTitleBar
    
from modules.chat_input_text_edit import ChatInputTextEdit
from modules.ui_main_window import Ui_MainWindow

from fixed_contacts import FixedContacts





        

        

        
    
if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
