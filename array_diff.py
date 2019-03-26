#!/usr/bin/python

def main():
    '''
    Your goal in this kata is to implement a difference function, which
    subtracts one list from another and returns the result.

    It should remove all values from list a, which are present in list b.
    '''
    
    l1 = [1, 2, 2]
    l2 = [1]
    print (array_diff(l1, l2))

def array_diff(a, b):
    return [x for x in a if x not in b]

    
if __name__ == "__main__":
    main()
