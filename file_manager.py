import os

def file_manager_menu():
    while True:
        print("\n[1] List Files")
        print("[2] Pull File")
        print("[3] Push File")
        print("[4] Back")
        choice = input("Choose: ")

        if choice == '1':
            path = input("Enter device path (e.g. /sdcard): ")
            os.system(f"adb shell ls {path}")
        elif choice == '2':
            src = input("Enter device file path: ")
            dest = input("Enter local destination: ")
            os.system(f"adb pull {src} {dest}")
        elif choice == '3':
            src = input("Enter local file path: ")
            dest = input("Enter device destination: ")
            os.system(f"adb push {src} {dest}")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

