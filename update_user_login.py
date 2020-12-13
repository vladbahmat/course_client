# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_user_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1131, 601))
        self.frame.setStyleSheet("background-color:#d1d8e0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1131, 80))
        self.frame_2.setStyleSheet("background-color:#9980FA;\n"
"color:white;\n"
"text-align:center;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(390, 10, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#black;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(470, 590, 461, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgonline-com-ua-Transparent-backgr-48tgqomMjDUEwY.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(320, 80, 461, 181))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imgonline-com-ua-Transparent-backgr-48tgqomMjDUEwY.png"))
        self.label_3.setObjectName("label_3")
        self.submit_button = QtWidgets.QPushButton(self.frame)
        self.submit_button.setGeometry(QtCore.QRect(490, 540, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.submit_button.setObjectName("submit_button")
        self.clients_list = QtWidgets.QPlainTextEdit(self.frame)
        self.clients_list.setGeometry(QtCore.QRect(0, 230, 1121, 141))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clients_list.setFont(font)
        self.clients_list.setStyleSheet("background-color:#5758BB;\n"
"color:white;\n"
"border: 2px solid white;\n"
"")
        self.clients_list.setObjectName("clients_list")
        self.login_choose = QtWidgets.QLineEdit(self.frame)
        self.login_choose.setGeometry(QtCore.QRect(350, 380, 420, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.login_choose.setFont(font)
        self.login_choose.setStyleSheet("background-color:#5758BB;\n"
"color:white;\n"
"border: 2px solid white;\n"
"border-radius: 30px;")
        self.login_choose.setText("")
        self.login_choose.setAlignment(QtCore.Qt.AlignCenter)
        self.login_choose.setObjectName("login_choose")
        self.new_login = QtWidgets.QLineEdit(self.frame)
        self.new_login.setGeometry(QtCore.QRect(350, 450, 420, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.new_login.setFont(font)
        self.new_login.setStyleSheet("background-color:#5758BB;\n"
"color:white;\n"
"border: 2px solid white;\n"
"border-radius: 30px;")
        self.new_login.setText("")
        self.new_login.setAlignment(QtCore.Qt.AlignCenter)
        self.new_login.setObjectName("new_login")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dynamo-Bank"))
        self.submit_button.setText(_translate("MainWindow", "Изменить"))