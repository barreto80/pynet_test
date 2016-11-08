#!/usr/bin/env python

#usr_ip_addr = raw_input("Please enter your IP Address: ")
usr_ip_addr = "192.168.57.100"
usr_oct = usr_ip_addr.split(".")

print
print usr_oct
print
print "{:<12} {:<12} {:<12} {:<12}".format(usr_oct[0], usr_oct[1], usr_oct[2], usr_oct[3])
print

usr_oct[-1] = 0

print usr_oct


usr_oct_bin = []
usr_oct_bin.append(bin(int(usr_oct[0])))
usr_oct_bin.append(bin(int(usr_oct[1])))
usr_oct_bin.append(bin(int(usr_oct[2])))
usr_oct_bin.append(bin(int(usr_oct[3])))

print
print usr_oct_bin
print

print
print "{:<12} {:<12} {:<12} {:<12}".format(usr_oct_bin[0], usr_oct_bin[1], usr_oct_bin[2], usr_oct_bin[3])
print
