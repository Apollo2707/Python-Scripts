#Programmer: Andrew Allen Neumann
#Purpose: Pulls raw html off of a website


import urllib
from pprint import pprint
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-u", "--url", dest="url",
                  help="which url to read", metavar="url")

(options, args) = parser.parse_args()
print options.url
url = options.url
print urllib.urlopen(url).read()