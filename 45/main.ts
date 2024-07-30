function jump(nums: number[]): number {
  let cache = new Map();
  function getNextPositionsForPosition(x: number) {
    if (cache.has(x)) return cache.get(x);
    let result: number[] = [];
    for (let i = 1; i <= nums[x]; i++) {
      result.push(x + i);
    }
    cache.set(x, result);
    return result;
  }

  let numberOfJumps = 0;
  let reacheablePositions = new Set([0]);
  while (true) {
    numberOfJumps++;
    let newReacheablePositions: Set<number> = new Set();
    for (let pos of reacheablePositions) {
      for (let next of getNextPositionsForPosition(pos)) {
        newReacheablePositions.add(next);
      }
    }
    if (newReacheablePositions.has(nums.length - 1)) return numberOfJumps;
    reacheablePositions = newReacheablePositions;
  }
}

// loop through number of steps
// for each number of steps, generate a list of the possible next positions
// if no next positions, break
// if any of the next positions are the end, return number of steps + 1
// else go on to the next number of steps
