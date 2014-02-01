# USING DYNAMIC PROGRAMMING
#
# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. # Although it has not been proved yet (Collatz Problem), it is thought that all starting # numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
def longest_collatz_sequence_number(until):
  # Collatz Sequence starting with 2 has size 2 (2 -> 1)
  sequence_sizes = { 2: 2 }

  # Use dynamic programming on overlapping subproblems to find solution faster
  def collatz_sequence_size(number):
    # return size of sequence if already calculated
    if number in sequence_sizes:
      return sequence_sizes[number]
    # recursively calculate new sequence sizes
    else:
      next = next_collatz_number(number)
      sequence_sizes[number] = 1 + collatz_sequence_size(next)

    # return calculated sequence size
    return sequence_sizes[number]

  # largest sequence until
  largest_sequence_size = 2
  number_that_generated_sequence = 2
  for i in range(2, until + 1):
    sequence_size = collatz_sequence_size(i)
    if (largest_sequence_size < sequence_size):
      number_that_generated_sequence = i
      largest_sequence_size = sequence_size

  return number_that_generated_sequence

def next_collatz_number(number):
  if number % 2 == 0:
    return number / 2
  else:
    return 3 * number + 1

print longest_collatz_sequence_number(1000000)
