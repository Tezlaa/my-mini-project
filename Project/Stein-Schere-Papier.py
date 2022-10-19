import os
import random

from colorama import Fore, Style, init

init()
print(Style.BRIGHT)

select = 0

print(Fore.GREEN + "Stein-Schere-Papier\n" + Fore.WHITE)

win_user = 0
win_bot = 0
player = ""
bot = ""

stats_game = {}

class User_game():
    def __init__(self, name):
        self.name = name
        self.stats_win = 0
        stats_game.update({self.name:self.stats_win})
    
    def win(self):
        self.stats_win += 1
        stats_game.update({self.name:self.stats_win})
        
    def lose(self):
        if stats_game[self.name] > 0:
            self.stats_win -= 1
            stats_game.update({self.name:self.stats_win})
    
    def display(self, quation):
        if quation == "name":
            return self.name
        elif quation == "wins":
            return self.stats_win
        
def startmenu():
    global select, player, bot
    
    #Create player and bot
    player = User_game(input("Please write your name: "))
    bot = User_game("BOT")                                          
    
    clear_console()
    
    while select < 3:
        clear_console()
        
        print( Fore.GREEN +"MAIN MENU\n\n"+ Fore.WHITE +"-1) Go to game\n-2) Check stats game\n\n" + Fore.RED + "-0) exit" + Fore.WHITE)
        select = int(input(Fore.GREEN + ">>>" + Fore.WHITE))
        if select == 1:
            maingame()
        elif select == 2:
            stats()
        elif select == 0:
            select = 3
        else:
            print(Fore.RED + "Error" + Fore.WHITE )
            select = 0
        
def maingame():
    global select_in_game
    
    print(Fore.GREEN + "GAME\n" + Fore.WHITE)
    exit = False
    while exit == False:
        clear_console()
        print(Fore.WHITE)
        try: 
            select_in_game = int(input("1) STONE\n2) SCHERE\n3) PAPER\n\n" + Fore.RED + "0) exit\n" + Fore.GREEN +  ">>>" + Fore.WHITE).strip())
            if select_in_game == 1 or select_in_game == 2 or select_in_game == 3:
                game()
            elif select_in_game == 0:
                exit = True
            else:
                print(Fore.RED + "Select item (1 or 2 or 3)" + Fore.WHITE);input()
        except:
            pass

def game():
    global select_in_game, player, bot
    
    enemy = random.randint(1, 3)
    print(enemy)
    if select_in_game == 1 and enemy == 2 or select_in_game == 2 and enemy == 3 or select_in_game == 3 and enemy == 1:
        clear_console()
        
        player.win()
        bot.lose()
        
        result("win")
            
        clear_console()
    elif enemy == 1 and select_in_game == 2 or enemy == 2 and select_in_game == 3 or enemy == 3 and select_in_game == 1:
        clear_console()
        
        bot.win()
        player.lose()
        
        result("lose")
        
        clear_console()
    else:
        clear_console()
        
        result("draw")
        
        clear_console()

def stats():
    clear_console()
    print(Fore.GREEN + "\t STATS")
    print(Fore.BLUE + "_" * 23 + Fore.WHITE)
    print(f'1:{player.display("name")}\t\t {player.display("wins")}--WIN\n2:{bot.display("name")}\t\t {bot.display("wins")}--WIN'); input(Fore.BLACK + "type any key..." + Fore.WHITE)
    
def result(symbol):
    if symbol == "win":
        print(Fore.WHITE + "|" * 15)
        print(Fore.GREEN + "|   YOU WIN!  |" + Fore.WHITE)
        print("|" * 15)
        input(Fore.BLACK + "type any key..." + Fore.WHITE)
    elif symbol == "lose":
        print(Fore.WHITE + "|" * 15)
        print(Fore.GREEN + "|  YOU LOSE!  |" + Fore.WHITE)
        print("|" * 15)
        input(Fore.BLACK + "type any key..." + Fore.WHITE)
    elif symbol == "draw":
        print(Fore.WHITE + "|" * 15)
        print(Fore.GREEN + "|    DRAW!    |" + Fore.WHITE)
        print(Fore.WHITE + "|" * 15)
        input(Fore.BLACK + "type any key..." + Fore.WHITE)

def clear_console():
    return os.system('cls||clear')

startmenu()
