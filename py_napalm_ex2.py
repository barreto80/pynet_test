#!/usr/bin/env python


from pprint import pprint as pp
from napalm_base import get_network_driver
from my_devices import pynet_rtr2

pp(pynet_rtr2)

def main():
    for a_device in (pynet_rtr2,):
        dev_type = a_device.pop("device_type")
        driver = get_network_driver(dev_type)
        device = driver(**a_device)

        print
        print ">>>Device open"
        device.open()

        print
        print ">>>Load config change (merge) - no commit"
        device.load_merge_candidate(filename="cisco_merge.txt")
        print device.compare_config()

if __name__ == "__main__":
  main()
