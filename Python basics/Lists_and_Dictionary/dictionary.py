# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin']) # Prints Puffin's room number


#Like Lists, Dictionaries are "mutable". This means they can be changed after they are created
#dict_name[new_key] = new_value

residents['koala'] = 102
print(residents)


'''
Items can be removed from a dictionary with the del command:
del dict_name[key_name]
'''

del residents['koala']
print(residents)