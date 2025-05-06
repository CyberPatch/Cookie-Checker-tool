# admin_panel.py
# Admin panel to manage saved cookies

import os

ADMIN_PIN = "9999"
COOKIE_FILE = "saved_cookies.txt"

def load_cookies():
    if not os.path.exists(COOKIE_FILE):
        print("No cookies saved yet.")
        return []
    with open(COOKIE_FILE, "r") as f:
        return f.read().splitlines()

def save_cookie(cookie):
    with open(COOKIE_FILE, "a") as f:
        f.write(cookie + "\n")

def clear_cookies():
    if os.path.exists(COOKIE_FILE):
        os.remove(COOKIE_FILE)
        print("All saved cookies have been deleted.")
    else:
        print("No cookie file found.")

def show_menu():
    print("""
[ Admin Panel ]
1. View Saved Cookies
2. Clear All Saved Cookies
3. Exit Admin Panel
""")

def admin_panel():
    os.system("clear")
    pin = input("Enter Admin PIN: ")
    if pin != ADMIN_PIN:
        print("Invalid PIN. Access Denied.")
        return
    while True:
        os.system("clear")
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            cookies = load_cookies()
            if cookies:
                print("\nSaved Cookies:")
                for c in cookies:
                    print("-", c)
            else:
                print("No cookies saved.")
        elif choice == "2":
            clear_cookies()
        elif choice == "3":
            break
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    admin_panel()
