# Distinct primes factors
# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 x 7
# 15 = 3 x 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.
#
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

import copy

# Generate primes array using the Sieve of Eratosthenes
def primes_until(until):
  primes = [2]
  primes_index = { 2: 0 }

  sieve = [1] * until
  prime = 3
  prime_index = 1

  while prime < until:
    if sieve[prime]:
      primes.append(prime)
      primes_index[prime] = prime_index
      prime_index += 1
      temp = prime
      while temp < until:
        sieve[temp] = 0
        temp += prime

    prime += 2

  # Define hash and array for awesome quick access for:
  # next_prime => access number index in hash O(1), use array to access index + 1 O(1) too
  return {
    'primes': primes,
    'primes_index': primes_index
  }


# use global to store primes list - blargh :P
primes_list = primes_until(5000000)
print 'sieve generated'
def next_prime(n):
  prime_index = primes_list['primes_index'][n]
  return primes_list['primes'][prime_index + 1]


def prime_factors(n):
  factors = []
  prime = 2

  while n > 1:
    if n % prime == 0:
      factors.append(prime)
      n /= prime
    else:
      prime = next_prime(prime)

  return factors

def distinct_prime_factors(n):
  factors = prime_factors(n)

  # map factors to a dictionary with the count of each element
  factors_count = dict([(x, factors.count(x)) for x in set(factors)])

  # map arrays to its corresponding power
  # [2, 2, 3] => [4, 3]
  distinct_factors = []
  for number in factors_count.keys():
    distinct_factors.append(number**factors_count[number])

  return distinct_factors

def distinct_prime_factors_consecutive_numbers(total_factors):
  # first number
  numbers = [2]

  # first number has one factor => 2
  numbers_factors = [[2]]

  # current number
  number = 2

  while len(numbers) < total_factors:
    factors = distinct_prime_factors(number)
    # possible valid result
    if len(factors) == total_factors:
      numbers_factors_copy = copy.deepcopy(numbers_factors)
      numbers_factors_copy.append(factors)
      # add number to result
      if distinct_arrays(numbers_factors_copy):
        numbers_factors.append(factors)
        numbers.append(number)
      # start over
      else:
        numbers_factors = [factors]
        numbers = [number]
    # start over, numbers must be consecutive
    else:
      numbers_factors = []
      numbers = []

    number += 1

  return numbers

def distinct_arrays(arrays):
  all_numbers = []
  for array in arrays:
    all_numbers += array

  return len(all_numbers) == len(set(all_numbers))


print distinct_prime_factors_consecutive_numbers(4)
