#!/usr/bin/env python3

"""
Use Jinja2 templating to render the following:
vlan {{ vlan_id }}
   name {{ vlan_name }}
Your template should be inside of your Python program for simplicity.
The output from processing your template should be as follows. This should be printed to stdout.
vlan 400
   name red400
"""

import jinja2

vars = {
    'vlan': 400,
    'name': 'red400',
}

jinja_template = '''
vlan {{ vlan }}
  name {{ name }}
'''

t = jinja2.Template(jinja_template)

print(t.render(vars))
