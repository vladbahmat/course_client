from admin import Admin,server
from clients import Clients
import psycopg2
import time
from functions import text_string

class Bank:
    def menu(self):
        client=Clients()
        admin=Admin()
        buf='0'
        while True:
            buf=server.recover()
            if buf=='1':
                check=admin.authorization()
                server.sending(str(check))

bank=Bank()
bank.menu()