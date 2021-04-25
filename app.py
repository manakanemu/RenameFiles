from Window import Window
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon
import os

"""
 安装命令：
 pyinstaller -F -w app.py --icon=icon.icns
 如果出现打不开的情况，删除-F，以多文件方式打包，然后用终端运行生成的文件夹中的app文件
 如果出现程序模糊，可以去看收藏的书签
"""


os.environ['QT_MAC_WANTS_LAYER'] = '1'
PYTHONUNBUFFERED=1;QT_MAC_WANTS_LAYER=1



app = QApplication([])
# app.setWindowIcon(QIcon('icon.png'))
main_window = Window()

main_window.show()
app.exec_()
