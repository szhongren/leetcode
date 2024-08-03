function findMinArrowShots(points: number[][]): number {
  let sortedBallons = points.sort((a, b) => b[0] - a[0]);
  let pops = 0;
  while (sortedBallons.length !== 0) {
    let intersection: number[] = [];
    while (true) {
      let balloon = sortedBallons.pop();
      if (!balloon) break;
      if (intersection.length === 0) intersection = balloon;
      let newIntersection = findIntersection(intersection, balloon);
      if (newIntersection.length === 0) {
        sortedBallons.push(balloon);
        break;
      }
      //   console.log(`balloon: ${balloon}`);
      //   console.log(`intersection: ${intersection}`);
      //   console.log(`newIntersection: ${newIntersection}`);
      intersection = newIntersection;
    }
    // console.log("increase pop");
    pops++;
  }
  return pops;
}

function findIntersection(intersection: number[], balloon: number[]): number[] {
  if (intersection[1] < balloon[0] || intersection[0] > balloon[1]) return [];
  return [
    Math.max(intersection[0], balloon[0]),
    Math.min(intersection[1], balloon[1]),
  ];
}

// greedy approach
// from the left
// get intersecting ballons
// ballons that intersect with that intersection
// until we can't intersect
// burst these
// repeat
console.log(
  findMinArrowShots([
    [10, 16],
    [2, 8],
    [1, 6],
    [7, 12],
  ])
);
