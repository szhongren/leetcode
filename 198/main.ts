function rob(nums: number[]): number {
  let maxSums = [0, 0];
  for (let i = 0; i < nums.length; i++) {
    maxSums.push(Math.max(nums[i] + maxSums[i], maxSums[i + 1]));
  }
  return maxSums[maxSums.length - 1];
}

// for each house, we decide if we can rob it or not
// if rob, total = current + nums[i - 2]
// if not rob, total = nums[i - 1]
//
