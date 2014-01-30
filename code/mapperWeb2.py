#!/usr/bin/python
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment



import sys
import urlparse

for line in sys.stdin:
    line = line.strip()
    firstIndex = line.find("\"")
    lastIndex = line.rfind("\"")
    if (firstIndex > 1 and lastIndex > 2):
        requestString = line[firstIndex+1:lastIndex]
        actualUrl = requestString.split(" ")[1]
        docname = urlparse.urlparse(actualUrl)
        print "{0}\t{1}".format(docname.path, 1)


