#!/usr/bin/env python3

"""
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with
a default value of 'cisco_ios'. Print all four of the function variables out as part of the
function's execution.
Call the 'ssh_conn2' function both with and without specifying the device_type
Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using
the **kwargs technique.
"""

def ssh_conn2(ip_addr, username, password, device_type="cisco_ios"):
    print()
    print("IP address: {}".format(ip_addr))
    print("Username: {}".format(username))
    print("Password: {}".format(password))
    print("Device Type: {}".format(device_type))
    print("-" * 50)
    return

ssh_conn2("10.10.10.10", "admin", "cisco", "junos")
ssh_conn2("11.11.11.11", "admin", "pass123")

dict_param = {
    "ip_addr": "10.11.12.13",
    "username": "admin",
    "password": "secret",
    "device_type": "junos"
}

ssh_conn2(**dict_param)
