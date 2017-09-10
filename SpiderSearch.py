#Programmer: Andrew Allen Neumann
#Purpose: This web crawler will pursue links while looking for any refernce to hitler in the text. 

import HTMLParser
import urllib
import argparse
from pprint import pprint

CheckedList = []
ToCheckList = []
#Argument Parser
parser = argparse.ArgumentParser(description='Searches for a specified keyword through all links')
parser.add_argument('URL',
                    help='Starting webpage for Spider Search')
parser.add_argument('Phrase', 
                    help='Key phrase to search for')
args = parser.parse_args()
thisurl = args.URL
SearchValue = args.Phrase
ToCheckList.append(thisurl)

#      Define HTML Parser
class parseLink(HTMLParser.HTMLParser):
    rootURL = ""
    Search = False
    def handle_data(self, data):
        #print "DATA Handle"
        #print data.lower
        if SearchValue in data.lower():
            self.Search = True
            #print "!!!!!!!!!!!!!!!!!!!""
            #urlText.append(data)

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            #print attr
            if  not attr[0] or not attr[1]:
                pass
            elif attr[1].startswith("http"):
                NewToCheckList.append(attr[1])
                #print "iftrue"
            elif "href"  in attr[0] or "content" in attr[0]:
                #print "iffalse"
                if attr[1].startswith("http") or attr[1].startswith("www."): 
                     NewToCheckList.append(attr[1])
                elif attr[1].startswith("/") and not attr[1].startswith("//"):
                    NewToCheckList.append(self.rootURL + attr[1])

Counter = 1
while Counter < 10:
    print ("Wave {}".format(Counter))
    Counter += 1
    NewToCheckList = []

    for link in ToCheckList:
        try:
            lParser = parseLink()
            lParser.rootURL = link[0:link[8:len(link)].find("/")+8]
            lParser.feed(urllib.urlopen(link).read())
            if lParser.Search:
                print "[!]{0} at {1}".format(SearchValue,link)
                print "[!] Found on Wave {}".format(Counter)
                Counter = 11
                break
            lParser.close()
            print ("[%] Checked {}".format(link))
        except:
            pass
            print ("[?] Invalid {}".format(link))
        CheckedList.append(link)

    ToCheckList = []

    for item in NewToCheckList:
        if item in CheckedList:
            pass 
        elif item in ToCheckList:
            pass
        else:
            ToCheckList.append(item)

    NewToCheckList = []
    

    
