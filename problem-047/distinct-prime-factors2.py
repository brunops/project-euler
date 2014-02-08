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

# Solve it all while generating the good old Sieve - waaaay faster algorithm


LIMIT = 200000

def consecutive_distinct_prime_factors_numbers(total_factors):
  # each number will account how many distinct factors it has
  sieve = [0] * LIMIT

  consecutive = 0
  for i in range(2, LIMIT):
    # prime factor
    if sieve[i] == 0:
      consecutive = 0
      temp = sieve[i]
      while temp < LIMIT:
        # add a factor to each number in sieve
        sieve[temp] += 1
        temp += i
    # number with total_factors found
    elif sieve[i] == total_factors:
      consecutive += 1
      if consecutive == total_factors:
        # first number
        return i - total_factors + 1
    # reset counter
    else:
      consecutive = 0

  # not found - try increasing the limit
  return False

print consecutive_distinct_prime_factors_numbers(4)



