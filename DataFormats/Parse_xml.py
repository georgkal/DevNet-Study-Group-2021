import xmltodict
from pprint import pprint

raw_data = open("XML.xml").read()

xml_data = xmltodict.parse(raw_data)
#print(type(xml_data))

print("")
#pprint(xml_data)
#pprint(xml_data["body"]["spine"])
print("====== SPINE ========")
for spine in xml_data["body"]["spine"]:
    print("Switch is: {} " .format(spine["switch"]))
    print("Switch type is: {} ".format(spine["type"]))
    print("Switch hostaname is: {} ".format(spine["hostname"]))

print("====== LEAF =========")
for leaf in xml_data["body"]["leaf"]:
    print("Switch is: {} ".format(leaf["switch"]))
    print("Switch type is: {} ".format(leaf["type"]))
    print("Switch hostaname is: {} ".format(leaf["hostname"]))
