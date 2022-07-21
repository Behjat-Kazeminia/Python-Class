a = [42 , 13, 15, 10, 5, 8, 3, 2, 0]

if len(a) == 0:
    counter = 0
elif len(a) == 1:
    counter = 1
else:
    counter = 0
    for i in range (0, len(a)):
        for j in range (i, len(a)):
            if a[i] <= a[j]:
                break
            elif j == len(a) - 1:
                counter = counter + 1

print(counter)


               
