import os
import sys
import time
from colorama import Fore, Style, init
from admin_panel import run_admin_panel
from uid_extractor import run_uid_extractor
from token_extractor import run_token_extractor
from login_session_saver import run_login_session_saver

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(Fore.CYAN + r"""
__        __   _     _ _       _           _         
\ \      / /__| |__ (_) |__   | |__   ___ | | _____  
 \ \ /\ / / _ \ '_ \| | '_ \  | '_ \ / _ \| |/ / _ \ 
  \ V  V /  __/ |_) | | | | | | |_) | (_) |   <  __/ 
   \_/\_/ \___|_.__/|_|_| |_| |_.__/ \___/|_|\_\___| 
                                                    
    """ + Style.BRIGHT + Fore.WHITE + "Facebook Cookie Checker v1.0")
    print(Fore.LIGHTWHITE_EX + "Ethical Tool for Account Analysis")
    print(Fore.GREEN + "by cyberPatch
")

def menu():
    print(Fore.CYAN + "[1]" + Fore.WHITE + " Check FB Cookie")
    print(Fore.CYAN + "[2]" + Fore.WHITE + " Get Token from Cookie")
    print(Fore.CYAN + "[3]" + Fore.WHITE + " Extract UID from Profile")
    print(Fore.CYAN + "[4]" + Fore.WHITE + " Login using Cookie or Token")
    print(Fore.CYAN + "[5]" + Fore.WHITE + " Contact Owner")
    print(Fore.CYAN + "[6]" + Fore.WHITE + " Learn About Tool")
    print(Fore.CYAN + "[0]" + Fore.WHITE + " Admin Panel (PIN Required)")
    print(Fore.CYAN + "[7]" + Fore.WHITE + " Exit Tool
")

def wait():
    input(Fore.YELLOW + "Press Enter to return...")

def contact_owner():
    clear()
    print(Fore.CYAN + "Contact Owner:")
    print(Fore.GREEN + "GitHub: https://github.com/cyberPatch")
    print(Fore.GREEN + "Telegram: https://t.me/cyberPatch")
    wait()

def learn_about():
    clear()
    print(Fore.LIGHTBLUE_EX + "About this tool:")
    print(Fore.WHITE + "This is a Facebook cookie and UID analyzer built for ethical hacking and testing only.")
    wait()

def check_cookie():
    clear()
    print(Fore.YELLOW + "Feature not yet implemented.")
    wait()

def main():
    while True:
        banner()
        menu()
        choice = input(Fore.YELLOW + "Enter option: ")

        if choice == '1':
            check_cookie()
        elif choice == '2':
            run_token_extractor()
        elif choice == '3':
            run_uid_extractor()
        elif choice == '4':
            run_login_session_saver()
        elif choice == '5':
            contact_owner()
        elif choice == '6':
            learn_about()
        elif choice == '0':
            run_admin_panel()
        elif choice == '7':
            clear()
            print(Fore.CYAN + "Exiting... Stay ethical!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option!")
            time.sleep(1)

if __name__ == '__main__':
    main()
