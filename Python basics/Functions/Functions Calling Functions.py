# def fun(n):
#     return n**3
#
#
# #functon fu calls the function fun
# def fu(m):
#     print(type(fun(m)+7))
#
# fu(2)

def one_good_turn(n):
    return n + 1


def deserves_another(n):
    print(type(one_good_turn(n) + 2))

deserves_another(2)