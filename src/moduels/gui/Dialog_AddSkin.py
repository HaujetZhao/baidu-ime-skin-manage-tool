# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from moduels.component.NormalValue import 常量
from moduels.component.HBox_SelectPath import HBox_SelectPath

# 添加预设对话框
class Dialog_AddSkin(QDialog):
    def __init__(self, 列表, 数据库连接, 表单名字, 显示的列名):
        super().__init__()
        self.列表 = 列表
        self.数据库连接 = 数据库连接
        self.表单名字 = 表单名字
        self.显示的列名 = 显示的列名
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值

    def initElements(self):
        self.表单布局 = QFormLayout()

        self.皮肤名字_输入框 = QLineEdit()
        self.输出文件名_输入框 = QLineEdit()
        self.皮肤路径_HBox = HBox_SelectPath(按钮文字='选择', 标题='选择目录', 选择类型=1, 起始目录=常量.源文件默认父路径, 过滤器='所有目录 (*)')
        self.皮肤路径_输入框 = self.皮肤路径_HBox.路径输入框

        self.确认按钮 = QPushButton('确认')
        self.取消按钮 = QPushButton('取消')
        self.按钮横向布局 = QHBoxLayout()

    def initSlots(self):
        self.确认按钮.clicked.connect(self.确认)
        self.取消按钮.clicked.connect(self.取消)

    def initLayouts(self):
        self.按钮横向布局.addWidget(self.确认按钮)
        self.按钮横向布局.addWidget(self.取消按钮)

        self.表单布局.addRow('皮肤名字：', self.皮肤名字_输入框)
        self.表单布局.addRow('输出文件名：', self.输出文件名_输入框)
        self.表单布局.addRow('皮肤源路径：', self.皮肤路径_HBox)
        self.表单布局.addRow(self.按钮横向布局)


        self.setLayout(self.表单布局)

    def initValues(self):
        self.setWindowTitle('添加或更新皮肤')
        self.setWindowIcon(QIcon(常量.图标路径))
        if self.列表.currentItem():
            已选中的列表项 = self.列表.currentItem().text()
            填充数据 = self.从数据库得到选中项的数据(已选中的列表项)
            self.皮肤名字_输入框.setText(已选中的列表项)
            self.输出文件名_输入框.setText(填充数据[0])
            self.皮肤路径_输入框.setText(填充数据[1])
        self.exec()

    def 确认(self):
        self.皮肤名字 = self.皮肤名字_输入框.text() # str
        self.输出文件名 = self.输出文件名_输入框.text() # str
        self.皮肤源路径 = self.皮肤路径_HBox.路径输入框.text() # str
        self.有重名项 = self.检查数据库是否有重名项()
        if self.皮肤名字 == '':
            return False
        if self.有重名项:
            是否覆盖 = QMessageBox.warning(self, '覆盖确认', '已存在相同名字的皮肤，是否覆盖？', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
            if 是否覆盖 != QMessageBox.Yes:
                return False
            self.更新数据库()
        else:
            self.插入数据库()
        self.close()

    def 取消(self):
        self.close()

    def 从数据库得到选中项的数据(self, 已选中的列表项):
        conn = self.数据库连接
        cursor = conn.cursor()
        result = cursor.execute(f'select outputFileName, sourceFilePath, supportDarkMode from {self.表单名字} where {self.显示的列名} = :皮肤名字;',
                                {'皮肤名字': 已选中的列表项})
        return result.fetchone()

    def 检查数据库是否有重名项(self):
        conn = self.数据库连接
        cursor = conn.cursor()
        result = cursor.execute(f'select * from {self.表单名字} where {self.显示的列名} = :皮肤名字;', {'皮肤名字': self.皮肤名字})
        if result.fetchone() == None: return False # 没有重名项，返回 False
        return True

    def 更新数据库(self):
        conn = self.数据库连接
        cursor = conn.cursor()
        cursor.execute(f'''update {self.表单名字} set outputFileName = :输出文件名, 
                                        sourceFilePath = :皮肤源路径
                                        where {self.显示的列名} = :皮肤名字 ''',
                       {'输出文件名': self.输出文件名,
                        '皮肤源路径': self.皮肤源路径,
                        '皮肤名字': self.皮肤名字})
        conn.commit()

    def 插入数据库(self):
        conn = self.数据库连接
        cursor = conn.cursor()
        cursor.execute(f'''insert into {self.表单名字} (skinName, outputFileName, sourceFilePath) values 
                                                (:皮肤名字, :输出文件名, :皮肤源路径)''',
                       {'输出文件名': self.输出文件名,
                        '皮肤源路径': self.皮肤源路径,
                        '皮肤名字': self.皮肤名字})
        conn.commit()

    # 根据刚开始预设名字是否为空，设置确定键可否使用
    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            self.列表.刷新列表()
        except:
            print('皮肤列表刷新失败')
