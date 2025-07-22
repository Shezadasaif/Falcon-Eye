import requests

def track_devices():
    ip = input("Enter IP address: ")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"\nIP: {res['query']}")
        print(f"Country: {res['country']}")
        print(f"Region: {res['regionName']}")
        print(f"City: {res['city']}")
        print(f"ISP: {res['isp']}")
        print(f"Location: {res['lat']}, {res['lon']}")
    except:
        print("Error: Could not fetch IP details.")


