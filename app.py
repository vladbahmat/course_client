import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import bond_add,show_user_list,main_menu,admin_login,admin_menu,register,show_user_list
import update_user_login,user_login,user_menu,show_accounts_list,delete_account,add_account
import show_bonds_list,buy_bond,survey,card,credit_add,buy_credit,manager,show_survey_list
import find
from server import Client
#from functions import *
import socket
import time

client=Client()
client.create_connection_client()

def int_control(n):
    while True:
        try:
            n=int(n)
            if type(n)!=int:
                raise ValueError
            elif n>1000000000:
                raise Exception
            else:
                return True
        except ValueError:
            print('Enter a NUMBER')
            return False
        except Exception:
            print("Number can't be more than 1000000000")
            return False

class Find(QtWidgets.QMainWindow,find.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.find_button.clicked.connect(self.find_def)

    def find_def(self):
        check = self.find_input.text()
        client.sending(check+"\n")
        self.close()
        client.sending("19\n")
        time.sleep(0.1)
        self.accs_list=Show_accounts()
        self.accs_list.show()
        client.sending("h\n")

class Show_survey(QtWidgets.QMainWindow,show_survey_list.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in range(100):
            buf=client.recover()
            buf.replace("\r",'')
            if buf.find("nd"):
                break
        self.survey_list.appendPlainText(buf[:-5])
        self.exit_from_survey_list.clicked.connect(lambda:self.close())

class Manager(QtWidgets.QMainWindow,manager.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_survey_button.clicked.connect(self.show_surveys)
        self.print_info.clicked.connect(self.otchet)
        self.exit_bank_button.clicked.connect(lambda:self.close())

    def otchet(self):
        client.sending("20\n")
        time.sleep(0.1)

    def show_surveys(self):
        client.sending("18\n")
        time.sleep(0.1)
        self.buy=Show_survey()
        self.buy.show()

class Buy_credit(QtWidgets.QMainWindow,buy_credit.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.credit_button.clicked.connect(self.button_credit)
        for i in range(100):
            buf=client.recover()
            if buf.find("nd"):
                break
        buf=buf[:-6]
        checklist=buf.split('&')
        print(checklist)
        for elem in checklist:
            self.take_credit.addItem(elem)

    def button_credit(self):
        to_buy=self.take_credit.currentText()
        to_buy=to_buy[(to_buy.rfind(',')+2):]
        client.sending(to_buy+"\n")
        print(to_buy)
        self.close()

class Add_credit(QtWidgets.QMainWindow,credit_add.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_credit.clicked.connect(self.add_def)

    def add_def(self):
        money = self.credit_money_input.text()
        name = self.credit_degree_input.text()
        client.sending(money+"\n")
        client.sending(name+"\n")
        self.close()

class Card(QtWidgets.QMainWindow,card.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_card.clicked.connect(lambda:self.close())
        for i in range(100):
            buf=client.recover()
            if buf.find("nd"):
                break
        self.balance.setText(buf[:-5])


class Survet(QtWidgets.QMainWindow,survey.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.send_button.clicked.connect(self.survey_results)

    def survey_results(self):
        choose_list=[]
        choose_list.append(self.byn_rub.currentText())
        choose_list.append(self.byn_usd.currentText())
        choose_list.append(self.byn_eur.currentText())
        choose_list.append(self.eur_usd.currentText())
        choose_list.append(self.rub_eur.currentText())
        choose_list.append(self.rub_usd.currentText())
        client.sending(str(choose_list.count("BYN"))+"\n")
        time.sleep(0.1)
        client.sending(str(choose_list.count("USD"))+"\n")
        time.sleep(0.1)
        client.sending(str(choose_list.count("EUR"))+"\n")
        time.sleep(0.1)
        client.sending(str(choose_list.count("RUB"))+"\n")
        self.close()

class Buy_bond(QtWidgets.QMainWindow,buy_bond.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in range(100):
            buf=client.recover()
            if buf.find("nd"):
                break
        buf=buf[:-6]
        checklist=buf.split('&')
        print(checklist)
        for elem in checklist:
            self.buy_bond.addItem(elem)
        self.bond_button.clicked.connect(self.buy_bnds)

    def buy_bnds(self):
        to_buy=self.buy_bond.currentText()
        to_buy=to_buy[(to_buy.rfind(',')+2):]
        client.sending(to_buy+"\n")
        print(to_buy)
        self.close()

class Show_bonds_list(QtWidgets.QMainWindow,show_bonds_list.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_from_bonds_list.clicked.connect(lambda:self.close())
        for i in range(100):
            buf=client.recover()
            buf.replace("\r",'')
            if buf.find("nd"):
                break
        self.bond_list.appendPlainText(buf[:-5])

class Add_account(QtWidgets.QMainWindow,add_account.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_add.clicked.connect(self.add_account)

    def add_account(self):
        money = self.money_input.text()
        name = self.account_name_input.text()
        client.sending(money+"\n")
        client.sending(name+"\n")
        self.close()

class Delete_account(QtWidgets.QMainWindow,delete_account.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in range(100):
            buf=client.recover()
            buf.replace("\r",'')
            if buf.find("nd"):
                break
        buf=buf[:-6]
        checklist=buf.split('&')
        print(checklist)
        for elem in checklist:
            self.account_delete.addItem(elem)
        self.delete_button.clicked.connect(self.delete_submit)
        #self.account_list.appendPlainText(buf[:-5])

    def delete_submit(self):
        to_buy=self.account_delete.currentText()
        to_buy=to_buy[(to_buy.rfind(',')+2):]
        client.sending(to_buy+"\n")
        print(to_buy)
        self.close()

class Show_accounts(QtWidgets.QMainWindow,show_accounts_list.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_from_accounts_list.clicked.connect(lambda:self.close())
        for i in range(100):
            buf=client.recover()
            buf.replace("\r",'')
            if buf.find("nd"):
                break
        self.account_list.appendPlainText(buf[:-5])

class User_menu(QtWidgets.QMainWindow,user_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_user.clicked.connect(self.user_close)
        self.show_accounts.clicked.connect(self.show_accs)
        self.delete_account.clicked.connect(self.delete_acc)
        self.open_account.clicked.connect(self.open_acc)
        self.show_bonds.clicked.connect(self.bonds_list)
        self.buy_bond.clicked.connect(self.buy_bnd)
        self.survey.clicked.connect(self.survey_def)
        self.make_card.clicked.connect(self.card)
        self.take_credit.clicked.connect(self.credit)
        self.fund_acoount.clicked.connect(self.poisk)

    def poisk(self):
        client.sending("19\n")
        time.sleep(0.1)
        self.buy=Find()
        self.buy.show()

    def credit(self):
        client.sending("17\n")
        time.sleep(0.1)
        self.buy=Buy_credit()
        self.buy.show()

    def card(self):
        client.sending("15\n")
        time.sleep(0.1)
        self.buy=Card()
        self.buy.show()

    def survey_def(self):
        client.sending("14\n")
        time.sleep(0.1)
        self.buy=Survet()
        self.buy.show()

    def buy_bnd(self):
        client.sending("13\n")
        time.sleep(0.1)
        self.buy=Buy_bond()
        self.buy.show()

    def bonds_list(self):
        client.sending("12\n")
        time.sleep(0.1)
        self.show_list=Show_bonds_list()
        self.show_list.show()

    def open_acc(self):
        client.sending("11\n")
        self.add_acc=Add_account()
        self.add_acc.show()

    def delete_acc(self):
        client.sending("10\n")
        time.sleep(0.1)
        self.delete_list=Delete_account()
        self.delete_list.show()


    def user_close(self):
        self.close()

    def show_accs(self):
        client.sending("9\n")
        time.sleep(0.1)
        self.accs_list=Show_accounts()
        self.accs_list.show()

class Update_user_login(QtWidgets.QMainWindow,update_user_login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(self.submit_update)
        for i in range(100):
            buf=client.recover()
            if buf.find("nd"):
                break
        self.clients_list.appendPlainText(buf[:-5])

    def submit_update(self):
        time.sleep(0.5)
        login=self.login_choose.text()
        new_login=self.new_login.text()
        client.sending(login+"\n")
        time.sleep(0.5)
        client.sending(new_login+"\n")
        self.close()

class Bond_add(QtWidgets.QMainWindow,bond_add.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_bond_button.clicked.connect(self.add_bond)
        self.bond_cost_input.setPlaceholderText("Цена акции")
        self.bond_long_input.setPlaceholderText("Срок действия")

    def add_bond(self):
        money = self.bond_cost_input.text()
        name = self.bond_long_input.text()
        client.sending(money+"\n")
        client.sending(name+"\n")
        self.close()


class Clients_list(QtWidgets.QMainWindow,show_user_list.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_from_clients_list.clicked.connect(self.exit_clients_list)
        for i in range(100):
            buf=client.recover()
            if buf.find("nd"):
                break
        self.clients_list.appendPlainText(buf[:-5])

    def exit_clients_list(self):
        self.close()

class Admin_menu(QtWidgets.QMainWindow,admin_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_admin_button.clicked.connect(self.admin_exit)
        self.client_list_button.clicked.connect(self.show_clients_list)
        self.add_bond_button.clicked.connect(self.add_bond)
        self.edit_login_button.clicked.connect(self.edit_login)
        self.add_credit.clicked.connect(self.add_def)

    def add_def(self):
        client.sending("16\n")
        time.sleep(0.1)
        self.open_window=Add_credit()
        self.open_window.show()

    def edit_login(self):
        client.sending("6\n")
        time.sleep(0.1)
        self.edit_login_window=Update_user_login()
        self.edit_login_window.show()

    def admin_exit(self):
        self.close()

    def show_clients_list(self):
        client.sending("4\n")
        time.sleep(0.1)
        self.clients_list=Clients_list()
        self.clients_list.show()

    def add_bond(self):
        client.sending("5\n")
        time.sleep(0.1)
        self.bond_add=Bond_add()
        self.bond_add.show()


class Admin_login(QtWidgets.QMainWindow,admin_login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.admin_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_login_input.setPlaceholderText("Введите логин")
        self.admin_password_input.setPlaceholderText("Введите пароль")
        self.enter_amin_button.clicked.connect(self.admin_auth)

    def admin_auth(self):
        admin_lgn = self.admin_login_input.text()
        admin_pswrd = self.admin_password_input.text()
        client.sending(admin_lgn+"\n")
        client.sending(admin_pswrd+"\n")
        check=client.recover()
        #check=from_str_to_bool(check)
        #print(check)
        if check.find("rue")!=-1:
            self.adm_menu_window=Admin_menu()
            self.adm_menu_window.show()
            self.close()
        else:
            self.close()

class Register(QtWidgets.QMainWindow,register.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_new_user_button.clicked.connect(self.register)

    def register(self):
        new_lgn = self.new_user_login.text()
        new_pswrd = self.new_user_password.text()
        client.sending(new_lgn+"\n")
        client.sending(new_pswrd+"\n")
        self.close()


class User_login(QtWidgets.QMainWindow,user_login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter_user_button.clicked.connect(self.user_auth)

    def user_auth(self):
        user_lgn = self.user_login_input.text()
        user_pswrd = self.user_password_input.text()
        client.sending(user_lgn+"\n")
        client.sending(user_pswrd+"\n")
        check=client.recover()
        #check=from_str_to_bool(check)
        #print(check)
        if check.find("rue")!=-1:
            self.usr_menu_window=User_menu()
            self.usr_menu_window.show()
            self.close()
        else:
            self.close()


class Main_menu(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.admin_login.clicked.connect(self.admin_login_def)
        self.user_login.clicked.connect(self.user_login_def)
        self.register_2.clicked.connect(self.register_new_user)
        self.exit.clicked.connect(self.exit_from_main_window)
        self.babk_button.clicked.connect(self.bank_menu_def)
        self.setWindowTitle("Главное меню")

    def bank_menu_def(self):
        self.bank_window=Manager()
        self.bank_window.show()

    def admin_login_def(self):
        client.sending("1\n")
        self.adm_login_window=Admin_login()
        self.adm_login_window.show()

    def user_login_def(self):
        client.sending("8\n")
        self.usr_login_window=User_login()
        self.usr_login_window.show()

    def register_new_user(self):
        client.sending("3\n")
        self.register_window=Register()
        self.register_window.show()

    def exit_from_main_window(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_menu_window=Main_menu()
    main_menu_window.show()
    app.exec_()

if __name__=='__main__':
    main()