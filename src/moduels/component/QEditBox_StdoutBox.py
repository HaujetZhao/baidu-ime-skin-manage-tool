# -*- coding: UTF-8 -*-

import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from moduels.component.Stream import Stream

# 命令输出窗口中的多行文本框
class QEditBox_StdoutBox(QTextEdit):
    # 定义一个 QTextEdit 类，写入 print 方法。用于输出显示。
    def __init__(self, parent=None):
        super(QEditBox_StdoutBox, self).__init__(parent)
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值


    def initElements(self):
        self.标准输出流 = Stream()

    def initSlots(self):
        self.标准输出流.newText.connect(self.print)

    def initLayouts(self):
        ...

    def initValues(self):
        self.setReadOnly(True)
        sys.stdout = self.标准输出流

    def print(self, text):
        try:
            cursor = self.textCursor()
            cursor.movePosition(QTextCursor.End)
            cursor.insertText(text)
            self.setTextCursor(cursor)
            self.ensureCursorVisible()
        except:
            print('文本框更新文本失败')
