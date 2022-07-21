a = [1 , 2 , [2, 4, 1, 4], 7, 8, [5, 2]]
a1 = []
a2 = []

for i in range (0, len(a)):
    if type(a[i]) == list:
        a1.append(a[i])
    else:
        a2.append(a[i])


a = sorted(a2)
a.extend(sorted(a1))
print(a)
