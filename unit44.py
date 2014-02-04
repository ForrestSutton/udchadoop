#!/usr/bin/python
import sys
import csv
import heapq

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    numberList = []
    lines      = []
    for line in reader:
        if line:
            numberList.append(len(line[4]))
            lines.append(line)
    top10 = heapq.nlargest(10, numberList)
    minTop10 = min(top10)
    for i in range(0, len(lines)):
        if numberList[i] >= minTop10:
            writer.writerow(lines[i])

            