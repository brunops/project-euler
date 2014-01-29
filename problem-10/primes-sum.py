# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from math import sqrt

def is_prime(number):
  for x in range(2, int(sqrt(number)) + 1):
    if number % x == 0:
      return False

  return True

def primes_sum(until):
  # first prime
  total = 2

  # first odd prime
  num = 3

  while num < until:
    if is_prime(num):
      total += num

    num += 2

  return total

print primes_sum(2000000)
