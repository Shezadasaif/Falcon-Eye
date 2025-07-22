def file_menu():
    print("""
[1] Pull File
[2] Push File
[3] Install APK
[4] Uninstall APK
""")
    choice = input("Choose: ")
    if choice == "1":
        remote = input("Remote path: ")
        local = input("Local path: ")
        pull_file(remote, local)
    elif choice == "2":
        local = input("Local path: ")
        remote = input("Remote path: ")
        push_file(local, remote)
    elif choice == "3":
        apk = input("APK path: ")
        install_apk(apk)
    elif choice == "4":
        pkg = input("Package name: ")
        uninstall_apk(pkg)
