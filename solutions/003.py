"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def solution():
    number = int(600851475143)
    current = number
    last = None
    while current > 1:
        for i in range(2, int(current) + 1):
            if current % i == 0:
                current = int(current / i)
                last = i
                break
    return last
