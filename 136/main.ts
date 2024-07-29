function singleNumber(nums: number[]): number {
  let accumulator = 0;
  for (let num of nums) {
    accumulator ^= num;
  }
  return accumulator;
}
