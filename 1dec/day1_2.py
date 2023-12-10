# Now the second part of the puzzle spelled out digits also count

file_path = "1dec\input1full.txt"

lines = []


###
#one, two, three, four, five, six, seven, eight, and nine also count as valid "digits"
###
words_that_mean_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip())

def get_first_and_last_digit(n_list): 
    first_digit = n_list[0]
    last_digit = n_list[-1]
    return first_digit + last_digit

def only_first_and_last(numbers):
    # numbers is a list of strings
    only_first_and_last = []
    for n in numbers:
        # optimizing run for digitis that already have 2 digits
        if len(n) > 2:
            only_first_and_last.append(get_first_and_last_digit(n))
        elif len(n) == 2:
            only_first_and_last.append(n)
        elif len(n) == 1:
            only_first_and_last.append(n+n)
        else:
            # no digit found
            print("Error")
    return only_first_and_last

def sum_list_of_strings(list_of_strings):
    sum = 0
    for n in list_of_strings:
        sum += int(n)
    return sum

def get_list_of_numbers(lines):
    # filter out characters that are not numbers
    numbers = []
    for line in lines:
        tmp = ''
        for char in line:
            if char.isdigit():
                tmp += char
        numbers.append(tmp)
    return numbers

def convert_word_of_numbers_to_number(word):
    # word is a string of numbers
    # convert to a list of numbers
    # then convert to a string
    # then convert to an int
    return int(''.join(list(word)))