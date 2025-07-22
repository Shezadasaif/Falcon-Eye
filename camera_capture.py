import os

def capture_image():
    print("[*] Capturing image from target device...")
    os.system("adb shell 'input keyevent 27'")  # Simulate camera shutter
    os.system("adb shell screencap -p /sdcard/captured_image.png")
    os.system("adb pull /sdcard/captured_image.png")
    print("[+] Image saved as captured_image.png")
