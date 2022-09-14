import json
import xmltodict
import requests
import time

keyword_input = input("Enter the keyword: ")

def parser(keyword_api, pgno):
    api_url = "https://www.plantz.org/api/"+keyword_api+"/"+str(pgno)+"/2000/api.xml"
    resp = requests.get(api_url)
    print(resp.content)
    data_dict = xmltodict.parse(resp.content)
    #print(type(data_dict))
    json_data = json.dumps(data_dict)
    #print(json_data)
    response_info = json.loads(json_data)
    #print(response_info)

    global list_response
    list_response = zip(response_info.keys(), response_info.values())
    list_response = list(list_response)
    #print(list_response)
    time.sleep(3.5)

json_response = None

def page_getter(list_response): 
    for i in list_response:
        for i in i:
            print(i)
            json_response = i

    print(json_response.get("page"))
    page_element = json_response.get("page")

    global totalpages
    totalpages = page_element.get("@totalpages")
    print(totalpages)

def basic_crawl(list_response):
    for i in list_response:
        for i in i:
            print(i)
            json_response = i

def crawler(totalpages):
    for i in range(1, int(totalpages)+1):
        parser(keyword_input, i)
        basic_crawl(list_response)

parser(keyword_input, 1)
page_getter(list_response)
crawler(totalpages)
