'''
Simple nmap target analyzer by deshio
'''
import os
import ipaddress
import subprocess

class colours:
    RED = '\33[31m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUE   = '\33[34m'
    GREEN  = '\33[32m'

def start():
    os.system("clear")
    print("Debug: Run Start")
    print(colours.BOLD + colours.RED + "-/-/-/-/-/-/-/- Target Analyzer by deshio -\-\-\-\-\-\-\-" + colours.END)
    print(colours.RED + colours.BOLD + "                    Choose what to do: " + colours.END)
    print(colours.GREEN + "                    1. " + colours.BLUE + "Analyze Target")
    print(colours.GREEN + "                    2. " + colours.BLUE + "Exit program" + colours.END)
    print(colours.BOLD + colours.RED + "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" + colours.END)
    
    global choice1
    choice1 = input("                        Choice: ")
    
    if choice1 == '2':
        os.system("clear")
        os.system("exit")
        return 2
    elif choice1 == '1':
        return 1
    else:
        print("WRONG INPUT! ")
        return 0
    
global target2

def analyze():
    global target
    # os.system("clear")
    print("Debug: Run Analyze")
    print(colours.BOLD + colours.RED + "-/-/-/-/-/-/-/- Target Analyzer by deshio -\-\-\-\-\-\-\-" + colours.END)
    print(colours.GREEN + "             ! " + colours.BLUE + "Type 'back' to return ")
    target = input(colours.GREEN + "             1. " + colours.BLUE + "Target address: ")
    print(colours.BOLD + colours.RED + "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" + colours.END)
    
    def ipcheck():
        try:
            ipaddress.IPv4Network(target, strict=False)
            return True
        except ValueError:
            return False
    
    if target == "back":
        return 1
    elif ipcheck() == True:
        print("Debug: Actual analyze")
        os.system("nmap -oN " + target + ".txt " + target + " > /dev/null 2>&1")
        os.system("cat " + target + ".txt " + "| grep open")
        input("good?")
    else:
        print("Wrong input!")
    
    
# -----------------------------------------------

global checking

while True:
    checking = start()
    if checking == 1:
        while True:
            choice2 = analyze()
            if choice2 == 1:
                break
    if checking == 2:
        exit()
    
