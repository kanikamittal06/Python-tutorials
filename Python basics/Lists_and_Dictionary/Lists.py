'''
Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name
'''

zoo_animals = ["pangolin", "cassowary", "sloth", "panda" ];

print(zoo_animals[0])
print(zoo_animals[1])
print(zoo_animals[2])
print(zoo_animals[3])
print(zoo_animals[-1])
print(zoo_animals[-2])
print(zoo_animals[-3])
print(zoo_animals[-4])
# print(zoo_animals[34])


#adding items to the list dynamically
letters = ["a", "b","c"]
print ("old list is: ", letters)

letters.append("d")
letters.insert(2, "e")
print("the new list is: ", letters)


#searching items in a list
animals = ["ant", "bat", "cat"]
print (animals.index("bat"))



