rmdir /s /q .\dist\�ٶ����뷨Ƥ��������

pyinstaller --hidden-import sqlite3  --noconfirm   -i "../src/misc/icon.ico" "../src/__init__.pyw"

::pyinstaller --hidden-import sqlite3 --hidden-import PySide2.QtSql   --noconfirm   -i "../src/misc/icon.ico" "../src/__init__.py"

echo d | xcopy /y /s .\dist\rely .\dist\__init__

ren .\dist\__init__\__init__.exe  �ٶ����뷨Ƥ��������.exe

move .\dist\__init__ .\dist\�ٶ����뷨Ƥ��������

del /F /Q �ٶ����뷨Ƥ��������_Win64_pyinstaller.7z

7z a -t7z �ٶ����뷨Ƥ��������_Win64_pyinstaller.7z .\dist\�ٶ����뷨Ƥ�������� -mx=9 -ms=200m -mf -mhc -mhcf  -mmt -r

pause