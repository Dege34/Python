# Copyright © 2023 Dogan Ege BULTE
# https://github.com/Dege34
# dege.bulte@studenti.polito.it

def filter_max_min_numbers(numbers):
    filtered_nums = []

    for num in numbers:
        if num != max(numbers) and num != min(numbers):
            filtered_nums.append(str(num))

    return ":".join(filtered_nums)

def filter_even_numbers(numbers):

    even_nums = [] 
    
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(str(num))

    return ":".join(even_nums)

def filter_two_digit_numbers(numbers):

    two_digit_nums = []
    for num in numbers:
        if 10 <= num <= 99:
             two_digit_nums.append(str(num))

    return ":".join(two_digit_nums)

def main(filename):
    try:

        with open(filename, 'r') as file:
            input_str = file.read().strip()
    
    except OSError as problem:
        
        print("SIR ! we have problem")

        exit(1)

    # i splited the input string into individual number
    numbers = input_str.split(":")

    # i convert the numbers from string to integers without empty string
    numbers =  [int(num) for num in numbers if num]

    # first print the input numbers excluding the maximum and minimum

    filtered_nums_str = filter_max_min_numbers(numbers)

    print("II. I filtered without max and min numbers: {}".format (filtered_nums_str))

    # second print only the even values among the input numbers

    even_nums_str = filter_even_numbers(numbers)

    print("II. Even numbers in file: {}".format(even_nums_str))

    # third print only the 2-digit numbers among the input numbers

    two_digit_nums_str = filter_two_digit_numbers(numbers)

    print("III. Two-digit numbers in file : {}".format(two_digit_nums_str))

if __name__ == "__main__":
    INPUT_FILE = input("Write file name with type (.txt/.csv):")
    main(INPUT_FILE)