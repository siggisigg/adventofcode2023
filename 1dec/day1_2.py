# Now the second part of the puzzle spelled out digits also count

file_path = "1dec\input1full.txt"

#one, two, three, four, five, six, seven, eight, and nine also count as valid "digits"
words_that_mean_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
first_letter_of_digits = [word[0] for word in words_that_mean_digits]

def get_first_and_last_digit(n_list): 
    first_digit = n_list[0]
    last_digit = n_list[-1]
    return first_digit + last_digit


def only_first_and_last(n):
    # numbers is a list of strings
    only_first_and_last = []
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
    tmp = ''
    for char in line:
        if char.isdigit():
            tmp += char
    return tmp


def convert_word_of_numbers_to_number(word):
    # given a word that means a number, return the number as a string
    match word:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return "0"

# Setup
answer = 0
lines = []
with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip())

#
# find the words that mean a number
numbers =[]
for line in lines:
    #print(l)
    for wor in words_that_mean_digits:
        if wor in line:
            #print(wor)
            # replace the word with the number
            line = line.replace(wor, convert_word_of_numbers_to_number(wor))
            #print(line)
    # Debug: print the line with the words replaced with numbers
    #print(line)
    numbers.append(get_first_and_last_digit(get_list_of_numbers(line)))

#print(numbers)
print(len(numbers))
print(len(lines))

print(sum_list_of_strings(numbers))
