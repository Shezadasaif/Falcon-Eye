from utils.banner import show_banner
from modules import ip_tracker

def main():
    show_banner()
    ip_tracker.track_ip()

if __name__ == "__main__":
    main()
