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

   
    print sorted_list.values().
        


test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

main()