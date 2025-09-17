import os
import sys
import random
import argparse

def main():
    parser = argparse.ArgumentParser(description="Hello World CLI")
    parser.add_argument(
        "-n", "--name",
        type=str,
        help="Name to greet"
    )
    args = parser.parse_args()
    if args.name:
        print(f"Hello {args.name}!")
    else:
        print("Hello World!")

if __name__ == "__main__":
    main()

