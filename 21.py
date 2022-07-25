#input: a text (type: str)
#output: (len(input) - 1) number of texts (type: all str)
#goal:
"""reverse the first two letters of the text and print it, do the same with the
first three letters of the previous result and print it. this loop has to go on
until there is no letters left of the given text which hasn't been reversed"""

def pancake_scramble(text):

        number_of_reversed_indexes = 1

        while number_of_reversed_indexes < len(text):
            first_part_of_the_text = text[0:number_of_reversed_indexes + 1]
            reversed_of_the_first_part = ''
            for element in first_part_of_the_text:
                reversed_of_the_first_part = element + reversed_of_the_first_part
            text = reversed_of_the_first_part + text[number_of_reversed_indexes + 1: len(text)]
            print(text)
            number_of_reversed_indexes += 1

while True:
    text = input('please enter any word you want: ')
    pancake_scramble(text)
