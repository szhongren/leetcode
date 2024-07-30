function containsNearbyDuplicate(nums: number[], k: number): boolean {
  let seen = new Set();
  for (let i = 0; i < nums.length; i++) {
    let beforeWindowIndex = i - k - 1;
    if (beforeWindowIndex >= 0) {
      seen.delete(nums[beforeWindowIndex]);
    }
    if (seen.has(nums[i])) return true;
    seen.add(nums[i]);
  }
  return false;
}

// create a set of seen numbers in window
// loop through nums
// if val in seen
// return true
// at end return false
