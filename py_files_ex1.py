#!/usr/bin/env python

## Read Part

f = open ("3lines.txt")
file_lines = f.readlines()
for lines in file_lines: 
  print lines.strip()
f.close()


## Write Part

with open ("new_file.txt", "w") as new_file:
  new_file.write("New line is added on this file")
new_file.close()
