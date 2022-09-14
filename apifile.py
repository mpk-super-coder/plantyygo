import requests
import xml.etree.ElementTree as ET
import time
#import feedparser
import os
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

if os.path.exists("plantzorg_api.xml"):
  os.remove("plantzorg_api.xml")
  logging.info("plantzord_api.xml file removed")
else:
  print("The file does not exist") 
  logging.info("plantzord_api.xml file does not exist")
keyword_input = input("Enter the keyword: ")
logging.info("User entered", keyword_input)
api_url = "https://www.plantz.org/api/"+keyword_input+"/1/2000/api.xml"
resp = requests.get(api_url)
with open('plantzorg_api.xml', 'wb') as f:
    f.write(resp.content)
    logging.info("Wrote XML file", keyword_input)

tree = ET.parse("plantzorg_api.xml")
root = tree.getroot()
print(root.tag)
print(root[0].tag)
print(root[1].attrib)
attribpage = root[1].attrib
attribtotalpages = attribpage['totalpages']
print(attribtotalpages)

for i in range(1, int(attribtotalpages)):
    api_url = "https://www.plantz.org/api/"+keyword_input+"/"+str(i)+"/1000/api.xml"
    resp = requests.get(api_url)
    with open('plantzorg_api.xml', 'wb') as f:
        f.write(resp.content)
    api_url = None
    tree = ET.parse("plantzorg_api.xml")
    theroot = tree.getroot()
    print(theroot)
    print("On page", i)
    for x in root.findall('plant'):
        apiid = x.find('id')
        print(apiid )
        apiattrib = apiid.attrib
        scientific = apiattrib['scientific']
        print(scientific)
    time.sleep(2)