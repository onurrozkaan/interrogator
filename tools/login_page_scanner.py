import httplib
import socket
import sys
sys.path.append('../assets/dork/')
from config import php, asp, cfm, js, cgi, brf


try:
    result_count = 0
    page_count = 0

    try:
        site = raw_input("Enter URL to scan Login page: ")
        site = site.replace("http://", "")
        print ("\tChecking website " + site + "...")
        conn = httplib.HTTPConnection(site)
        conn.connect()
        print "\t[$] Yes... Server is Online."
    except (httplib.HTTPResponse, socket.error) as Exit:
        raw_input("\t [!] Oops Error occured, Server offline or invalid URL")
        exit()
    print "Enter site source code:"
    print "1) PHP"
    print "2) ASP"
    print "3) CFM"
    print "4) JS"
    print "5) CGI"
    print "6) BRF"
    print "\nPress 1 and 'Enter key' for Select PHP\n"
    code = input("> ")

    if code == 1:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in php:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            page_count = page_count + 1
            if response.status == 200:
                result_count = result_count + 1
                print "%s %s" % ("\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                page_count = page_count
            elif response.status == 302:
                print "%s %s" % (
                    "\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (
                    host, " Interesting response:", response.status)
            connection.close()
        print("\n\n*****- Scanning is completed -***** \n")
        print result_count, " pages you have got."
        print page_count, " total page scanned"
        raw_input("[/] The Game Over; Press Enter to Exit")

    if code == 2:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in asp:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            page_count = page_count + 1
            if response.status == 200:
                result_count = result_count + 1
                print "%s %s" % ("\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning...\n")
            elif response.status == 404:
                page_count = page_count
            elif response.status == 302:
                print "%s %s" % (
                    "\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (
                    host, " Interesting response:", response.status)
            connection.close()
        print("\n\n*****- Scanning is completed -***** \n")
        print result_count, " Admin Page Found !"
        print page_count, " Total Page Scanned !"
        raw_input("Press Enter to Exit")

    if code == 3:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in cfm:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            page_count = page_count + 1
            if response.status == 200:
                result_count = result_count + 1
                print "%s %s" % ("\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                page_count = page_count
            elif response.status == 302:
                print "%s %s" % (
                    "\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (
                    host, " Interesting response:", response.status)
            connection.close()
        print("\n\n*****- Scanning is completed -***** \n")
        print result_count, " Admin Page Found !"
        print page_count, " Total Page Scanned !"
        raw_input("Press Enter to Exit")

    if code == 4:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in js:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            page_count = page_count + 1
            if response.status == 200:
                result_count = result_count + 1
                print "%s %s" % ("\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                page_count = page_count
            elif response.status == 302:
                print "%s %s" % (
                    "\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (
                    host, " Interesting response:", response.status)
            connection.close()
        print("\n\n*****- Scanning is completed -***** \n")
        print result_count, " Admin Page Found !"
        print page_count, " Total Page Scanned !"
        raw_input("Press Enter to Exit")

    if code == 5:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in cgi:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            page_count = page_count + 1
            if response.status == 200:
                result_count = result_count + 1
                print "%s %s" % ("\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                page_count = page_count
            elif response.status == 302:
                print "%s %s" % (
                    "\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (
                    host, " Interesting response:", response.status)
            connection.close()
        print("\n\n*****- Scanning is completed -***** \n")
        print result_count, " Admin Page Found !"
        print page_count, " Total Page Scanned !"
        raw_input("Press Enter to Exit")

    if code == 6:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in brf:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            page_count = page_count + 1
            if response.status == 200:
                result_count = result_count + 1
                print "%s %s" % ("\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                page_count = page_count
            elif response.status == 302:
                print "%s %s" % (
                    "\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (
                    host, " Interesting response:", response.status)
            connection.close()
        print("\n\n*****- Scanning is completed -***** \n")
        print result_count, " Admin Page Found !"
        print page_count, " Total Page Scanned !"
        raw_input("Press Enter to Exit")
except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Session Cancelled; Error Occured. Check Internet Settings."
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] Session Cancelled !"
