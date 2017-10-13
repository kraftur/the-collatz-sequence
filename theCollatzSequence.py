#!/usr/bin/python3
# -*- coding: utf-8 -*-

# The Collatz Sequence - the simplest impossible math problem
# No matter what number you enter this sequence will always arrive at 1


def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)


number = collatz(int(input('Enter a number. ')))
