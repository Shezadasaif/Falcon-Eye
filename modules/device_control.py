def control_device():
    print("\n[1] Vibrate Device")
    print("[2] Take Screenshot (via ADB)")
    print("[3] Back")

    choice = input("Choose: ")

    if choice == '1':
        print("Command: adb shell cmd vibrator vibrate 1000")
        print("Run this manually on rooted device.")
    elif choice == '2':
        print("Taking screenshot...")
        print("Command: adb shell screencap -p /sdcard/screen.png && adb pull /sdcard/screen.png .")
    elif choice == '3':
        return
    else:
        print("Invalid option.")
