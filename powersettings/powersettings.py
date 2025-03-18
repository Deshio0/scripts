'''
Simple power settings by deshio
Using powerprofilesctl and optimus-manager
'''
import os

check = bool(0)

class colours:
    RED = '\33[31m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUE   = '\33[34m'
    GREEN  = '\33[32m'
    
def show_menu():
    print(colours.END + colours.RED + "Simple power settings by deshio!")
    print(colours.BOLD + "Choose desired profile: " + colours.END)
    print(colours.BLUE + " 1. Full-Performance -" + colours.GREEN + " I need more power!")
    print(colours.BLUE + " 2. Balanced - " + colours.GREEN + "As all things should be")
    print(colours.BLUE + " 3. Power-saver - " + colours.GREEN + "Least consumption" + colours.END)

def choice():
    ch = input(colours.BOLD + colours.RED + "Choice: ")
    if (ch == '1'):
        os.system("powerprofilesctl set performance")
        os.system("optimus-manager --switch nvidia")
        return 0
    elif (ch == '2'):
        os.system("powerprofilesctl set balanced")
        os.system("optimus-manager --switch integrated")
        return 0
    elif (ch == '3'):
        os.system("powerprofilesctl set power-saver")
        os.system("optimus-manager --switch integrated")
        return 0
    else:
        print("Wrong choice! ")
        return 1
        
while(True):
    show_menu()
    choice()
    check = choice()
    if(check == 0):
        break
    os.system("clear")
    if(check == 0):
        break
    os.system("clear")
