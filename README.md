# Cookie Checker Tool

A Facebook cookie checking and UID extraction tool created by **cyberPatch**.

## Features

- Check multiple cookies from a file or directly
- Get Facebook tokens from valid cookies
- Extract UIDs from public profile links (friends of friends)
- Login using cookies or tokens
- Save and manage checked cookies with admin panel
- Built-in contact and tool info section

## Run in Termux

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/cyberPatch/cookie-checker-tool.git
cd cookie-checker-tool
pip install -r requirements.txt
python cookie_checker.py
```
