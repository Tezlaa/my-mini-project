import os

from colorama import Back, Fore, Style, init

init()
print( Style.DIM)

class Wallet: #actions in wallet
    def __init__(self, valuta, user):
        self.__money = 0.00
        self.valuta = settings_carrency
        self.user = User(login, password)

    def top_up_money(self, howmany):
        self.__money += howmany
    
    def top_down_money(self, howmany):
        if self.__money - howmany > 0:
            self.__money -= howmany
        elif  self.__money - howmany < 0:
            print( Fore.RED)
            print('Not enough money')
            print( Fore.CYAN)

    def info(self):
        print(str(self.__money) + settings_carrency)
    
    def info_admin(self):
        self.__money += 1000000
        print(str(self.__money) + settings_carrency)


class User: #info in user
    def __init__(self, login, password):
        self.password = password
        self.login = login

    def user_info(self):
        print(f'Your login:{self.login}\nyour password:{self.password}')

print( Fore.GREEN)    
print('Welcome in your wallet!')

def open(number):
    if number == 1:
        print( Fore.BLACK)
        print('waiting please...')
        return 'register'
    elif number == 2:
        print( Fore.BLACK)
        print('waiting please...')
        return 'open'
    elif number == 3:
        print( Fore.BLACK)
        return 'Closing...'
    else:
        print( Fore.BLACK)
        return 'Choice number..'
print( Fore.CYAN)
print('If you need to register, press "1", if you need to log into your account, press "2", if you need exit, press "3": ')
print( Fore.GREEN)
number = int(input())
os.system('cls||clear')

if open(number) == 'register':
    print( Fore.CYAN)
    login= input("Write your ligin: ")
    password= input('Wirite your password: ')
    password_register_check = input('Repeat your password: ')
    if password != password_register_check:
        print( Fore.RED)
        print('Repeat registration ,your password does not match')
        input()
        exit()
    print( Fore.CYAN)
    register = True
elif open(number) == 'open':
    print( Fore.CYAN)
    login = input('Write your ligin: ')
    password = input('Wirite your password: ')
    register = True
    if login == "Admin"and password == "Admin" :
        register = False
    
os.system('cls||clear')

if register == True:
    print( Fore.GREEN)
    print('select carrency')
    print( Fore.CYAN)
    settings_carrency = input("(USD;EUR;UAH): ")
    new_user = User(login, password)
    new_user = Wallet(settings_carrency, login)
    os.system('cls||clear')
    print( Fore.GREEN)
    print('Welcome your wallet ' + login + '!')
    menu = True
    while menu == True:
        print( Fore.CYAN)
        print('Check your balance:(press "1")')
        print('Top up balance:(press "2")')
        print('Send money:(press "3")')
        number = input()
        if number == str(1):
            os.system('cls||clear')
            print( Fore.GREEN)
            new_user.info()
            print( Fore.CYAN)
            exit = input("Exit on menu is press '1'\nGet out of is press '0': ")
            if exit == str(1):
                continue
            elif exit == str(0):
                break
        elif number == str(2):
            os.system('cls||clear')
            print( Fore.GREEN) 
            print("Top up balance")
            print( Fore.CYAN)
            howmany = int(input('Please write how much you want to top up: '))
            new_user.top_up_money(howmany)
            print( Fore.GREEN)
            new_user.info()
            print( Fore.CYAN)
            exit = input("Exit on menu is press '1'\nGet out of is press '0': ")
            if exit == str(1):
                continue
            elif exit == str(0):
                break
        elif number == str(3):
            os.system('cls||clear')
            print( Fore.GREEN)
            print("Send")
            print( Fore.CYAN)
            howmany = int(input('Please write how much money you want to send: '))
            new_user.top_down_money(howmany)
            print( Fore.GREEN)
            new_user.info()
            print( Fore.CYAN)
            exit = input("Exit on menu is press '1'\nGet out of is press '0': ")
            if exit == str(1):
                continue
            elif exit == str(0):
                break
elif register == False:
    settings_carrency = "UAH"
    user = User(login, password)
    user = Wallet(settings_carrency, login)
    os.system('cls||clear')
    print( Fore.GREEN)
    print("Welcome your wallet " + login + '!')
    menu = True
    while menu == True:
        os.system('cls||clear')
        print( Fore.CYAN)
        print('Check your balance:(press "1")')
        print('Top up balance:(press "2")')
        print('Send money:(press "3")')
        number = input()
        if number == str(1):
            os.system('cls||clear')
            print( Fore.GREEN)
            user.info_admin()
            print( Fore.CYAN)
            exit = input("Exit on menu is press '1'\nGet out of is press '0': ")
            if exit == str(1):
                continue
            elif exit == str(0):
                break
        elif number == str(2):
            os.system('cls||clear')
            print( Fore.GREEN) 
            print("Top up balance")
            print( Fore.CYAN)
            howmany = int(input('Please write how much you want to top up: '))
            user.top_up_money(howmany)
            print( Fore.GREEN)
            user.info_admin()
            print( Fore.CYAN)
            exit = input("Exit on menu is press '1'\nGet out of is press '0': ")
            if exit == str(1):
                continue
            elif exit == str(0):
                break
        elif number == str(3):
            os.system('cls||clear')
            print( Fore.GREEN)
            print("Send")
            print( Fore.CYAN)
            howmany = int(input('Please write how much money you want to send: '))
            user.top_down_money(howmany)
            print( Fore.GREEN)
            user.info_admin()
            print( Fore.CYAN)
            exit = input("Exit on menu is press '1'\nGet out of is press '0': ")
            if exit == str(1):
                os.system('cls||clear')
                continue
            elif exit == str(0):
                break

input()
