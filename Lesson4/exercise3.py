#!/usr/bin/env python3

"""
Read in the "show_version.txt" file. From this file use regular expressions to extract the
os_version, serial_number, and configuration register value.
Your output should look as follows:
          OS Version: 15.4(2)T1
       Serial Number: FTX0000038X
     Config Register: 0x2102
"""

import re

with open('show_version.txt') as f:
    show_ver = f.read()

os_ver = re.search(r"Version (\S+?),", show_ver).group(1)
ser_num = re.search(r"^Processor board ID (\w+)", show_ver, flags=re.M).group(1)
conf_reg = re.search(r"^Configuration register is (\w+)", show_ver, flags=re.M).group(1)

print()
print("{:>20}: {:15}".format("OS Version", os_ver))
print("{:>20}: {:15}".format("Serial Number", ser_num))
print("{:>20}: {:15}".format("Config Register", conf_reg))
print()
