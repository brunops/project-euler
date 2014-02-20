# Circular primes
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
def get_sieve(until):
  sieve = [1] * until
  prime = 2
  while prime < until:
    if sieve[prime]:
      temp = prime + prime
      while temp < until:
        sieve[temp] = 0
        temp += prime

    prime += 1

  return sieve

def is_circular_prime(n, sieve):
  # return false if number itself is not prime
  if sieve[n] == 0:
    return False

  # check each rotation
  n = list(str(n))
  rotations = len(n) - 1
  while rotations > 0:
    last = [n.pop()]
    n = last + n

    # return false if current rotation is not a prime
    if sieve[int(''.join(n))] == 0:
      return False

    rotations -= 1

  return True

def total_circular_primes(until):
  total = 0
  sieve = get_sieve(until)
  for i in range(2, until):
    if is_circular_prime(i, sieve):
      total += 1

  return total


print total_circular_primes(1000000)
