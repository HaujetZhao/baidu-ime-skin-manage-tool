# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from moduels.component.NormalValue import 常量
from moduels.component.NormalValue import 线程值

import subprocess
import os
import shutil



class Thread_ExtractAllSkin(QThread):
    状态栏消息 = Signal(str, int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.正在运行 = 0
        QApplication.instance().aboutToQuit.connect(self.要退出了)

    def 要退出了(self):
        self.terminate()

    def run(self):
        if self.正在运行 == 1: return False
        self.正在运行 = 1
        self.状态栏消息.emit('正在提取', 2000)
        提取皮肤命令 = f'adb pull /sdcard/baidu/ime/skins "{常量.皮肤输出路径}"'
        print(f'提取命令：{提取皮肤命令}')
        subprocess.run(提取皮肤命令, startupinfo=常量.subprocessStartUpInfo)
        提取出的皮肤所在目录 = os.path.join(常量.皮肤输出路径, 'skins')
        if not os.path.exists(提取出的皮肤所在目录):
            self.状态栏消息.emit('提取失败，控制台可查看详情', 3000)
            self.正在运行 = 0
            return
        with os.scandir(提取出的皮肤所在目录) as 目录条目:
            for entry in 目录条目:
                if entry.name.endswith('.bds') and entry.is_file():
                    bds路径 = entry.path
                    txt路径 = os.path.splitext(bds路径)[0] + '.txt'
                    if os.path.exists(txt路径):
                        with open(txt路径, encoding='utf-8') as f:
                            txt文件第一行 = f.readline().strip('\n')
                            if txt文件第一行 != '':
                                目标文件名 = os.path.join(os.path.dirname(bds路径), txt文件第一行 + '.bds')
                                os.replace(bds路径, 目标文件名)
                elif entry.name.endswith('.bda') and entry.is_file():
                    bda路径 = entry.path
                    txt路径 = os.path.splitext(bda路径)[0] + '.txt'
                    if os.path.exists(txt路径):
                        with open(txt路径, encoding='utf-8') as f:
                            txt文件第一行 = f.readline().strip('\n')
                            if txt文件第一行 != '':
                                目标文件名 = os.path.join(os.path.dirname(bda路径), txt文件第一行 + '.bda')
                                os.replace(bda路径, 目标文件名)
        with os.scandir(提取出的皮肤所在目录) as 目录条目:
            for entry in 目录条目:
                if not entry.name.endswith('.bds') and not entry.name.endswith('.bda') and entry.is_file():
                    os.remove(entry.path)
        if os.path.exists(os.path.join(常量.皮肤输出路径, '提取自手机的皮肤')): shutil.rmtree(os.path.join(常量.皮肤输出路径, '提取自手机的皮肤'))
        shutil.move(提取出的皮肤所在目录, os.path.join(常量.皮肤输出路径, '提取自手机的皮肤'))
        # except:pass
        self.状态栏消息.emit('提取结束，控制台可查看详情，点击“打开输出文件夹”按钮查看所提取文件', 5000)
        self.正在运行 = 0