# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025#
# Hence the difference between the sum of the squares of the first ten natural numbers and # the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference(number):
  nums = range(1, number + 1)
  return sum(nums)**2 - sum(map((lambda x: x**2), nums))

print sum_square_difference(100)
