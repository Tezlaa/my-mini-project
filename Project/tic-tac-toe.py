import numpy as np
import os
from colorama import Fore, Style, init

init()
print(Style.BRIGHT, Fore.WHITE)

field = np.array([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])

class Player():
    cout_player = 0
    
    def __init__(self, name):
        self.name = name
        Player.cout_player += 1
        self.symbol = "X"
        if Player.cout_player == 2:
            self.symbol = "O"
    
    def display_win(self):
        print(f'{self.name} WIN')
    
    def select_field(self):
        
        exit_with_select = False
        while exit_with_select == False:
            try:
                self.select_i = int(input(f'\n{self.name} select line: ')) - 1
            
                self.select_j = int(input(f'{self.name} select column: ')) - 1
                
                if field[self.select_i][self.select_j] == "_":
                    field[self.select_i][self.select_j] = self.symbol
                    exit_with_select = True
                else:
                    red_text("ERROR THIS FIELD IS BUSY")
            except:
                red_text("ERROR")
        clear_console()

def check_win():
    i = 0; j = 0
    
    for j in range(3):
        if field[0][j] == "X" and field[1][j] == "X" and field[2][j] == "X" or field[0][j] == "O" and field[1][j] == "O" and field[2][j] == "O":
            if field[0][j] == "X":
                print(Fore.GREEN); player1.display_win(); print(Fore.WHITE)
            else:
                print(Fore.GREEN); player2.display_win(); print(Fore.WHITE)
            return 0
    for i in range(3):
        if field[i][0] == "X" and field[i][1] == "X" and field[i][2] == "X" or field[i][0] == "O" and field[i][1] == "O" and field[i][2] == "O":
            if field[i][0] == "X":
                print(Fore.GREEN); player1.display_win(); print(Fore.WHITE)
            else:
                print(Fore.GREEN); player2.display_win(); print(Fore.WHITE)
            return 0
    if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X" or field[0][0] == "O" and field[1][1] == "O" and field[2][2] == "O":
        if field[0][0] == "X":
            print(Fore.GREEN); player1.display_win(); print(Fore.WHITE)
        else:
            print(Fore.GREEN); player2.display_win(); print(Fore.WHITE)
        return 0
    if field[2][0] == "X" and field[1][1] == "X" and field[0][2] == "X" or field[2][0] == "O" and field[1][1] == "O" and field[0][2] == "O":
        if field[2][0] == "X":
            print(Fore.GREEN); player1.display_win(); print(Fore.WHITE)
        else:
            print(Fore.GREEN); player2.display_win(); print(Fore.WHITE)
        return 0
    return            
                 
def result():
    global field, step
    
    if check_win() == 0:
        
        quation = input("\nDo you want a repeat?\n1)-Repeat\n2)-Close the game\n" + Fore.GREEN + ">>>" + Fore.WHITE) 
        if quation == "2":
            return 2
        else :
            field = np.array([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])
            step = 0
            return 1
                     
#supporting funcions
def red_text(text):
    print(Fore.RED + text + Fore.WHITE)   
    
def green_text(text):
    print(Fore.GREEN + text + Fore.WHITE) 
    
def clear_console():
    return os.system('cls||clear')

def display_field():
    for fields in field:
        print(fields)

#main code
if __name__=="__main__":
    print("\tTIC-TAC-TOE\n")
    
    player1 = Player(input("Write your name: "))
    player2 = Player(input("Write second name: "))

    step = 0
    game = True
    while game == True:
        if step != 8:
            clear_console()
            display_field()
            player1.select_field()
            
            quation = result()
            if quation == 1:
                continue
            if quation == 2:
                break
            
            display_field()
            player2.select_field()
            
            quation = result()
            if quation == 1:
                continue
            if quation == 2:
                break
            
            step += 2
        else:
            green_text("THE DRAW!")
            
            quation = input("\nDo you want a repeat?\n1)-Repeat\n2)-Close the game\n" + Fore.GREEN + ">>>" + Fore.WHITE) 
            if quation == "2":
                break
            else:
                field = np.array([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])
                step = 0
                continue