zoo_animals = ["pangolin", "cassowary", "sloth", "panda" ];

print(zoo_animals[2:])#print  everything from index 2 to the end of list
print(zoo_animals[1:4])#print  everything from index 2 to index(4-1) i.e index 3

#print all list itemms from index 1 to list_size at a gap of 2
print(zoo_animals[0:len(zoo_animals):2])



############### Note #############
# a[start:end] # items start through the end (but the end is not included!)
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through the end (but the end is not included!)