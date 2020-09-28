#!/usr/bin/env python3

"""
Use send_command() to send a show command down the SSH channel. Retrieve the results and print the
results to the screen.
"""

from netmiko import Netmiko
from getpass import getpass

net_conn = Netmiko(host="10.10.10.10", username="admin", password=getpass(), device_type="cisco_ios")

command = "show arp"
output = net_conn.send_command(command)

print(output)
