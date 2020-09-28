#!/usr/bin/env python3

'''Create three different variables the first variable should use all lower case 
characters with underscore ( _ ) as the word separator. The second variable should
use all upper case characters with underscore as the word separator. The third
variable should use numbers, letters, and underscore, but still be a valid
variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3

'''

first_var = "2001:3f1:87ab::32"
CONST_VAR = "2001:3f1:87ab::1"
test_var3 = "192:168:aa::11"

#if first_var == CONST_VAR:
#    print("variable1 equals variable2")

print("Is variable1 equal to variable2? {}".format(first_var == CONST_VAR))

#if first_var != test_var3:
#    print("variable1 is not equal to variable3")

print("Is variable1 not equal to variable3? {}".format(first_var != test_var3))
