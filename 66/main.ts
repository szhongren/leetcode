function plusOne(digits: number[]): number[] {
  let carry = false;
  for (let i = digits.length - 1; i >= 0; i--) {
    let sum = digits[i] + 1;
    if (carry || i === digits.length - 1) {
      digits[i] = sum % 10;
      carry = sum >= 10;
    } else {
      carry = false;
    }
  }
  if (carry) return [1].concat(digits);
  return digits;
}

console.log(plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]));
