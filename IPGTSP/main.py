import requests
import os
import json

API_KEY = "96fd8f01f0cf4d3b86da7aa9ad9200d8"

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop", "ip_info.txt")

def print_green(msg):
    print(f"\033[92m{msg}\033[0m")

def print_red(msg):
    print(f"\033[91m{msg}\033[0m")

def print_cyan(msg):
    print(f"\033[96m{msg}\033[0m")

def track_own_ip():
    try:
        res = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}")
        data = res.json()

        ip_info = {
            "IP": data.get("ip"),
            "Location": f"{data.get('city')}, {data.get('state_prov')}, {data.get('country_name')}",
            "Latitude": data.get("latitude"),
            "Longitude": data.get("longitude"),
            "ISP": data.get("isp"),
            "Timezone": data["time_zone"]["name"],
            "Currency": data["currency"]["name"]
        }

        for k, v in ip_info.items():
            print_green(f"[+] {k:12}: {v}")

        path = get_desktop_path()
        with open(path, "w") as f:
            for k, v in ip_info.items():
                f.write(f"{k}: {v}\n")

        print_cyan(f"\n[✓] Geo data saved to: {path}")
        get_threat_info(data.get("ip"))

    except Exception as e:
        print_red(f"\n[X] Failed to fetch IP info. Error: {e}")

def scan_ip(ip):
    print(f"\n[+] Scanning IP: {ip}")
    try:
        res = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}")
        data = res.json()

        ip_info = {
            "IP": data.get("ip"),
            "Location": f"{data.get('city')}, {data.get('state_prov')}, {data.get('country_name')}",
            "Latitude": data.get("latitude"),
            "Longitude": data.get("longitude"),
            "ISP": data.get("isp"),
            "Timezone": data["time_zone"]["name"],
            "Currency": data["currency"]["name"]
        }

        for k, v in ip_info.items():
            print_green(f"[+] {k:12}: {v}")

        path = get_desktop_path()
        with open(path, "w") as f:
            for k, v in ip_info.items():
                f.write(f"{k}: {v}\n")

        print_cyan(f"\n[✓] Geo data saved to: {path}")
        get_threat_info(ip)

    except Exception as e:
        print_red(f"\n[X] Failed to scan IP. Error: {e}")

def get_threat_info(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=proxy,host,isp,query,tor,bot")
        data = res.json()

        print(f"[?] VPN       : {'Detected' if data.get('proxy') else 'Not Detected'}")
        print(f"[?] ISP       : {data.get('isp')}")
        print(f"[?] TOR       : {'Detected' if data.get('tor') else 'Not Detected'}")
        print(f"[?] Bot Status: {'Detected' if data.get('bot') else 'Clean'}")
    except Exception as e:
        print_red(f"[X] Failed to fetch threat info. Error: {e}")

def main():
    banner = """
/* @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */
/* @                                                                              @ */
/* @   ▪   ▄▄▄·     ▄▄ • ▄▄▄ .      ▄▄▌         ▄▄·  ▄▄▄· ▄▄▄▄▄▪         ▐ ▄      @ */
/* @   ██ ▐█ ▄█    ▐█ ▀ ▪▀▄.▀·▪     ██•  ▪     ▐█ ▌▪▐█ ▀█ •██  ██ ▪     •█▌▐█     @ */
/* @   ▐█· ██▀·    ▄█ ▀█▄▐▀▀▪▄ ▄█▀▄ ██▪   ▄█▀▄ ██ ▄▄▄█▀▀█  ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌     @ */
/* @   ▐█▌▐█▪·•    ▐█▄▪▐█▐█▄▄▌▐█▌.▐▌▐█▌▐▌▐█▌.▐▌▐███▌▐█ ▪▐▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌     @ */
/* @   ▀▀▀.▀       ·▀▀▀▀  ▀▀▀  ▀█▄▀▪.▀▀▀  ▀█▄▀▪·▀▀▀  ▀  ▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪     @ */
/* @   ▄▄▄▄▄ ▄ .▄▄▄▄  ▄▄▄ . ▄▄▄· ▄▄▄▄▄    .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▄     @ */
/* @   •██  ██▪▐█▀▄ █·▀▄.▀·▐█ ▀█ •██      ▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█•█▌▐█▀▄.▀·▀▄ █·   @ */
/* @    ▐█.▪██▀▐█▐▀▀▄ ▐▀▀▪▄▄█▀▀█  ▐█.▪    ▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌▐█▐▐▌▐▀▀▪▄▐▀▀▄    @ */
/* @    ▐█▌·██▌▐▀▐█•█▌▐█▄▄▌▐█ ▪▐▌ ▐█▌·    ▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌██▐█▌▐█▄▄▌▐█•█▌   @ */
/* @    ▀▀▀ ▀▀▀ ·.▀  ▀ ▀▀▀  ▀  ▀  ▀▀▀      ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀  ▀   @ */
/* @                                                                              @ */
/* @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */
"""
    print_cyan(banner)
    while True:
        print("\nChoose an option:")
        print("1) Track your own IP Address")
        print("2) Scan an IP Address")
        print("3) Exit")
        choice = input(">> ")

        if choice == "1":
            track_own_ip()
        elif choice == "2":
            ip = input("Enter IP Address: ")
            scan_ip(ip)
        elif choice == "3":
            print("\nExiting...")
            break
        else:
            print_red("[!] Invalid option. Try again.")

if __name__ == "__main__":
    main()
