'''
A lot of times we want to keep track of when something happened.
We can do so in Python using datetime.
We can use a function called datetime.now() to retrieve the current date and time.
'''

from datetime import datetime
now = datetime.now()
print(now)
#print(datetime.now())

#extracting specific info from now variable
print(now.year)#returns year
print(now.month)#returns month
print(now.day)#returns day