function twoSum(nums: number[], target: number): number[] {
  let differences = new Map();
  // map of (target - num) to index
  for (let i = 0; i <= nums.length; i++) {
    let num = nums[i];
    if (differences.has(num)) return [i, differences.get(num)];
    differences.set(target - num, i);
  }
}

// for each number, add the difference from it to the target to a set
// if the number is in the set, that means that we have already seen a number that will sum with that number to the target, so return true
// else return false
