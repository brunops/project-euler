# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
def largest_prime_factor(number):
  if number == 1:
    return 1

  test = 2
  while number > 1:
    if number % test == 0:
      number /= test
    else:
      test += 1

  return test


print largest_prime_factor(600851475143)
