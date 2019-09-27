"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import solutions.pe_utils as pe


def solution():
    count = 0
    for i in pe.primes():
        count += 1
        if count == 10001:
            return i
