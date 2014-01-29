# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallest_multiple(number):
  step = 1
  test = step

  # incorporate multiples
  for i in range(2, number + 1):
    while True:
      is_multiple = True
      # test if number is multiple of all incorporated numbers so far
      for j in range(1, i + 1):
        if test % j != 0:
          is_multiple = False
          break

      # if all numbers are multiple
      # incorporate test number as new step
      if is_multiple:
        step = test
        break

      test += step

  return test


print smallest_multiple(20)
