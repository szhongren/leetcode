function canJump(nums: number[]): boolean {
  let canJump = [true];
  for (let i = 1; i < nums.length; i++) canJump.push(false);
  for (let i = 0; i < nums.length; i++) {
    let jumps = nums[i];
    if (canJump[i]) {
      for (let j = 1; j <= jumps; j++) {
        if (i + j >= nums.length) break;
        canJump[i + j] = true;
      }
    }
  }
  return canJump[canJump.length - 1];
}

// assume we can't reach any places but the first
// for each step, if can jump to it, mark everything between it and i + val as can jump
// return last item in the list
