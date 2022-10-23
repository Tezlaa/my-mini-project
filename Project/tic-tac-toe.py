import colorama
import numpy as np
import os
from colorama import Fore, Style, init

init()
print(Style.BRIGHT)

#print("_|_|_")
#print("_|_|_")
#print(" | | ")

field = np.array([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])

class Player():
    cout_player = 0
    
    def __init__(self, name):
        self.name = name
        Player.cout_player += 1
        self.symbol = "X"
        if Player.cout_player == 2:
            self.symbol = "O"
    
    def select_field(self):
        
        exit_with_select = False
        while exit_with_select == False: 
            self.select_i = int(input(f'\n{self.name} select line: ')) - 1
            
            self.select_j = int(input(f'{self.name} select column: ')) - 1
            
            if field[self.select_i][self.select_j] == "_":
                field[self.select_i][self.select_j] = self.symbol
                exit_with_select = True
            else:
                red_text("ERROR")
        clear_console()
            
#supporting funcions
def red_text(text):
    print(Fore.RED + text + Fore.WHITE)   

def clear_console():
    return os.system('cls||clear')

def display_field():
    for fields in field:
        print(fields)

#main code
if __name__=="__main__":
    print("\tHELLO TIC-TAC-TOE\n")
    
    player1 = Player(input("Write your name: "))
    player2 = Player(input("Write second name: "))

    game = True
    while game == True:
        display_field()
        player1.select_field()
        display_field()
        player2.select_field()
