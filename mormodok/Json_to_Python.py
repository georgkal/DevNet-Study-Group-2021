import requests
import json 

url = "http://www.mapquestapi.com/directions/v2/route?key=FmBfPBACT5cedyXhmGMv5u9UOdkzw21m&from=Orpington&to=London"

payload={}
headers = {
  'Cookie': 'JSESSIONID=55DFB1BF7AA183B04457D04B1CD97006'
}

response = requests.get(url = url, headers=headers).json()

# # print(response["route"]["narrative"])
# print(response["route"]["streets"][2])
print(response["route"]["legs"][0]["formattedTime"],"TIME TO GO")
print(response["route"]["legs"][0]["maneuvers"][0]["narrative"])
print(response["route"]["legs"][0]["maneuvers"][0]["distance"],"km")
print(response["route"]["legs"][0]["maneuvers"][0]["streets"][0])
print(response["route"]["legs"][0]["maneuvers"][0]["directionName"])
print(response["route"]["legs"][0]["maneuvers"][1]["distance"],"km")
print(response["route"]["legs"][0]["maneuvers"][0]["streets"][1])
print(response["route"]["legs"][0]["maneuvers"][1]["directionName"])
print(response["route"]["legs"][0]["maneuvers"][2]["narrative"])
print(response["route"]["legs"][0]["maneuvers"][2]["distance"],"km")
print(response["route"]["legs"][0]["maneuvers"][2]["directionName"])
print(response["route"]["legs"][0]["maneuvers"][3]["narrative"])
print(response["route"]["legs"][0]["maneuvers"][3]["distance"],"km")
print(response["route"]["legs"][0]["maneuvers"][3]["directionName"])
print(response["route"]["legs"][0]["maneuvers"][4]["narrative"])
print(response["route"]["legs"][0]["maneuvers"][4]["distance"],"km")
print(response["route"]["legs"][0]["maneuvers"][5]["narrative"])
print(response["route"]["legs"][0]["maneuvers"][5]["distance"], "km")
print(response["route"]["legs"][0]["maneuvers"][6]["narrative"])
print(response["route"]["legs"][0]["maneuvers"][6]["distance"],"km")
print(response["route"]["legs"][0]["maneuvers"][7]["narrative"])
print(response["route"]["legs"][0]["maneuvers"][7]["distance"],"km")
print(response["route"]["legs"][0]["maneuvers"][8]["narrative"])
print(response["route"]["legs"][0]["maneuvers"][8]["distance"],"km") 
# print (response ["route"]["sessionId"])
# print (response ["distance"]["narrative"]["lng"])
# print(response["route"]["fuelUsed"])
# print(response["route"]["legs"][0]["index"])