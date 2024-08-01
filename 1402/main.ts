function maxSatisfaction(satisfaction: number[]): number {
  let sortedSatisfaction = satisfaction.sort((a, b) => b - a);
  let result = 0;
  let runningSum = 0;
  for (let dish of sortedSatisfaction) {
    runningSum += dish;
    result = Math.max(result, result + runningSum);
  }
  return result;
}

console.log(maxSatisfaction([-1, -8, 0, 5, -7]));
console.log(maxSatisfaction([4, 3, 2]));
