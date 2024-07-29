function removeDuplicates(nums: number[]): number {
  let currentValueDestinationIndex = 0;
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    if (i + 1 === nums.length) {
      nums[currentValueDestinationIndex++] = num;
      break;
    }
    let nextNum = nums[i + 1];
    if (nextNum !== num) {
      nums[currentValueDestinationIndex++] = num;
    }
  }
  return currentValueDestinationIndex;
}

// approach
// have a var, current to keep track of the current value we are looking at
// have a current index to keep track of where to put the number
// for num in list
// if num != current || is last item in list
// nums[index++] = num
// else
// continue
