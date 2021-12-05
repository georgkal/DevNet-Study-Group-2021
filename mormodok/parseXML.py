import xmltodict
from pprint import pprint

my_data = open("myfile.xml").read()

xml_myfile = xmltodict.parse(my_data)
# pprint(xml_myfile)

print (xml_myfile["rpc"]["edit-config"]["default-operation"])
print (xml_myfile["rpc"]["edit-config"]["test-option"])
# print (xml_myfile["rpc"]["edit-config"]["config"])
# print (xml_myfile["rpc"]["edit-config"]["config"]["int8.1"])
