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

#function for polling a network device detail 'Test-9300-1'
def device_details(network_device):
    print(ise.get_device(device=network_device)['response'])
    
#function for polling the endpoint group details 'Cisco-IP-Phone'
def endpoint_group_details(endpoint_group):
    print(ise.get_endpoint_group(group=endpoint_group)['response'])

#function for populate a list of endpoint in the database
def endpoint_list():
    print(ise.get_endpoints['response'])

#function for polling the endpoint details and print out the group name '00:D6:FE:EC:12:A9'
def endpoint_details(mac):
    device = ise.get_endpoint(mac_address= mac)['response']
    print(json.dumps(device, indent = 4))
    groupid = device['groupId']
    for i in ise.get_endpoint_groups()['response']:
        groupname = i[0]
        if i[1] == groupid:
            print ("{0:22s} {1:36s}".format('Endpoint Group:', groupname))
        else:
            pass

def func_select():
    while(True):
        print("1. List Endpoint Groups")
        print("2. Endpoint Group Details")
        print("3. Endpoint Deatils")
        print("4. Network Device Details")
        print("0. EXIT(0)")
        select_input = input("SELECT => ")
        if select_input == "0":
            break
        elif select_input == "1":
            endpoint_groups()
        elif select_input == "2":
            input_val = input("Endpoint Group Name => ")
            endpoint_group_details(input_val)
        elif select_input == "3":
            input_val = input("Endpoint MAC => ")
            endpoint_details(input_val)
        elif select_input == "4":
            input_val = input("Network Device Name => ")
            device_details(input_val)
        else:
            print("input error!!!")
            continue

if __name__ == "__main__":
    func_select()
