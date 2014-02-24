# Pandigital prime
# Problem 41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

from math import sqrt

def is_prime(number):
  for x in range(2, int(sqrt(number)) + 2):
    if number % x == 0:
      return False

  return True

# Returns boolean indicating if permutation was successful
# Code from problem 24
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

def int_array_to_number(elements):
  return int(''.join(map((lambda x: str(x)), elements)))

def largest_pandigital_prime():
  # We know that exists a number with 4 digits that is a pandigital number
  # namely 2143
  known_pandigital_number_size = 4

  # By the Divisibility Rule http://en.wikipedia.org/wiki/Divisibility_rule
  # A Pandigital number of size 8 or 9 is divisible by 3, so they're not prime
  # start with permutations with 7 numbers
  size = 7

  # We know that exists a number with 4 digits with the disired characteristics
  # So we can execute until 4
  while size >= 4:
    # generate range for permutations
    elements = range(1, size + 1)

    largest = 0

    number_from_elements = int_array_to_number(elements)
    if is_prime(number_from_elements):
      largest = number_from_elements

    # find biggest number for given total number of elements
    while next_permutation(elements):
      number_from_elements = int_array_to_number(elements)
      if number_from_elements > largest and is_prime(number_from_elements):
        largest = number_from_elements

    # no number with set of characteristics found
    if largest == 0:
      size -= 1
    # biggest number already found
    else:
      return largest

  return False

print largest_pandigital_prime()



