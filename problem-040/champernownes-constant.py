# encoding: utf-8
#
# Champernowne's constant
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def champernownes_constant_digit_at(position):
  if position == 1:
    return 1

  total_digits = 0
  decimal_order = 1

  while total_digits < position:
    total_order_digits = total_digits_of_order(decimal_order)

    if total_digits + total_order_digits < position:
      total_digits += total_order_digits
      decimal_order += 1
    # position is in current decimal order
    else:
      # start with first number of current order
      curr_number = 10 ** (decimal_order - 1)

      while total_digits + decimal_order < position:
        curr_number += 1
        total_digits += decimal_order

      return int(str(curr_number)[position - total_digits - 1])

  return decimal_order

def total_numbers_of_order(order):
  return (10 ** order) - (10 ** (order - 1))

def total_digits_of_order(order):
  return order * total_numbers_of_order(order)

# some tests, bro
assert(total_numbers_of_order(1) == 9)
assert(total_numbers_of_order(2) == 90)
assert(total_numbers_of_order(3) == 900)
assert(total_numbers_of_order(4) == 9000)

assert(total_digits_of_order(1) == 9)
assert(total_digits_of_order(2) == 180)
assert(total_digits_of_order(3) == 2700)
assert(total_digits_of_order(4) == 36000)

assert(champernownes_constant_digit_at(1) == 1)
assert(champernownes_constant_digit_at(2) == 2)
assert(champernownes_constant_digit_at(3) == 3)

assert(champernownes_constant_digit_at(12) == 1)
assert(champernownes_constant_digit_at(13) == 1)
assert(champernownes_constant_digit_at(14) == 1)


# Problem solution
def problem_40():
  total = 1
  for i in range(0, 7):
    total *= champernownes_constant_digit_at(10 ** i)

  return total

print problem_40()

