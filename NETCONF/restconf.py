import requests
import json

host = "sandbox-iosxe-recomm-1.cisco.com"
url = "https://{}/restconf/data/ietf-interfaces:interfaces".format(host)

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

responce = requests.get(url=url, headers=headers, verify=False)
json_data = responce.json()

#print(json_data['ietf-interfaces:interfaces']['interface'])
for interface in json_data['ietf-interfaces:interfaces']['interface']:
  url = "https://{}/restconf/data/ietf-interfaces:interfaces-state/interface={}/statistics/out-errors".format(host, interface["name"])
  out_errors = requests.get(url=url, headers=headers, verify=False)
  errors_json = out_errors.json()
  print("Interface: {} Out-Errors: {}".format(interface["name"], errors_json['ietf-interfaces:out-errors']))