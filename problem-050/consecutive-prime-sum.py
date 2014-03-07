# Consecutive prime sum
# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?
def get_primes(until):
  sieve = [1] * until
  prime = 2

  primes = []

  while prime < until:
    if sieve[prime]:
      primes.append(prime)

      temp = prime + prime
      while temp < until:
        sieve[temp] = 0
        temp += prime

    prime += 1

  return primes

def longest_consecutive_prime_sum(until):
  primes = get_primes(until)

  primes_set = set(primes)
  primes_sum = [0]

  for i in range(0, len(primes)):
    primes_sum.append(primes_sum[i] + primes[i])


  total_primes = 0
  result = 0
  for i in range(0, len(primes_sum)):
    for j in range(i - (total_primes + 1), -1, -1):
      if primes_sum[i] - primes_sum[j] > until:
        break

      if primes_sum[i] - primes_sum[j] in primes_set:
        total_primes = i - j
        result = primes_sum[i] - primes_sum[j]

  return result

print longest_consecutive_prime_sum(1000000)
