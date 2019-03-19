#!/usr/bin/python

def main():
    a = eval(raw_input("Enter number 1: "))
    b = eval(raw_input("Enter number 2: "))

    print get_sum(a,b)

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

if __name__ == "__main__":
    main()
