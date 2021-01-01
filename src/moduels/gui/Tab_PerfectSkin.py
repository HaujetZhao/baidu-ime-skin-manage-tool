# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import os, re, subprocess, time

from moduels.component.QLEdit_FilePathQLineEdit import QLEdit_FilePathQLineEdit
from moduels.component.NormalValue import 常量
# from moduels.component.SpaceLine import QHLine, QVLine
from moduels.thread.Thread_WirelessAdb import Thread_WirelessAdb
from moduels.thread.Thread_GenerateSkins import Thread_GenerateSkins
from moduels.thread.Thread_ExtractAllSkin import Thread_ExtractAllSkin

from moduels.function.applyTemplate import applyTemplate
from moduels.function.openSkinSourcePath import openSkinSourcePath

from moduels.gui.Dialog_AddSkin import Dialog_AddSkin
from moduels.gui.Dialog_DecompressSkin import Dialog_DecompressSkin
from moduels.gui.Dialog_RestoreSkin import Dialog_RestoreSkin
from moduels.gui.Group_EditableList import Group_EditableList
from moduels.gui.VBox_RBtnContainer import VBox_RBtnContainer
from moduels.gui.Combo_SoundList import Combo_SoundList


class Tab_PerfectSkin(QWidget):
    def __init__(self):
        super().__init__()
        self.initElements()  # 先初始化各个控件
        self.initSlots()  # 再将各个控件连接到信号槽
        self.initLayouts()  # 然后布局
        self.initValues()  # 再定义各个控件的值


    def initElements(self):
        self.初始化左侧部件()
        self.初始化中部部件()
        self.两个分区Box横向布局 = QHBoxLayout()

        self.无线adb线程 = Thread_WirelessAdb(self)
        self.生成皮肤线程 = Thread_GenerateSkins(self.皮肤列表Box.列表, self)
        self.提取皮肤线程 = Thread_ExtractAllSkin(self)

    def initLayouts(self):
        self.setLayout(self.两个分区Box横向布局)
        self.布局左侧部件()
        self.布局中部部件()
        self.两个分区Box横向布局.addWidget(self.皮肤列表Box)
        self.两个分区Box横向布局.addLayout(self.中间功能区Box纵向布局)
        self.两个分区Box横向布局.setStretch(0, 2)
        self.两个分区Box横向布局.setStretch(1, 3)

    def 初始化左侧部件(self):
        self.皮肤列表Box = Group_EditableList('皮肤列表', Dialog_AddSkin, 常量.数据库连接, 常量.数据库皮肤表单名, 'skinName')

    def 布局左侧部件(self):
        pass

    def 初始化中部部件(self):

        self.输出选项Box = QGroupBox('输出选项')
        self.压缩图片选项Box = QGroupBox('图片压缩')
        self.输出格式选项Box = QGroupBox('输出格式')
        self.其它选项Box = QGroupBox('其它')


        self.adb功能按钮Box = QGroupBox('adb')
        self.皮肤文件操作功能按钮Box = QGroupBox('皮肤文件')
        self.文件夹功能按钮Box = QGroupBox('文件夹')
        self.备份功能按钮Box = QGroupBox('备份')
        self.打包功能按钮Box = QGroupBox('打包')

        self.中间功能区Box纵向布局 = QVBoxLayout()
        self.输出选项Box栅格布局 = QGridLayout()

        self.adb功能按钮Box栅格布局 = QGridLayout()
        self.皮肤文件操作功能按钮Box栅格布局 = QGridLayout()
        self.文件夹功能按钮Box栅格布局 = QGridLayout()
        self.备份功能按钮Box栅格布局 = QGridLayout()
        self.打包功能按钮Box栅格布局 = QGridLayout()

        self.压缩图片_按钮纵向布局 = VBox_RBtnContainer()
        self.压缩图片_不压缩_选择按钮 = QRadioButton('不压缩')
        self.压缩图片_无损压缩_选择按钮 = QRadioButton('无损压缩')
        self.压缩图片_有损压缩_选择按钮 = QRadioButton('有损压缩')

        self.输出格式_按钮纵向布局 = VBox_RBtnContainer()
        self.输出格式_安卓_选择按钮 = QRadioButton('安卓')
        self.输出格式_苹果_选择按钮 = QRadioButton('苹果')

        self.其它_按钮纵向布局 = QVBoxLayout()
        self.其它_安装到手机选框 = QCheckBox('adb发送到手机')
        self.其它_清理注释选框 = QCheckBox('清理注释')

        self.无线adb连接手机_按钮 = QPushButton('无线adb连接手机')
        self.提取手机所有皮肤_按钮 = QPushButton('提取手机所有皮肤')

        self.解压皮肤_按钮 = QPushButton('解包皮肤文件')
        self.发送皮肤_按钮 = QPushButton('发送皮肤到手机')

        self.打开皮肤源文件夹_按钮 = QPushButton('打开皮肤源文件夹')
        self.打开输出文件夹_按钮 = QPushButton('打开输出文件夹')

        self.备份选中皮肤_按钮 = QPushButton('备份选中皮肤')
        self.还原选中皮肤_按钮 = QPushButton('还原选中皮肤')

        self.打包选中皮肤_按钮 = QPushButton('打包选中皮肤')
        self.打包所有皮肤_按钮 = QPushButton('打包所有皮肤')


    def 布局中部部件(self):
        self.压缩图片_按钮纵向布局.addWidget(self.压缩图片_不压缩_选择按钮)
        self.压缩图片_按钮纵向布局.addWidget(self.压缩图片_无损压缩_选择按钮)
        self.压缩图片_按钮纵向布局.addWidget(self.压缩图片_有损压缩_选择按钮)
        self.压缩图片_按钮纵向布局.addStretch(1)
        self.压缩图片选项Box.setLayout(self.压缩图片_按钮纵向布局)

        self.输出格式_按钮纵向布局.addWidget(self.输出格式_安卓_选择按钮)
        self.输出格式_按钮纵向布局.addWidget(self.输出格式_苹果_选择按钮)
        self.输出格式_按钮纵向布局.addStretch(1)
        self.输出格式选项Box.setLayout(self.输出格式_按钮纵向布局)

        self.其它_按钮纵向布局.addWidget(self.其它_安装到手机选框)
        self.其它_按钮纵向布局.addWidget(self.其它_清理注释选框)
        self.其它_按钮纵向布局.addStretch(1)
        self.其它选项Box.setLayout(self.其它_按钮纵向布局)

        self.输出选项Box栅格布局.addWidget(self.压缩图片选项Box, 0, 0)
        self.输出选项Box栅格布局.addWidget(self.输出格式选项Box, 0, 1)
        self.输出选项Box栅格布局.addWidget(self.其它选项Box, 0, 2)
        self.输出选项Box栅格布局.setColumnStretch(0, 1)
        self.输出选项Box栅格布局.setColumnStretch(1, 1)
        self.输出选项Box栅格布局.setColumnStretch(2, 1)
        self.输出选项Box.setLayout(self.输出选项Box栅格布局)

        self.adb功能按钮Box栅格布局.addWidget(self.无线adb连接手机_按钮, 0, 0)
        self.adb功能按钮Box栅格布局.addWidget(self.提取手机所有皮肤_按钮, 0, 1)

        self.皮肤文件操作功能按钮Box栅格布局.addWidget(self.解压皮肤_按钮, 0, 0)
        self.皮肤文件操作功能按钮Box栅格布局.addWidget(self.发送皮肤_按钮, 0, 1)


        self.文件夹功能按钮Box栅格布局.addWidget(self.打开皮肤源文件夹_按钮, 0, 0)
        self.文件夹功能按钮Box栅格布局.addWidget(self.打开输出文件夹_按钮, 0, 1)

        self.备份功能按钮Box栅格布局.addWidget(self.备份选中皮肤_按钮, 0, 0)
        self.备份功能按钮Box栅格布局.addWidget(self.还原选中皮肤_按钮, 0, 1)

        self.打包功能按钮Box栅格布局.addWidget(self.打包选中皮肤_按钮, 0, 0)
        self.打包功能按钮Box栅格布局.addWidget(self.打包所有皮肤_按钮, 0, 1)

        # self.按钮Box栅格布局.addWidget(self.打开皮肤源文件夹_按钮, 0, 0)
        # self.按钮Box栅格布局.addWidget(self.打开输出文件夹_按钮, 0, 1)
        # self.按钮Box栅格布局.addWidget(self.无线adb连接手机_按钮, 0, 2)
        # self.按钮Box栅格布局.addWidget(self.生成选中皮肤_按钮, 0, 3)
        # self.按钮Box栅格布局.addWidget(self.生成所有皮肤_按钮, 0, 4)
        # self.按钮Box.setLayout(self.按钮Box栅格布局)
        self.adb功能按钮Box.setLayout(self.adb功能按钮Box栅格布局)
        self.皮肤文件操作功能按钮Box.setLayout(self.皮肤文件操作功能按钮Box栅格布局)
        self.文件夹功能按钮Box.setLayout(self.文件夹功能按钮Box栅格布局)
        self.备份功能按钮Box.setLayout(self.备份功能按钮Box栅格布局)
        self.打包功能按钮Box.setLayout(self.打包功能按钮Box栅格布局)

        self.中间功能区Box纵向布局.addWidget(self.输出选项Box)
        self.中间功能区Box纵向布局.addWidget(self.adb功能按钮Box)
        self.中间功能区Box纵向布局.addWidget(self.皮肤文件操作功能按钮Box)
        self.中间功能区Box纵向布局.addWidget(self.文件夹功能按钮Box)
        self.中间功能区Box纵向布局.addWidget(self.备份功能按钮Box)
        self.中间功能区Box纵向布局.addWidget(self.打包功能按钮Box)
        # self.中间功能区Box纵向布局.setStretch(0, 5)
        # self.中间功能区Box纵向布局.setStretch(1, 2)
        # self.中间功能区Box纵向布局.setStretch(2, 1)


    def initSlots(self):
        self.为输出选项按钮设置id和slot()

        self.无线adb连接手机_按钮.clicked.connect(self.无线adb)
        self.提取手机所有皮肤_按钮.clicked.connect(self.提取皮肤)

        self.解压皮肤_按钮.clicked.connect(self.解压皮肤)
        self.发送皮肤_按钮.clicked.connect(self.发送皮肤)

        self.打开皮肤源文件夹_按钮.clicked.connect(lambda: openSkinSourcePath(self.皮肤列表Box.列表))
        self.打开输出文件夹_按钮.clicked.connect(self.打开皮肤输出文件夹)

        self.备份选中皮肤_按钮.clicked.connect(self.备份选中皮肤)
        self.还原选中皮肤_按钮.clicked.connect(self.还原选中皮肤)

        self.打包选中皮肤_按钮.clicked.connect(self.打包选中皮肤)
        self.打包所有皮肤_按钮.clicked.connect(self.打包所有皮肤)

        self.生成皮肤线程.完成信号.connect(self.生成皮肤线程完成)
        self.无线adb线程.状态栏消息.connect(lambda 消息, 时间: 常量.状态栏.showMessage(消息, 时间))
        self.提取皮肤线程.状态栏消息.connect(lambda 消息, 时间: 常量.状态栏.showMessage(消息, 时间))
        self.生成皮肤线程.状态栏消息.connect(lambda 消息, 时间: 常量.状态栏.showMessage(消息, 时间))
        pass

    def 为输出选项按钮设置id和slot(self):
        self.压缩图片_不压缩_选择按钮.setProperty('id', 0)
        self.压缩图片_不压缩_选择按钮.toggled.connect(lambda e: self.设置输出选项值('图片压缩', 0) if e else 0)
        self.压缩图片_无损压缩_选择按钮.setProperty('id', 1)
        self.压缩图片_无损压缩_选择按钮.toggled.connect(lambda e: self.设置输出选项值('图片压缩', 1) if e else 0)
        self.压缩图片_有损压缩_选择按钮.setProperty('id', 2)
        self.压缩图片_有损压缩_选择按钮.toggled.connect(lambda e: self.设置输出选项值('图片压缩', 2) if e else 0)

        self.输出格式_安卓_选择按钮.setProperty('id', 0)
        self.输出格式_安卓_选择按钮.toggled.connect(lambda e: self.设置输出选项值('输出格式', 0) if e else 0)
        self.输出格式_苹果_选择按钮.setProperty('id', 1)
        self.输出格式_苹果_选择按钮.toggled.connect(lambda e: self.设置输出选项值('输出格式', 1) if e else 0)

        self.其它_安装到手机选框.toggled.connect(lambda e: self.设置输出选项值('adb发送至手机', e))
        self.其它_清理注释选框.toggled.connect(lambda e: self.设置输出选项值('清理注释', e))

    def 设置输出选项值(self, 名, 值): 常量.输出选项[名] = 值

    def initValues(self):
        self.压缩图片_按钮纵向布局.通过id勾选单选按钮(常量.输出选项['图片压缩'])
        self.输出格式_按钮纵向布局.通过id勾选单选按钮(常量.输出选项['输出格式'])
        self.其它_安装到手机选框.setChecked(常量.输出选项['adb发送至手机'])
        self.其它_清理注释选框.setChecked(常量.输出选项['清理注释'])

    def 无线adb(self):
        self.无线adb线程.start()

    def 提取皮肤(self):
        self.提取皮肤线程.start()

    def 解压皮肤(self):
        解压皮肤对话框 = Dialog_DecompressSkin()

    def 发送皮肤(self):
        获得的皮肤路径 = QFileDialog.getOpenFileName(self, caption='选择皮肤', dir=常量.皮肤输出路径, filter='皮肤文件 (*.bds)')[0]
        if 获得的皮肤路径 == '': return True
        皮肤文件名 = os.path.basename(获得的皮肤路径)
        手机皮肤路径 = '/sdcard/baidu/ime/skins/' + 皮肤文件名
        发送皮肤命令 = f'''adb push "{获得的皮肤路径}" "{手机皮肤路径}"'''
        subprocess.run(发送皮肤命令, startupinfo=常量.subprocessStartUpInfo)
        安装皮肤命令 = f'''adb shell am start -a android.intent.action.VIEW -c android.intent.category.DEFAULT -n com.baidu.input/com.baidu.input.ImeUpdateActivity -d '{手机皮肤路径}' '''
        subprocess.run(安装皮肤命令, startupinfo=常量.subprocessStartUpInfo)


    def 备份选中皮肤(self):
        if self.皮肤列表Box.列表.currentRow() < 0: return
        已选中的列表项 = self.皮肤列表Box.列表.currentItem().text()
        输出文件名, 皮肤源文件目录 = 常量.数据库连接.cursor().execute(
            f'select outputFileName, sourceFilePath from {常量.数据库皮肤表单名} where skinName = :皮肤名字;',
            {'皮肤名字': 已选中的列表项}).fetchone()
        备份时间 = time.localtime()
        备份压缩文件名 = f'{输出文件名}_备份_{备份时间.tm_year}年{备份时间.tm_mon}月{备份时间.tm_mday}日{备份时间.tm_hour}时{备份时间.tm_min}分{备份时间.tm_sec}秒.bds'
        备份文件完整路径 = os.path.join(常量.皮肤输出路径, '皮肤备份文件', 备份压缩文件名)
        备份命令 = f'''winrar a -afzip -ibck -r -ep1 "{备份文件完整路径}" "{皮肤源文件目录}/*"'''
        if not os.path.exists(os.path.dirname(备份文件完整路径)): os.makedirs(os.path.dirname(备份文件完整路径))
        subprocess.run(备份命令, startupinfo=常量.subprocessStartUpInfo)
        os.startfile(os.path.dirname(备份文件完整路径))


    def 还原选中皮肤(self):
        if self.皮肤列表Box.列表.currentRow() < 0: return
        已选中的列表项 = self.皮肤列表Box.列表.currentItem().text()
        输出文件名, 皮肤源文件目录 = 常量.数据库连接.cursor().execute(
            f'select outputFileName, sourceFilePath from {常量.数据库皮肤表单名} where skinName = :皮肤名字;',
            {'皮肤名字': 已选中的列表项}).fetchone()
        备份文件夹路径 = os.path.join(常量.皮肤输出路径, '皮肤备份文件')
        Dialog_RestoreSkin(备份文件夹路径, 输出文件名, 皮肤源文件目录)

    def 打开皮肤输出文件夹(self):
        if not os.path.exists(常量.皮肤输出路径): os.makedirs(常量.皮肤输出路径)
        os.startfile(常量.皮肤输出路径)

    def 打包选中皮肤(self):
        if self.皮肤列表Box.列表.currentRow() < 0: return True
        self.备份选中皮肤_按钮.setDisabled(True)
        self.还原选中皮肤_按钮.setDisabled(True)
        self.打包选中皮肤_按钮.setDisabled(True)
        self.打包所有皮肤_按钮.setDisabled(True)
        self.生成皮肤线程.是否要全部生成 = False
        self.生成皮肤线程.start()

    def 打包所有皮肤(self):
        self.备份选中皮肤_按钮.setDisabled(True)
        self.还原选中皮肤_按钮.setDisabled(True)
        self.打包选中皮肤_按钮.setDisabled(True)
        self.打包所有皮肤_按钮.setDisabled(True)
        self.生成皮肤线程.是否要全部生成 = True
        self.生成皮肤线程.start()

    def 生成皮肤线程完成(self):
        self.备份选中皮肤_按钮.setEnabled(True)
        self.还原选中皮肤_按钮.setEnabled(True)
        self.打包选中皮肤_按钮.setEnabled(True)
        self.打包所有皮肤_按钮.setEnabled(True)
        常量.状态栏.showMessage('打包任务完成！', 5000)
