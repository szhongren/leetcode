function numIslands(grid: string[][]): number {
  let land: Set<string> = new Set();
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      const cell = grid[i][j];
      if (cell === "1") {
        land.add(JSON.stringify([i, j]));
      }
    }
  }

  function getAdjacentCells(cell: number[]): number[][] {
    const [i, j] = cell;
    const adjacentCells = [
      [i - 1, j],
      [i + 1, j],
      [i, j - 1],
      [i, j + 1],
    ];
    return adjacentCells.filter(([i, j]) => land.has(JSON.stringify([i, j])));
  }

  let result = 0;
  while (land.size > 0) {
    let rep = JSON.parse(land.values().next().value);
    let currentLevel = [rep];
    let seen = new Set();
    // console.log("outer loop");
    // console.log(rep);
    // console.log(currentLevel);
    // console.log(seen);
    while (currentLevel.length !== 0) {
      currentLevel = currentLevel.flatMap((coord) => {
        // console.log("inner loop");
        // console.log(coord);
        seen.add(JSON.stringify(coord));
        land.delete(JSON.stringify(coord));
        return getAdjacentCells(coord).filter(
          (coord2) => !seen.has(JSON.stringify(coord2))
        );
      });
      //   console.log(currentLevel);
      //   console.log(seen);
      //   console.log("---------------------------");
    }
    result++;
  }
  return result;
}

// do a kind of bfs
// for every cell in the Set
// find all connected cells
// start with list of just that cell
// while list is not empty
// take every item in the list, land.delete(item) and calculate adjacent cells
// add them to a new list if not seen before
// set list to new list

// 2 steps
// convert to sparse graph with just indices of 1s
// iterate through those

console.log(
  numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
  ])
);

console.log(
  numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
  ])
);
