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
    number_slice = array_to_number(splitted_number[i + 1:i + 4])

    if number_slice % primes[i] != 0:
      is_property_present = False
      break

  return is_property_present

# Returns boolean indicating if permutation was successful
def next_permutation(elements):
  # find elements suffix index, from right to left
  suffix_index = len(elements) - 1
  while (suffix_index > 0 and elements[suffix_index - 1] >= elements[suffix_index]):
    suffix_index -= 1

  # Return False if already last permutation
  if suffix_index == 0:
    return False

  # Define pivot index as first element to the left of the suffix (necessairly smaller)
  pivot_index = suffix_index - 1

  # Minimize the prefix by swaping the pivot with the smallest number on the suffix that is greater than the pivot
  # Find smallest number that is greater than the pivot on the suffix
  smallest_prefix_index = len(elements) - 1
  while (elements[smallest_prefix_index] <= elements[pivot_index]):
    smallest_prefix_index -= 1

  # Swap pivot with smallest
  temp = elements[pivot_index]
  elements[pivot_index] = elements[smallest_prefix_index]
  elements[smallest_prefix_index] = temp

  # Make suffix as small as possible because prefix was increased
  # This can be achieved by reversing the suffix
  elements[suffix_index:] = elements[suffix_index:][::-1]

  return True

def sum_of_pandigital_numbers_with_divisibility_property(until):
  elements = range(until)

  total = 0
  number = array_to_number(elements)
  if has_divisibility_property(number):
    total += number

  while next_permutation(elements):
    number = array_to_number(elements)
    if has_divisibility_property(number):
      print number
      total += number

  return total

def array_to_number(elements):
  return int(''.join(map(str, elements)))

print sum_of_pandigital_numbers_with_divisibility_property(10)
