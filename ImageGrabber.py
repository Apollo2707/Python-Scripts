#Programmer: Andrew Allen Neumann
#Purpose: Pulls every image(img, png, gif, jpg) off of a website


import HTMLParser
import urllib
from pprint import pprint
import argparse

parser = argparse.ArgumentParser(description='Searches for a specified keyword through all links')
parser.add_argument('URL',
                    help='Starting webpage for Spider Search')

args = parser.parse_args()
thisurl = args.URL
ToCheckList.append(thisurl)

urlText = []

#      Define HTML Parser
class parseText(HTMLParser.HTMLParser):
        
    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[1]:
                print ("{}".format(attr))
                if attr[1].endswith((".img",".png",".gif",".jpg")) == True:
                    print ("IMAGE--{}".format(attr[1]))
                    urllib.urlretrieve("{}{}".format(thisurl[0:thisurl.rfind('/')+1],attr[1]), "{}".format(attr[1]))

lParser = parseText()
lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
