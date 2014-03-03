# Non-abundant sums
# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from math import sqrt

def get_divisors(number):
  divisors = [1]
  for i in range(2, int(sqrt(number)) + 1):
    if number % i == 0:
      divisors.append(i)

      if number / i != i:
        divisors.append(number / i)

  divisors.sort()

  return divisors

def is_abundant(number, divisors = None):
  divisors = divisors or get_divisors(number)
  return sum(divisors) > number


print is_abundant(11)
print is_abundant(12)
print is_abundant(13)
