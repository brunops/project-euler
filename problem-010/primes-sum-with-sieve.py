# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def primes_sum(until):
  sieve = [1] * until
  total = 2
  curr = 3

  while curr < until:
    if sieve[curr]:
      total += curr
      temp = curr
      while temp < until:
        sieve[temp] = 0
        temp += curr

    curr += 2

  return total


print primes_sum(2000000)
