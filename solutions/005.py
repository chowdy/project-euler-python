"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def solution():
    max_num = 20
    i = 0
    while True:
        i += max_num * 3 * 7 * 11 * 13 * 17 * 19
        for j in range(2, max_num + 1):
            if i % j != 0:
                break
            elif j == max_num:
                return i
