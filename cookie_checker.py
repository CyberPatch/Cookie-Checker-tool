# cookie_checker.py
# Main script for the Cookie Checker tool

import json
import os
from datetime import datetime

def banner():
    print("""\033[95m
  ██████╗  ██████╗  ██████╗██╗  ██╗██╗███████╗
  ██╔══██╗██╔═══██╗██╔════╝██║  ██║██║██╔════╝
  ██████╔╝██║   ██║██║     ███████║██║█████╗  
  ██╔═══╝ ██║   ██║██║     ██╔══██║██║██╔══╝  
  ██║     ╚██████╔╝╚██████╗██║  ██║██║███████╗
  ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝
          [94mFacebook Cookie Checker v1.0
         [0mby [92mcyberPatch[0m
""")

def main_menu():
    banner()
    print("""\033[96m
[1] Check FB Cookie
[2] Get Token from Cookie
[3] Extract UID from Profile
[4] Login using Cookie or Token
[5] Contact Owner
[6] Learn About Tool
[0] Admin Panel (PIN Required)
[7] Exit Tool
\033[0m""")
    input("\nEnter option: ")

if __name__ == "__main__":
    main_menu()
