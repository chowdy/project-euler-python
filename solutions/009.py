"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solution():
    for c in range(1000, 0, -1):
        for b in range(c-1, 0, -1):
            for a in range(1000 - (b + c), 0, -1):
                if a + b + c == 1000 and a*a + b*b == c*c:
                    return a*b*c
