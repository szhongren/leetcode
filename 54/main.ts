function spiralOrder(matrix: number[][]): number[] {
  let rows = matrix.length;
  let cols = matrix[0].length;
  // directions:
  // 0: right
  // 1: down
  // 2: left
  // 3: up
  let seen = new Set(
    [
      [0, -1],
      [0, cols],
      [-1, cols - 1],
      [rows, cols - 1],
      [rows - 1, cols],
      [rows - 1, -1],
      [-1, 0],
      [rows, 0],
      [1, -1],
    ].map((x) => x.toString())
  );
  function getNextCoordAndDirection(
    coords: number[],
    direction: number
  ): number[] {
    let [y, x] = coords;
    seen.add(coords.toString());
    // console.log(coords, direction);
    // console.log(seen);
    if (
      seen.has([y, x + 1].toString()) &&
      seen.has([y + 1, x].toString()) &&
      seen.has([y, x - 1].toString()) &&
      seen.has([y - 1, x].toString())
    )
      return [];
    if (direction === 0) {
      if (seen.has([y, x + 1].toString())) {
        return [y + 1, x, 1];
      }
      return [y, x + 1, direction];
    } else if (direction === 1) {
      if (seen.has([y + 1, x].toString())) {
        return [y, x - 1, 2];
      }
      return [y + 1, x, direction];
    } else if (direction === 2) {
      if (seen.has([y, x - 1].toString())) {
        return [y - 1, x, 3];
      }
      return [y, x - 1, direction];
    } else {
      if (seen.has([y - 1, x].toString())) {
        return [y, x + 1, 0];
      }
      return [y - 1, x, direction];
    }
  }
  let coordAndDirection = [0, 0, 0];
  let result: number[] = [];
  while (coordAndDirection.length !== 0) {
    let [y, x, direction] = coordAndDirection;
    result.push(matrix[y][x]);
    coordAndDirection = getNextCoordAndDirection([y, x], direction);
    // console.log(coordAndDirection);
  }
  return result;
}

// have a direction to go in, start with right
// if next coordinate is in seen,
// turn right
// continue
// seed with a barrier around the matrix

// console.log(
//   spiralOrder([
//     [1, 2, 3],
//     [4, 5, 6],
//     [7, 8, 9],
//   ])
// );

// console.log(
//   spiralOrder([
//     [1, 2, 3, 4],
//     [5, 6, 7, 8],
//     [9, 10, 11, 12],
//   ])
// );

console.log(
  spiralOrder([
    [2, 5],
    [8, 4],
    [0, -1],
  ])
);
