# token_extractor.py
# Extracts access token from Facebook using a live cookie

import requests
import re
import os

def get_token(cookie):
    headers = {
        'user-agent': 'Mozilla/5.0',
        'cookie': cookie
    }

    print("Trying to extract access token...")
    try:
        res = requests.get("https://business.facebook.com/business_locations", headers=headers)
        token = re.search(r'EAAA\w+', res.text)
        if token:
            print("\n[+] Access Token Found:")
            print(token.group(0))
        else:
            print("[-] Failed to extract token. Make sure the cookie is alive and valid.")
    except Exception as e:
        print("Error:", e)

def main():
    os.system("clear")
    print("=== Facebook Token Extractor ===")
    cookie = input("Enter your Facebook Cookie: ")
    get_token(cookie)
    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
