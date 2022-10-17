import random

from colorama import Fore, Style, init

init()
print(Style.BRIGHT)

select = 0

print(Fore.GREEN + "\tSTONE OF NONES\n")

def startmenu():
    global select
    while select < 3:
        print(Fore.WHITE + "\tMAIN MENU\n\n-1) Go to game\n-2) Check stats game\n")
        select = int(input("Make your choice: "))
        if select == 1:
            maingame()
        elif select == 2:
            stats()
        
def maingame():
    global select_in_game
    
    print(Fore.GREEN + "GAME\n")
    exit = False
    while exit == False:
        select_in_game = int(input("-1) STONE\n-2) NONES\n-3) PAPER\n-0) exit\n>>>"))
        if select_in_game == 1 or select_in_game == 2 or select_in_game == 3:
            game()
        elif select_in_game == 0:
            exit = True
        else:
            print("Select item (1 or 2 or 3)")

def game():
    global select_in_game
    
    enemy = random.randint(1, 3)
    print(enemy)
    if select_in_game == 1 and enemy == 2 or select_in_game == 2 and enemy == 3 or select_in_game == 3 and enemy == 1:
        result("win")
    elif enemy == 1 and select_in_game == 2 or enemy == 2 and select_in_game == 3 or enemy == 3 and select_in_game == 1:
        result("lose")
    else:
        result("draw")

def stats():
    print(Fore.GREEN + "STATUS")
    
def result(symbol):
    if symbol == "win":
        print(Fore.GREEN + "YOU WIN!" + Fore.WHITE)
    elif symbol == "lose":
        print(Fore.GREEN + "YOU LOSE!" + Fore.WHITE)
    elif symbol == "draw":
        print(Fore.GREEN + "DRAW!" + Fore.WHITE)

startmenu()
