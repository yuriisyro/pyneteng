#!/usr/bin/env python3

"""Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the
first and last lines of the output.
From the first line use the string .split() method to obtain the local AS number.
From the last line use the string .split() method to obtain the BGP peer IP address.
Print both local AS number and the BGP peer IP address to the screen.
"""

with open("show_ip_bgp_summ.txt") as file:
    show_bgp = file.readlines()

first_line = show_bgp[0]
last_line = show_bgp[-1]

print("AS is: {}".format(first_line.split()[-1]))
print("BGP Peer IP: {}".format(last_line.split()[0]))
