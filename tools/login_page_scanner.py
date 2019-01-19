import http.client
import socket
import sys
from assets.colors import *
from assets.dork.config import php, asp, cfm, js, cgi, brf

def login_scanner():
    try:
        result_count = 0
        page_count = 0

        try:
            message = sys.stdout.write(red+"Enter URL to scan Login page: ")
            domain = input()
            domain = domain.replace("http://", "")
            print(("\tChecking website " + domain + "..."))
            conn = http.client.HTTPConnection(domain)
            conn.connect()
        except (http.client.HTTPResponse, socket.error) as Exit:
            input("\t ERROR! Make sure the URL which you typed is correct.")
            exit()
        print("Select one of the following languages:")
        print("1) Website based with PHP")
        print("2) Website based with ASP")
        print("3) Website based with CFM")
        print("4) Website based with JS")
        print("5) Website based with CGI")
        print("6) Website based with BRF")
        code = eval(input("> "))

        if code == 1:
            print(("\t [+] Processing on " + domain))
            for admin in php:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for" + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "There would be something interesting (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Page Found !")
            print(page_count, " count of scanned pages")
            input("Press Enter to Exit")

        if code == 2:
            print(("\t [+] Processing on " + domain))
            for admin in asp:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for" + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "1 page detected, might be admin page."))
                    input("Press enter to continue scanning...\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "There would be something interesting (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Login Page Found !")
            print(page_count, " count of scanned pages")
            input("Press Enter to Exit")

        if code == 3:
            print(("\t [+] Processing on " + domain))
            for admin in cfm:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for" + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "There would be something interesting (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Login Page Found !")
            print(page_count, " count of scanned pages")
            input("Press Enter to Exit")

        if code == 4:
            print(("\t [+] Processing on " + domain))
            for admin in js:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for" + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "There would be something interesting (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Login Page Found !")
            print(page_count, " count of scanned pages")
            input("Press Enter to Exit")

        if code == 5:
            print(("\t [+] Processing on " + domain))
            for admin in cgi:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for" + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "There would be something interesting (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Login Page Found !")
            print(page_count, " count of scanned pages")
            input("Press Enter to Exit")

        if code == 6:
            print(("\t [+] Processing on " + domain))
            for admin in brf:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Loading for" + host))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "1 page detected, might be admin page."))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "There would be something interesting (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Login Page Found !")
            print(page_count, " count of scanned pages")
            input("Press Enter to Exit")
    except (http.client.HTTPResponse, socket.error):
        print("\n\t Scanning stopped, Make sure you have your connection online.")
    except (KeyboardInterrupt, SystemExit):
        print("\n\t Session stopped.")
