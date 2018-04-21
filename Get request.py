import json
import requests
import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

url = "https://api.microshare.io/share/uk.reading.ttn.sodaq.Isaac"

querystring = {"details":"true","page":"","perPage":""}

headers = {
    'Authorization': "Bearer 45d6c3e96c5024df48795657cbff76d0c6f1afbb54e8e95c9ada1f7c22053a93",
    'Cache-Control': "no-cache",
    'Postman-Token': "849bdf64-160c-4e41-81a5-54e272f93882"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
x = 0
jsonData = data["objs"]
for item in jsonData:
    name = item["data"]
    isaac = name["payload_fields"]
    bob = isaac.get("temperature_3")
    time = item["data"]
    time = time["metadata"]
    time = time.get("time")
    timelist = time.split("T")
    timelist = timelist[1].split(".")
    sheet1.write(x,0,timelist[0])
    sheet1.write(x,1,bob)

    
    print(bob)
    x = x + 1
book.save("trial.xls")

