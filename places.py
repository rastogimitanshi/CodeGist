import urllib, json
from PIL import Image
import requests
from StringIO import StringIO
from io import BytesIO
def printresult(finallist):
    i=1
    for p in finallist:
        print i
        print "\n"
        print p
        print "\n"
        i=i+1
location =raw_input(" Enter the location you want to search")
print location
print"\n"

url ="https://maps.googleapis.com/maps/api/geocode/json?address="+location+"&key=YOUR_KEY"
response = urllib.urlopen(url)
jsonRaw = response.read()
jsonData = json.loads(jsonRaw)
print ("Location: "+str(jsonData['results'][0]['geometry']['location']))
val="lodging in"+location
newurl="https://maps.googleapis.com/maps/api/place/textsearch/json?query="+val+"&key=YOUR_KEY"
response1 = urllib.urlopen(newurl)
jsonRaw1 = response1.read()
jsonData1 = json.loads(jsonRaw1)
#print jsonData1
print "\n*****Names of Hotels Near "+location+"****"
print "\n"
i=0
finallist=[]
for item in jsonData1['results']:
    print ("\n  PLACE "+str(i+1))
    
    print("Name: "+jsonData1['results'][i]['name'])
    print("Address: "+jsonData1['results'][i]['formatted_address'])
    print("Rating: "+str(jsonData1['results'][i]['rating']))
    placeid=str(jsonData1['results'][i]['place_id'])
    placeurl="https://maps.googleapis.com/maps/api/place/details/json?placeid="+placeid+"&key=AIzaSyBT86SmDWPDILhXQDKJw9GM3rKiQ51QO0E"
    response2 = urllib.urlopen(placeurl)
    jsonRaw2 = response2.read()
    jsonData2 = json.loads(jsonRaw2)
    
    if('website' in jsonData2['result']):
        print ("URL : "+jsonData2['result']['website'])
        website=jsonData2['result']['website']
    else:
        print("Website :  ")
        website=" "
    if('formatted_phone_number' in jsonData2['result']):
        print ("Phone Number: "+jsonData2['result']['formatted_phone_number'])
        num=jsonData2['result']['formatted_phone_number']
    else:
        print("Phone Number :  ")
        num=" "
    dictionary ={
        "Name": jsonData1['results'][i]['name'],
        "Address": jsonData1['results'][i]['formatted_address'],
        "avg_rating": jsonData1['results'][i]['rating'],
        "place_id": jsonData1['results'][i]['place_id'],
        "website": website,
        "Phone Number": num,
        "Reviews": [],
        }
    print" \n\n\n******REVIEWS*******"
    j=0
    for item in jsonData2['result']['reviews']:
        
        print (" Review No"+str(j+1))
        print "\n"
        print ("AUTHOR: "+item['author_name'])
        print ("REVIEW: "+item['text'])
        print ("RATING: "+str(item['rating']))
        new_dictionary={
            "Author":item['author_name'],
            "Review_text":item['text'],
            "Rating": item['rating'],
            }
        dictionary["Reviews"].append(new_dictionary)
        
        #variable = item['profile_photo_url']
        #print variable
        #urllib.urlretrieve(variable, "images/image+"+str(j)+str(i)+".jpg")
        #image = Image.open(StringIO(urllib.urlopen(variable).read()))
        #image.show()
        print "\n"
        j=j+1
    i=i+1
    finallist.append(dictionary)
    print"\n"
printresult(finallist)  
