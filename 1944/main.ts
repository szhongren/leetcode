function canSeePersonsCount(heights: number[]): number[] {
  let results: number[] = [];
  let runningCanSee: number[] = [];
  for (let i = heights.length - 1; i >= 0; i--) {
    let height = heights[i];
    let canSee = 0;
    for (let j = runningCanSee.length - 1; j >= 0; j--) {
      canSee += 1;
      if (runningCanSee[j] >= height) break;
    }
    results.push(canSee);
    console.log(`${height} can see ${runningCanSee}`);

    while (runningCanSee[runningCanSee.length - 1] <= height)
      runningCanSee.pop();
    runningCanSee.push(height);
  }
  return results.reverse();
}

// for each height from the back
// keep a running count of heights we can see
// every time we get a hight

console.log(canSeePersonsCount([10, 6, 8, 5, 11, 9]));
console.log(canSeePersonsCount([5, 1, 2, 3, 10]));
console.log(canSeePersonsCount([3, 1, 5, 8, 6]));
// 11 can see 9
// 5 can see 11
