#in-built functions

#(1)int()
#(2)str()
#(3)bool()
#(4)float()


#module

#import math
#from math import *
from math import sqrt
print(sqrt(4))

#User defined functions

def sum (first,second):
    print(first+second)

sum(100,200)
    
def sum2 (first,second=1): #1=by default value incase the second parameter is not passed
    print(first+second)

sum2(100)    