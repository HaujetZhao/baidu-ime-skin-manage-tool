# -*- coding: UTF-8 -*-

from moduels.component.NormalValue import 常量

def createDB():

    conn = 常量.数据库连接
    偏好设置表单名 = 常量.数据库偏好设置表单名
    模板表单名 = 常量.数据库模板表单名
    皮肤表单名 = 常量.数据库皮肤表单名
    cursor = conn.cursor()

    result = cursor.execute(f'select * from sqlite_master where name = "{偏好设置表单名}";')
    if result.fetchone() == None:
        cursor.execute(f'''create table {偏好设置表单名} (
                                            id integer primary key autoincrement,
                                            item text,
                                            value text
                                            )''')
    else:
        print('偏好设置表单已存在')

    result = cursor.execute(f'select * from sqlite_master where name = "{模板表单名}";')
    if result.fetchone() == None:
        cursor.execute(f'''create table {模板表单名} (
                                    id integer primary key autoincrement,
                                    templateName text,
                                    userName text,
                                    contact text,
                                    notes text, 
                                    拼音9键 integer,
                                    拼音26键 integer,
                                    五笔26键 integer,
                                    英文26键 integer,
                                    笔画 integer,
                                    音效 text, 
                                    图片压缩 integer, 
                                    输出格式 integer, 
                                    adb发送至手机 integer, 
                                    清理注释 integer
                                    )''')
    else:
        print('模板表单已存在')

    result = cursor.execute(f'select * from sqlite_master where name = "{皮肤表单名}";')
    if result.fetchone() == None:
        cursor.execute(f'''create table {皮肤表单名} (
                                    id integer primary key autoincrement,
                                    skinName text,
                                    outputFileName text,
                                    sourceFilePath text,
                                    supportDarkMode BOOLEAN)''')
    else:
        print('皮肤表单已存在')

    conn.commit() # 最后要提交更改
