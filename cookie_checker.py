# cookie_checker.py
# White-Hat Themed Cookie Checker Tool by cyberPatch

import os

def banner():
    print(""" __        __   _ _     _       _     _           
 \ \      / /__| | |__ (_)_ __ | |__ (_)_ __  ___ 
  \ \ /\ / / _ \ | '_ \| | '_ \| '_ \| | '_ \/ __|
   \ V  V /  __/ | |_) | | | | | | | | | |_) \__ \
    \_/\_/ \___|_|_.__/|_|_| |_|_| |_|_| .__/|___/
                                       |_|        
    Facebook Cookie Checker v1.0
    Ethical Tool for Account Analysis
    by cyberPatch
""")

def main_menu():
    while True:
        os.system("clear")
        banner()
        print("""
[1] Check FB Cookie
[2] Get Token from Cookie
[3] Extract UID from Profile
[4] Login using Cookie or Token
[5] Contact Owner
[6] Learn About Tool
[0] Admin Panel (PIN Required)
[7] Exit Tool
""")
        choice = input("\nEnter option: ")
        if choice == '7':
            break
        else:
            input("Feature not yet implemented. Press Enter to return...")

if __name__ == "__main__":
    main_menu()
