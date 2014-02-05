#reducerWC5.py
#!/usr/bin/python

import sys

def outout(previous_key, total):
  if previous_key !=  None:
    if total > 10:
      print str(total)+"\t"+ previous_key

previous_key = None
total = 0

for line in sys.stdin:
   key, value = line.split("\t", 1)
   if key != previous_key:
     outout(previous_key, total)
     previous_key = key
     total = 0

   total += int(value)
outout(previous_key, total)