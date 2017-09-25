def hanoy(n, a, b, c):
    if n > 0:
        hanoy(n-1, a, c, b)
        print('disk'+str(n)+' take from '+a+' to '+c)
        hanoy(n-1, b, a, c)
hanoy(3, 'a', 'b', 'c')
