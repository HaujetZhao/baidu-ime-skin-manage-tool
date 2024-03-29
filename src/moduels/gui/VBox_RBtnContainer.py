# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# 添加预设对话框
class VBox_RBtnContainer(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值

    def initElements(self):
        pass

    def initSlots(self):
        pass

    def initLayouts(self):
        pass

    def initValues(self):
        pass

    def 通过id勾选单选按钮(self, id):
        for index in range(self.count()):
            widget = self.itemAt(index).widget()
            if type(widget) == QRadioButton:
                if widget.property('id') == id:
                    widget.setChecked(1)
