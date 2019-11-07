#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: November 2019
# This is a program which displays the numbers 1000-2000.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # This is what runs the program.
    number = 0
    print("")
    print("This program will tell you all the numbers from 1001 - 2000.")
    print("")

    for number in range(1001, 2001):
        print((color.BOLD + color.DARKCYAN + '{0}'.format(number) + color.END),
              end=(color.BOLD + color.GREEN + ' | ' + color.END))
        if number % 5 == 0:
            print("")


if __name__ == "__main__":
    main()
