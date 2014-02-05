#!/usr/bin/python

import sys

def outout(previous_key, total):
  if previous_key is not None:
    print previous_key+" Was found " +str(total)+" times"

previous_key = None
total = 0
quiz = 0
for line in sys.stdin:
   key, value = line.split("\t", 1)
   if key is not previous_key:
     outout(previous_key, total)
     previous_key = key
     total = 0

   total += int(value)
outout(previous_key, total)