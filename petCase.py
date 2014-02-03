#!/usr/bin/python

class pet:  
    number_of_legs = 0  

    def sleep(self):
	print('zzz')

    def count_legs(self):
        print("I have {} legs".format(self.number_of_legs))
 
doug = pet()  
doug.number_of_legs = 4  
doug.count_legs()

nemo = pet()
nemo.number_of_legs = 0
nemo.count_legs()
