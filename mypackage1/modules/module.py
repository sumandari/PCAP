#!/usr/bin/env python3
""" module.py - an example of pyhton module """

__counter = 0

def sum1(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum


def prod1(list):
    global __counter
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("I prefer to be a module")
    l = [i+1 for i in range(5)]
    print(sum(l) == 15)
    print(prod1(l) == 120)
else:
    print("I like to be a module")
