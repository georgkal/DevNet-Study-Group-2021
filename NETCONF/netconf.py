from ncclient import manager
from pprint import pprint as pp
import xml.dom.minidom
import xmltodict

m = manager.connect(
 host="sandbox-iosxe-latest-1.cisco.com",
 port=830,
 username="developer",
 password="C1sco12345",
 hostkey_verify=False
 )

# print("#Supported Capabilities (YANG models):")
# for capability in m.server_capabilities:
#   print(capability)

# netconf_reply = m.get_config(source="running")
# #pp(netconf_reply)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# netconf_filter = """
# <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
# </interfaces>
# """
netconf_reply = m.get_config(source="running", filter=('subtree', '<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>'))
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
# print(type(netconf_reply))
xml_dict = xmltodict.parse(netconf_reply.xml)
#pp(xml_dict)
#pp(xml_dict["rpc-reply"]["data"]["interfaces"]["interface"])
for interface in xml_dict["rpc-reply"]["data"]["interfaces"]["interface"]:
    if interface["name"] == "Loopback49":
        print("Loopback 49 was found!")
    else:
        print(interface["name"])
