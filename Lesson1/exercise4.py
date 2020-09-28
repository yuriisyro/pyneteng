#!/usr/bin/env python3

'''Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.'''

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.strip()

splitted = show_version.split()
model = splitted[1]
serial_number = splitted[2]

cisco = "cisco" in model.lower()
print("Checking if it's Cisco: {}".format(cisco))

model_881 = "881" in model
print("Checking if model contains 881: {}".format(model_881))

print("Serial number: {}".format(serial_number))
print("Model: {}".format(model))
