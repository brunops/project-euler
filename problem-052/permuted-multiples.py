# Permuted multiples
# Problem 52
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def same_digit_multiples(number, multiples):
  sorted_digits = sorted(str(number))

  for m in multiples:
    if sorted(str(number * m)) != sorted_digits:
      return False

  return True

curr = 1
while not same_digit_multiples(curr, [2, 3, 4, 5, 6]):
  curr += 1

print curr
