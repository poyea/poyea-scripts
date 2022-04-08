#!/bin/python3
import json
import urllib.request


# A simple locator for any IP address
def Locator(ip):
    if not ip:
        return "ERROR"
    link = "http://ip-api.com/json/" + ip
    with urllib.request.urlopen(link) as url:
        res = json.loads(url.read().decode())
    if not res:
        return "ERROR"
    out = (res["city"], res["country"], res["timezone"])
    return ", ".join(filter(None, out))


while True:
    print("Input an IP address. Press Ctrl+C to exit.")
    print(Locator(input()))
