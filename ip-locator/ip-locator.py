#!/bin/python3
import json
import urllib.request


# A simple locator for any IP address
def locate_ip(ip=""):
    link = "http://ip-api.com/json/" + ip
    with urllib.request.urlopen(link) as url:
        res = json.loads(url.read().decode())
    if not res:
        return "ERROR"
    out = (res["city"], res["country"], res["timezone"])
    return ", ".join(filter(None, out))


if __name__ == "__main__":
    print(locate_ip(""))
    while True:
        print("Input an IP address. Press Ctrl+C to exit.")
        print(locate_ip(input()))
