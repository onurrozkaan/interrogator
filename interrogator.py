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
import argparse

parser = argparse.ArgumentParser(description='This is a cyber security tool created by Nimda')
parser.add_argument('-f','--function', type=str, help="Avaible functions= 'catch.boss' 'catch.infoip' 'catch.igathering'")
parser.add_argument('-v','--version', type=str, const="version_controll", nargs='?', help="Version information.")


if __name__ == "__main__":
    args = parser.parse_args()

banner_printer()

if args.function == 'catch.boss':
    login_scanner()

elif args.function == 'catch.infoip':
    getOutput()

elif args.version == "version_controll":
    print("Interrogator version is currently > @0.0.10-beta")

elif args.function == 'catch.igathering':
    sys.stdout.write(red + "Enter Address Website > ")
    query_url = input()
    whois(query_url)

else:
    print("Unidentified entry. Check <--help> command to see usable arguments.")