# encoding: utf-8
#
# Digit canceling fractions
# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import gcd

def incorrectly_simplified(num, den):
  splitted_num = list(str(num))
  splitted_den = list(str(den))

  for digit in splitted_num:
    if digit != '0' and digit in splitted_den:
      filtered_num = ''.join(filter(lambda x: x != digit, splitted_num))
      filtered_den = ''.join(filter(lambda x: x != digit, splitted_den))

      if len(filtered_num) == 0 or len(filtered_den) == 0:
        return False
      else:
        filtered_num = float(filtered_num)
        filtered_den = float(filtered_den)

        if filtered_den == 0:
          return False

      if num / float(den) == filtered_num / filtered_den:
        return True

def digit_canceling_fractions_product(until):
  fractions = []
  for num in range(1, until):
    for den in range(num + 1, until):
      if incorrectly_simplified(num, den):
        # store valid fractions as an array of numerator and denominator
        fractions.append([num, den])

  # multiply fractions
  fractions_product = reduce(lambda x, y: [x[0] * y[0], x[1] * y[1]], fractions)

  return fractions_product[1] / gcd(fractions_product[0], fractions_product[1])

print digit_canceling_fractions_product(100)

assert(incorrectly_simplified(1, 1) == False)
assert(incorrectly_simplified(49, 98) == True)
