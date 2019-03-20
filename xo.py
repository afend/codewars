#!/usr/bin/python

def main():
    '''
    Check to see if a string has the same amount of 'x's and 'o's.
    The method must return a boolean and be case insensitive.
    The string can contain any char.
    '''

    str = input("Enter a string: ")
    str = str.lower()
    
    print (xo(str))

def xo(s):
    # Note this is basically a variation of getCount.py
    return (sum(1 for letter in s if letter in "x") == sum(1 for letter in s if letter in "o"))

if __name__ == "__main__":
    main()
