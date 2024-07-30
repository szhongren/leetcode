function isHappy(n: number): boolean {
  let seen = new Set();
  while (n !== 1) {
    if (seen.has(n)) return false;
    seen.add(n);
    n = sumOfDigitSquares(n);
  }
  return true;
}

function sumOfDigitSquares(x: number): number {
  let sum = 0;
  while (x > 0) {
    let lastDigit = x % 10;
    sum += lastDigit * lastDigit;
    x = Math.floor(x / 10);
  }
  return sum;
}

console.log(isHappy(19));
