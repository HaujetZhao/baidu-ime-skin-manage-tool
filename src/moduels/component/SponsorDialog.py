# -*- coding: UTF-8 -*-

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from moduels.component.NormalValue import 常量


# 打赏对话框
class SponsorDialog(QDialog):
    def __init__(self, parent=None):
        super(SponsorDialog, self).__init__(parent)
        self.resize(500, 567)
        图标路径 = 'misc/icon.icns' if 常量.系统平台 == 'Darwin' else 'misc/icon.ico'
        self.setWindowIcon(QIcon(图标路径))
        self.setWindowTitle(self.tr('打赏作者'))
        self.exec()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap('misc/sponsor.jpg')
        painter.drawPixmap(self.rect(), pixmap)