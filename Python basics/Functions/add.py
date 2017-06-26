#program to calculate the square of a number
def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print("%d squared is %d." % (n, squared))


# Call the square function  Make sure to
# include the number 10 between the parentheses.
square(10)

#program to calculate the power of a number
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))

power(2, 3)  # Add your arguments here!