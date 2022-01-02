#!/usr/bin/env python3
import urllib.request, json

# A simple locator for any IP address
def Locator(ip):
    if not ip:
        return "ERROR"
    link = "https://extreme-ip-lookup.com/json/" + ip
    with urllib.request.urlopen(link) as url:
        res = json.loads(url.read().decode())
    if not res:
        return "ERROR"
    out = (res["city"], res["country"], res["continent"])
    return ", ".join(filter(None, out))


while True:
    print("Input an IP address. Press Ctrl+C to exit.")
    print(Locator(input()))
