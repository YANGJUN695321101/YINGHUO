from PyQt5.QtWidgets import QListWidgetItem
from modules.contact_item联系人列表头像 import ContactItem

class FixedContacts:
    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.add_fixed_contacts()

    def add_fixed_contacts(self):
        # 老王联系人
        contact_item_lao_wang = ContactItem("老王", "D:\\DESK\\remHENKEAI\\ABC.png")
        contact_lao_wang = QListWidgetItem()
        contact_lao_wang.setSizeHint(contact_item_lao_wang.sizeHint())
        self.contact_list.addItem(contact_lao_wang)
        self.contact_list.setItemWidget(contact_lao_wang, contact_item_lao_wang)

        # 鸡哥联系人
        contact_item_ji_ge = ContactItem("鸡哥", "D:\\DESK\\remHENKEAI\\JI_GE.png")
        contact_ji_ge = QListWidgetItem()
        contact_ji_ge.setSizeHint(contact_item_ji_ge.sizeHint())
        self.contact_list.addItem(contact_ji_ge)
        self.contact_list.setItemWidget(contact_ji_ge, contact_item_ji_ge)
