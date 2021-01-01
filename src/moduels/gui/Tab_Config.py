from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtSql import *
from PySide2.QtWidgets import *
from moduels.component.NormalValue import 常量
from moduels.gui.Group_PathSetting import Group_PathSetting


class Tab_Config(QWidget):
    def __init__(self, parent=None):
        super(Tab_Config, self).__init__(parent)
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值

    def initElements(self):
        self.开关_关闭窗口时隐藏到托盘 = QCheckBox(self.tr('点击关闭按钮时隐藏到托盘'))
        self.程序设置横向布局 = QHBoxLayout()
        self.程序设置Box = QGroupBox(self.tr('程序设置'))
        self.路径设置Box = Group_PathSetting()

        self.选项Box纵向布局 = QVBoxLayout()

    def initSlots(self):
        self.开关_关闭窗口时隐藏到托盘.stateChanged.connect(self.设置_隐藏到状态栏)
        self.路径设置Box.皮肤输出路径输入框.textChanged.connect(self.设置_皮肤输出路径)
        self.路径设置Box.音效文件路径输入框.textChanged.connect(self.设置_音效文件路径)
        self.路径设置Box.皮肤源文件默认父路径输入框.textChanged.connect(self.设置_皮肤源文件默认父路径)

    def initLayouts(self):
        self.程序设置横向布局.addWidget(self.开关_关闭窗口时隐藏到托盘)
        self.程序设置Box.setLayout(self.程序设置横向布局)

        self.选项Box纵向布局.addWidget(self.程序设置Box)
        self.选项Box纵向布局.addWidget(self.路径设置Box)
        self.选项Box纵向布局.addStretch(1)

        self.setLayout(self.选项Box纵向布局)

    def initValues(self):
        self.检查数据库()


    def 检查数据库(self):
        数据库连接 = 常量.数据库连接
        self.检查数据库_关闭时最小化(数据库连接)
        self.检查数据库_皮肤输出路径(数据库连接)
        self.检查数据库_音效文件路径(数据库连接)
        self.检查数据库_皮肤源文件默认父路径(数据库连接)

    def 检查数据库_关闭时最小化(self, 数据库连接):
        result = 数据库连接.cursor().execute(f'''select value from {常量.数据库偏好设置表单名} where item = :item''',
                                {'item': 'hideToTrayWhenHitCloseButton'}).fetchone()
        if result == None: # 如果关闭窗口最小化到状态栏这个选项还没有在数据库创建，那就创建一个
            初始值 = 'False'
            数据库连接.cursor().execute(f'''insert into {常量.数据库偏好设置表单名} (item, value) values (:item, :value) ''',
                           {'item': 'hideToTrayWhenHitCloseButton',
                            'value':初始值})
            数据库连接.commit()
            self.开关_关闭窗口时隐藏到托盘.setChecked(初始值 == 'True')
        else:
            self.开关_关闭窗口时隐藏到托盘.setChecked(result[0] == 'True')

    def 检查数据库_皮肤输出路径(self, 数据库连接):
        result = 数据库连接.cursor().execute(f'''select value from {常量.数据库偏好设置表单名} where item = :item''',
                                        {'item': 'skinOutputPath'}).fetchone()
        if result == None:  # 如果关闭窗口最小化到状态栏这个选项还没有在数据库创建，那就创建一个
            初始值 = 'output'
            数据库连接.cursor().execute(f'''insert into {常量.数据库偏好设置表单名} (item, value) values (:item, :value) ''',
                                   {'item': 'skinOutputPath',
                                    'value': 初始值})
            数据库连接.commit()
            self.路径设置Box.皮肤输出路径输入框.setText(初始值)
        else:
            self.路径设置Box.皮肤输出路径输入框.setText(result[0])

    def 检查数据库_音效文件路径(self, 数据库连接):
        result = 数据库连接.cursor().execute(f'''select value from {常量.数据库偏好设置表单名} where item = :item''',
                                        {'item': 'soundFilePath'}).fetchone()
        if result == None:  # 如果关闭窗口最小化到状态栏这个选项还没有在数据库创建，那就创建一个
            初始值 = 'sound'
            数据库连接.cursor().execute(f'''insert into {常量.数据库偏好设置表单名} (item, value) values (:item, :value) ''',
                                   {'item': 'soundFilePath',
                                    'value': 初始值})
            数据库连接.commit()
            self.路径设置Box.音效文件路径输入框.setText(初始值)
        else:
            self.路径设置Box.音效文件路径输入框.setText(result[0])

    def 检查数据库_皮肤源文件默认父路径(self, 数据库连接):
        result = 数据库连接.cursor().execute(f'''select value from {常量.数据库偏好设置表单名} where item = :item''',
                                        {'item': '皮肤源文件默认父路径'}).fetchone()
        if result == None:  # 如果关闭窗口最小化到状态栏这个选项还没有在数据库创建，那就创建一个
            初始值 = 'skinSource'
            数据库连接.cursor().execute(f'''insert into {常量.数据库偏好设置表单名} (item, value) values (:item, :value) ''',
                                   {'item': '皮肤源文件默认父路径',
                                    'value': 初始值})
            数据库连接.commit()
            self.路径设置Box.皮肤源文件默认父路径输入框.setText(初始值)
        else:
            self.路径设置Box.皮肤源文件默认父路径输入框.setText(result[0])

    def 设置_隐藏到状态栏(self):
        数据库连接 = 常量.数据库连接
        数据库连接.cursor().execute(f'''update {常量.数据库偏好设置表单名} set value = :value where item = :item''',
                               {'item': 'hideToTrayWhenHitCloseButton',
                                'value': str(self.开关_关闭窗口时隐藏到托盘.isChecked())})
        数据库连接.commit()
        常量.关闭时隐藏到托盘 = self.开关_关闭窗口时隐藏到托盘.isChecked()

    def 设置_皮肤输出路径(self):
        数据库连接 = 常量.数据库连接
        数据库连接.cursor().execute(f'''update {常量.数据库偏好设置表单名} set value = :value where item = :item''',
                               {'item': 'skinOutputPath',
                                'value': self.路径设置Box.皮肤输出路径输入框.text()})
        数据库连接.commit()
        常量.皮肤输出路径 = self.路径设置Box.皮肤输出路径输入框.text()


    def 设置_音效文件路径(self):
        数据库连接 = 常量.数据库连接
        数据库连接.cursor().execute(f'''update {常量.数据库偏好设置表单名} set value = :value where item = :item''',
                               {'item': 'soundFilePath',
                                'value': self.路径设置Box.音效文件路径输入框.text()})
        数据库连接.commit()
        常量.音效文件路径 = self.路径设置Box.音效文件路径输入框.text()

    def 设置_皮肤源文件默认父路径(self):
        数据库连接 = 常量.数据库连接
        数据库连接.cursor().execute(f'''update {常量.数据库偏好设置表单名} set value = :value where item = :item''',
                               {'item': '皮肤源文件默认父路径',
                                'value': self.路径设置Box.皮肤源文件默认父路径输入框.text()})
        数据库连接.commit()
        常量.音效文件路径 = self.路径设置Box.皮肤源文件默认父路径输入框.text()

    def 隐藏到状态栏开关被点击(self):
        cursor = 常量.数据库连接.cursor()
        cursor.execute(f'''update {常量.数据库偏好设置表单名} set value='{str(self.开关_关闭窗口时隐藏到托盘.isChecked())}' where item = '{'hideToTrayWhenHitCloseButton'}';''')
        常量.数据库连接.commit()
