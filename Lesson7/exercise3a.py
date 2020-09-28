#!/usr/bin/env python3

"""
Create a YAML file that defines a list of interface names. Use the expanded form of YAML.
Use Python to read in this YAML list and print this to the screen.
The output of your Python script should look as follows:
['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5', 'Ethernet6', 'Ethernet7',
 'Management1', 'Vlan1']
"""

import yaml

file = 'exercise3a.yaml'

with open(file) as f:
    output = yaml.load(f)

print(output)
