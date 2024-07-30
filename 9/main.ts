function isPalindrome(x: number): boolean {
  if (x < 0) return false;
  if (x < 10) return true;
  let reversedNumber = 0;
  let divisor = 1;
  while (Math.floor(x / divisor) > 0) {
    reversedNumber = reversedNumber * 10 + (Math.floor(x / divisor) % 10);
    divisor *= 10;
  }
  return reversedNumber === x;
}

// recursive solution
