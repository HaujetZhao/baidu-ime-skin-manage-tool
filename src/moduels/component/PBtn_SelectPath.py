# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from moduels.component.NormalValue import 常量

# 可拖入文件的单行编辑框
class PBtn_SelectPath(QPushButton):
    signal = Signal(str)
    def __init__(self, 按钮文字='打开', 标题='打开文件', 选择类型=0, 起始目录='.', 过滤器='所有文件 (*.*)'):
        super().__init__()
        self.按钮文字 = 按钮文字
        self.标题 = 标题
        self.选择类型 = 选择类型 # 0表示选择文件，1表示选择文件夹，2表示保存文件名，3表示保存到的文件夹
        self.起始目录 = 起始目录
        self.过滤器 = 过滤器
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
        self.setText(self.按钮文字)

    def mousePressEvent(self, e:QMouseEvent):
        # 0表示选择文件，1表示选择文件夹，2表示保存文件名
        if self.选择类型 == 0:
            获得的路径 = QFileDialog.getOpenFileName(self, caption=self.标题, dir=self.起始目录, filter=self.过滤器)
            self.signal.emit(获得的路径[0])
        if self.选择类型 == 1:
            获得的路径 = QFileDialog.getExistingDirectory(self, caption=self.标题, dir=self.起始目录, filter=self.过滤器)
            self.signal.emit(获得的路径)
        if self.选择类型 == 2:
            获得的路径 = QFileDialog.getSaveFileName(self, caption=self.标题, dir=self.起始目录, filter=self.过滤器)
            self.signal.emit(获得的路径)

        # QStringList
        # files = QFileDialog::getOpenFileNames(
        #     this,
        #     "Select one or more files to open",
        #     "/home",
        #     "Images (*.png *.xpm *.jpg)");
        # "Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)"