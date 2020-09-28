#!/usr/bin/env python3

"""
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
"""

with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read().splitlines()

for line in show_lldp:
    fields = line.split(":")
    if "Port id" in fields[0]:
        port_id = fields[1]
    elif "System Name" in fields[0]:
        system_name = fields[1]
        break

print()
print("Port id: {}".format(port_id))
print("System Name: {}".format(system_name))
print()
