# Lattice paths
# Problem 15
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

def factorial(n):
  if n <= 2:
    return n
  else:
    return n * factorial(n - 1)

# Combinatory problem of "n choose k"
def total_lattice_paths(size):
  return factorial(size * 2) / (factorial(size) * factorial (size))

print total_lattice_paths(20)
