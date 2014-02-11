#!/usr/bin/python
# Your task is to write a mapper code that combines 2 datasets
# This is fairly involved task.
# You want to combine the datasets by joining them by the userid
# so, the mapper key should be "user_ptr_id" from "forum_users.tsv"
# and "author_id" from "forum_nodes.tsv" file. The value would be the full line
# from the respective files: either reputation and badges for the user,
# or full information about forum node.
# To be able to combine the records in the reducer you also need to know
# from which of the tables the informations comes from.
# So, the mapper should output A or B (or something similar) in front
# of the value. Output would be:
# 12345\tA"11"\t"0"\t"0"\t"0"
# 12345\tB"6336"\t"Unit 1: Same Value Q"\t"cs101 value same"  (etc...)
 
# The reducer will get the values sorted, so the line starting with "A"
# will be information about the user, values starting with "B" will be forum nodes.
# Then you can store the user information, append this information to each forum node
# that this user had made, and print it out.
 
import sys
import csv
 
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
 
for line in reader:
    if len(line) == 5 and line[0].isdigit():
        print "A", "\t", line[0], "\t", line[1], "\t", line[2], "\t", line[3], "\t", line[4]
    if len(line) > 10 and line[0].isdigit():
        postid = line[0]
        userid = line[3]
        print "B", "\t", postid, "\t", userid
        # YOUR CODE HERE

## reducer
#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value start starts with A will be the user data
# Values that start with B will be forum node data
 
import sys
import csv
 
reader = csv.reader(sys.stdin, delimiter='\t')
users = {}
for line in reader:
    if "A" in line[0]:
        users[line[1].strip(" ")] = [line[2].strip(" "),line[3].strip(" "),line[4].strip(" ")]
    if "B" in line[0]:
        if line[2] in users:
            rep = users[line[2].strip(" ")]
            print line[1], line[2], rep[0], rep[1], rep[2]
        # YOUR CODE HERE