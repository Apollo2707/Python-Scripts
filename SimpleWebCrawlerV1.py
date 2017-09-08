import HTMLParser
import urllib
from pprint import pprint

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

   ## def handle_endtag(self, tag):
        #print ("endtag-{}".format(tag))

#Create instance of HTML parser
lParser = parseText()

thisurl = "https://en.wikipedia.org/wiki/Dictatorship"
##http://gawron.sdsu.edu/gawron2.jpg
#Feed HTML file into parser
lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
#for item in urlText:
  ##print (item)
##print urllib.urlopen(thisurl).read()
