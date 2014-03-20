# Double-base palindromes
# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrome(number):
  str_number = str(number)
  return str_number == ''.join(reversed(list(str_number)))

def total_double_base_palindromes(until):
  total = 0
  curr = 1
  while curr < until:
    if is_palindrome(curr) and is_palindrome(bin(curr)[2:]):
      total += curr

    curr += 1

  return total

print total_double_base_palindromes(1000000)
