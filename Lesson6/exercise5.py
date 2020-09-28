#!/usr/bin/env python3

"""
Optional, use send_command() in conjunction with ntc-templates to execute a show command. Have
TextFSM automatically convert this show command output to structured data.
"""

from netmiko import Netmiko
from getpass import getpass

my_device = {
    "host": "10.10.10.10",
    "username": "admin",
    "password": getpass(),
    "device_type": "cisco_ios"
}

net_conn = Netmiko(**my_device)
output = net_conn.send_command("show ip arp", use_textfsm=True)
print(output)
