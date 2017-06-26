def biggest_number(*args):
    #The max() function takes any number of arguments and returns the largest one.
    print(max(args))
    return max(args)


def smallest_number(*args):
    # The min() function takes any number of arguments and returns the smallest one.
    print(min(args))
    return min(args)


'''
The abs() function returns the absolute value of the number it takes as an argument—that is, that number's
distance from 0 on an imagined number line. For instance, 3 and -3 both have the same absolute value: 3. 
The abs() function always returns a positive value, and unlike max() and min(), it only takes a single number
'''
def distance_from_zero(arg):
    print(abs(arg))
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


#type() function returns the type of the data it receives as an argument
print (type(42))
print (type(4.2))
print (type('spam'))
