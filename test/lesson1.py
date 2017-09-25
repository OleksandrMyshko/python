def map(f,lis):
    return [f(i) for i in lis]
def fun(x):
    return x+2
def plus(a,b):
    return a+b
def reduce(g,init,lis):
    sum = init
    for i in lis:
        sum = g(sum,i)
    return sum
l = [10,20,30]
res = reduce(plus,0,map(fun,l))
print(res)
