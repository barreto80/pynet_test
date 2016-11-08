#!/usr/bin/env python

i = 0
while i <= 49:
  if i == 13:
     i += 1
     continue
  if i == 39:
     break
  print i
  i += 1
