# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RenameUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RenameWidget(object):
    def setupUi(self, RenameWidget):
        if not RenameWidget.objectName():
            RenameWidget.setObjectName(u"RenameWidget")
        RenameWidget.resize(813, 612)
        self.verticalLayout_3 = QVBoxLayout(RenameWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.edit_path = QLineEdit(RenameWidget)
        self.edit_path.setObjectName(u"edit_path")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_path.sizePolicy().hasHeightForWidth())
        self.edit_path.setSizePolicy(sizePolicy)
        self.edit_path.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.edit_path)

        self.button_select_path = QPushButton(RenameWidget)
        self.button_select_path.setObjectName(u"button_select_path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_select_path.sizePolicy().hasHeightForWidth())
        self.button_select_path.setSizePolicy(sizePolicy1)
        self.button_select_path.setFocusPolicy(Qt.NoFocus)
        self.button_select_path.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.button_select_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.edit_filter = QLineEdit(RenameWidget)
        self.edit_filter.setObjectName(u"edit_filter")

        self.horizontalLayout_4.addWidget(self.edit_filter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.edit_match_pattern = QLineEdit(RenameWidget)
        self.edit_match_pattern.setObjectName(u"edit_match_pattern")
        sizePolicy.setHeightForWidth(self.edit_match_pattern.sizePolicy().hasHeightForWidth())
        self.edit_match_pattern.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.edit_match_pattern)

        self.edit_start = QLineEdit(RenameWidget)
        self.edit_start.setObjectName(u"edit_start")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit_start.sizePolicy().hasHeightForWidth())
        self.edit_start.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.edit_start)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.edit_match_result = QLineEdit(RenameWidget)
        self.edit_match_result.setObjectName(u"edit_match_result")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.edit_match_result.sizePolicy().hasHeightForWidth())
        self.edit_match_result.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.edit_match_result)

        self.button_change_name = QPushButton(RenameWidget)
        self.button_change_name.setObjectName(u"button_change_name")
        sizePolicy1.setHeightForWidth(self.button_change_name.sizePolicy().hasHeightForWidth())
        self.button_change_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.button_change_name)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listview_filted = QListWidget(RenameWidget)
        self.listview_filted.setObjectName(u"listview_filted")

        self.horizontalLayout.addWidget(self.listview_filted)

        self.line = QFrame(RenameWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.listview_changed = QListWidget(RenameWidget)
        self.listview_changed.setObjectName(u"listview_changed")

        self.horizontalLayout.addWidget(self.listview_changed)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(RenameWidget)

        QMetaObject.connectSlotsByName(RenameWidget)
    # setupUi

    def retranslateUi(self, RenameWidget):
        RenameWidget.setWindowTitle(QCoreApplication.translate("RenameWidget", u"批量重命名", None))
        self.button_select_path.setText(QCoreApplication.translate("RenameWidget", u"\u6253\u5f00", None))
        self.edit_filter.setPlaceholderText(QCoreApplication.translate("RenameWidget", u"\u8bf7\u8f93\u5165\u6587\u4ef6\u8fc7\u6ee4\u6761\u4ef6(\u6b63\u5219\u8868\u8fbe\u5f0f)", None))
        self.edit_match_pattern.setPlaceholderText(QCoreApplication.translate("RenameWidget", u"\u6a21\u5f0f\u5339\u914d\u5668\uff0c\u7528\":\"\u5206\u5272\u591a\u4e2a\u5339\u914d\u5668", None))
        self.edit_start.setPlaceholderText(QCoreApplication.translate("RenameWidget", u"\u8ba1\u6570\u5668", None))
        self.edit_match_result.setPlaceholderText(QCoreApplication.translate("RenameWidget", u"\u8f93\u5165\u6587\u4ef6\u540d\uff0c{}\u5f15\u7528\u5339\u914d\u5668\uff0c$count\u5f15\u7528\u8ba1\u6570\u5668", None))
        self.button_change_name.setText(QCoreApplication.translate("RenameWidget", u"\u6539\u540d", None))
    # retranslateUi

