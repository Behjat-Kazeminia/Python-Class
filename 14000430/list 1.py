list1 = ['a', 'b', 'a', 'c', 'a']

for index, element in enumerate(list1):
    if(element == 'a'):
        list1.remove('a')

print(list1)
