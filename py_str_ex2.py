#!/usr/bin/env python

usr_ip_addr = raw_input("Please enter your IP Address: ")
usr_oct = usr_ip_addr.split(".")
print

print usr_oct
print

print usr_oct[0]
print usr_oct[1]
print usr_oct[2]
print usr_oct[3]
print

print "*" *50
print
print "{:<12} {:<12} {:<12} {:<12}".format(usr_oct[0], usr_oct[1], usr_oct[2], usr_oct[3])
print
print "*" *50
