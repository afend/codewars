#!/usr/bin/python

def main():
    '''
    ake 2 strings s1 and s2 including only letters from ato z.
    Return a new sorted string, the longest possible, containing
    distinct letters, each taken only once - coming from s1 or s2.
    '''
    
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    
    print (longest(s1, s2))

def longest(s1, s2):
    return ("".join(sorted(set(s1+s2))))

if __name__ == "__main__":
    main()
