'''
First, def a function called cube that takes an argument called number.
Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).
Define a second function called by_three that takes an argument called number.
if that number is divisible by 3, by_three should call cube(number) and return its result. Otherwise, by_three should return False.
Don't forget that if and else statements need a : at the end of that line!
'''


def cube(n):
    print( n**3)

def by_three(number):
    if(number %3 == 0 ):
        cube(number)
    else:
        return False

by_three(9)
by_three(3)