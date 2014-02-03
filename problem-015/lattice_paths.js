// Total Lattice paths for a grid using
// recursion + memoization

var results = {};
function lattice_paths(x, y) {
  // memoize results
  if (results[[x, y]]) {
    return results[[x, y]];
  }

  var paths = 0;

  if (x > 0) {
    // recurse vertically
    paths += lattice_paths(x - 1, y);
  }
  if (y > 0) {
    // recurse horizontally
    paths += lattice_paths(x, y - 1);
  }

  if (x == 0 && y == 0) {
    // reached destination
    paths += 1
  }

  // memoize and return
  return results[[x, y]] = paths
}

console.log(lattice_paths(20, 20));
