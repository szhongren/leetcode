function findPeakElement(nums: number[]): number {
  return findPeakElementRecur(nums, 0, nums.length);
}

function findPeakElementRecur(
  nums: number[],
  start: number,
  end: number
): number {
  console.log(start, end);
  if (end - start <= 1) return start;
  if (end - start === 2)
    return nums[start] > nums[start + 1] ? start : start + 1;
  let mid = start + Math.floor((end - start) / 2);
  //   console.log(mid);
  //   console.log("----------------------------");
  if (isPeak(nums, mid)) return mid;
  if (nums[mid - 1] > nums[mid + 1])
    return findPeakElementRecur(nums, start, mid);
  else return findPeakElementRecur(nums, mid + 1, end);
}

function isPeak(nums: number[], i: number): boolean {
  if (i - 1 < 0) return nums[i] > nums[i + 1];
  if (i + 1 >= nums.length) return nums[i - 1] < nums[i];
  return nums[i - 1] < nums[i] && nums[i] > nums[i + 1];
}

// cases
// 1 2 3
// 1 3 2 *
// 2 1 3
// 2 3 1 *
// 3 1 2
// 3 2 1

console.log(findPeakElement([1, 2, 3, 1]));
console.log(findPeakElement([1, 2, 1, 3, 5, 6, 4]));
