a, b = 999, 999
k = 0
while a > 99 and k != 1:
    while b > 99 and k != 1:
        product = str(a * b)
        i, j = 0, -1
        k = 1
        for n in range(len(product)):
            if product[i] == product[j]:
                i += 1
                j -= 1
            else:
                k = 2
                break

        if k == 1:
            print(product)
            print(a, b)
            break
        b -= 1
    a -= 1



