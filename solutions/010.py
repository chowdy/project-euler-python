"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import solutions.pe_utils as pe


def solution():
    answer = 0
    for p in pe.PrimesIterator():
        if p >= 2e6:
            return answer
        answer += p
