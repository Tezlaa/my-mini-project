from colorama import init
from colorama import Fore, Back , Style
import random

init()
print(Fore.CYAN, Style.BRIGHT)
print("YOUR LIST\n")

user_list = {}
dictionary = {}

class Accaunt_notepad:
    def __init__(self, user):
        self.user_name = user
        self.iduser = random.randint(1, 100)
        
        dictionary.update({self.iduser:user})
        
        user_list.update({self.iduser:[]})
            
    def display_info(self):
        print(Style.DIM + f'\nYour name: {self.user_name}\nYour ID: {self.iduser}\n\n {user_list}\n{dictionary}' + Style.BRIGHT)
    
    def display_acc(self):
        return dictionary
    
    def display_list(self):
        print(self.user_list)

    
    def add_append(self, text):
        user_list[self.iduser] += [text]
        
    def notepad_count(self, word):
        return list(user_list[self.iduser]).count(word)
    
    def notepad_remove(self, word):
        return list(user_list[self.iduser]).remove(word)

    def notepad_clear(self):
        list(user_list[self.iduser]).clear()
    
    def notepad_pop(self, number):
        list(user_list[self.iduser]).pop(number)
        
    def visual_list(self):
        number = 1
        for open_list in user_list.get(self.iduser):
            print(Fore.GREEN + str(number) + Fore.WHITE + " >>> " + Fore.CYAN + open_list + Fore.WHITE)
            number += 1
        if number < 2:
            print(Fore.RED + "\nYOU DON`T HAVE A NOTE" + Fore.WHITE)
                
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
        
        quation = input("You sure (yes or no)?\n>>> ").lower().strip()

        
        if quation == "yes":
            acc.notepad_clear()
            return
        elif quation == "no":
            return
        else:
            print(Fore.RED + "\n---Error---\n" + Fore.WHITE )

#add text in notepad
def add_in_notepad():
    
    user_name.display_info()
    
    i = 0
    while(i == 0):
        print("__" * 50)
        
        user_name.add_append(input("\nwrite text in your list: ").strip())
        
        if user_name.notepad_count("@menu"):
            user_name.notepad_remove("@menu")
            i = 1
        elif user_name.notepad_count("@list"):
            user_name.notepad_remove("@list")
            your_list()
        elif user_name.notepad_count("@help"):
            user_name.notepad_remove("@help")
            print(Fore.MAGENTA + "\nHi, this is a management information page\n\n" + 
                  Fore.GREEN + "@list" + Fore.WHITE + " - info that in your list\n" +
                  Fore.GREEN + "@help" + Fore.WHITE + " - this page\n" +
                  Fore.GREEN + "@menu" + Fore.WHITE + " - go to start menu")
    return

#print full list
def your_list():
    
    user_name.display_info()
    
    print("\n")
    user_name.visual_list()

#delete in lists 
def delete_in_add():
    
    user_name.display_info()
    
    exit = True
    while exit == True:
        your_list()
        print(Fore.RED, Style.DIM + "\n@exit - EXIT" + Fore.WHITE, Style.BRIGHT)
        number_delete = input("Write number which do you want delete: ")
        
        if number_delete == "@exit":
            return
        else:
            try:
                delete_result = int(number_delete) - 1
                user_name.notepad_pop(delete_result)
                continue
            except:
                print(Fore.RED + "\n---Error, write correct number...---\n" + Fore.WHITE)
                continue

def sing_in():
    
    user_name.display_info()
    
    print(Fore.YELLOW + "SING IN" + Fore.WHITE)
    
    sing_id = int(input("Write your ID: "))
    sing_user = input("Write your USER NAME: ")
    
    user_name2 = Real_acc(sing_id, sing_user)

    valuelist = list(dictionary.values())
    valuelist2 = list(user_name2.display_acc2().values())
    idlist = list(dictionary.keys())
    idlist2 = list(user_name2.display_acc2().keys())
    
    sing = True
    while(sing == True):
        i = 0
        for check in range(len(dictionary)):
            if valuelist[i] == valuelist2[0] and idlist[i] == idlist2[0]:
                main_menu()
                sing = False
            i += 1
        else:
            print(Fore.RED + "\n---Error ID or USER NAME---\n" + Fore.WHITE)
            sing = False
            start_lobby = True
    return

#main menu
def main_menu():
    menu = True
    while(menu == True):
        
        user_name.display_info()
        print(dictionary[id])
        
        
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
            print(Fore.RED + "\n---Error number---\n" + Fore.WHITE)
            continue
            
        if select_menu == 1:
            add_in_notepad()
        elif select_menu == 2:
            delete_in_add()
        elif select_menu == 3:
            delete_all()
        elif select_menu == 4:
            your_list()
            input("\ntype any key...")
        elif select_menu == 0:
            exit_menu = True
            while (exit_menu == True):
                
                quation_exit = input("You sure? >>> ").strip().lower()
                
                if quation_exit == "yes":
                    return "\nExit...\n"

                elif quation_exit == "no":
                    exit_menu = False    
                else:
                    exit_menu = True
                    print( Fore.RED + "\nWrite (\"yes\" or \"no\"\n)" + Fore.WHITE)

#started menu
start_lobby = True
while(start_lobby == True):
    
    #select lobby
    try:
        print(Fore.GREEN + "HELLO USER!" +
              Fore.GREEN + "\n1"  + Fore.WHITE + " - REGISTER NEW ACCOUNT" +
              Fore.GREEN + "\n2"  + Fore.WHITE + " - LOGIN IN" +
              Fore.GREEN + "\n3"  + Fore.WHITE + " - INFO" +
              Fore.GREEN + "\n0"  + Fore.WHITE + " - EXIT\n")
        select_register = int(input(">>> ").strip())
    except:
        print(Fore.RED + "\n---Error number---\n" + Fore.WHITE)
        continue
    
    #select
    if select_register == 1:
        
        #OOP register
        user_name = Accaunt_notepad(input("\nWrite the name for your acc: "))
        
        #open main menu 
        main_menu()
    elif select_register == 2:
        sing_in()
    elif select_register == 3:
        your_list()
    elif select_register == 0:
        start_lobby = False

input(Fore.RED + "EXIT..." + Fore.WHITE)