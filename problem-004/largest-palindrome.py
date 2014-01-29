# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
  return str(num) == str(num)[::-1]

def largest_palindrome_multiplication(max_range, min_range):
  largest = 0
  num1 = max_range
  while num1 > min_range:
    num2 = max_range

    # check if there's a chance of finding a bigger palindrome
    if (not (num1 * num2 > largest)):
      break

    while (num2 > min_range):
      palindrome_test = num1 * num2
      if (is_palindrome(palindrome_test)):
        largest = max(largest, palindrome_test)

      num2 -= 1
    num1 -= 1

  return largest

print largest_palindrome_multiplication(999, 100)
