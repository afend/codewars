#!/usr/bin/python

def main():
    '''
    Move the first letter of each word to the end of it, then add "ay"
    to the end of the word. Leave punctuation marks untouched.
    '''

    str = input("Enter a string to convert to pig latin: ")
    #str = "Pig latin is cool"  # igPay atinlay siay oolcay
    print(pig_it(str))


def pig_it(text):
    str = ""
    for word in text.split(" "):
        if word.isalpha():
            str += word[1:] + word[0] + "ay "
        else:
            str += word
    return str.strip()


if __name__ == "__main__":
    main()