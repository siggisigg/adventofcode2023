###
# Puzzle source: https://adventofcode.com/2023/day/1
#   On each line, the calibration value can be found by 
#   combining the first digit and the last digit (in that order)
#   to form a single two-digit number.
###
file_path = "1dec\input1full.txt"
lines = []

Dessired_output = [12, 38, 15, 77]
output_product = 12 + 38 + 15 + 77 #142

with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip())

# debug input print
#print(lines)


# filter out characters that are not numbers
numbers = []
for line in lines:
    tmp = ''
    for char in line:
        if char.isdigit():
            tmp += char
    numbers.append(tmp)

# debug print
#print([len(val) for val in numbers])

# general solution
def get_first_and_last_digit(n_list): 
    first_digit = n_list[0]
    last_digit = n_list[-1]
    return first_digit + last_digit


# now get the first and last digit of each number in the numbers list
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

    #only_first_and_last.append(get_first_and_last_digit(n)) # this is the same as the if statement above

# debug print
print(only_first_and_last)

# sum the numbers in the list from strings
sum = 0
for n in only_first_and_last:
    sum += int(n)
print(sum)
