#!/usr/bin/env python

from pprint import pprint

def open_file (filename):
  with open (filename) as f:
    text = f.read()
    return text 

def parse_vendor(text):
  for line in text.splitlines():
    if "Cisco IOS" in line:
       vendor_result, _ = line.split("IOS")
       return vendor_result


def parse_model(text):
  for line in text.splitlines():
    if "bytes of memory" in line:
       _, model_result = line.split("processor")
       return model_result


#for i in router_info

full_file = open_file("show_version.txt")
vendor = parse_vendor(full_file)
model = parse_model(full_file)

print "Vendor is {}".format(vendor)
