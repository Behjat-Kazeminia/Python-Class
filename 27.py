#input: number (type: int)
#output: a number in the string type (str)
#goal: find the smallest number that contains only sevens and zeros and it is divisible by the input number

def seven_zero(number):
    
        d = len(number)
        number = int(number)
        Flag = True
        
        while Flag:
            for i in range(0, d):
                result = ((i + 1) * '7') + ((d - 1 - i) * '0')
                if int(result) % number == 0:
                    Flag = False
                    print(result)
                    print(len(result))
                    break
            d += 1

while True:
    number = input("please enter your number: ")
    while number.isnumeric() == False:
        number = input("please enter a valid number: ")
    seven_zero(number)
