#! /usr/bin/env python

def readfile(filename):
  with open(filename) as f:
    return f.read()

def findSN(show_ver):
  for line in show_ver.splitlines():
    if "Processor board ID" in line:
       _, serial_number = line.split("Processor board ID ")
  return serial_number

sh_ver_output = readfile("show_version.txt")
SN_output = findSN(sh_ver_output)

print "*" *50
print "Serial Number is {}".format(SN_output)
print "*" *50
