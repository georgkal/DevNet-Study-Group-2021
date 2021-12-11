import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
orig = "Varma" 
dest = "Plovdiv" 
key = "VM2iegp5adnjsJ1AREgOVwkHx6QiCP9M" 

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json() 
print(json_data) 