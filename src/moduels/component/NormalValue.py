import sqlite3
import platform
import subprocess


class NormalValue():
    样式文件 = 'misc/style.css'
    软件版本 = '0.0.1'

    主窗口 = None
    托盘 = None
    状态栏 = None

    数据库路径 = 'misc/database.db'
    数据库连接 = sqlite3.connect(数据库路径)

    数据库偏好设置表单名 = 'Preferences'
    数据库模板表单名 = 'Templates'
    数据库皮肤表单名 = 'Skins'

    关闭时隐藏到托盘 = False

    皮肤输出路径 = ''
    音效文件路径 = ''
    皮肤选项 = {'拼音9键': 1,
            '拼音26键': 1,
            '五笔26键': 1,
            '英文26键': 1,
            '笔画': 1,
            '音效':''
            }
    输出选项 = {'图片压缩': 0,  # 0 不压缩, 1 无损压缩, 2 有损压缩
            '输出格式': 0,     # 0 安卓, 1 苹果
            'adb发送至手机': True,
            '清理注释': True
            }

    系统平台 = platform.system()

    图标路径 = 'misc/icon.icns' if 系统平台 == 'Darwin' else 'misc/icon.ico'

    if 系统平台 == 'Windows':
        subprocessStartUpInfo = subprocess.STARTUPINFO()
        subprocessStartUpInfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
        subprocessStartUpInfo.wShowWindow = subprocess.SW_HIDE
    else:
        pass

class ThreadValue():
    线程状态_无线adb = 0

常量 = NormalValue()
线程值 = ThreadValue()