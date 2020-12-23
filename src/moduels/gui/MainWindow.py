# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *



from moduels.component.NormalValue import 常量, 线程值
from moduels.component.Stream import Stream
from moduels.gui.Tab_PerfectSkin import Tab_PerfectSkin
from moduels.gui.Tab_Config import Tab_Config
from moduels.gui.Tab_Stdout import Tab_Stdout

import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        常量.主窗口 = self
        self.loadStyleSheet()
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值


        # self.setWindowState(Qt.WindowMaximized)
        # sys.stdout = Stream(newText=self.onUpdateText)

    def initElements(self):
        self.状态栏 = self.statusBar()
        # 定义中心控件为多 tab 页面
        self.tabs = QTabWidget()

        # 定义多个不同功能的 tab
        self.设置标签页 = Tab_Config() # 设置页要在前排加载，以确保一些设置加载成功
        self.皮肤制作标签页 = Tab_PerfectSkin()  # 主要功能的 tab

        self.打印输出标签页 = Tab_Stdout()

        self.标准输出流 = Stream()

        # self.consoleTab = ConsoleTab() # 新的控制台输出 tab
        # self.helpTab = HelpTab()  # 帮助
        # self.aboutTab = AboutTab()  # 关于

        # self.setWindowFlag(Qt.WindowStaysOnTopHint) # 始终在前台



    def initSlots(self):
        self.标准输出流.newText.connect(self.更新控制台输出)
        pass


    def initLayouts(self):

        self.tabs.addTab(self.皮肤制作标签页, '皮肤制作')
        self.tabs.addTab(self.打印输出标签页, '控制台输出')
        self.tabs.addTab(self.设置标签页, '设置')
        self.setCentralWidget(self.tabs)

    def initValues(self):

        self.adjustSize()
        # self.setGeometry(QStyle(Qt.LeftToRight, Qt.AlignCenter, self.size(), QApplication.desktop().availableGeometry()))
        图标路径 = 'misc/icon.icns' if 常量.系统平台 == 'Darwin' else 'misc/icon.ico'
        self.setWindowIcon(QIcon(图标路径))
        self.setWindowTitle('百度手机输入法皮肤辅助管理工具  作者：淳帅二代')

        # sys.stdout = self.标准输出流
        常量.状态栏 = self.状态栏
        self.show()

    def 移动到屏幕中央(self):
        rectangle = self.frameGeometry()
        center = QApplication.desktop().availableGeometry().center()
        rectangle.moveCenter(center)
        self.move(rectangle.topLeft())

    def 更新控制台输出(self, text):
        self.打印输出标签页.print(text)

    def loadStyleSheet(self):
        try:
            try:
                with open(常量.样式文件, 'r', encoding='utf-8') as style:
                    self.setStyleSheet(style.read())
            except:
                with open(常量.样式文件, 'r', encoding='gbk') as style:
                    self.setStyleSheet(style.read())
        except:
            QMessageBox.warning(self, self.tr('主题载入错误'), self.tr('未能成功载入主题，请确保软件 misc 目录有 "style.css" 文件存在。'))

    def keyPressEvent(self, event) -> None:
        # 在按下 F5 的时候重载 style.css 主题
        if (event.key() == Qt.Key_F5):
            self.loadStyleSheet()
            self.status.showMessage('已成功更新主题', 800)

    def onUpdateText(self, text):
        """Write console output to text widget."""

        cursor = self.consoleTab.consoleEditBox.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.consoleTab.consoleEditBox.setTextCursor(cursor)
        self.consoleTab.consoleEditBox.ensureCursorVisible()

    def 状态栏提示(self, 提示文字:str, 时间:int):
        self.状态栏.showMessage(提示文字, 时间)


    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        if 常量.关闭时隐藏到托盘:
            event.ignore()
            self.hide()
        else:
            sys.stdout = sys.__stdout__
            super().closeEvent(event)
