# input: a positive integer(number)
# output: list of numbers (increasing_list_of_numbers)
# goal: split the given integer from left to right to a increasing list of numbers

def extract_increasing(number):

    """this variable was created to add the remaining elements of the given
    number from left to right to it until the variable is bigger than the
    last item of the increasing_list_of_numbers and it can be added to the list"""
    new_number = ''
    
    """output"""
    increasing_list_of_numbers = []

    for index, element in enumerate(number):
        new_number += element
        if len(increasing_list_of_numbers) > 0:
            if int(new_number) > int(increasing_list_of_numbers[-1]):
                increasing_list_of_numbers.append(new_number)
                new_number = ''
            #if the first element of an item of the output is equal to zero
            elif new_number == '0':
                new_number = ''
        #if there is one or more zeros at the first of given number you have
        #to ignore them
        elif new_number == '0':
            new_number = ''
        #for the first element of the given number
        else:
            increasing_list_of_numbers.append(element)
            new_number = ''        

    return increasing_list_of_numbers

while True:
    number = input("please enter your number: ")
    while number.isnumeric() == False:
        number = input("please enter a valid number: ")
    print(extract_increasing(number))

