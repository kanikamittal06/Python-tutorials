
#
# a = 10
# while(a < 20):
#     print (a)
#



#This program calculates the Fibonacci sequence
a = -1
b = 1
count = 0
max_count = 5
while count < max_count:
    count = count + 1
    #we need to keep track of a since we change it
    c = a+b
    a = b
    b = c
    #Notice that the , at the end of a print statement keeps it
    # from switching to a new line
    print (c)