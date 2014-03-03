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

def can_be_written_as_sum(number, abundant_numbers, abundant_numbers_lookup):
  for num1 in abundant_numbers:
    if number - num1 in abundant_numbers_lookup:
      return True

  return False

# sum_of_numbers_that_cannot_be_written_as_sum_of_two_abundant_numbers was too big
def non_abundant_sums(upper_bound):
  abundant_numbers = []
  index = 0
  abundant_numbers_lookup = {}

  total = 0
  for n in range(1, upper_bound):
    if is_abundant(n):
      abundant_numbers.append(n)
      abundant_numbers_lookup[n] = index
      index += 1

    if not can_be_written_as_sum(n, abundant_numbers, abundant_numbers_lookup):
      total += n

  return total


print non_abundant_sums(28123)
