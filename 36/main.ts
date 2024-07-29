function isValidSudoku(board: string[][]): boolean {
  for (let i = 0; i < 9; i++) {
    let seen = new Set();
    for (let j = 0; j < 9; j++) {
      let val = board[i][j];
      //   console.log(i, j, val);
      if (val === ".") continue;
      if (seen.has(val)) return false;
      seen.add(val);
    }
  }
  for (let j = 0; j < 9; j++) {
    let seen = new Set();
    for (let i = 0; i < 9; i++) {
      let val = board[i][j];
      //   console.log(i, j, val);
      if (val === ".") continue;
      if (seen.has(val)) return false;
      seen.add(val);
    }
  }
  let topLeftCoords = [
    [0, 0],
    [0, 3],
    [0, 6],
    [3, 0],
    [3, 3],
    [3, 6],
    [6, 0],
    [6, 3],
    [6, 6],
  ];
  for (let coord of topLeftCoords) {
    let seen = new Set();
    while (coord.length !== 0) {
      let [i, j] = coord;
      let val = board[i][j];
      console.log(i, j, val);
      coord = getNextBoxCoord(coord);
      if (val === ".") continue;
      if (seen.has(val)) return false;
      seen.add(val);
    }
  }
  return true;
}

function getNextBoxCoord(coords: number[]): number[] {
  let [i, j] = coords;
  let threshold = new Set([2, 5, 8]);
  if (threshold.has(i) && threshold.has(j)) return [];
  if (threshold.has(j)) return [i + 1, j - 2];
  return [i, j + 1];
}
// 3 loops
// for i in 0..9
// for j in 0..9
// use set, if value in set, return false
// for j in 0..9
// for i in 0..9
// use set, if value in set, return false
// for coord in topleft coord of each box
// for coord in next_coord
// use set, if value in set, return false
// return true

console.log(
  isValidSudoku([
    [".", ".", ".", ".", ".", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["9", "3", ".", ".", "2", ".", "4", ".", "."],
    [".", ".", "7", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "3", "4", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "."],
    [".", ".", ".", ".", ".", "5", "2", ".", "."],
  ])
);
