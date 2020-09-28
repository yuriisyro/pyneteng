#!/usr/bin/env python3
"""
Optional, connect to three networking devices one after the other. Use send_command() to execute a
show command on each of these devices. Print this output to the screen.
"""

from netmiko import Netmiko
from getpass import getpass

password = getpass()

cisco1 = {
    "host": "10.10.10.10",
    "username": "admin",
    "password": password,
    "device_type": "cisco_ios"
}

arista1 = {
    "host": "10.20.20.1",
    "username": "admin",
    "password": password,
    "device_type": "arista_eos"
}

juniper1 = {
    "host": "10.30.10.11",
    "username": "admin",
    "password": password,
    "device_type": "juniper_junos"
}

for device in (cisco1, arista1, juniper1):
    net_conn = Netmiko(**device)
    output = net_conn.send_command("show arp")
    print(output)
