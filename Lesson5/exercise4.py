#!/usr/bin/env python3

"""
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement
outside of your function (i.e. where you have your function calls).
Inside of pdb, experiment with:
1. Listing your code.
2. Using 'next' and 'step' to walk through your code. Make sure you understand the difference
   between the two.
3. Experiment with 'up' and 'down' to move up and down the code stack.
4. Use p <variable> to look at a variable.
5. Set a breakpoint and run your code to the breakpoint.
6. Use '!command' to change a variable (for example !new_mac = [])
"""

import pdb
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

pdb.set_trace()
print(mac_normalize("ab:de:12:14:ac:1"))
print(mac_normalize("0010.ab12.133"))
print(mac_normalize("ab-ca-1-de-d1-34"))
