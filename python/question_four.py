
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrom made from the product of two 3-digit numbers
"""

from datetime import datetime
startTime = datetime.now()

from math import sqrt

for n in reversed(range(100,998)): #999 * 999 is 998001 so largest palindrom is 997799

    palindrome = int(str(n)+str(n)[::-1])

    root_palindrome = int(sqrt(palindrome)) #one of the factors must be larger than palindrome ** 1/2

    for i in reversed(range(root_palindrome, 1000)):

        if palindrome % i == 0 and palindrome/i < 1000:

            j = palindrome/i

            print i * j

            break

        else:
            pass

print datetime.now() - startTime



