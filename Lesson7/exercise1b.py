#!/usr/bin/env python3
"""
Using a conditional in a Jinja2 template, generate the following output:
crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
The encryption of aes, and the Diffie-Hellman group should be variables in the template.
Additionally this entire ISAKMP section should only be added if the isakmp_enable variable is set
to True.
Your template should be inside your Python program for simplicity.
"""

import jinja2

vars = {
    'encryption': 'aes',
    'group_num': 5,
    'isakmp_enable': False,
}

template = '''
{%- if isakmp_enable %}
crypto isakmp policy 10
 encr {{ encryption }}
 authentication pre-share
 group {{ group_num }}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{%- endif %}
'''

t = jinja2.Template(template)
print(t.render(vars))
