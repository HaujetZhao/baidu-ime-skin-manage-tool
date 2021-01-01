# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from moduels.component.NormalValue import 常量
from moduels.component.HBox_SelectPath import HBox_SelectPath
from moduels.function.package import zip, unzip

import os, subprocess

# 添加预设对话框
class Dialog_DecompressSkin(QDialog):
    def __init__(self):
        super().__init__()
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值

    def initElements(self):
        self.表单布局 = QFormLayout()

        self.皮肤路径_HBox = HBox_SelectPath(按钮文字='打开', 标题='打开皮肤', 选择类型=0, 起始目录=常量.皮肤输出路径, 过滤器='皮肤文件 (*.bds *.bds)')
        self.解压目录_HBox = HBox_SelectPath(按钮文字='保存', 标题='选择解压路径', 选择类型=1, 起始目录=常量.源文件默认父路径, 过滤器='所有目录 (*)')

        self.确认按钮 = QPushButton('确认')
        self.取消按钮 = QPushButton('取消')
        self.按钮横向布局 = QHBoxLayout()

    def initSlots(self):
        self.确认按钮.clicked.connect(self.确认)
        self.取消按钮.clicked.connect(self.取消)

    def initLayouts(self):
        self.按钮横向布局.addWidget(self.确认按钮)
        self.按钮横向布局.addWidget(self.取消按钮)

        self.表单布局.addRow('皮肤文件：', self.皮肤路径_HBox)
        self.表单布局.addRow('解压路径：', self.解压目录_HBox)
        self.表单布局.addRow(self.按钮横向布局)

        self.setLayout(self.表单布局)

    def initValues(self):
        self.setWindowTitle('添加或更新皮肤')
        self.setWindowIcon(QIcon(常量.图标路径))
        self.exec()

    def 确认(self):
        皮肤路径 = self.皮肤路径_HBox.路径输入框.text()
        解压目录 = self.解压目录_HBox.路径输入框.text()
        unzip(皮肤路径, 解压目录)
        # subprocess.run(f'''winrar x -afzip -ibck -y "{皮肤路径}" "{解压目录 + '/'}"''', startupinfo=常量.subprocessStartUpInfo)
        os.startfile(解压目录)
        self.close()

    def 取消(self):
        self.close()

