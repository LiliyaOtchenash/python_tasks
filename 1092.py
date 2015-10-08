def d1(F): return lambda: 'X' + F()
def d2(F): return lambda: 'Y' + F()
def d3(F): return lambda: 'Z' + F()

@d1
@d2
@d3
def func(): return 'spam'#func = d1(d2(d3(func)))


print(func())

# print(func()) ==
# print(d1(d2(d3(func()))))
# print(d1(d2(d3 ==)))
#         d3(func): return lambda: 'z' + func()
#          == 'Z' + 'spam' == Zspam ....


