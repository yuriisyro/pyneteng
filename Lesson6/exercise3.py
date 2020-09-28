#!/usr/bin/env python3

"""
Find a command on your device that has additional prompting. Use send_command_timing to send the
command down the SSH channel. Capture the output and handle the additional prompting.
"""

from netmiko import Netmiko
from getpass import getpass

device = {
    'host': '10.10.10.10',
    'username': 'admin',
    'password': getpass(),
    'device_type': 'cisco_ios'
}

net_conn = Netmiko(**device)

filename = "log.txt"
cmd = "delete flash:{}".format(filename)
print(cmd)
output = net_conn.send_command_timing(cmd)

if 'confirm' in output:
    output += net_conn.send_command_timing("\n")
else:
    raise ValueError("No confirm message in output")

print(output)
