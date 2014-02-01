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
def collatz_sequence(number):
  sequence = []
  while number > 1:
    sequence.append(number)
    if (number % 2 == 0):
      number /= 2
    else:
      number = 3 * number + 1

  sequence.append(1)

  return sequence

def longest_collatz_sequence_number(until):
  longest_sequence_size = 1
  number = 2
  for i in range(2, until + 1):
    seq = collatz_sequence(i)
    seq_len = len(seq)
    if (seq_len > longest_sequence_size):
      longest_sequence_size = seq_len
      number = i

  return number

print longest_collatz_sequence_number(1000000)


