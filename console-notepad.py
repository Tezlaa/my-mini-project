from colorama import init
from colorama import Fore, Back , Style
import os
import random

init()
print(Fore.CYAN, Style.BRIGHT)
print("YOUR LIST\n")

user_list = {}
dictionary = {1992:"ADMIN",}
sing_id = 0


def account(name_user):
    global sing_id
    sing_id = random.randint(1, 100)
    
    dictionary.update({sing_id:name_user})
    
    user_list.update({sing_id:[]})

def display_info():
    print(Style.DIM + Fore.CYAN + f'\nYour name: {user_name}\nYour ID: {sing_id}\n\n {user_list}\n{dictionary}'+ Fore.WHITE + Style.BRIGHT)
        
class Real_acc:
    def __init__(self, iduser, user):
        self.user = user
        self.id = iduser
        self.sing_in_acc = {iduser:user}
        
    def display_acc2(self):
        return self.sing_in_acc

#delete all list
def delete_all():
    delete_all_quation = True
    
    while(delete_all_quation == True):
        os.system('cls||clear')
        
        quation = input("You sure (yes or no)?\n>>> ").lower().strip()

        if quation == "yes":
            os.system('cls||clear')
            
            notepad_list.clear()
            return
        elif quation == "no":
            return
        else:
            print(Fore.RED + "\n---Error---\n" + Fore.WHITE )
            input(Fore.RED + "\ntype any key..." + Fore.WHITE)

#add text in notepad
def add_in_notepad():    
    
    i = 0
    while(i == 0):
        os.system('cls||clear')
        print("__" * 50)
        
        user_list[sing_id] += [input("\nWRITE TEXT IN YOUR LIST"+  Fore.GREEN +">>"+ Fore.WHITE).strip()]
        os.system('cls||clear')
        
        check_menu = notepad_list.count("@menu")
        check_list = notepad_list.count("@list")
        check_help = notepad_list.count("@help")
        
        if check_menu == 1:
            notepad_list.remove("@menu")
            i = 1
        elif check_list == 1:
            os.system('cls||clear')
            
            notepad_list.remove("@list")
            your_list(True)
        elif check_help == 1:
            os.system('cls||clear')
            
            notepad_list.remove("@help")
            print(Fore.MAGENTA + "\nHi, this is a management information page\n\n" + 
                  Fore.GREEN + "@list" + Fore.WHITE + " - info that in your list\n" +
                  Fore.GREEN + "@help" + Fore.WHITE + " - this page\n" +
                  Fore.GREEN + "@menu" + Fore.WHITE + " - go to start menu\n")
            input(Fore.RED + "\ntype any key..." + Fore.WHITE)
        else:
            continue
    return

#print full list
def your_list(quation):
    os.system('cls||clear')
    
    print("\n")
    number = 1
    
    print("__" * 50 + "\n")
    for open_list in user_list.get(sing_id):
        print(Fore.GREEN + str(number) + Fore.WHITE + " >>>  " + Fore.CYAN + open_list + Fore.WHITE)
        number += 1
    if number < 2:
        os.system('cls||clear')
        
        print(Fore.RED + "\nYOU DON`T HAVE A NOTE" + Fore.WHITE)
        input(Fore.RED + "\ntype any key..." + Fore.WHITE)
        return
    if quation == True:
        print("__" * 50)
        input(Fore.RED + "\ntype any key..." + Fore.WHITE)
        return os.system('cls||clear')
    print("__" * 50)

#delete in lists 
def delete_in():

    exit = True
    while exit == True:
        os.system('cls||clear')
        
        your_list(False)
        print(Fore.RED, Style.DIM + "\n@exit - EXIT" + Fore.WHITE, Style.BRIGHT)
        number_delete = input("Write number which do you want delete: ")
        
        if number_delete == "@exit":
            return
        else:
            try:
                delete_result = int(number_delete) - 1
                notepad_list.pop(delete_result)
                continue
            except:
                os.system('cls||clear')
                
                print(Fore.RED + "\n---Error, write correct number...---\n" + Fore.WHITE)
                continue

def sing_in():
    global sing_id

    print(Fore.YELLOW + "SING IN" + Fore.WHITE)
    
    sing_id = int(input("Write your ID: "))
    sing_user = input("Write your USER NAME: ")
    
    os.system('cls||clear')
    
    user_name2 = Real_acc(sing_id, sing_user)

    valuelist = list(dictionary.values())
    valuelist2 = list(user_name2.display_acc2().values())
    idlist = list(dictionary.keys())
    idlist2 = list(user_name2.display_acc2().keys())
    
    sing = True
    while(sing == True):
        i = 0
        for check in range(len(dictionary)):
            if sing_id == 1992 and sing_user == "ADMIN":
                try:
                    os.system('cls||clear')
                    
                    display_info()
                    input(Fore.RED + "\ntype any key..." + Fore.WHITE)
                    
                    os.system('cls||clear')
                except:
                    os.system('cls||clear')
                    
                    print(Fore.RED + "\n\nError, only one account" + Fore.WHITE)
                    input(Fore.RED + "\ntype any key..." + Fore.WHITE)
                return
            if valuelist[i] == valuelist2[0] and idlist[i] == idlist2[0]:
                os.system('cls||clear')
                
                main_menu()
                return
            i += 1
        else:
            os.system('cls||clear')
            
            print(Fore.RED + "\n---Error ID or USER NAME---\n" + Fore.WHITE)
            sing = False
            start_lobby = True
    return

#main menu
def main_menu():
    menu = True
    while(menu == True):
        global notepad_list
        notepad_list = user_list[sing_id]
        
        os.system('cls||clear')

        try:
            print(Fore.GREEN + "Y O U R   N O T E P A D |")
            print(Fore.GREEN + "________________________|" +
                Fore.GREEN + "\n1"  + Fore.WHITE + " - ADD IN LIST" +
                Fore.GREEN + "\n2"  + Fore.WHITE + " - DELETE IN LIST" +
                Fore.GREEN + "\n3"  + Fore.WHITE + " - DELETE ALL LIST" +
                Fore.GREEN + "\n4"  + Fore.WHITE + " - YOUR LIST" +
                Fore.GREEN + "\n0"  + Fore.WHITE + " - EXIT\n")
            select_menu = int(input(">>> ").strip())
        except:
            os.system('cls||clear')
            
            print(Fore.RED + "\n---Error number---\n" + Fore.WHITE)
            input(Fore.RED + "\ntype any key..." + Fore.WHITE)
            continue
            
        if select_menu == 1:
            add_in_notepad()
        elif select_menu == 2:
            delete_in()
        elif select_menu == 3:
            delete_all()
        elif select_menu == 4:
            your_list(True)
        elif select_menu == 0:
            exit_menu = True
            while (exit_menu == True):
                os.system('cls||clear')
                
                quation_exit = input("You sure? >>> ").strip().lower()
                
                if quation_exit == "yes":
                    os.system('cls||clear')
                    input(Fore.RED + "EXIT..." + Fore.WHITE)
                    return

                elif quation_exit == "no":
                    exit_menu = False    
                else:
                    exit_menu = True
                    print( Fore.RED + "\nWrite (\"yes\" or \"no\"\n)" + Fore.WHITE)
                    input(Fore.RED + "\ntype any key..." + Fore.WHITE)
                    os.system('cls||clear')

#started menu
start_lobby = True
number_start = 1
while(start_lobby == True):
    os.system('cls||clear')
    
    #select lobby
    try:
        if number_start == 1:
            print(Fore.GREEN + "HELLO NEW USER!\n")
        print(Fore.GREEN + "\n1"  + Fore.WHITE + " - REGISTER NEW ACCOUNT" +
              Fore.GREEN + "\n2"  + Fore.WHITE + " - LOGIN IN" +
              Fore.GREEN + "\n3"  + Fore.WHITE + " - INFO" +
              Fore.GREEN + "\n0"  + Fore.WHITE + " - EXIT\n")
        select_register = int(input(">>> ").strip())
    except:
        os.system('cls||clear')
        
        print(Fore.RED + "\n---Error number---\n" + Fore.WHITE)
        continue

    
    #select
    if select_register == 1:
        os.system('cls||clear')
        
        #add in dictionary and in list
        user_name = input("\nWrite the name for your acc: ")
        account(user_name)
        
        os.system('cls||clear')
        
        print(Fore.GREEN + "SUCCESSFULL REGISTER" + Fore.WHITE)
        print(Fore.YELLOW + f'YOUR ID: {sing_id}' + Fore.WHITE)
        input(Fore.YELLOW + "\nLog in your account" + Fore.WHITE)
        
        os.system('cls||clear')
    elif select_register == 2:
        os.system('cls||clear')
        
        sing_in()
    elif select_register == 3:
        os.system('cls||clear')
        print(Fore.MAGENTA + "\nHi, this is a management information page\n\n" + 
                  Fore.GREEN + "@list" + Fore.WHITE + " - info that in your list(in add list)\n" +
                  Fore.GREEN + "@help" + Fore.WHITE + " - this page(in add list)\n" +
                  Fore.GREEN + "@menu" + Fore.WHITE + " - go to start menu(in add list)\n")
        input(Fore.RED + "\ntype any key..." + Fore.WHITE)
        
        os.system('cls||clear')
    elif select_register == 0:
        start_lobby = False
    number_start += 1

input(Fore.RED + "EXIT..." + Fore.WHITE)