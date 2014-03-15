# Path sum: two ways
# Problem 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
# *131*  673   234   103   18
# *201* *96*  *342*  965   150
# 630    803  *746*  *422* 111
# 537    699   497   *121* 956
# 805    732   524   *37*  *331*
#
# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.


def minimal_path_sum(file_name):
  matrix = [line.rstrip('\n') for line in open('matrix.txt')]
  matrix = [map(int, row.split(',')) for row in matrix]

  size = len(matrix)
  # calculate minimal sums for bottom row and last column
  # as they don't have any other way to be reached
  for i in reversed(range(0, size - 1)):
    matrix[size - 1][i] += matrix[size - 1][i + 1]
    matrix[i][size - 1] += matrix[i + 1][size - 1]

  for i in reversed(range(0, size - 1)):
    for j in reversed(range(0, size - 1)):
      matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

  return matrix[0][0]



print minimal_path_sum('matrix.txt')
