function minPathSum(grid: number[][]): number {
  let rows = grid.length;
  let cols = grid[0].length;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (i === 0 && j === 0) continue;
      else if (i === 0) grid[i][j] = grid[i][j] + grid[i][j - 1];
      else if (j === 0) grid[i][j] = grid[i][j] + grid[i - 1][j];
      else grid[i][j] = grid[i][j] + Math.min(grid[i][j - 1], grid[i - 1][j]);
    }
  }
  return grid[rows - 1][cols - 1];
}

// for row in grid
// for val in row
// val = val + min(grid[i - 1][j], grid[i][j - 1])
// return bottom right of grid
