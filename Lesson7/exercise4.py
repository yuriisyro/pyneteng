#!/usr/bin/env python3

"""
Take the YAML file and corresponding data structure that you defined in exercise3b:
{'interfaces': {
    'Ethernet1': {'mode': 'access', 'vlan': 10},
    'Ethernet2': {'mode': 'access', 'vlan': 20},
    'Ethernet3': {'mode': 'trunk',
                  'native_vlan': 1,
                  'trunk_vlans': 'all'}
    }
}
From this YAML data input source, use Jinja templating to generate the following configuration
output:
----
interface Ethernet1
  switchport mode access
  switchport access vlan 10
interface Ethernet2
  switchport mode access
  switchport access vlan 20
interface Ethernet3
  switchport mode trunk
  switchport trunk native vlan 1
  switchport trunk allowed vlan all
----
The following should all be variables in your Jinja template (the names may be different than
below, but they should be variabilized and not be hard-coded in your template).
----
interface_name
switchport_mode
access_vlan
native_vlan
trunk_vlans
----
All your Jinja2 variables should be retrieved from your YAML file.
This exercise might be challenging.
"""

import jinja2
import yaml

file = 'exercise3b.yaml'

with open(file) as f:
    output = yaml.load(f)


jinja_template = '''
{%- for iface, iface_config in interfaces.items() %}
interface {{ int }}
  {%- if iface_config['mode'] == 'access' %}
  switchport mode {{ iface_config['mode'] }}
  switchport access vlan {{ iface_config['vlan'] }}
  {%- else %}
  switchport mode trunk
  switchport trunk native vlan {{ iface_config['native_vlan'] }}
  switchport trunk allowed vlan {{ iface_config['trunk_vlans'] }}
  {%- endif %}
{%- endfor %}
'''

template = jinja2.Template(jinja_template)
print(template.render(output))
