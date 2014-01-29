# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
def prime(position):
  primes = [2]
  current_position = 1
  current_number = 3

  # calculate primes until reaching desired position
  while current_position < position:
    is_prime = True
    for prime in primes:
      if current_number % prime == 0:
        is_prime = False
        break

    if is_prime:
      primes.append(current_number)
      current_position += 1

    # try only odd numbers (started with 3)
    current_number += 2

  return primes[len(primes) - 1]


print prime(10001)
