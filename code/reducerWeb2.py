#!/usr/bin/python

import sys

hitTotal = 0
oldKey = None
maxHit = 0
mostPopular = None




for line in sys.stdin:
   data_mapped = line.strip().split("\t")
   if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
       continue
 
   thisKey, thisHit = data_mapped
 
   if oldKey and oldKey != thisKey:
#        print oldKey, "\t", hitTotal
    if maxHit < int(hitTotal):
       maxHit = int(hitTotal) 
       mostPopular = str(oldKey)
       oldKey = thisKey;
       hitTotal = 0
 
   oldKey = thisKey
   hitTotal += int(thisHit)
 
if oldKey != None:
#    print oldKey, "\t", hitTotal
   if maxHit < int(hitTotal):
       maxHit = int(hitTotal) 
       mostPopular = str(oldKey)
 
print mostPopular, "\t", maxHit
