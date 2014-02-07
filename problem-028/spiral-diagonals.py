# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
def print_matrix(matrix):
  for i in range(0, len(matrix)):
    print matrix[i]

def spiral_matrix(size):
  # odd number required
  if size % 2 == 0:
    size += 1

  # generate matrix
  matrix = []
  for i in range(0, size):
    matrix.append([0] * size)

  # populate in spiral
  current_size = 1
  number = 1

  # set starting point
  row = size / 2
  col = size / 2
  matrix[row][col] = number
  number += 1
  current_size += 2

  while current_size <= size:
    # right column
    col += 1
    for i in range(0, current_size - 1):
      matrix[row][col] = number
      number += 1
      row += 1

    # lower row
    row -= 1
    for i in range(0, current_size - 1):
      col -= 1
      matrix[row][col] = number
      number += 1

    # left column
    for i in range(0, current_size - 1):
      row -= 1
      matrix[row][col] = number
      number += 1

    # upper row
    for i in range(0, current_size - 1):
      col += 1
      matrix[row][col] = number
      number += 1

    # odd multiples
    current_size += 2

  return matrix

def spiral_matrix_diagonals_sum(size):
  matrix = spiral_matrix(size)

  total = 0
  for i in range(0, size):
    total += matrix[i][i] + matrix[i][size - i - 1]

  # central element (1) is counted twice, remove it
  total -= 1

  return total


print spiral_matrix_diagonals_sum(1001)
