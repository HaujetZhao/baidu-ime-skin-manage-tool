# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from moduels.gui.List_List import List_List
from moduels.component.QLEdit_FilePathQLineEdit import QLEdit_FilePathQLineEdit

# 添加预设对话框
class Group_PathSetting(QGroupBox):
    def __init__(self):
        super().__init__('路径设置')
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值

    def initElements(self):
        self.表单布局 = QFormLayout()
        self.皮肤输出路径输入框 = QLEdit_FilePathQLineEdit()
        self.音效文件路径输入框 = QLEdit_FilePathQLineEdit()

    def initSlots(self):
        pass



    def initLayouts(self):
        self.setLayout(self.表单布局)
        self.表单布局.addRow('皮肤输出路径：', self.皮肤输出路径输入框)
        # self.表单布局.addRow('音效文件路径：', self.音效文件路径输入框)


    def initValues(self):
        pass




