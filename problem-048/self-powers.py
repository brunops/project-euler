# Self powers
# Problem 48
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

def self_powers_sum(until):
  return reduce((lambda x, y: x + y), map((lambda x: x ** x), range(1, until + 1)))

print ''.join(list(str(self_powers_sum(1000)))[-10:])
