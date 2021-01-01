# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from moduels.component.NormalValue import 常量
from moduels.component.HBox_SelectPath import HBox_SelectPath

import os, subprocess

# 添加预设对话框
class Dialog_RestoreSkin(QDialog):
    def __init__(self, 备份文件夹路径, 皮肤开头文件名, 皮肤源文件目录):
        super().__init__()
        self.备份文件夹路径 = 备份文件夹路径
        self.皮肤开头文件名 = 皮肤开头文件名
        self.皮肤源文件目录 = 皮肤源文件目录
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值

    def initElements(self):
        self.纵向布局 = QVBoxLayout()

        self.备份文件列表 = QListWidget()

        self.确认按钮 = QPushButton('确认')
        self.取消按钮 = QPushButton('取消')
        self.按钮横向布局 = QHBoxLayout()

    def initSlots(self):
        self.确认按钮.clicked.connect(self.确认)
        self.取消按钮.clicked.connect(self.取消)

    def initLayouts(self):
        self.按钮横向布局.addWidget(self.确认按钮)
        self.按钮横向布局.addSpacing(40)
        self.按钮横向布局.addWidget(self.取消按钮)

        self.纵向布局.addWidget(self.备份文件列表)
        self.纵向布局.addLayout(self.按钮横向布局)

        self.setLayout(self.纵向布局)

    def initValues(self):
        self.setWindowTitle('还原皮肤')
        self.setWindowIcon(QIcon(常量.图标路径))
        with os.scandir(self.备份文件夹路径) as 目录条目:
            for entry in 目录条目:
                if entry.name.startswith(self.皮肤开头文件名) and entry.is_file():
                    self.备份文件列表.addItem(entry.name)
        self.exec()

    def 确认(self):
        if self.备份文件列表.currentRow() < 0: return
        备份文件路径 = os.path.join(self.备份文件夹路径, self.备份文件列表.currentItem().text())
        # 备份命令 = f'''winrar x -afzip -ibck -y "{}" "{self.皮肤源文件目录}"'''
        备份命令 = f'''7z x -y -tzip "{备份文件路径}" -aoa -o"{self.皮肤源文件目录}" '''
        确认恢复 = QMessageBox.warning(self, '确认恢复', f'恢复将会使用 “{self.备份文件列表.currentItem().text()}” 文件的内容覆盖当前的皮肤源文件，当真要恢复？', QMessageBox.Yes | QMessageBox.Cancel,
                                   QMessageBox.Cancel)
        if 确认恢复 != QMessageBox.Yes:
            return False
        subprocess.run(备份命令, startupinfo=常量.subprocessStartUpInfo)
        print(f'恢复完成：{备份文件路径}')
        self.close()

    def 取消(self):
        self.close()

