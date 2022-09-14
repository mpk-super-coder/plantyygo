import json
import xmltodict
import requests

keyword_input = input("Enter the keyword: ")

api_url = "https://www.plantz.org/api/"+keyword_input+"/1/2000/api.xml"
resp = requests.get(api_url)
#print(resp.content)
data_dict = xmltodict.parse(resp.content)
#print(type(data_dict))
json_data = json.dumps(data_dict)
#print(json_data)
response_info = json.loads(json_data)
#print(response_i)

list_response = zip(response_info.keys(), response_info.values())
list_response = list(list_response)
#print(list_response)

json_response = None

for i in list_response:
    for i in i:
        print(i)
        json_response = i

print(json_response.get("plant").get("id"))

for i in json_response.get("plant").get("id"):
    print(i)
    scientific = i["@scientific"]
    common = i["@common"]
    family = i["@family"]
    print(scientific, common, family)