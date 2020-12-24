import os, sys, subprocess
from moduels.component.NormalValue import 常量

def pngquant压缩图片(文件夹):
    """
    遍历文件内所有 png 图片，一一压缩。
    在 Windows 上 pngquant 不支持中文路径，所以使用了 stdin 的方式对图片进行压缩
    它是有损压缩，会将 24bit 图片压缩成 8bit 的
    """
    for 文件夹路径, 子文件夹名, 子文件名 in os.walk(文件夹):
        file_names = filter(lambda 子文件名: 子文件名[-4:] == '.png', 子文件名)
        file_names = map(lambda 子文件名: os.path.join(文件夹路径, 子文件名), file_names)
        for file in file_names:
            print(f'正在 pngquant 压缩图片：{file}')
            文件内容 = open(file, 'rb').read()
            pngquant进程 = subprocess.Popen(f'pngquant - > "{file}"', stdin=subprocess.PIPE, shell=True, startupinfo=常量.subprocessStartUpInfo)
            pngquant进程.communicate(文件内容)

def optipng压缩图片(文件夹):
    """
    遍历文件内所有 png 图片，一一压缩。
    它是无损压缩
    """
    for 文件夹路径, 子文件夹名, 子文件名 in os.walk(文件夹):
        file_names = filter(lambda 子文件名: 子文件名[-4:] == '.png', 子文件名)
        file_names = map(lambda 子文件名: os.path.join(文件夹路径, 子文件名), file_names)
        for file in file_names:
            print(f'正在 optipng 压缩图片：{file}')
            subprocess.run(f'optipng -quiet "{file}"', startupinfo=常量.subprocessStartUpInfo)