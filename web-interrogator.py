#!/usr/bin/python
# -*- coding: utf-8 -*- 
from urllib2 import Request, urlopen, URLError, HTTPError

while True:
    def catchLogin(url):
        catcher = open("dork/pages.txt", "r")
        print "\n\nAvilable Links : \n"
        while True:
            data_url = catcher.readline()
            if not data_url:
                break
            request_url = "http://" + url + "/" + data_url
            request_starter = Request(request_url)
            try:
                response = urlopen(request_starter)
            except HTTPError as e:
                continue
            except URLError as e:
                break
                write(var="@", color=r, data="Please enter correct URL.")
            else:
                print("Following link might help: ", request_url