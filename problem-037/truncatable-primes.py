# Truncatable primes
# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def get_sieve(until):
  sieve = [1] * until
  sieve[1] = 0
  prime = 2
  while prime < until:
    if sieve[prime]:
      temp = prime + prime
      while temp < until:
        sieve[temp] = 0
        temp += prime

    prime += 1

  return sieve

def is_left_truncatable_prime(num, sieve):
  while sieve[num] and len(str(num)) > 1:
    num = int(''.join(list(str(num))[1:]))

  return (sieve[num] == 1 and len(str(num)) == 1)

def is_right_truncatable_prime(num, sieve):
  while sieve[num] and len(str(num)) > 1:
    num = int(''.join(list(str(num))[:-1]))

  return (sieve[num] == 1 and len(str(num)) == 1)

def is_truncatable_prime(num, sieve):
  return is_left_truncatable_prime(num, sieve) and is_right_truncatable_prime(num, sieve)


sieve = get_sieve(1000000)
total = 0
for i in range(13, 1000000):
  if is_truncatable_prime(i, sieve):
    total += i

print total

