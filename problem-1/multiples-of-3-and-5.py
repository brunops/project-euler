# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_3_or_5(limit):
  sum = 0
  for val in range(1, limit):
    if val % 3 == 0 or val % 5 == 0:
      sum += val

  return sum

print multiples_of_3_or_5(1000)
