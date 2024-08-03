function searchInsert(nums: number[], target: number): number {
  let start = 0;
  let end = nums.length;
  while (true) {
    if (end - start === 0) return start;
    let midpoint = start + Math.floor((end - start) / 2);
    if (nums[midpoint] === target) return midpoint;
    if (target > nums[midpoint]) {
      start = midpoint + 1;
    } else if (target < nums[midpoint]) {
      end = midpoint - 1;
    }
  }
  // 2, 4, 6
  // 1, 2, 3
  // 3, 5, 7
  // 1, 2, 3
}
