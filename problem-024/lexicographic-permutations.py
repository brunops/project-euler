# Lexicographic permutations
# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

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

def permute(elements, times):
  perm = 0
  while perm < times and next_permutation(elements):
    perm += 1



elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# permute 999999 times because elements itself is the first permutation
permute(elements, 999999)
print ''.join(map((lambda x: str(x)), elements))





