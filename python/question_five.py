"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def gcd(a,b):

    if max(a,b) % min(a,b) == 0:

        answer = min(a,b)

        return answer

    else:

        return gcd(min(a,b), max(a,b) % min(a,b))

def lcm(a,b):

    return abs(a*b) / gcd(a,b)

series = range(1,21)

print reduce(lcm, series)


