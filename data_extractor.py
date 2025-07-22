import os

def extract_data():
    print("[*] Extracting Contacts, SMS, Call Logs...")

    os.system("adb shell content query --uri content://contacts/phones/ > contacts.txt")
    os.system("adb shell content query --uri content://sms/ > sms.txt")
    os.system("adb shell content query --uri content://call_log/calls/ > call_logs.txt")

    print("[+] Data saved as contacts.txt, sms.txt, and call_logs.txt")
