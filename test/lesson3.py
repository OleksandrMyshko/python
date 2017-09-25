def myfun():
    print('1')
    yield 11
    print('2')
    yield 22


f = myfun()
res = next(f)
print(res)
res = next(f)
print(res)


def myrange(begin, end):
    init = begin
    while init < end:
        yield init
        init += 1


for i in myrange(0, 10):
    print(i)
print()


def g():
    print('1')
    k = yield 3
    print(k)
    l = yield 4
    print(l)


f = g()
next(f)
k1 = f.send(10)
print(k1)
# анотация
def f(a:int,b:int)->int:
    return a+b

print(f('addsd','asd'))

import re
s = 'dssadsfsfsdfsgghhsqpwbebevqeaaadsgsg'
array = re.split("a+",s)
print(array)
