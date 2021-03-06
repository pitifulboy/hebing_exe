# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combine_files_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 1200)
        mainWindow.setMinimumSize(QtCore.QSize(1200, 1200))
        mainWindow.setMaximumSize(QtCore.QSize(2400, 1200))
        mainWindow.setBaseSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TextEdit_filefolder_path = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextEdit_filefolder_path.sizePolicy().hasHeightForWidth())
        self.TextEdit_filefolder_path.setSizePolicy(sizePolicy)
        self.TextEdit_filefolder_path.setBaseSize(QtCore.QSize(300, 20))
        self.TextEdit_filefolder_path.setObjectName("TextEdit_filefolder_path")
        self.verticalLayout_4.addWidget(self.TextEdit_filefolder_path)
        self.TextEdit_savefolder_path = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit_savefolder_path.setBaseSize(QtCore.QSize(300, 0))
        self.TextEdit_savefolder_path.setObjectName("TextEdit_savefolder_path")
        self.verticalLayout_4.addWidget(self.TextEdit_savefolder_path)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_select_filefolder = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_select_filefolder.sizePolicy().hasHeightForWidth())
        self.btn_select_filefolder.setSizePolicy(sizePolicy)
        self.btn_select_filefolder.setBaseSize(QtCore.QSize(100, 0))
        self.btn_select_filefolder.setObjectName("btn_select_filefolder")
        self.verticalLayout_3.addWidget(self.btn_select_filefolder)
        self.btn_select_savefolder = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_select_savefolder.sizePolicy().hasHeightForWidth())
        self.btn_select_savefolder.setSizePolicy(sizePolicy)
        self.btn_select_savefolder.setObjectName("btn_select_savefolder")
        self.verticalLayout_3.addWidget(self.btn_select_savefolder)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(20, 0))
        self.label.setBaseSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setBaseSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_top_drop_num = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_top_drop_num.sizePolicy().hasHeightForWidth())
        self.textEdit_top_drop_num.setSizePolicy(sizePolicy)
        self.textEdit_top_drop_num.setMinimumSize(QtCore.QSize(20, 20))
        self.textEdit_top_drop_num.setBaseSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_top_drop_num.setFont(font)
        self.textEdit_top_drop_num.setObjectName("textEdit_top_drop_num")
        self.verticalLayout_2.addWidget(self.textEdit_top_drop_num)
        self.textEdit_buttom_drop_num = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_buttom_drop_num.setMinimumSize(QtCore.QSize(20, 20))
        self.textEdit_buttom_drop_num.setBaseSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_buttom_drop_num.setFont(font)
        self.textEdit_buttom_drop_num.setObjectName("textEdit_buttom_drop_num")
        self.verticalLayout_2.addWidget(self.textEdit_buttom_drop_num)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.Btn_combine = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_combine.sizePolicy().hasHeightForWidth())
        self.Btn_combine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Btn_combine.setFont(font)
        self.Btn_combine.setObjectName("Btn_combine")
        self.horizontalLayout.addWidget(self.Btn_combine)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.textBrowser_msg = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_msg.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser_msg.setObjectName("textBrowser_msg")
        self.verticalLayout_5.addWidget(self.textBrowser_msg)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setRowMinimumHeight(2, 5)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 5)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.btn_select_filefolder.clicked.connect(mainWindow.select_filefolderpath_click) # type: ignore
        self.Btn_combine.clicked.connect(mainWindow.combine_click) # type: ignore
        self.btn_select_savefolder.clicked.connect(mainWindow.select_savepath_click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "?????????????????? V1.1"))
        self.btn_select_filefolder.setText(_translate("mainWindow", "????????????????????????"))
        self.btn_select_savefolder.setText(_translate("mainWindow", "?????????????????????"))
        self.label.setText(_translate("mainWindow", "???????????????"))
        self.label_2.setText(_translate("mainWindow", "???????????????????????????"))
        self.textEdit_top_drop_num.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.textEdit_buttom_drop_num.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.Btn_combine.setText(_translate("mainWindow", "????????????"))
        self.label_3.setText(_translate("mainWindow", "????????????"))
        self.label_4.setText(_translate("mainWindow", "powered  by  ?????????  13027923626"))
