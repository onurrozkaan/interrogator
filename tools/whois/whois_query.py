from assets.styling.colors import *
import requests
import re

class okayX:
    x = " "

_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

empty_Website = "Url, which you enter is not valid. ".format(red=red, blue=blue)

wrong_URL = "URL DOESNT EXIST! PLEASE TRY AGAIN.".format(red=red)

str_Index = "Enter a Integer Value: ".format(red=red)

val_Select = "Please Use The Index Value From The List Not By Your Own: "

def webNotEmpty(website):
    
    if len(website) >= 1:
        return "valid"
    else:
        return "!valid"

def validWebsite(website):

    web = webNotEmpty(website)
    if web is "valid":
        if not (re.match(r"(^(http://|https://)?([a-z0-9][a-z0-9-]*\.)+[a-z0-9][a-z0-9-]*$)", website)):
            exit(wrong_URL)
    else:
        exit(empty_Website)

def cleanURL(website):

    web = validWebsite(website)
    website = website.replace("http://", "")
    website = website.replace("http://www.", "")
    website = website.replace("https://", "")
    website = website.replace("https://www.", "")
    website = website.replace("www.", ""); return(website)

def removeHTTP(website):

    website = cleanURL(website); return(website)

def addHTTP(website):

    website = cleanURL(website)
    website = ("http://" + website); return(website)

def write(var, color, data):
    if var == None:
        print(color + str(data))
    elif var != None:
        print(red + var + white  + color + str(data))

def Request(website, _timeout=None, _encode=None):

    try:
        if _encode == None:
            return requests.get(website, headers=_headers, timeout=_timeout).content
        elif _encode == True:
            return requests.get(website, headers=_headers, timeout=_timeout).text.encode('utf-8')
    except requests.exceptions.MissingSchema:
        pass
    except requests.exceptions.ContentDecodingError:
        pass
    except requests.exceptions.ConnectionError:
        return "  WARNING: Check your connection or the url which you typed is correctly works."
        pass
    except Exception as e:
        return "Error: " + str(e)
        pass
def whois(website):
        website = addHTTP(website)
        webs = removeHTTP(website)
        url = "http://api.hackertarget.com/whois/?q="
        combo ="{url}{website}".format(url=url, website=webs)
        request = requests.get(combo, headers=_headers, timeout=5).text.encode('UTF-8')
        try:
            if len(request) != 5:
                list = request.decode().strip("").split("\n")[:-10]

                for _links in list:
                    if len(_links) != 0:
                        write(var="-->", color=yellow, data=_links)
        except:
            print(red + "ERROR! " + green + "Please try Again")