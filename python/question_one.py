"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""
from datetime import datetime
startTime = datetime.now()

#slow


print sum([i for i in range(1000) if (i % 3 == 0) | (i % 5 == 0)])
print datetime.now() - startTime


#faster


def sum_divisible_by_n(n,target):

    p = target / n

    return n * 0.5 * p * (p+1)

startTime = datetime.now()

print sum_divisible_by_n(3,999) + sum_divisible_by_n(5,999) - sum_divisible_by_n(15,999)
print datetime.now() - startTime

