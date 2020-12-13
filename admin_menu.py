# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 600)
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
        self.client_list_button = QtWidgets.QPushButton(self.frame)
        self.client_list_button.setGeometry(QtCore.QRect(20, 380, 210, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.client_list_button.setFont(font)
        self.client_list_button.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.client_list_button.setObjectName("client_list_button")
        self.edit_login_button = QtWidgets.QPushButton(self.frame)
        self.edit_login_button.setGeometry(QtCore.QRect(460, 380, 210, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_login_button.setFont(font)
        self.edit_login_button.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.edit_login_button.setObjectName("edit_login_button")
        self.add_credit = QtWidgets.QPushButton(self.frame)
        self.add_credit.setGeometry(QtCore.QRect(680, 380, 210, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_credit.setFont(font)
        self.add_credit.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.add_credit.setObjectName("add_credit")
        self.exit_admin_button = QtWidgets.QPushButton(self.frame)
        self.exit_admin_button.setGeometry(QtCore.QRect(900, 380, 210, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_admin_button.setFont(font)
        self.exit_admin_button.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.exit_admin_button.setObjectName("exit_admin_button")
        self.add_bond_button = QtWidgets.QPushButton(self.frame)
        self.add_bond_button.setGeometry(QtCore.QRect(240, 380, 210, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_bond_button.setFont(font)
        self.add_bond_button.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.add_bond_button.setObjectName("add_bond_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dynamo-Bank"))
        self.client_list_button.setText(_translate("MainWindow", "Список клиентов"))
        self.edit_login_button.setText(_translate("MainWindow", "Изменить логин клиента"))
        self.add_credit.setText(_translate("MainWindow", "Добавить тариф кредита"))
        self.exit_admin_button.setText(_translate("MainWindow", "Выйти из аккаунта"))
        self.add_bond_button.setText(_translate("MainWindow", "Добавить акцию"))
