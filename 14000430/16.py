number = input("please enter your number: ")
while number.isnumeric() == False:
    number = input("please enter a valid number: ")

new_result_number = ''
result = []

for index, element in enumerate(number):
    new_result_number += element
    if len(result) > 0:
        if int(new_result_number) > int(result[-1]):
            result.append(new_result_number)
            new_result_number = ''
    elif new_result_number == '0':
        new_result_number = ''
    else:
        result.append(element)
        new_result_number = ''        

print(result)
