function minimumTotal(triangle: number[][]): number {
  for (let i = triangle.length - 2; i >= 0; i--) {
    let row = triangle[i];
    for (let j = 0; j < row.length; j++) {
      triangle[i][j] =
        triangle[i][j] + Math.min(triangle[i + 1][j], triangle[i + 1][j + 1]);
    }
  }
  return triangle[0][0];
}

// DP from the lowest level of the triangle
// for each level above the lowest, set value = value + min(triangle[i + 1][j], triangle[i + 1][j + 1])
// return triangle [0][0]
