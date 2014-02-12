#!/usr/bin/python
import sys
import csv
import collections


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    top_ten = []
    ten = {}
    
    for line in reader:
        # YOUR CODE HERE
        body = line[4]
 
        if (len(top_ten) < 10):
            top_ten.append(int(body))
            ten[int(body)] = line
        elif (body > min(top_ten)):
            min_num = min(top_ten)
            top_ten.remove(min_num)
            del ten[min_num]
            ten[int(body)] = line
            top_ten.append(int(body))
       
        #writer.writerow(line)
    sorted_list = collections.OrderedDict(sorted(ten.items()))
    top_ten.sort()

    #print '\n'.join(str(p) for p in myList)
    
    LIST = sorted_list.values()
    for i in LIST:
       print(i)

