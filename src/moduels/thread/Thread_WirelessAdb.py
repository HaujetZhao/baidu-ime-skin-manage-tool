# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from moduels.component.NormalValue import 常量
from moduels.component.NormalValue import 线程值

from moduels.function.wirelessAdb import wirelessAdb


class Thread_WirelessAdb(QThread):

    def __init__(self, parent=None):
        super(Thread_WirelessAdb, self).__init__(parent)
        self.正在运行 = 0
        QApplication.instance().aboutToQuit.connect(self.要退出了)

    def 要退出了(self):
        self.terminate()

    def run(self):
        if self.正在运行 == 1: return False
        self.正在运行 = 1
        常量.状态栏.showMessage('正在无线连接', 2000)
        无线adb连接结果 = wirelessAdb()
        常量.状态栏.showMessage('无线连接成功，现在可以拔掉数据线了！', 2000) if 无线adb连接结果 else 常量.状态栏.showMessage('无线连接失败', 2000)
        self.正在运行 = 0