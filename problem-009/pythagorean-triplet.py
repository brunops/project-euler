# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

# Use Euclid's formula to generate triples given m and n, where m > n
def generate_triplet(m, n):
  a = m**2 - n**2
  b = 2 * m * n
  c = m**2 + n**2
  return [a, b, c]

def pythagorean_triplet(total):
  m = 2
  n = 1

  for m in range(2, int(sqrt(total)) + 1):
    for n in range(1, m + 1):
      triplet = generate_triplet(m, n)
      # found!
      if sum(triplet) == total:
        return triplet

  return False

def pythagorean_triplet_product(total):
  triplet = pythagorean_triplet(total)

  if triplet:
    return reduce((lambda x, y: x * y), triplet)
  else:
    return False

print pythagorean_triplet_product(1000)
