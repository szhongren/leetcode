function majorityElement(nums: number[]): number {
  let counts = new Map();
  for (let num of nums) {
    if (!counts.has(num)) counts.set(num, 0);
    counts.set(num, counts.get(num) + 1);
    if (counts.get(num) > Math.floor(nums.length / 2)) return num;
  }
}

// have a map of counts
// for each char, increase counts. if counts of any char >= n/2, return
