import os
import sys
import random
import argparse

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
        help="Uses numbers in the string"
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        help="Length of the string"
    )
    parser.add_argument(
        "-r", "--random",
        action="store_true",
        help="Creates a strong random string using all characters (default: 16 char long)"
    )
    
    # we execute at the end so all arguments are added
    args = parser.parse_args()

if __name__ == "__main__":
    main()
