# encoding: utf-8
#
# Reciprocal cycles
# Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10  =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def reciprocal_cycle_size(number):
  remainders = []
  remainder = 1 % number
  remainders.append(remainder)

  while remainder > 0:
    remainder *= 10
    remainder %= number

    # once the remainder was found before, it means we found a reccuring cycle
    if remainder in remainders:
      return len(remainders) - (remainders.index(remainder))
    else:
      remainders.append(remainder)

max_number = 1
max_size = 0
for i in reversed(range(1, 1001)):
  if max_size > i:
    break

  curr_size = reciprocal_cycle_size(i)
  if curr_size > max_size:
    max_size = curr_size
    max_number = i

print max_number
