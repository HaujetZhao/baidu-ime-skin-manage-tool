from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from moduels.component.QLEdit_FilePathQLineEdit import QLEdit_FilePathQLineEdit
from moduels.component.PBtn_SelectPath import PBtn_SelectPath


class HBox_SelectPath(QHBoxLayout):
    def __init__(self, 按钮文字='打开', 标题='打开', 选择类型=0, 起始目录='.', 过滤器='所有文件 (*.*)'):
        super().__init__()
        self.按钮文字 = 按钮文字
        self.标题 = 标题
        self.选择类型 = 选择类型
        self.起始目录 = 起始目录
        self.过滤器 = 过滤器
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值

    def initElements(self):
        self.路径输入框 = QLEdit_FilePathQLineEdit()
        self.选择文件按钮 = PBtn_SelectPath(按钮文字=self.按钮文字, 标题=self.标题, 选择类型=self.选择类型, 起始目录=self.起始目录, 过滤器=self.过滤器)

    def initSlots(self):
        self.选择文件按钮.signal.connect(self.路径输入框.得到路径)
        pass
        # self.hideToSystemTraySwitch.clicked.connect(self.隐藏到状态栏开关被点击)

    def initLayouts(self):
        self.setContentsMargins(0,0,0,0)
        self.addWidget(self.路径输入框)
        self.addWidget(self.选择文件按钮)

    def initValues(self):
        pass
        # self.检查数据库()



