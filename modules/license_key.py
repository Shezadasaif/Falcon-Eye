import hashlib
import os

def get_hwid():
    if os.name == 'nt':
        return os.popen("wmic csproduct get uuid").read().split("\n")[1].strip()
    else:
        return os.popen("cat /var/lib/dbus/machine-id").read().strip()

def check_license(input_key):
    hwid = get_hwid()
    generated = hashlib.sha256(hwid.encode()).hexdigest()
    return input_key == generated

def check_license(input_key):
    # Fixed key (you can change it to anything secret)
    VALID_LICENSE_KEY = "FALCON-2025-ACCESS"
    return input_key == VALID_LICENSE_KEY

if __name__ == "__main__":
    user_input = input("🔐 Enter License Key: ")
    if check_license(user_input):
        print("✅ License Validated. Access Granted.")
    else:
        print("❌ Invalid License. Exiting...")

