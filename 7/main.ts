function reverse(x: number): number {
  let result = 0;
  let sign = x < 0 ? -1 : 1;
  x = Math.abs(x);
  while (x > 0) {
    console.log(x);
    console.log(result);
    let last_digit = x % 10;
    result += last_digit;
    result *= 10;
    x = (x - last_digit) / 10;
  }
  if (result >= 2147483648) return 0;
  return (sign * result) / 10;
}

console.log(reverse(123));
console.log(reverse(-123));
console.log(reverse(120));
