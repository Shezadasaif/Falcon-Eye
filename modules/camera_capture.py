import os
import time

def capture_image(device_id):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    remote_path = f"/sdcard/capture_{timestamp}.jpg"
    local_path = f"captured_images/capture_{timestamp}.jpg"

    # Take picture using intent (may need user permission)
    print("[*] Attempting silent image capture (might not work without rooted device)...")
    command = f"adb -s {device_id} shell 'am start -a android.media.action.IMAGE_CAPTURE -d file://{remote_path}'"
    os.system(command)
    time.sleep(5)  # wait for capture to complete

    # Pull image to local
    os.makedirs("captured_images", exist_ok=True)
    os.system(f"adb -s {device_id} pull {remote_path} {local_path}")
    print(f"[+] Image saved to {local_path}")
