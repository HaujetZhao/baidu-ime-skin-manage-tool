# -*- coding: UTF-8 -*-

import os
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from moduels.component.NormalValue import 常量

# 添加预设对话框
class Combo_SoundList(QComboBox):
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
        self.初始化列表()

    def mousePressEvent(self, e):
        self.列表更新()
        self.showPopup()

    def 初始化列表(self):
        self.列表项 = []
        if not os.path.exists(常量.音效文件路径): os.makedirs(常量.音效文件路径)
        with os.scandir(常量.音效文件路径) as 目录条目:
            for entry in 目录条目:
                if not entry.name.startswith('.') and entry.is_dir():
                    self.列表项.append(entry.name)
        self.addItems(self.列表项)

    def 列表更新(self):
        新列表 = []
        if not os.path.exists(常量.音效文件路径): os.makedirs(常量.音效文件路径)
        with os.scandir(常量.音效文件路径) as 目录条目:
            for entry in 目录条目:
                if not entry.name.startswith('.') and entry.is_dir():
                    新列表.append(entry.name)
        if self.列表项 == 新列表: return True
        self.clear()
        self.列表项 = 新列表
        self.addItems(self.列表项)

