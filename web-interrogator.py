#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tools.page_finder.login_page_scanner import login_scanner
from tools.whois.whois_query import *
from tools.ipgeo.ipgeo import *
from assets.styling.brand_logo import banner_printer
from assets.styling.colors import *
import http.client
import requests,json
import socket
import builtwith
import sys

try:

    banner_printer()

    print( yellow + "1: " + blue + "Administrator Login Page Scanner" )
    print( yellow + "2: " + blue + "Whois database information query" )
    print( yellow + "3: " + blue + "Geographic location information via Ip Address" )
    print( yellow + "4: " + blue + " " )
    print( yellow + "5: " + blue + " " )
    print( yellow + "6: " + blue + " " )
    print( yellow + "7: " + blue + " " )
    print("\r")
    print(purple + "Which option do you want to continue with ?")
    controller = input("> ")

    if controller == "1":
        login_scanner()
    if controller == "2":
        sys.stdout.write(red + "Enter Address Website > ")
        query_url = input()
        whois(query_url)
    if controller == "3":
        getOutput()
    else:
        print(red + "Unknown choise. Please select one of the above options.")

except (http.client.NotConnected):
    print("Unidentified Error. Please verify the source files.")