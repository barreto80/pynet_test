#!/usr/bin/env python

## Any of the values of the function can be set directly on the function definition

def my_func1(x,y,z):
  print "Hellow world"
  print "x is: {}".format(x)
  print "y is: {}".format(y)
  print "z is: {}".format(z)
  print
  print "The sum of the variables is:"
  print x + y + z
  print
  return x + y

a = 10
b = 20
c = 2
my_list = [4, 7, 9]
some = {
  "x": 3,
  "y": 2,
  "z": 9,
}

my_func1(a,b,c)
my_func1(y=17,x=30, z=1)
my_func1(7,z=5, y=1)

## The asterisk in front of my_list basically umpacks the list
my_func1(*my_list)


## The DOUBLE asterisk in front of some umpacks the dictionary
my_func1(**some)

## Return value practice:
ret_val = my_func1(**some)
print type(ret_val)
print ret_val

print "{} {} {}".format(a, b, c)

print "{} {} {}".format(*my_list)
