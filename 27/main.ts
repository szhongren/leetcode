function removeElement(nums: number[], val: number): number {
  let count = 0;
  let slow_pointer = 0;
  for (let i = 0; i < nums.length; i++) {
    nums[slow_pointer] = nums[i];
    if (nums[i] === val) {
      count++;
    } else {
      slow_pointer++;
    }
  }
  return nums.length - count;
}

let a = [3, 2, 2, 3];
console.log(removeElement(a, 3));
console.log(a);
