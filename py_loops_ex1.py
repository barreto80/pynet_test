#!/usr/bin/env python

my_list = range (1,50)
print my_list
print

for i in my_list:
  if i == 13:
    continue
  if i == 40:
     break
  else:
    print i
