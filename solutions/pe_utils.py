from bitarray import bitarray


def is_palindrome(s):
    s = str(s)
    for i in range(0, int(len(s) / 2)):
        other = len(s) - i - 1
        if s[i] != s[other]:
            return False
    return True


class PrimesIterator:
    sieve = bitarray()

    @staticmethod
    def extend_sieve():
        if len(PrimesIterator.sieve) == 0:
            PrimesIterator.sieve = bitarray([False, False, True])
        curr_max = len(PrimesIterator.sieve)
        PrimesIterator.sieve.extend(curr_max * [True])
        for i in range(2, len(PrimesIterator.sieve)):
            if PrimesIterator.sieve[i]:
                for j in range(i + i, len(PrimesIterator.sieve), i):
                    if PrimesIterator.sieve[j]:
                        PrimesIterator.sieve[j] = False

    def __init__(self):
        None

    def __iter__(self):
        self.count = 0
        self.curr_index = 0
        return self

    def __next__(self):
        curr_prime = None
        while curr_prime is None:
            self.curr_index += 1
            try:
                if PrimesIterator.sieve[self.curr_index]:
                    curr_prime = self.curr_index
                    return curr_prime
            except IndexError:
                self.extend_sieve()
                self.curr_index -= 1

        self.count += 1


def primes(max_num=0, max_count=0):
    pi = PrimesIterator()
    return iter(pi)
