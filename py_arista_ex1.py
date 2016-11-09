#!/usr/bin/env python

from pprint import pprint
import pyeapi

def main():

  arista_sw = pyeapi.connect_to("pynet-sw2")
  output = arista_sw.enable("show ip route")
  #pprint (output)

  #Output comes as a list with only one item in it. Stripping the list off to have only the dictionary:
  output = output[0]
  #pprint (output)
  #print "\n" *5

  #The dictionary comes with outer useless layers, stripping those off too:
  output = output["result"]["vrfs"]["default"]
  #pprint (output)
  #print "\n" *5
  
  #Getting the routes:
  routes = output["routes"]
  pprint (routes)
  print "\n" *5
  print "{:>15} {:>15} {:>15}".format("prefix", "interface", "next_hop")
  
  for k, v in routes.items():
    int_nexthop = v["vias"][0]
    pprint (int_nexthop)


if __name__ == "__main__":
  main()
