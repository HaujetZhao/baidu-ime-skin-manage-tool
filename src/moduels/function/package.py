import os
import zipfile

def zip(输入, 输出):
    '''
    只接受 folder/to/zip 和 folder/to/zip/ 两种形式
    前者压缩 zip 文件夹，后者压缩 zip 文件夹内的文件（不带 zip 前缀）
    '''
    if not os.path.exists(输入): return
    if os.path.isfile(输入):
        with zipfile.ZipFile(输出, 'w') as package:
            package.write(输入, arcname=os.path.basename())
    else:
        除去的部分 = 输入
        if os.path.basename(输入) != '':
            除去的部分 = 输入[0:len(os.path.dirname(输入)) + 1]
        else:
            除去的部分 = 输入
        with zipfile.ZipFile(输出, 'w') as package:
            for root, dirs, files in os.walk(输入):
                for file in files:
                    文件名 = os.path.join(root, file)
                    包内文件名 = os.path.join(root, file).replace(除去的部分, '', 1)
                    package.write(文件名, arcname=包内文件名, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

def unzip(输入, 输出):
    with zipfile.ZipFile(输入, 'r') as package:
        package.extractall(path=输出)
