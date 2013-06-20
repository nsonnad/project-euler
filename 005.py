# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

# This solution works, but is a bit slow!

def divisible_by(n, range_min, range_max):
    x = range_max

    while x > range_min + 1:
        if n % x != 0:
            return False
        else:
            x = x - 1

    return True


def smallest_mult(range_min, range_max):
    n = range_max

    while divisible_by(n, range_min, range_max) is False:
        n = n + range_max

    return n