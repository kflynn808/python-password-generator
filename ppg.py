import os
import sys
import random
import argparse
import string



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
    length_char = 16
    args = parser.parse_args()
    # creating the characters variable and adding onto it allows us to dynamically
    # choose what type of characters to use based on the arguments and values passed 
    characters = string.ascii_lowercase
    if args.special:
        characters += string.punctuation
    elif args.capitals:
        characters += string.ascii_uppercase        
    elif args.numbers:
        characters += string.digits        
    elif args.random:
        characters = string.ascii_letters + string.punctuation + string.digits
    elif args.length:
        length_char = args.length
    else:
        parser.print_help()
        return
    random_string = ''.join(random.choice(characters) for i in range(length_char))    
    print(f"[*] Generated String:> {random_string} ")   

if __name__ == "__main__":
    main()
