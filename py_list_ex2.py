#!/usr/bin/env python

ex_list = range(5)
ex_list.append ("dog")
ex_list.append (3.1415)

print ex_list

ex_list.pop(0)

print
print ex_list
print

print "List lenght is: "
print len(ex_list)
print

print "This is another way of sorting the list:"
print "Length of list: {}".format(len(ex_list))
ex_list.sort()
print ex_list
print

print "This is the list sorted by index:"
for i, ex_list in enumerate(ex_list):
  print i, ex_list
print
