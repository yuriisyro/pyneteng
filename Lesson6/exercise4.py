#!/usr/bin/env python3

"""
Use send_config_set() and send_config_from_file() to make configuration changes.
The configuration changes should be benign. For example, on Cisco IOS I typically change the
logging buffer size.
As part of your program verify that the configuration change occurred properly. For example, use
send_command() to execute 'show run' and verify the new configuration.
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
command_logging = "show conf | inc logging"

show_log = net_conn.send_command(command_logging)
print(show_log)

config_update = net_conn.send_config_set("logging buffered 10000")
print(config_update)

config_from_file = net_conn.send_config_from_file("config.txt")
print(config_from_file)

print(show_log)
