# Sub-string divisibility
# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2 d3 d4 = 406 is divisible by 2
# d3 d4 d5 = 063 is divisible by 3
# d4 d5 d6 = 635 is divisible by 5
# d5 d6 d7 = 357 is divisible by 7
# d6 d7 d8 = 572 is divisible by 11
# d7 d8 d9 = 728 is divisible by 13
# d8 d9 d10 = 289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

def has_divisibility_property(number):
  is_property_present = True

  primes = [2, 3, 5, 7, 11, 13, 17]
  splitted_number = list(str(number))

  for i in range(len(primes)):
    # generate integer with 3 numbers
    number_slice = int(''.join(splitted_number[i + 1:i + 4]))

    if number_slice % primes[i] != 0:
      is_property_present = False
      break

  return is_property_present

print has_divisibility_property(1406357289)
