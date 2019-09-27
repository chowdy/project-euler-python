"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import solutions.pe_utils as pe


def solution():
    answer = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            p = int(i*j)
            if p < answer:
                break
            if pe.is_palindrome(p):
                if p > answer:
                    answer = p
    return answer
