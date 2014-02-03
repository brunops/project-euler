# Total Lattice paths using recursion + memoization

require 'memoize'
include Memoize

def lattice_paths(row, col)
  paths = 0

  if row > 0
    # recurse vertically
    paths += lattice_paths(row - 1, col)
  end

  if col > 0
    # recurse horizontally
    paths += lattice_paths(row, col - 1)
  end

  if row == 0 && col == 0
    # reached destination
    paths += 1
  end

  return paths
end

# make stuff fast
memoize :lattice_paths

p lattice_paths(20, 20)
