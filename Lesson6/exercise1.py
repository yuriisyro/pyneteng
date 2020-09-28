#!/usr/bin/env python3

"""Establish a connection to the network device and print out the device's prompt."""

from netmiko import Netmiko
from getpass import getpass

net_conn = Netmiko(host="10.10.10.10", username="admin", password=getpass(), device_type="cisco_ios")

print(net_conn.find_prompt())
