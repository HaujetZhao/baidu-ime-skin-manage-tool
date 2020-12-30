rmdir /s /q .\dist\百度输入法皮肤管理工具

pyinstaller --hidden-import sqlite3  --noconfirm   -i "../src/misc/icon.ico" "../src/__init__.pyw"

::pyinstaller --hidden-import sqlite3 --hidden-import PySide2.QtSql   --noconfirm   -i "../src/misc/icon.ico" "../src/__init__.py"

echo d | xcopy /y /s .\dist\rely .\dist\__init__

ren .\dist\__init__\__init__.exe  百度输入法皮肤管理工具.exe

move .\dist\__init__ .\dist\百度输入法皮肤管理工具

del /F /Q 百度输入法皮肤管理工具_Win64_pyinstaller.7z

7z a -t7z 百度输入法皮肤管理工具_Win64_pyinstaller.7z .\dist\百度输入法皮肤管理工具 -mx=9 -ms=200m -mf -mhc -mhcf  -mmt -r

pause