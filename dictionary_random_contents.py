import random
import time

list1 = [1,2,3,4,5]
list2 = ["a", "s", "d", "f", "g"]
list3 = ["A", "S", "D", "F", "G"]
list4 = ["!", "@", "#", "$", "%"]

'''
The following will create a lambda function that will do a random choice on each of the 4 lists
this can be used for many things beyond this, it allows a dictionary to contain dynamic shifting
data, where if this were done without the use of a lambda, it would only randomise the data on
creation, and not on each call, this does however add the extra step of needing to preform a
function call on the dictionary call
'''

dict_1 = {"rando": (lambda: ( random.choice(list1),
                            random.choice(list2),
                            random.choice(list3),
                            random.choice(list4)))
        }

random.seed(time.time())
print dict_1["rando"]()
