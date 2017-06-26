#Here we are importing entire maths library
#and using a specific sqrt function from it

# import math
#
# def sqrt(n):
#     return math.sqrt(n) #sqrt is an inbuilt function in maths class
#
# n = sqrt(25)
# print (n)


#here rather tahn importing entire maths library we are only importing sqrt
from math import sqrt

def sqroot(n):
    return sqrt(n)

n = sqroot(25)
print (n)

#Universal import
'''
What if we still want all of the variables and functions in a module but don't want to have to constantly type math.?
'''
from math import *