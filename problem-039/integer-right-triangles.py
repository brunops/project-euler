# encoding: utf-8
# Integer right triangles
# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

# Euclid's formula
# Return pythagorean triplet given m and n, where m > n
def pythagorean_triplet(m, n):
  a = m**2 - n**2
  b = 2 * m * n
  c = m**2 + n**2

  return [a, b, c]

def derive_triplet(triplet, modifier = 1):
  return map(lambda x: x * modifier, triplet)

def perimeter_for(triplet):
  return sum(triplet)

def maximized_solution(max_perimeter):
  perimeter_triplets = {}
  m = 2

  # find triplets and perimeters
  # while they may obey the invariant perimeter < max_perimeter
  while perimeter_for(pythagorean_triplet(m, 1)) <= max_perimeter:

    for n in range(1, m):
      triplet = pythagorean_triplet(m, n)
      perimeter = perimeter_for(triplet)

      add_triplet_for_perimeter(perimeter_triplets, perimeter, triplet)

      modifier = 2

      # find all combinations for given triplet
      while True:
        derived_triplet = derive_triplet(triplet, modifier)
        perimeter = perimeter_for(derived_triplet)

        if perimeter <= max_perimeter:
          add_triplet_for_perimeter(perimeter_triplets, perimeter, derived_triplet)
          modifier += 1
        else:
          break

    m += 1

  return max_triplets_perimeter(perimeter_triplets)

def add_triplet_for_perimeter(perimeter_triplets, perimeter, triplet):
  if perimeter not in perimeter_triplets:
    perimeter_triplets[perimeter] = set()

  perimeter_triplets[perimeter].add(frozenset(triplet))

def max_triplets_perimeter(perimeter_triplets):
  max_triplets = 0
  perimeter = 0

  for curr in perimeter_triplets:
    curr_triplets = len(perimeter_triplets[curr])
    if max_triplets < curr_triplets:
      max_triplets = curr_triplets
      perimeter = curr

  return perimeter


print maximized_solution(1000)
