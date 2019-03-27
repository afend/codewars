#!/usr/bin/python

def main():
    '''
    Build Tower
    Build Tower by the following given argument:
    number of floors (integer and always greater than 0).

    Tower block is represented as *

    Python: return a list;
    Have fun!
    '''

    floors = input("Enter number of floors: ")
    if not floors.isdigit():
        while not floors.isdigit():
            floors = input("Enter number of floors: ")
    print(tower_builder(int(floors)))


def tower_builder(n_floors):
    arr = []
    ast = 1
    for i in range(1, n_floors + 1):
        arr.append("*" * (ast))
        ast += 2

    i = 0
    for a in arr:
        spaces = (ast - 2 - len(a)) / 2
        arr[i] = " " * int(spaces) + a + " " * int(spaces)
        i += 1

    return arr


if __name__ == "__main__":
    main()
