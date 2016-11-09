#!/usr/bin/env python

from pynxos.device import Device
from pprint import pprint

nexus_ip = "nxos1.twb-tech.com"
nxos_device = Device(host=nexus_ip, username="pyclass", password="88newclass", transport='https', port=8443)

nxos_facts = nxos_device.facts
print
print nxos_facts 
print
print "*" *50
print "*" *50
pprint(nxos_device.facts)
print "*" *50
print "*" *50

for k,v in nxos_facts():
  if k = model
  print v
 

