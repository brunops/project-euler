# Lychrel numbers
# Problem 55
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
#
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

def is_palindrome(number):
  str_number = str(number)
  return str_number == str_number[::-1]

def is_number_plus_reverse_palindromic(number):
  str_number = str(number)
  str_reverse = str_number[::-1]

  return is_palindrome(number + int(str_reverse))

def find_lychrel_numbers(until, max_iterations):
  total_lychrel_numbers = until

  for number in range(1, until + 1):
    tests = []
    curr_number = number
    curr_iteration = 0

    while curr_iteration < max_iterations:
      if is_number_plus_reverse_palindromic(curr_number):
        total_lychrel_numbers -= 1
        break
      else:
        curr_number += int(str(curr_number)[::-1])

      curr_iteration += 1

  return total_lychrel_numbers


print find_lychrel_numbers(10000, 50)
