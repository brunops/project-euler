# Even Fibonacci numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def even_fib_sum(until):
  previous = 1
  current = 2
  total = 0

  while current <= until:
    if current % 2 == 0:
      total += current

    current = current + previous
    previous = current - previous

  return total

print even_fib_sum(4000000)
