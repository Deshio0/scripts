'''
Simple nmap target analyzer by deshio
'''
import os
import ipaddress

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
    
    choice = input("                        Choice: ")
    
    if choice == "2":
        os.system("clear")
        os.system("exit")
        return choice
    elif choice == "1":
        return "1"
    else:
        print("WRONG INPUT! ")
        return False

def mode():
    os.system("clear")
    print("Debug: Run Start")
    print(colours.BOLD + colours.RED + "-/-/-/-/-/-/-/- Target Analyzer by deshio -\-\-\-\-\-\-\-" + colours.END)
    print(colours.RED + colours.BOLD + "                    Choose what to do: " + colours.END)
    print(colours.GREEN + "                    1. " + colours.BLUE + "Standard Scan")
    print(colours.GREEN + "                    2. " + colours.BLUE + "Slow Scan" + colours.END)
    print(colours.GREEN + "                    3. " + colours.BLUE + "Return back" + colours.END)
    print(colours.BOLD + colours.RED + "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" + colours.END)
    choice = input("                        Choice: ")
    return choice

def analyze():
    global target
    os.system("clear")
    print("Debug: Input Target")
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
        return "back"
    elif ipcheck() == True:
        print("Debug: nmap analyze")
        os.system("nmap -oN " + target + ".txt " + target + " > /dev/null 2>&1")
        print(colours.BOLD + colours.RED + "Currently open ports: "+ colours.END)
        os.system("cat " + target + ".txt " + "| grep open")
        print(colours.RED +"Full scan details saved in " + "./" + target + ".txt" + colours.END)
        print(colours.BOLD + colours.RED + "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" + colours.END)
        input("Continue ")
    else:
        print("Wrong input!")
    
    
# -----------------------------------------------


while True:

    if start() == "1":
        
        while True:
            
            if mode() == "1":
                
                while True:
                    
                    if analyze() == "back":
                        break
                    else:
                        continue
            else:
                break
    elif "2":
        exit()
    else:
        continue
