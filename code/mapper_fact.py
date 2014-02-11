#!/usr/bin/python
import sys
import csv
#import re

#exp = re.compile("[\w\s]+[!.?]")
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
    count = 0

    for line in reader:
        body = line[4].split()
        if exp.search(body) == None:
            writer.writerow(body)
            if body == "fantastic":
                count +=1
            continue
            writer.writerow(count)

test_text = """\"\"\ fantastic \"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\" fantastic \"\t\"Also one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\ fantastic  "
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()