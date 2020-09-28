#!/usr/bin/env python3

"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.
Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.
Using a for-loop iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""

net_dev = {
    "ip_addr": "10.10.10.10",
    "vendor": "cisco",
    "username": "admin",
    "password": "password"
}

print()
print(net_dev["ip_addr"])
print()

if net_dev["vendor"].lower() == "cisco":
    net_dev["platform"] = "ios"
if net_dev["vendor"].lower() == "juniper":
    net_dev["platform"] = "junos"

bgp_fields = {
    "bgp_as": "",
    "peer_as": "",
    "peer_ip": ""
}

net_dev.update(bgp_fields)

for k in net_dev.keys():
    print("-" * 20)
    print("{:^15}".format(k))
    print("-" * 20)

for k, v in net_dev.items():
    print("-" * 40)
    print("{:15} = {:15}".format(k, v))
    print("-" * 40)
