# encoding: utf-8
#
# Pandigital multiples
# Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def form_pandigital(number):
  n = 2
  str_number = str(number)
  while len(str_number) < 9:
    str_number += str(n * number)
    n += 1

  if '0' not in str_number and len(str_number) == 9 and len(set(list(str_number))) == 9:
    return int(str_number)
  else:
    return None

max_pandigital = 0
number = 1
while len(str(number) + str(number * 2)) <= 9:
  pandigital = form_pandigital(number)
  if pandigital:
    max_pandigital = max(max_pandigital, pandigital)

  number += 1

print max_pandigital



