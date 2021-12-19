import requests
import json

url = "http://www.mapquestapi.com/directions/v3/route?key=bl6ZWKGu8xEo1GnxKGZ9jrusCqSOQvsV&from=Sofia&to=Plovdiv"

payload={}
headers = {
  'Cookie': 'JSESSIONID=E58BA6F4D16F305906063B1E3C26B4CE'
}

response = requests.get(url=url, headers=headers)
try:
    if response.status_code == 200:
        print(response.status_code)
        json_data = response.json()
        print(json_data["route"]["legs"][0]["destNarrative"])
    elif response.status_code == 400:
        print("Failed. Error code {}".format(response.status_code))
except:
    print("Script failed")

print("End of script")






# url = "https://testdomain.domain.com"

# responce = requests.get(url=url)
# print(responce)