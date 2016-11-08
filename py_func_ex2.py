#!/usr/bin/env python

def func1(x,y,z=20):
 print "x is: {}".format(x)
 print "y is: {}".format(y)
 print "z is: {}".format(z)
 return x + y + z

print "Using all three positional arguments"
output1 = func1(3, 2, 10)
print "The total is: {}".format(output1)
print

print "Using named arguments x, y (let z be the default)"
a = 10
b = 2
output2 = func1(a, b)
print "The total is: {}".format(output2)
print

print "With one positional argument and two named arguments"
output3 = func1(3, a, b)
print "The total is: {}".format(output3)
print

print "Using three strings"
output4 = func1(3, 2, 10)
print "The total is: {}".format(output4)
print

print "Using three lists"
output5 = func1(3, 2, 10)
print "The total is: {}".format(output5)
print
