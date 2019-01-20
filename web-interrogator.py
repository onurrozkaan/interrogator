#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tools.login_page_scanner import login_scanner
from tools.brand_logo import banner_printer
from assets.colors import *

try:

    banner_printer()

    print( yellow + "1: " + blue + "Administrator Login Page Scanner" )
    print( yellow + "2: " + blue + " " )
    print( yellow + "3: " + blue + " " )
    print( yellow + "4: " + blue + " " )
    print( yellow + "5: " + blue + " " )
    print( yellow + "6: " + blue + " " )
    print( yellow + "7: " + blue + " " )
    print("\r")
    controller = eval(input("What do you want to process ? "))

    if controller == 1:
        login_scanner()
    else:
        print(red + "Unknown choise. Please select one of the above options.")
except:
    print("Unidentified Error. Please verify the source files or check Internet Connection.")
