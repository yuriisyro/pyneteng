#!/usr/bin/env python3

"""
Create three separate lists of IP addresses. The first list should be the IP addresses for the
Houston data center routers and should have over ten IP addresses in it including some duplicate IP
addresses.
The second list should be the Atlanta data center routers and should have at least eight IP
addresses including some that overlap with the Houston data center.
The third list should be the Chicago data center routers and should have at least eight IP
addresses. The Chicago IP addresses have some overlap with the IP addresses in both Houston
and in Atlanta
Convert each of these three lists to a set.
Using set operations, find the IP addresses that are duplicated between Houston and Atlanta.
Using set operations, find the IP addresses that are duplicated in all three sites.
Using set operations, find the IP addresses that are entirely unique in Chicago.
"""

houston_ips = [
    "10.40.1.1",
    "10.40.1.2",
    "10.40.1.3",
    "10.40.2.1",
    "10.40.1.1",
    "10.40.2.1",
    "10.42.135.1",
    "10.42.135.231",
    "10.42.135.16",
    "10.48.32.12",
    "10.48.32.12"
]

atlanta_ips = [
    "10.40.2.1",
    "10.88.1.21",
    "10.88.1.21",
    "10.213.12.12",
    "10.42.135.16",
    "10.12.13.14",
    "12.13.14.15",
    "135.12.56.45"
]

chicago_ips = [
    "10.42.135.16",
    "10.48.32.12",
    "12.13.14.15",
    "140.140.2.1",
    "10.12.13.14",
    "235.16.172.1",
    "15.16.17.18",
    "10.10.10.10"
]


houston_set = set(houston_ips)
atlanta_set = set(atlanta_ips)
chicago_set = set(chicago_ips)

print()
print("-" * 80)
print("Duplicated IPs between Houston and Atlanata: \n\n{}".format(houston_set & atlanta_set))
print("-" * 80)
print()

print()
print("-" * 80)
print("Duplicated IPs in all three sites: \n\n{}".format(houston_set & atlanta_set & chicago_set))
print("-" * 80)
print()

print()
print("-" * 80)
print("Unique elements for Chicago: \n\n{}".format(houston_set - atlanta_set - chicago_set))
print("-" * 80)
print()
