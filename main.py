import requests
from sys import argv, exit
from init import banner

banner()
try:
    url = argv[1]
except:
    print("Usage : python3 main.py <ip or domain>")
    exit()

API = "https://api.shrtco.de/v2/shorten?url="
req = requests.get(f"{API}{url}")
urls = req.json()
x = urls["result"]["full_short_link"]
x2 = urls["result"]["full_short_link2"]
x3 = urls["result"]["full_short_link3"]
shape = '\033[34m' + "[" +  '\033[91m' + "+" + '\033[34m' + "]"

print(f"{shape} "+"\033[32m" + f"{x}"  +" --->> " + '\033[91m'+f"{url}")
print(f"{shape} "+"\033[32m" + f"{x2}" + " --->> " + '\033[91m' + f"{url}")
print(f"{shape} "+"\033[32m" + f"{x3}" + " --->> " + '\033[91m' + f"{url}")

