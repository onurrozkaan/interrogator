#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tools.page_finder.login_page_scanner import login_scanner
from tools.whois.whois_query import *
from assets.styling.brand_logo import banner_printer
from assets.styling.colors import *
import http.client
import requests,json
import os
import socket
import builtwith

try:

    os.system('clear')
    banner_printer()

    print( yellow + "1: " + blue + "Administrator Login Page Scanner" )
    print( yellow + "2: " + blue + "Whois database information query " )
    print( yellow + "3: " + blue + " " )
    print( yellow + "4: " + blue + " " )
    print( yellow + "5: " + blue + " " )
    print( yellow + "6: " + blue + " " )
    print( yellow + "7: " + blue + " " )
    print("\r")
    controller = eval(input("What do you want to process ? "))

    if controller == 1:
        login_scanner()
    if controller == 2:
        m = input("Enter Address Website = ")
        whois(m)
    else:
        print(red + "Unknown choise. Please select one of the above options.")

except (http.client.NotConnected):
    print("Unidentified Error. Please verify the source files.")