"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 =

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
"""
from datetime import datetime
startTime = datetime.now()

# slow

print sum([i for i in range(101)])**2 - sum([i**2 for i in range(101)])

print datetime.now() - startTime

# faster

startTime = datetime.now()


def sum_n_numbers(n):
    return 0.5 * n * (n+1)


def sum_square_numbers(n):
    return (n * (n+1) *  (2*n+1)) * 1/6

print sum_n_numbers(100)**2 - sum_square_numbers(100)

print datetime.now() - startTime
