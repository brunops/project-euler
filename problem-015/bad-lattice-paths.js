// Lattice Paths total for a given grid size
// This has NO memoization and will take a long time to run (more than an hour)
// use the other algorithms in this folder
function lat(size) {
  var paths = 0;

  function walk(row, col) {
    if (row == size && col == size) {
      paths++;
    }
    else {
      if (row < size) {
        walk(row + 1, col);
      }
      if (col < size) {
        walk(row, col + 1);
      }
    }
  }

  walk(0, 0);

  return paths;
}

console.log(lat(20));
