import sys
import json
from ise import ERS

#ise_config is a file to store the ISE's address and credentials for API
from ise_config import ISE_NODE, USER, PASSWORD
ise = ERS(ise_node=ISE_NODE, ers_user=USER, ers_pass=PASSWORD, verify=False, disable_warnings=True)

#function for polling the Group and UUID
def endpoint_groups():
    print ("{0:22s} {1:36s}".format("EndpointGroup", "UUID"))
    for i in ise.get_endpoint_groups()['response']:
        groupname = i[0]
        uuid = i[1]
        print ("{0:22s} {1:36s}".format(groupname, uuid))

#function for polling a network device detail
def device_details():
    print(ise.get_device(device='Test-9300-1')['response'])
    
#function for polling the endpoint group details
def endpoint_group_details():
    print(ise.get_endpoint_group(group='Cisco-IP-Phone')['response'])

#function for populate a list of endpoint in the database
def endpoint_list():
    print(ise.get_endpoints['response'])

#function for polling the endpoint details and print out the group name
def endpoint_details():
    device = ise.get_endpoint(mac_address='00:D6:FE:EC:12:A9')['response']
    print(json.dumps(device, indent = 4))
    groupid = device['groupId']
    for i in ise.get_endpoint_groups()['response']:
        groupname = i[0]
        if i[1] == groupid:
            print ("{0:22s} {1:36s}".format('Endpoint Group:', groupname))
        else:
            pass
if __name__ == "__main__":
    endpoint_details()
