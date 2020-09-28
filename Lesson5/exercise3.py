#!/usr/bin/env python3

"""
Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following
format:
01:23:45:67:89:AB
This function should handle the lower-case to upper-case conversion.
It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
The function should have one parameter, the mac_address. It should return the normalized MAC address
Single digit bytes should be zero-padded to two digits. In other words, this:
a:b:c:d:e:f
should be converted to:
0A:0B:0C:0D:0E:0F
Write several test cases for your function and verify it is working properly.
"""

import re

def mac_normalize(mac_addr):
    mac_addr = mac_addr.upper()

    if ":" in mac_addr or "-" in mac_addr:
        new_mac = []
        octets = re.split(r"[:-]", mac_addr)

        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    else:
        new_mac = []
        octets = mac_addr.split(".")

        for octet in octets:
            if len(octet) < 4:
                octet = octet.zfill(4)
            new_mac.append(octet[:2])
            new_mac.append(octet[2:])

    return ":".join(new_mac)

print(mac_normalize("ab:de:12:14:ac:1"))
print(mac_normalize("0010.ab12.133"))
print(mac_normalize("ab-ca-1-de-d1-34"))
