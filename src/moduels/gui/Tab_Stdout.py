# -*- coding: UTF-8 -*-


from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from moduels.component.QEditBox_StdoutBox import QEditBox_StdoutBox
from moduels.component.NormalValue import 常量


class Tab_Stdout(QWidget):
    def __init__(self):
        super().__init__()
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值

    def initElements(self):

        self.标准输出框 = QEditBox_StdoutBox()
        self.主布局 = QVBoxLayout()
        pass

    def initSlots(self):
        pass

    def initLayouts(self):
        self.主布局.addWidget(self.标准输出框)
        self.setLayout(self.主布局)

    def initValues(self):
        # 常量.控制台标签页 = self
        ...






