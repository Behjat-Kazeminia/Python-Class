while True:
    string = input('please enter any word you want: ')

    item = 1

    while item < len(string):
        a = string[0:item+1]
        b = ''
        for element in a:
            b = element + b
        string = b + string[item + 1: len(string)]
        print(string)
        item += 1
