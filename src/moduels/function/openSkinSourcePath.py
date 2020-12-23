# -*- coding: UTF-8 -*-

from moduels.component.NormalValue import 常量
import os

def openSkinSourcePath(列表):
    """
    打开皮肤源文件路径
    :param 模板名:
    :return:
    """
    if 列表.currentRow() < 0: return False
    皮肤名字 = 列表.currentItem().text()
    # print(皮肤名字)
    数据库连接 = 常量.数据库连接
    路径 = 数据库连接.cursor().execute(f'''select
                                        sourceFilePath
                                        from {常量.数据库皮肤表单名}
                                        where skinName = :skinName''',
                                {'skinName': 皮肤名字}).fetchone()[0]
    if not os.path.exists(路径):
        print(f'皮肤路径不存在：{路径}')
        return False
    os.startfile(路径)

