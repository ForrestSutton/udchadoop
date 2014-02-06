#!/usr/bin/python
import sys
import csv


def mapper():
   reader = csv.reader(sys.stdin, delimiter='\t')
   writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
#store the Length of the string and the actual CSV line in a dictionary
# {Len1 : CSV Line1, Len2 : CSV Line2}
# to be used later to sort based on length and taken top N items
l = {}
        for line in reader:
        #print (line[4])
           if len(line[4]) not in l: 
               l[len(line[4])] = line
            else:
               l[len(line[4])].update([line])

#get the keys of the dictionary as a list. Sort it based on the length
l2 = sorted(sorted(list(l.keys()), reverse = True)[:10])

for key in l2: 
    val = "\"\t\"".join((l[key]))
    print('"'+val+'"')



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