#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tools.login_page_scanner import login_scanner

try:

    print("1: Administrator Login Page Scanner")
    print("2: ...")
    print("3: ...")
    print("4: ...")
    print("5: ...")
    controller = eval(input("What do you want to process ? "))

    if controller == 1:
        login_scanner()
    else:
        print("Some alert will appear here.")
except:
    print("Some alert will appear here.")
