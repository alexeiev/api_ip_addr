#!/usr/bin/env python3
"""
Use API ipapi.co to get IP address information

How to use:
    Install library requests with:
    >pip3 install requests

Exec:
    # For information about your IP ADDRESS
    ./ip_addr.py

    # For information from another IP ADDRESS
    ./ip_addr.py IPADDRESS
"""
__version__ = "0.1"
__author__ = "Alexeiev Araújo"
__license__ = "Unlicence"

import requests
import json
import sys

if len(sys.argv) > 1:
    ip_addr = sys.argv[1]
else:
    ip_addr = None

def ip_info(ip_addr):
    if ip_addr:
        url = f"https://ipapi.co/{ip_addr}/json/"
        output = requests.get(url).json()
        msg = f"IP: {output['ip']}\nCity: {output['city']}\nRegion: {output['region']}\nCountry: {output['country_name']}"
    else:
        url = "https://ipapi.co/json/"
        output = requests.get(url).json()
        msg = f"IP: {output['ip']}\nCity: {output['city']}\nRegion: {output['region']}\nCountry: {output['country_name']}"
    return msg

try:
    print(ip_info(ip_addr))
except:
    print("[ERROR] - Wait a few minutes for a new query")