from bitarray import bitarray


def is_palindrome(s):
    s = str(s)
    for i in range(0, int(len(s) / 2)):
        other = len(s) - i - 1
        if s[i] != s[other]:
            return False
    return True


def get_prime_factors(n):
    prime_factors = []
    for prime in PrimesIterator():
        if n % prime == 0:
            prime_factors.append(prime)
        if prime > n:
            return prime_factors


def get_divisors(n):
    divisors = []
    n2 = n
    i = 1
    if n == 1:
        return [1]
    while i < n2:
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n / i))
            n2 = int(n / i)
        i += 1
    return divisors


# Not sure if this is actually any faster than get_divisors(), but it's fun lol
def get_num_divisors(n):
    divisors = 0
    n2 = n
    i = 1
    if n == 1:
        return 1
    while i < n2:
        if n % i == 0:
            divisors += 2
            n2 = int(n / i)
        i += 1
    return divisors


primes_sieve = bitarray()


def is_prime(n):
    try:
        return primes_sieve[n]
    except IndexError:
        extend_sieve()
        return is_prime(n)


def extend_sieve():
    global primes_sieve
    if len(primes_sieve) == 0:
        primes_sieve = bitarray([False, False, True, True])
    curr_max = len(primes_sieve)
    primes_sieve.extend(curr_max * [True])

    for i in range(2, len(primes_sieve)):
        if primes_sieve[i]:
            for j in range(i + i, len(primes_sieve), i):
                if primes_sieve[j]:
                    primes_sieve[j] = False


class PrimesIterator:

    def __init__(self):
        None

    def __iter__(self):
        self.count = 0
        self.curr_index = 0
        return self

    def __next__(self):
        global primes_sieve
        while True:
            self.curr_index += 1
            if is_prime(self.curr_index):
                return self.curr_index


class TriangleNumbersIterator:

    def __iter__(self):
        self.current = 0
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        self.current += self.count
        return self.current


class CollatzCounter:

    memo = {}

    @classmethod
    def count(cls, start):
        count = 1
        n = start
        while n != 1:
            if cls.memo.get(n):
                count += cls.memo[n] - 1
                break
            if n % 2 == 0:
                n = int(n/2)
            else:
                n = int(3*n+1)
            count += 1
        cls.memo[start] = count
        return count
