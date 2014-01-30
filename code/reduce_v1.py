#!/usr/bin/python

import sys

def output(previous_key, highest):
	if previous_key != None:
		print previous_key+"the max value"+(highest)+"for this store"

previous_key = None
highest = 0

for line in sys.stdin:
	key, value = line.split("\t", 1)
	if key != previous_key:
	  output(previous_key, highest)
	  previous_key = key
	  highest = 0

	highest = max(int(value))
output(previous_key, highest)
