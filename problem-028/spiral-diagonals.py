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

#  111 112 113 114 115 116 117 118 119 120 121
#  110 73  74  75  76  77  78  79  80  81  82
#  109 72  43  44  45  46  47  48  49  50  83
#  108 71  42  21  22  23  24  25  26  51  84
#  107 70  41  20  7   8   9   10  27  52  85
#  106 69  40  19  6   1   2   11  28  53  86
#  105 68  39  18  5   4   3   12  29  54  87
#  104 67  38  17  16  15  14  13  30  55  88
#  103 66  37  36  35  34  33  32  31  56  89
#  102 65  64  63  62  61  60  59  58  57  90
#  101 100 99  98  97  96  95  94  93  92  91
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
