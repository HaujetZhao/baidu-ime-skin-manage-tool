# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from moduels.component.NormalValue import 常量
from moduels.component.NormalValue import 线程值

from moduels.function.wirelessAdb import wirelessAdb
from moduels.function.compressImages import optipng压缩图片, pngquant压缩图片

import time, sqlite3, os, shutil, re, subprocess

class Thread_GenerateSkins(QThread):

    是否要全部生成 = False
    完成信号 = Signal()

    def __init__(self, 列表, parent=None):
        super().__init__(parent)
        self.正在运行 = 0
        self.列表 = 列表
        QApplication.instance().aboutToQuit.connect(self.要退出了)

    def 要退出了(self):
        self.terminate()

    def run(self):
        self.数据库连接 = sqlite3.connect(常量.数据库路径)
        self.图片压缩 = 常量.输出选项['图片压缩']
        self.输出格式 = 常量.输出选项['输出格式']
        self.发送到手机 = 常量.输出选项['adb发送至手机']
        self.是否清理注释 = 常量.输出选项['清理注释']
        self.临时skin目录 = os.path.join(常量.皮肤输出路径, 'skin')
        self.皮肤输出路径 = 常量.皮肤输出路径
        if self.是否要全部生成:
            全部皮肤名 = []
            for i in range(self.列表.count()):
                全部皮肤名.append(self.列表.item(i).text())
            for 皮肤 in 全部皮肤名:
                self.生成一个皮肤(皮肤)
        else:
            当前选中皮肤名 = self.列表.currentItem().text()
            self.生成一个皮肤(当前选中皮肤名)
        print('打包任务完成')
        self.完成信号.emit()
        self.数据库连接.close()

    def 清理注释(self, 文件夹, *全部文件类型):
        for 文件类型 in 全部文件类型:
            for 文件夹路径, 子文件夹名, 子文件名 in os.walk(文件夹):
                file_names = filter(lambda 子文件名: 子文件名.endswith(文件类型), 子文件名)
                file_names = map(lambda 子文件名: os.path.join(文件夹路径, 子文件名), file_names)
                for file in file_names:
                    try:
                        with open(file, mode='r', encoding='utf-8') as f: 文件内容 = f.read()
                    except:
                        with open(file, mode='r', encoding='gbk') as f: 文件内容 = f.read()
                    结果内容 = re.sub(r'\r?\n?_INFO=.*', '', 文件内容)
                    with open(file, mode='w', encoding='utf-8') as f: f.write(结果内容)

    def 生成一个皮肤(self, 皮肤名字):
        输出文件名, 皮肤源文件目录 = self.数据库连接.cursor().execute(
            f'select outputFileName, sourceFilePath from {常量.数据库皮肤表单名} where skinName = :皮肤名字;',
            {'皮肤名字': 皮肤名字}).fetchone()
        if self.输出格式 == 0:
            输出文件后缀名 = '.bds'
            压缩输入 = (self.临时skin目录 + '/*').replace('\\', '/')
        elif self.输出格式 == 1:
            输出文件后缀名 = '.bdi'
            self.发送到手机 = False
            压缩输入 = self.临时skin目录
        print('复制文件到临时 skin 目录')
        if os.path.exists(self.临时skin目录): shutil.rmtree(self.临时skin目录)
        shutil.copytree(皮肤源文件目录, self.临时skin目录)
        if self.图片压缩 == 1:
            print('开始无损压缩')
            optipng压缩图片(self.临时skin目录)
        elif self.图片压缩 == 2:
            print('开始有损压缩')
            pngquant压缩图片(self.临时skin目录)
        if self.是否清理注释:
            print('开始清理注释')
            self.清理注释(self.临时skin目录, '.ini')
        输出皮肤文件完整路径 = os.path.join(self.皮肤输出路径, 输出文件名 + 输出文件后缀名)
        压缩命令 = f'''winrar a -afzip -ibck -r -ep1 "{输出皮肤文件完整路径}" "{压缩输入}"'''
        if os.path.exists(输出皮肤文件完整路径) and os.path.isfile(输出皮肤文件完整路径):
            os.remove(输出皮肤文件完整路径)
        subprocess.run(压缩命令, startupinfo=常量.subprocessStartUpInfo)
        if self.发送到手机:
            皮肤文件名 = os.path.basename(输出皮肤文件完整路径)
            手机皮肤路径 = '/sdcard/baidu/ime/skins/' + 输出文件名 + 输出文件后缀名
            发送皮肤命令 = f'''adb push "{输出皮肤文件完整路径}" "{手机皮肤路径}"'''
            subprocess.run(发送皮肤命令, startupinfo=常量.subprocessStartUpInfo)
            安装皮肤命令 = f'''adb shell am start -a android.intent.action.VIEW -c android.intent.category.DEFAULT -n com.baidu.input/com.baidu.input.ImeUpdateActivity -d '{手机皮肤路径}' '''
            subprocess.run(安装皮肤命令, startupinfo=常量.subprocessStartUpInfo)

        # 输出文件完整路径
        pass
