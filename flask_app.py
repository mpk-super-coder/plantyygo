from flask import Flask, render_template, request, jsonify
import json
import xmltodict
import requests
import logging
import time

#logging.basicConfig(filename='example.log', encoding='utf-8', format='%(asctime)s %(message)s')

app = Flask(__name__)

@app.route("/")
def index():
    try:
        #logging.info("User with IP",request.remote_addr,"came")
        return render_template("desktop_index.html")
    except:
        return "An error occured. Please contact plantyygo@gmail.com if you want to report this error."
    

@app.route("/plantsearch/<keyword_word>")
def plantyygo(keyword_word):
    start_time = time.time()
    api_url = "https://www.plantz.org/api/%s/1/2000/api.xml" % keyword_word
    resp = requests.get(api_url)
    #print(resp.content)
    data_dict = xmltodict.parse(resp.content)
    #print(type(data_dict))
    json_data = json.dumps(data_dict)
    #print(json_data)
    response_info = json.loads(json_data)
    #print(response_i)

    list_response = zip(str(response_info.keys()).replace('@', ''), response_info.values())
    print(list_response)

    json_response = None

    for i in list_response:
        for i in i:
            print(i)
            json_response = i
        
    jsontag_status = json_response.get("status")
    if jsontag_status["@code"]=="200":
        print(json_response.get("plant").get("id"))
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        print(user_agent)
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_lapsed)
        if "iphone" in user_agent or "android" in user_agent:
            return render_template('mobile_results.html', jsonlist = json_response.get("plant").get("id"))
        else:
            return render_template("results_backup.html", jsonlist = json_response.get("plant").get("id"), keyword = keyword_word, time_lapsed = round(time_lapsed, 2))
    elif jsontag_status["@code"]=="404":
        print("Entered keyword does not exists")
        return render_template("404.html")
    else:
        print("plantz.org returned status code",jsontag_status["@code"],"returning error page.")
        return render_template("error.html")

@app.route("/termsandconditions")
def termsandconditions():
    try:
        return render_template("termsandconditions.html")
    except:
        return "An error occured. Please contact plantyygo@gmail.com if you want to report this error."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
