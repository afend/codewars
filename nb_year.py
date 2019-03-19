#!/usr/bin/python
from __future__ import division

def main():
    start = eval(raw_input("Enter starting population: "))
    percent = eval(raw_input("Enter annual percent increase: "))
    augment = eval(raw_input("Enter the minimum number of people per year that come randomly: "))
    target = eval(raw_input("Enter target population: "))

    print nb_year(start, percent, augment, target)

def nb_year(p0, percent, aug, p):
    yrs = 0
    percent = percent/100
    while p0 < p:
        p0 = p0 + p0 * percent + aug
        yrs += 1
    return yrs

if __name__ == "__main__":
    main()
