function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  let rows = obstacleGrid.length;
  let cols = obstacleGrid[0].length;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (obstacleGrid[i][j] === 1) {
        obstacleGrid[i][j] = 0;
        continue;
      }
      let topValue = i === 0 ? 0 : obstacleGrid[i - 1][j];
      let leftValue = j === 0 ? 0 : obstacleGrid[i][j - 1];
      obstacleGrid[i][j] = topValue + leftValue;
    }
  }
  return obstacleGrid[rows - 1][cols - 1];
}
