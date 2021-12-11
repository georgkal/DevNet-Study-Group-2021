import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "zMuE0nifgxAlrhjTlmqUuG7GGIkmtV3n"

#orig = "Sofia"
#dest = "Plovdiv"
while True:
    orig = input("Starting Location (or type 'quit' to exit): ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination (or type 'quit' to exit): ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")


