function permute(nums: number[]): number[][] {
  function permuteRecur(
    nums: number[],
    currentPermutation: number[]
  ): number[][] {
    if (nums.length === 1) return [[...currentPermutation, ...nums]];
    if (nums.length === 0) return [currentPermutation];
    let result = [];
    for (let i = 0; i < nums.length; i++) {
      const currentNum = nums[i];
    }
  }
  return permuteRecur(nums, []);
}
