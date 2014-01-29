# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
from math import sqrt

def is_prime(number):
  for x in range(2, int(sqrt(number)) + 1):
    if number % x == 0:
      return False

  return True

def prime(position):
  current_position = 1
  current_number = 3

  # calculate primes until reaching desired position
  while current_position < position:
    if is_prime(current_number):
      current_position += 1

    # try only odd numbers (started with 3)
    current_number += 2

  return current_number


print prime(10001)
