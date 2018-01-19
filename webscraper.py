import urllib2
from bs4 import BeautifulSoup
import json

with open("ThisCatList.txt",'r') as x:
    lines = [ ["http://web.sachamber.org" + z.strip(), z[1:]] for z in x.readlines()] 

allEntries = []
total = 0
for line in lines:
    total += 1
    print ""
    print ""
    print "{:2}/{:2} - {}".format(total,len(lines),line[0])
    print "-----"
    #get page
    soup = BeautifulSoup(urllib2.urlopen(line[0]),'html.parser')
    #collect all divs
    divs = soup.find_all("div",{"class": "ListingResults_All_CONTAINER"})

    if len(divs) == 0:
        for x in range(0,6):
            divs = divs + soup.find_all("div",{"class": "ListingDetails_Level"+str(x)+"_HEADERBOX"})

    if len(divs) == 0:
        print "This should not happen, check page" ## No entry at all was pulled
    #record data of every div
    for div in divs:
        #print div
        entry = {}
        entry["Catagory"] = line[1]
        items = ["street-address", "postal-code","locality","region","name", "url"]

        ##Pull all applicable data
        for x in items:
            #print "finding "+ x 
            data = div.find(itemprop = x)
            entry[x] =  data.get_text().strip() if data  else ""

        ##URL is alittle harder sometimes
        if entry["url"] == "":
            data = div.find('a',href=True,text='Visit Site')
            entry['url'] = data['href'].strip() if data else ""
        #DEBUG print all data pulled
        #print entry    
        
        # add to list
        allEntries += entry

allEntries.sort(key=lambda x: x.name, reverse=True)
#write to file
#dulicates checking
print "LENGTH BEFORE checking "+ len(allEntries)

d = {}
for obj in allEntries:
    d[obj.name] = obj
allEntries = d.values()

print "LENGTH AFTER checking "+ len(allEntries)

with open("outputfile.txt","w+") as out:
    json.dump(allEntries,out)
    print "\n\n File created Done!"
    print "total entries == " + len(allEntries)

    
    