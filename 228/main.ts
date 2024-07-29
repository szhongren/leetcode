function summaryRanges(nums: number[]): string[] {
  let result: string[] = [];

  if (nums.length === 0) return [];
  if (nums.length === 1) return [nums[0].toString()];
  let startRange = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === nums[i - 1] + 1) {
      continue;
    } else {
      if (i - 1 === startRange) result.push(`${nums[startRange]}`);
      else result.push(`${nums[startRange]}->${nums[i - 1]}`);
      startRange = i;
    }
  }
  if (startRange === nums.length - 1) result.push(`${nums[startRange]}`);
  else result.push(`${nums[startRange]}->${nums[nums.length - 1]}`);
  return result;
}

// loop through the list
// for each number
// if start of Range, continue

console.log(summaryRanges([0, 1, 2, 4, 5, 7]));
console.log(summaryRanges([0, 2, 3, 4, 6, 8, 9]));
