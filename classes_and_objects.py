#!/usr/bin/env python

class NetDevice(object):
  def __init__ (self, ip_addr, username, password):
    self.ip_addr = ip_addr
    self.username = username
    self.password = password

  def test_method(self):
    print "Device IP is: {}".format(self.ipaddr)
    print "Username is: {}".format(self.username)

rtr1 = NetDevice("10.22.1.1", "admin", "secret!") 
print "This is the output of rtr1.username: {}".format(rtr1.username)
