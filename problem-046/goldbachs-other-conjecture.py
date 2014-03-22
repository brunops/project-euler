# encoding: utf-8
#
# Goldbach's other conjecture
# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
from math import sqrt

def get_sieve(until):
  sieve = [1] * until
  sieve[0] = 0
  sieve[1] = 0

  prime = 2
  while prime < until:
    if sieve[prime] == 1:
      temp = prime + prime
      while temp < until:
        sieve[temp] = 0
        temp += prime

    prime += 1

  return sieve

def get_primes_from_sieve(sieve):
  primes = []

  for i in range(0, len(sieve)):
    if sieve[i] == 1:
      primes.append(i)

  return primes

sieve = get_sieve(10000)
primes = get_primes_from_sieve(sieve)

# short description for composite numbers..
# => numbers that are _not_ a prime
def is_composite_odd(number):
  return sieve[number] == 0 and number % 2 != 0

def get_twice_square(n):
  return 2 * n ** 2

def does_comply_with_goldbach_conjecture(number):
  n = 1
  current_twice_square = get_twice_square(n)

  while current_twice_square < number:
    for prime in primes:
      if current_twice_square + prime > number:
        break

      if sieve[number] == 0 and number == current_twice_square + prime:
        return True

    n += 1
    current_twice_square = get_twice_square(n)

  return False

def first_odd_composite_that_doesnt_comply():
  # run through odd numbers
  i = 9
  while sieve[i] == 1 or does_comply_with_goldbach_conjecture(i):
    i += 2

  return i

print first_odd_composite_that_doesnt_comply()
