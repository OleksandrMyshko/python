a = [1,4,6,5]
def merch_sort(a):
    if len(a) > 2:
        merch_sort(a[:len(a)//2])
    else:
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]
        else:
            return a

merch_sort(a)
print(a)
