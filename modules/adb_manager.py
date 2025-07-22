# modules/adb_manager.py
import os

def adb_menu():
    print("\n[1] Show Connected Devices")
    print("[2] Connect Device via IP")
    print("[3] Install APK")
    print("[4] Uninstall APK")
    print("[5] Pull File")
    print("[6] Push File")
    print("[7] Screen Mirror (scrcpy)")

    choice = input("Choose an option: ")

    if choice == '1':
        os.system("adb devices")
    elif choice == '2':
        ip = input("Enter device IP: ")
        os.system(f"adb connect {ip}")
    elif choice == '3':
        apk = input("Path to APK: ")
        os.system(f"adb install {apk}")
    elif choice == '4':
        package = input("Enter package name: ")
        os.system(f"adb uninstall {package}")
    elif choice == '5':
        src = input("Remote file path: ")
        dest = input("Destination path: ")
        os.system(f"adb pull {src} {dest}")
    elif choice == '6':
        src = input("Local file path: ")
        dest = input("Remote path: ")
        os.system(f"adb push {src} {dest}")
    elif choice == '7':
        os.system("scrcpy")
    else:
        print("Invalid option.")

