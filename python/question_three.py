"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from datetime import datetime
startTime = datetime.now()

def prime_factor(n):

    if n % 2 == 0:

        while n % 2 == 0:
            n = n / 2
        return n

    else:
        factor = 3

        while n % factor != 0:
            factor += 1

        if factor == n:
            return factor

        else:
            return prime_factor(n / factor)

print prime_factor(600851475143)

print datetime.now() - startTime
