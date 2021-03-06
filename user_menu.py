# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_menu.ui'
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
        self.exit_user = QtWidgets.QPushButton(self.frame)
        self.exit_user.setGeometry(QtCore.QRect(850, 410, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_user.setFont(font)
        self.exit_user.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.exit_user.setObjectName("exit_user")
        self.take_credit = QtWidgets.QPushButton(self.frame)
        self.take_credit.setGeometry(QtCore.QRect(50, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.take_credit.setFont(font)
        self.take_credit.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.take_credit.setObjectName("take_credit")
        self.survey = QtWidgets.QPushButton(self.frame)
        self.survey.setGeometry(QtCore.QRect(250, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.survey.setFont(font)
        self.survey.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.survey.setObjectName("survey")
        self.make_card = QtWidgets.QPushButton(self.frame)
        self.make_card.setGeometry(QtCore.QRect(450, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.make_card.setFont(font)
        self.make_card.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.make_card.setObjectName("make_card")
        self.open_account = QtWidgets.QPushButton(self.frame)
        self.open_account.setGeometry(QtCore.QRect(650, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.open_account.setFont(font)
        self.open_account.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.open_account.setObjectName("open_account")
        self.buy_bond = QtWidgets.QPushButton(self.frame)
        self.buy_bond.setGeometry(QtCore.QRect(850, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buy_bond.setFont(font)
        self.buy_bond.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.buy_bond.setObjectName("buy_bond")
        self.show_accounts = QtWidgets.QPushButton(self.frame)
        self.show_accounts.setGeometry(QtCore.QRect(50, 410, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.show_accounts.setFont(font)
        self.show_accounts.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.show_accounts.setObjectName("show_accounts")
        self.delete_account = QtWidgets.QPushButton(self.frame)
        self.delete_account.setGeometry(QtCore.QRect(250, 410, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_account.setFont(font)
        self.delete_account.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.delete_account.setObjectName("delete_account")
        self.fund_acoount = QtWidgets.QPushButton(self.frame)
        self.fund_acoount.setGeometry(QtCore.QRect(450, 410, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fund_acoount.setFont(font)
        self.fund_acoount.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.fund_acoount.setObjectName("fund_acoount")
        self.show_bonds = QtWidgets.QPushButton(self.frame)
        self.show_bonds.setGeometry(QtCore.QRect(650, 410, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.show_bonds.setFont(font)
        self.show_bonds.setStyleSheet("QPushButton{background-color:#5758BB;\n"
"color:white;\n"
"border-radius: 10px;}\n"
"QPushButton:pressed{\n"
"background-color:darkgreen;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.show_bonds.setObjectName("show_bonds")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dynamo-Bank"))
        self.exit_user.setText(_translate("MainWindow", "Выйти"))
        self.take_credit.setText(_translate("MainWindow", "Взять кредит"))
        self.survey.setText(_translate("MainWindow", "Соц. опрос"))
        self.make_card.setText(_translate("MainWindow", "Карточка"))
        self.open_account.setText(_translate("MainWindow", "Открыть счет"))
        self.buy_bond.setText(_translate("MainWindow", "Купить акцию"))
        self.show_accounts.setText(_translate("MainWindow", "Ваши счета"))
        self.delete_account.setText(_translate("MainWindow", "Удалить счет"))
        self.fund_acoount.setText(_translate("MainWindow", "Поиск счета"))
        self.show_bonds.setText(_translate("MainWindow", "Ваши акции"))
