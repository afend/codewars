#!/usr/bin/python

def main():
    '''
    Return the number (count) of vowels in the given string.

    We will consider a, e, i, o, and u as vowels for this Kata.

    The input string will only consist of lower case letters and/or spaces.
    '''

    str = input("Enter a string: ")
    str = str.lower()
    print (getCount(str))

def getCount(inputStr):
    return sum(1 for letter in inputStr if letter in "aeiou")

if __name__ == "__main__":
    main()
