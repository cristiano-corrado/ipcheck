import re ,os
import requests
from optparse import OptionParser, OptionGroup
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

url = "https://www.iplocation.net/"

def parseHtml(response):
    test = []
    soup = BeautifulSoup(response, "lxml")
    parsetable = soup.find_all("table",{"class":"table_dark_green"})
    for details in parsetable[1].find_all("tr"):
        cols = details.find_all('td')

        cols = [ x.text.strip() for x in cols ]
        if not len(cols) < 1:
            for elems in cols:
                test.append(elems)
    return test

def makereqIpLocation(ip):

    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Origin' : 'https://www.iplocation.net',
        'Referer' : 'https://www.iplocation.net/',
        'Upgrade-Insecure-Requests': '1'
    }

    data = {
        'query':ip,
        'submit':'IP+Lookup'
    }

    getres = requests.post(url,data=data,headers=headers,verify=False)
    if getres.status_code == 200 :
        return parseHtml(getres.text)


def parseData(data):
    if os.path.isfile(data):
        with open(data,'r') as ipfile:
            return ipfile.readlines()
    else:
        return [data]

def main():

    parser = OptionParser()
    opt = OptionGroup(parser, "Script to request information regarding an ip address Eg: citi/comapany/org/asnumber."
                              "usage: %prog -f iplist.txt")
    opt.add_option("-f", "--file", dest="filename", action="store_true", help="pass a list of ips from file, NOTE: IPs must be specified 1 by line.")
    opt.add_option("-i","--ip",dest="ip", action="store_true", help="Pass an ip from cli")

    parser.add_option_group(opt)

    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error("incorrect number of arguments")

    if ( options.filename and options.ip ):
        parser.error("you can only specify either of the two options")

    args = args[0]

    for elem in parseData(args):
        print(makereqIpLocation(elem))


if __name__ == "__main__":
    main()
