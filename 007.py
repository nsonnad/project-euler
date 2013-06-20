# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

# create list of all potential divisors, up to sqrt of n
def divisors_of(n):
    divisors = []
    r = range(int(math.sqrt(n)) + 1)

    for num in r:
        divisors.append(num)

    return divisors


def is_prime(n):
    divisors = [1, n]
    div_range = divisors_of(n)
    # only look for at most one divisor, hence len < 4
    while len(divisors) < 4:
        for divisor in div_range:
            if n > divisor >= 2 and n % int(divisor) == 0:
                # is composite
                return 0
        # is prime
        return 1


def nth_prime(n):
    # have to start somewhere
    primes = [2]
    x = primes[-1] + 1
    # go until we reach n
    while len(primes) + 1 <= n:
        if is_prime(x) == 1:
            primes.append(x)
        # add two to skip even numbers
        x = x + 2
    # return nth prime
    return primes[-1]