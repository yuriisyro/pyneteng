#!/usr/bin/env python3

"""
Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this
file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a
separate variable.
Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the
string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.
Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then
print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.
Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have
found both of these devices, 'break' out of the for loop.
"""

with open("show_arp.txt") as f:
    show_arp = f.read().splitlines()

found1, found2 = (False, False)
show_arp = show_arp[1:]
for line in show_arp:
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    if ip_addr == "10.220.88.1":
        print("Default gateway IP/MAC: {} / {}".format(ip_addr, mac_addr))
        found1 = True
    elif ip_addr == "10.220.88.30":
        print("Arista3 IP/MAC is: {} / {}".format(ip_addr, mac_addr))
        found2 = True

    if found1 and found2:
        print("Found both values... Breaking the loop")
        break
