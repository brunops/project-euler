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
primes_list = primes_until(5000)
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

def distinct_prime_factors_consecutive_numbers(total_factors):
  # first number
  numbers = [2]

  # first number has one factor => 2
  numbers_factors = [[2]]

  # current number
  number = 2

  while len(numbers) < total_factors:


    number += 1

  return numbers

def distinct_arrays(arrays):
  # map arrays to a dictionary with a count of each element
  arrays = map((lambda array: dict([(x, array.count(x)) for x in set(array)])), arrays)

  # store all factors
  all_factors = []
  # map arrays to its corresponding power
  # [[2, 2], [2]] => [[4], [2]]
  for i in range(len(arrays)):
    factors = []
    for number in arrays[i].keys():
      factors.append(number**arrays[i][number])

    all_factors += factors

  return len(all_factors) == len(set(all_factors))


print distinct_arrays([[2,2], [2, 2]])
# print distinct_prime_factors_consecutive_numbers(2)
# print distinct_prime_factors_consecutive_numbers(3)
