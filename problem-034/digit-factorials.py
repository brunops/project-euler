# Digit factorials
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

factorials = {}
def factorial(number):
  if number <= 1:
    return 1
  elif number in factorials:
    return factorials[number]
  else:
    factorials[number] = number * factorial(number - 1)
    return factorials[number]

def digit_factorial_sum(number):
  return sum(map(lambda x: factorial(int(x)), list(str(number))))

def is_digit_factorial(number):
  return number == digit_factorial_sum(number)

def total_digit_factorials_sum():
  # upper bound is 9! * 7 = 2540160, since 9! * 8 results in a 7 digit number
  upper_bound = 2540161
  # exclude numbers that are not sums
  total = 0
  curr = 10
  while curr < upper_bound:
    if is_digit_factorial(curr):
      total += curr

    curr += 1

  return total

print total_digit_factorials_sum()
