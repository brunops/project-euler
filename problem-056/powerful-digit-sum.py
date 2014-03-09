# Powerful digit sum
# Problem 56
# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def digit_sum(number):
  return sum(map(lambda x: int(x), list(str(number))))

def max_digit_sum(a, b):
  maximum = 0
  for i in range(1, a + 1):
    for j in range(1, b + 1):
      maximum = max(maximum, digit_sum(i ** j))

  return maximum
  
print max_digit_sum(99, 99)
