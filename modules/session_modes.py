import os

def connect_manual_ip(ip_address):
    os.system(f"adb connect {ip_address}")
    print(f"[+] Connected to {ip_address}")

def list_devices():
    os.system("adb devices")

def adb_wifi_autoconnect():
    print("[*] Make sure your phone is connected via USB and ADB is enabled")
    os.system("adb tcpip 5555")
    os.system("adb shell ip route")
    ip = input("[?] Enter phone's IP address (shown above): ")
    connect_manual_ip(ip)

def qr_pairing():  # placeholder method, QR pairing needs GUI
    print("[!] QR pairing requires GUI and is not yet supported in this terminal version.")
