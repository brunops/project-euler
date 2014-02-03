# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.
def divisors(n):
  divs = []
  for i in range(1, n / 2 + 1):
    if n % i == 0:
      divs.append(i)

  return divs
  
def sum_of_divisors(until):
  divisors_sum = {}
  for i in range(1, until + 1):
    divisors_sum[i] = sum(divisors(i))

  return divisors_sum

  
def amicable_numbers(until):
  divisors_sum = sum_of_divisors(until)
  amicables = []
  for i in range(1, until + 1):
    if divisors_sum[i] in divisors_sum \
      and i != divisors_sum[i] \
      and i == divisors_sum[divisors_sum[i]]:
        amicables.append(i)

  return amicables

def amicable_numbers_sum(until):
  return sum(amicable_numbers(until))

print amicable_numbers_sum(10000)
