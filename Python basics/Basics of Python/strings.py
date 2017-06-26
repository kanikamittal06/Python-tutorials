#creating a string

a= "satyam"
print(a)

#escaping characters - method1 by using ""
a = "there's our aunt"
print(a)

#escaping characters - method2 by using a backlash
b = 'there\'s our aunt'
print(b)


#accessing by index
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""

d = "there is a snake in the closet"
print (d[0])
print (d[1])
print (d[2])

# - sign indicates that we are starting the count from end
# here from tesolc
#note that there is no -0
print (d[-1])
print (d[-2])
print (d[-3])


#string methods
var = "satyam"
print ("The length is: " + str(len(var)))
#we cannot concatenate a string and a int value


#Methods that use dot notation only work with strings.
print(var.upper())

var_a = "SATYAM"
print(var.lower())

#The str() method turns non-strings into strings!
pi = 3.14
print(str(pi))



