# How To Convert A List To A String???

#You convert a list to a string by using ''.join().
listOfStrings = ['One', 'Two', 'Three']
strOfStrings = ''.join(listOfStrings)
print(strOfStrings)



# How To Convert Lists To A Dictionaries???
helloWorld = ['hello','world','1','2']
helloWorldDictionary = dict(zip(helloWorld[0::2], helloWorld[1::2]))

# Print out the result
print(helloWorldDictionary)

'''
Note that the second element that is passed to the zip() function makes use of the step value
to make sure that only the world and 2 elements are selected. Likewise, the first element uses 
the step value to select hello and 1
'''

# How To Concatenate Lists in Python???

list = [1,2,3,4,5]
list = list + list[0:len(list):2]
print(list)

# How To Sort a List in Python???/
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.sort()
print ("list now : ", list1)


#Counting the occurrences of one item in a list????
# Count the occurrences of the number 4
print([1, 2, 9, 4, 5, 4, 1].count(4))

# Count the occurrences of the letter "a"
list = ["d", "a", "t", "a", "c", "a", "m", "p"]
print(list.count("a"))

#How To Loop over A List in Python????
# This is your list
mylist = [[1,2,3],[4,5,6,7],[8,9,10]]

# Loop over your list and print all elements that are of size 3
for x in mylist:
      if len(x)==3:
        print(x)

