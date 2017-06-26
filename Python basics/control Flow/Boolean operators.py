"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""
bool_a = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
print(bool_a)

bool_b = 19 % 4 != 300 / 10 / 10 and False
print(bool_b)

bool_c = not not False
print(bool_c)