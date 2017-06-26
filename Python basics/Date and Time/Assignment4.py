'''
Print the current date in the form of mm/dd/yyyy
'''


from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
#print("%s/%s/%s" %(year, month, day))
a = "%s/%s/%s" %(year, month, day)
print(a)


hour = now.hour
minute = now.minute
second = now.second
#print("%s:%s:%s" %(hour,minute,second))
b = "%s:%s:%s" %(hour,minute,second)
print(b)

#printing together
print("%s/%s/%s %s:%s:%s" %(year, month, day, hour,minute,second))

'''
Print the current date in the form of mm-dd-yyyy
and time in the form of hr:min:seconds
and then combine the two

'''
