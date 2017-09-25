a = [1, 4, 52, 3, 22, 2, 6, 2, 2, 5, 6, 52, 23, 5]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
