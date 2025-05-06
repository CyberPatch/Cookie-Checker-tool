# uid_extractor.py
# Extracts friends' UIDs from public Facebook profiles using cookie or token

import requests
import re
import os

def extract_uids(cookie, uid_list, output_file):
    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0'
    }

    extracted = set()
    for uid in uid_list:
        print(f"Extracting from UID: {uid}")
        url = f'https://mbasic.facebook.com/profile.php?id={uid}&v=friends'
        try:
            res = requests.get(url, headers=headers)
            ids = re.findall(r'uid=(\d+)', res.text)
            extracted.update(ids)
            print(f"Found {len(ids)} friends from {uid}")
        except Exception as e:
            print("Error:", e)

    with open(output_file, 'w') as f:
        for eid in sorted(extracted):
            f.write(eid + '\n')

    print(f"Total unique friends extracted: {len(extracted)}")
    print("Saved to", output_file)

def main():
    os.system("clear")
    print("=== UID Extractor ===")
    cookie = input("Enter your Facebook Cookie: ")
    output_file = input("Enter filename to save extracted UIDs (e.g., uids.txt): ")
    total = int(input("How many public UIDs you want to add: "))
    uid_list = []
    for i in range(total):
        uid = input(f"UID {i+1}: ")
        uid_list.append(uid)
    extract_uids(cookie, uid_list, output_file)

if __name__ == "__main__":
    main()
