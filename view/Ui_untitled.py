# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jun/Documents/UWB_and_CAD/view/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 832)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.formGroupBox.setGeometry(QtCore.QRect(20, 10, 221, 201))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.open_serial_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_serial_button.setObjectName("open_serial_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.open_serial_button)
        self.close_serial_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_serial_button.setObjectName("close_serial_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.close_serial_button)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 220, 861, 571))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 10, 271, 201))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 61, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 160, 21, 20))
        self.label_6.setObjectName("label_6")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 30, 61, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_4.setGeometry(QtCore.QRect(90, 70, 61, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_5.setGeometry(QtCore.QRect(90, 110, 61, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_6.setGeometry(QtCore.QRect(90, 150, 61, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_7.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(160, 30, 21, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(160, 80, 61, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(160, 120, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(160, 160, 91, 20))
        self.label_10.setObjectName("label_10")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(570, 10, 221, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 31, 20))
        self.label_11.setObjectName("label_11")
        self.textEdit_8 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_8.setGeometry(QtCore.QRect(40, 30, 61, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(120, 40, 31, 20))
        self.label_12.setObjectName("label_12")
        self.textEdit_9 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_9.setGeometry(QtCore.QRect(150, 30, 61, 31))
        self.textEdit_9.setObjectName("textEdit_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(870, 220, 341, 561))
        self.groupBox_3.setObjectName("groupBox_3")
        self.anchorTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.anchorTable.setGeometry(QtCore.QRect(20, 30, 291, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anchorTable.sizePolicy().hasHeightForWidth())
        self.anchorTable.setSizePolicy(sizePolicy)
        self.anchorTable.setMinimumSize(QtCore.QSize(0, 112))
        self.anchorTable.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.anchorTable.setFont(font)
        self.anchorTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.anchorTable.setAlternatingRowColors(True)
        self.anchorTable.setRowCount(5)
        self.anchorTable.setColumnCount(4)
        self.anchorTable.setObjectName("anchorTable")
        self.anchorTable.horizontalHeader().setDefaultSectionSize(72)
        self.anchorTable.horizontalHeader().setMinimumSectionSize(70)
        self.anchorTable.horizontalHeader().setStretchLastSection(False)
        self.anchorTable.verticalHeader().setVisible(False)
        self.anchorTable.verticalHeader().setDefaultSectionSize(27)
        self.anchorTable.verticalHeader().setHighlightSections(True)
        self.anchorTable.verticalHeader().setMinimumSectionSize(20)
        self.vertexTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.vertexTable.setGeometry(QtCore.QRect(20, 230, 291, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertexTable.sizePolicy().hasHeightForWidth())
        self.vertexTable.setSizePolicy(sizePolicy)
        self.vertexTable.setMinimumSize(QtCore.QSize(0, 112))
        self.vertexTable.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vertexTable.setFont(font)
        self.vertexTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.vertexTable.setAlternatingRowColors(True)
        self.vertexTable.setRowCount(11)
        self.vertexTable.setColumnCount(4)
        self.vertexTable.setObjectName("vertexTable")
        self.vertexTable.horizontalHeader().setDefaultSectionSize(72)
        self.vertexTable.horizontalHeader().setMinimumSectionSize(70)
        self.vertexTable.horizontalHeader().setStretchLastSection(False)
        self.vertexTable.verticalHeader().setVisible(False)
        self.vertexTable.verticalHeader().setDefaultSectionSize(27)
        self.vertexTable.verticalHeader().setHighlightSections(True)
        self.vertexTable.verticalHeader().setMinimumSectionSize(20)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(570, 100, 221, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 30, 81, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 61, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 171, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.textEdit_2.raise_()
        self.label_2.raise_()
        self.groupBox_3.raise_()
        self.horizontalLayoutWidget.raise_()
        self.graphicsView.raise_()
        self.horizontalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.formGroupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.s1__lb_1.setText(_translate("MainWindow", "串口检测："))
        self.s1__box_1.setText(_translate("MainWindow", "检测串口"))
        self.s1__lb_2.setText(_translate("MainWindow", "串口选择："))
        self.open_serial_button.setText(_translate("MainWindow", "打开串口"))
        self.close_serial_button.setText(_translate("MainWindow", "关闭串口"))
        self.groupBox.setTitle(_translate("MainWindow", "dpi设置"))
        self.label_3.setText(_translate("MainWindow", "电脑分辨率："))
        self.label_4.setText(_translate("MainWindow", "电脑尺寸:"))
        self.label_5.setText(_translate("MainWindow", " =   dpi："))
        self.label_6.setText(_translate("MainWindow", "="))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1920</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">15.6</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">141.22</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">0.1799</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1080</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "X"))
        self.label_8.setText(_translate("MainWindow", "英寸"))
        self.label_9.setText(_translate("MainWindow", "PPI"))
        self.label_10.setText(_translate("MainWindow", "mm dot pitch"))
        self.groupBox_2.setTitle(_translate("MainWindow", "砖块设置 (单位 / mm)"))
        self.label_11.setText(_translate("MainWindow", "长："))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "宽："))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "坐标点设置"))
        self.groupBox_4.setTitle(_translate("MainWindow", "其他设置"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "房间个数："))
        self.label.setText(_translate("MainWindow", "  图纸比例   1："))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">50</span></p></body></html>"))


