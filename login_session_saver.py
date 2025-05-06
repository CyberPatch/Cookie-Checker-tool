# login_session_saver.py
# Saves login session from a given cookie

import os
import time
import requests

SESSION_FILE = "login_sessions.txt"

def save_session(cookie):
    with open(SESSION_FILE, "a") as f:
        f.write(cookie + "\n")
    print("Session saved successfully.")

def is_cookie_alive(cookie):
    try:
        headers = {
            "cookie": cookie,
            "user-agent": "Mozilla/5.0"
        }
        res = requests.get("https://mbasic.facebook.com/profile", headers=headers)
        return "mbasic_logout_button" in res.text
    except:
        return False

def main():
    os.system("clear")
    print("=== Save Login Session ===")
    cookie = input("Enter your Facebook cookie: ")
    if is_cookie_alive(cookie):
        print("[+] Cookie is alive.")
        save_session(cookie)
    else:
        print("[-] Cookie is expired or invalid.")
    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
