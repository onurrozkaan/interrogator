
import urllib.request
import sys
import json
from assets.styling.colors import *

def getOutput():
    print(purple + "Enter the Target IP:")
    sys.stdout.write(green + "> ")
    ip_input = input()

    with urllib.request.urlopen("http://ip-api.com/json/" + ip_input) as url:

        def is_input_ip(checker_value):
            data = checker_value.split('.')
            if len(data) != 4:
                return False
            for x in data:
                if not x.isdigit():
                    return False
                i = int(x)
                if i < 0 or i > 255:
                    return False
            return True
        
        if is_input_ip(ip_input) == True:
            
            data = url.read().decode()
            output = data.strip('"').split(",")
            print("\r")

            for value in output:

                print(red + "-->  " + value.replace('"', "").replace("}", "").replace("{", "").replace("as:", yellow + "AS: "+ green).replace("city:", yellow + "CITY: "+ green).replace("country:", yellow + "COUNTRY: " + green).replace("isp:", yellow + "ISP: " +green ).replace("lat:", yellow + "LAT: " +green ).replace("countryCode:", yellow + "COUNTRY CODE: " +green ).replace(
                    "lon:", yellow + "LON: " +green ).replace("org:", yellow + "ORG: " +green ).replace("query:", yellow + "QUERY: " +green ).replace("region:", yellow + "REGION: " +green ).replace("regionName:", yellow + "REGION NAME: " +green ).replace("status:", yellow + "STATUS: " +green ).replace("timezone:", yellow + "TIMEZONE: " +green ).replace("zip:", yellow + "ZIP: " +green ))

        else:
            print("\r")
            print(red + "Value looks like not an Ip Address, please enter a correct Ip Address.")