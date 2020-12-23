# -*- coding: UTF-8 -*-

import os, sys, time
try:
    os.chdir(os.path.dirname(__file__)) # 更改工作目录，指向正确的当前文件夹
    sys.path.append(os.path.dirname(__file__)) # 将当前目录导入 python 寻找 package 和 moduel 的变量
except:
    print('更改使用路径失败，不过没关系')
os.environ['PATH'] += os.pathsep + os.path.abspath('./bin') # 将可执行文件的目录加入环境变量

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from moduels.function.createDB import * # 引入检查和创建创建数据库的函数

from moduels.gui.MainWindow import MainWindow
from moduels.gui.SystemTray import SystemTray
from moduels.component.NormalValue import 常量


############# 主窗口和托盘 ################

def 要退出了():
    print('退出')

def main():
    app = QApplication(sys.argv)
    # app.aboutToQuit.connect(要退出了)
    createDB()
    mainWindow = MainWindow()
    tray = SystemTray(mainWindow)
    常量.托盘 = tray
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
