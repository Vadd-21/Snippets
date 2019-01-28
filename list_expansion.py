import random
import time

"""
the following is an example of how to take a list of lists and expand the sub-lists 0th content
by the sub-lists 1th content, this allows for expanded lists to be sent across the wire in a 
moreso compact form, rather then sending 100 items across the wire, it could be done with
as few as 4, or a json of 2, this exact example may not be fully useful to many applications
however it can be extreamly usefull when needed
"""

random.seed(time.time())
value = random.randint(0, 100) # can be anything really, in this case our desired max is 100
mylist = [["1", value], ["0", 100 - value]] # the 100 - value section is to represent our max as 100, this can be whatever is needed
mylist = [x for x, y in mylist for i in range(y)]

print mylist
