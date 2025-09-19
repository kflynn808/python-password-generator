import os
import sys
import random
import argparse
import string

lower_list = list(string.ascii_lowercase)
upper_list = list(string.ascii_uppercase)
number_list = list(string.digits)
special_list = list(string.punctuation)
non_valid = ["'","\"","`",".","," ]

for x in non_valid:
    while x in special_list:
        special_list.remove(x)

is_upper = False
is_number = False
is_special = False 
is_random = False


def getRandomChars(char_list, char_count):

    new_chars = []
    for x in range(char_count):
        new_chars.append(random.choice(char_list))
    
    return new_chars


def main():
    parser = argparse.ArgumentParser("Python Password Generator")
    parser.add_argument(
        "-s", "--special",
        action="store_true",
        help="Use special characters in the string (!,@,#,etc.)"
    )
    parser.add_argument(
        "-c", "--capitals",
        action="store_true",
        help="Use capital letters in the string"
    )
    parser.add_argument(
        "-n", "--numbers",
        action="store_true",
        help="Use numbers in the string"
    )
    parser.add_argument(
        "-r", "--random",
        action="store_true",
        help="Create a strong random string using all character types (default: 16 char long)"
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        help="Length of the string"
    )
    parser.add_argument(
        "-cS", "--count-special",
        type=int,
        help="Count of special characters used in the string"
    )
    parser.add_argument(
        "-cC", "--count-capital",
        type=int,
        help="Count of capital lettersused in the string"
    )
    parser.add_argument(
        "-cN", "--count-numbers",
        type=int,
        help="Count of numbers used in the string"
    )

    length_char = 16
    special_count = 4
    capital_count = 4
    lower_count = 4 # lowercase letters count
    number_count = 4
    
    args = parser.parse_args()

    characters = string.ascii_lowercase
    if args.special:
        is_special = True
    elif args.capitals:
        is_upper = True        
    elif args.numbers:
        is_number = True       
    elif args.random:
        is_random = True
    elif args.length:
        length_char = args.length
    elif args.count_special:
        special_count = args.count_special
    elif args.count_capital:
        capital_count = args.count_capital
    elif args.count_numbers:
        numbers_count = count_numbers
    else:
        parser.print_help()
        return


    



    random_string = ''.join(random.choice(characters) for i in range(length_char))    
    print(f"[*] Generated String:> {random_string} ")   

if __name__ == "__main__":
    main()
