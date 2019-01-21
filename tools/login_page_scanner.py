import http.client
import socket
import sys
from assets.colors import *
from assets.dork.config import *

def login_scanner():
    try:
        result_count = 0
        page_count = 0

        try:
            message = sys.stdout.write( red + "Enter URL to scan Login page: ")
            domain = input()
            domain = domain.replace("http://", "")
            print("\r")
            print(purple + ("\t Checking website " + domain + "..."))
            conn = http.client.HTTPConnection(domain)
            conn.connect()
        except (http.client.NotConnected, socket.error) as Exit:
            print("\r")
            sys.stdout.write(red + "\t ERROR! Make sure the URL or Internet Connection correctly works.")
            input()
            exit()
        print("\r")
        print("Select one of the following technologies:")
        print("\r")
        print(blue + "1) Website based with PHP")
        print(blue + "2) Website based with ASP")
        print(blue + "3) Website based with CFM")
        print(blue + "4) Website based with JS")
        print(blue + "5) Website based with CGI")
        print(blue + "6) Website based with BRF")
        print(blue + "7) All in one (Might take long time)")
        print(blue + "8) Deep scan (Might take 'very long' time)")
        print("\r")
        code = eval(input("> "))

        if code == 1:
            print(("\t [+] Processing on " + domain))
            for admin in php:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for > " + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host,
                                     "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    page_count = page_count
                else:
                    page_count = page_count
                connection.close()
            print(yellow + "\n\n*****- Scanning is completed -***** \n")
            print(result_count, green + " Admin Page Found !")
            print("\r")
            print(green + "Count of scanned pages: ", page_count)
            print("\r")
            sys.stdout.write(red + "Press Enter to Exit")
            input()

        if code == 2:
            print(("\t [+] Processing on " + domain))
            for admin in asp:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for > " + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host,
                                     "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    page_count = page_count
                else:
                    page_count = page_count
                connection.close()
            print(yellow + "\n\n*****- Scanning is completed -***** \n")
            print(result_count, green + " Admin Page Found !")
            print("\r")
            print(green + "Count of scanned pages: ", page_count)
            print("\r")
            sys.stdout.write(red + "Press Enter to Exit")
            input()

        if code == 3:
            print(("\t [+] Processing on " + domain))
            for admin in cfm:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for > " + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host,
                                     "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    page_count = page_count
                else:
                    page_count = page_count
                connection.close()
            print(yellow + "\n\n*****- Scanning is completed -***** \n")
            print(result_count, green + " Admin Page Found !")
            print("\r")
            print(green + "Count of scanned pages: ", page_count)
            print("\r")
            sys.stdout.write(red + "Press Enter to Exit")
            input()

        if code == 4:
            print(("\t [+] Processing on " + domain))
            for admin in js:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for > " + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host,
                                     "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    page_count = page_count
                else:
                    page_count = page_count
                connection.close()
            print(yellow + "\n\n*****- Scanning is completed -***** \n")
            print(result_count, green + " Admin Page Found !")
            print("\r")
            print(green + "Count of scanned pages: ", page_count)
            print("\r")
            sys.stdout.write(red + "Press Enter to Exit")
            input()

        if code == 5:
            print(("\t [+] Processing on " + domain))
            for admin in cgi:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for > " + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host,
                                     "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    page_count = page_count
                else:
                    page_count = page_count
                connection.close()
            print(yellow + "\n\n*****- Scanning is completed -***** \n")
            print(result_count, green + " Admin Page Found !")
            print("\r")
            print(green + "Count of scanned pages: ", page_count)
            print("\r")
            sys.stdout.write(red + "Press Enter to Exit")
            input()

        if code == 6:
            print(("\t [+] Processing on " + domain))
            for admin in brf:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for > " + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host,
                                     "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    page_count = page_count
                else:
                    page_count = page_count
                connection.close()
            print(yellow + "\n\n*****- Scanning is completed -***** \n")
            print(result_count, green + " Admin Page Found !")
            print("\r")
            print(green + "Count of scanned pages: ", page_count)
            print("\r")
            sys.stdout.write(red + "Press Enter to Exit")
            input()

        if code == 7:
            print(("\t [+] Processing on " + domain))
            for admin in all_together:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for > " + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host,
                                     "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    page_count = page_count
                else:
                    page_count = page_count
                connection.close()
            print(yellow + "\n\n*****- Scanning is completed -***** \n")
            print(result_count, green + " Admin Page Found !")
            print("\r")
            print(green + "Count of scanned pages: ", page_count)
            print("\r")
            sys.stdout.write(red + "Press Enter to Exit")
            input()

        if code == 8:
            print(("\t [+] Processing on " + domain))
            for admin in big_wordlist:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for > " + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host,
                                     "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    page_count = page_count
                else:
                    page_count = page_count
                connection.close()
            print(yellow + "\n\n*****- Scanning is completed -***** \n")
            print(result_count, green + " Admin Page Found !")
            print("\r")
            print(green + "Count of scanned pages: ", page_count)
            print("\r")
            sys.stdout.write(red + "Press Enter to Exit")
            input()
        elif code > 8:
            print("\r")
            print("Unknown choise. Please select one of the above options.")
    except (KeyboardInterrupt, SystemExit):
        print(yellow + "\n\t Session goes down. See ya next time!")
