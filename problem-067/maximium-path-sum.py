# encoding: utf-8
# Maximum path sum II
# Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
# 
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
# 

# Solve it using dynamic programming from bottom row to first row ... exactly same thing as problem 18
def max_path_sum(matrix):
  for row in reversed(range(0, len(matrix) - 1)):
    for col in range(0, len(matrix[row])):
      matrix[row][col] += max(matrix[row + 1][col], matrix[row + 1][col + 1])

  return matrix[0][0]

matrix = [line.rstrip('\n') for line in open('triangle.txt')]
matrix = [map(int, row.split(' ')) for row in matrix]

print max_path_sum(matrix)
