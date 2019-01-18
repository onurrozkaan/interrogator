import http.client
import socket
import sys
from assets.dork.config import php, asp, cfm, js, cgi, brf

def login_scanner():
    try:
        result_count = 0
        page_count = 0

        try:
            domain = input("Enter URL to scan Login page: ")
            domain = domain.replace("http://", "")
            print(("\tChecking website " + domain + "..."))
            conn = http.client.HTTPConnection(domain)
            conn.connect()
            print("\t[$] Yes... Server is Online.")
        except (http.client.HTTPResponse, socket.error) as Exit:
            input("\t [!] Oops Error occured, Server offline or invalid URL")
            exit()
        print("Enter domain source code:")
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
                print(("\t [#] Checking " + host + "..."))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "Admin page found!"))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "Possible admin page (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " pages you have got.")
            print(page_count, " total page scanned")
            input("[/] Please press Enter to Exit")

        if code == 2:
            print(("\t [+] Processing on " + domain))
            for admin in asp:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Checking " + host + "..."))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "Admin page found!"))
                    input("Press enter to continue scanning...\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "Possible admin page (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Page Found !")
            print(page_count, " Total Page Scanned !")
            input("Press Enter to Exit")

        if code == 3:
            print(("\t [+] Processing on " + domain))
            for admin in cfm:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Checking " + host + "..."))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "Admin page found!"))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "Possible admin page (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Page Found !")
            print(page_count, " Total Page Scanned !")
            input("Press Enter to Exit")

        if code == 4:
            print(("\t [+] Processing on " + domain))
            for admin in js:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Checking " + host + "..."))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "Admin page found!"))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "Possible admin page (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Page Found !")
            print(page_count, " Total Page Scanned !")
            input("Press Enter to Exit")

        if code == 5:
            print(("\t [+] Processing on " + domain))
            for admin in cgi:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Checking " + host + "..."))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "Admin page found!"))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "Possible admin page (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Page Found !")
            print(page_count, " Total Page Scanned !")
            input("Press Enter to Exit")

        if code == 6:
            print(("\t [+] Processing on " + domain))
            for admin in brf:
                admin = admin.replace("\n", "")
                admin = "/" + admin
                host = domain + admin
                print(("\t [#] Checking " + host + "..."))
                connection = http.client.HTTPConnection(domain)
                connection.request("GET", admin)
                response = connection.getresponse()
                page_count = page_count + 1
                if response.status == 200:
                    result_count = result_count + 1
                    print("%s %s" % ("\n\n>>>" + host, "Admin page found!"))
                    input("Press enter to continue scanning.\n")
                elif response.status == 404:
                    page_count = page_count
                elif response.status == 302:
                    print("%s %s" % (
                        "\n>>>" + host, "Possible admin page (302 - Redirect)"))
                else:
                    print("%s %s %s" % (
                        host, " Interesting response:", response.status))
                connection.close()
            print("\n\n*****- Scanning is completed -***** \n")
            print(result_count, " Admin Page Found !")
            print(page_count, " Total Page Scanned !")
            input("Press Enter to Exit")
    except (http.client.HTTPResponse, socket.error):
        print("\n\t[!] Session Cancelled; Error Occured. Check Internet Settings.")
    except (KeyboardInterrupt, SystemExit):
        print("\n\t[!] Session Cancelled !")
