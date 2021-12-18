# Fill in this file with the code from parsing YAML exercise
import json
import yaml
with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)
# print(ouryaml)

print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))
print("The refresh token is {}".format(ouryaml['refresh_token']))
print("The refreshtokenexpires_in after {} seconds.".format(ouryaml['refreshtokenexpires_in']))