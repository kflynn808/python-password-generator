import os
import sys
import random
import argparse
import string

lower_list = list(string.ascii_lowercase)
upper_list = list(string.ascii_uppercase)
number_list = list(string.digits)
special_list = list(string.punctuation)

# some punctuation characters aren't good for passwords
# so we remove the non valid characters early so we don't have to parse later
non_valid = ["'","\"","`",".","," ]
for x in non_valid:
    while x in special_list:
        special_list.remove(x)

# wrote this function to minimize copy and paste
def getRandomChars(char_list, char_count):
    new_chars = []
    for x in range(char_count):
        new_chars.append(random.choice(char_list))
    return new_chars


def main():
    is_upper = False
    is_number = False
    is_special = False 
    is_random = False

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

    length_char = 0
    special_count = 0
    capital_count = 0
    lower_count = 0 # lowercase letters count
    number_count = 0
    
    args = parser.parse_args()

    # removed elif statements because special_count, capital_count
    # and number_count were not being set a value, switching to if 
    # solved this problem
    if args.special:
        is_special = True
    if args.capitals:
        is_upper = True        
    if args.numbers:
        is_number = True       
    if args.random:
        is_random = True
        is_special = True
        is_capital = True
        is_number = True
        length_char = 16
        special_count = 4
        capital_count = 4
        lower_count = 4 
        number_count = 4
    if args.length:
        length_char = args.length
    if args.count_special:
        special_count += args.count_special
        is_special = True
    if args.count_capital:
        capital_count = args.count_capital
        is_upper = True    
    if args.count_numbers:
        numbers_count = args.count_numbers
        is_number = True       

    string_lists = []

    if is_special:
        string_lists.append(getRandomChars(special_list, special_count))
    if is_upper:
        string_lists.append(getRandomChars(upper_list, capital_count))
    if is_number:
        string_lists.append(getRandomChars(number_list, number_count))
    
    # we want the lowercase characters to fill the rest of the string
    # we count the total amount of characters requested in the flags (special, capital, numbers) to subtract
    # from the string length assigned. if there are no flags passed we fill the whole string with lowercase letters
    total_count = special_count + capital_count + number_count
    if total_count > 0:
        lower_count = length_char - total_count
    if total_count == 0:
        lower_count = length_char
    string_lists.append(getRandomChars(lower_list, lower_count))
    
    # In order to join the string properly we have to flatten the list before joining it (removes the extra brackets)
    flat_string_list = [item for sublist in string_lists for item in sublist]
    random_string = ''.join(random.choice(flat_string_list) for i in range(length_char))    
    
    if random_string == '':
        parser.print_help()
        return
    
    print(f"[*] Generated String:> {random_string} ")   

if __name__ == "__main__":
    main()
