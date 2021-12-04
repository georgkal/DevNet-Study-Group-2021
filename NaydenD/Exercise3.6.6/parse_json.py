import json
import yaml

with open('JSON-FILE.json','r') as json_file: 
    ourjson = json.load(json_file)

#print(ourjson)
print("\n\n---") 
print(yaml.dump(ourjson))
print("The access token is: {}".format(ourjson['access_token'])) 
print("The token expires in {} seconds.".format(ourjson['expires_in']))