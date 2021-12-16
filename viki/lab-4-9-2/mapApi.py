import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Sofia"
dest = "Plovdiv"
key = "zMuE0nifgxAlrhjTlmqUuG7GGIkmtV3n"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)
