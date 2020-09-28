#!/usr/bin/env python3

"""
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and
password. The function should print out each of these three variables and clearly indicate which
variable it is printing out.
Call this ssh_conn function using entirely positional arguments.
Call this ssh_conn function using entirely named arguments.
Call this ssh_conn function using a mix of positional and named arguments.
"""

def ssh_conn(ip_addr, username, password):
    print("IP address: {}".format(ip_addr))
    print("Username: {}".format(username))
    print("Password: {}".format(password))
    return

ssh_conn("10.10.10.10", "admin", "pass")
ssh_conn(username="adm", ip_addr="11.11.11.11", password="password")
ssh_conn("12.12.12.12", "juniper", password="secret")
