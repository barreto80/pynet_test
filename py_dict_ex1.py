#!/usr/bin/env python

router = {}
router["ip_addr"] = "10.0.0.1"
router["username"] = "cisco-user"
router["password"] = "Cisco123"
router["vendor"] = "Cisco"
router["model"] = "2921"

for k, v in router.items():
  print k, v

router["password"] = "Securepass123!"
router["secret"] = "Supersecretpass123!"

print
for k, v in router.items():
  print k, v

print
print router.get("device_type", "Cisco IOS")
print

try:
  device_type = router['device_type']
except KeyError:
  print "Device type not found"
