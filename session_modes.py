def session_menu():
    print("""
[1] Manual IP Connect
[2] QR Pairing (WIP)
[3] WiFi Auto-Connect
""")
    choice = input("Choose: ")
    if choice == "1":
        ip = input("Enter IP: ")
        os.system(f"adb connect {ip}")
    elif choice == "2":
        print("[!] QR Pairing feature under development.")
    elif choice == "3":
        os.system("adb devices")  # or auto scan & connect
