function countGoodNumbers(n: number): number {
  let half = BigInt(n) / BigInt(2);
  let moduloBy = BigInt(100000007);
  if (n % 2 === 1) {
    let total = BigInt(1);
    for (let i = 0; i < half; i++) {
      total *= BigInt(20);
    }
    total *= BigInt(5);
    return Number(total % moduloBy);
  } else {
    let total = BigInt(1);
    for (let i = 0; i < half; i++) {
      total *= BigInt(20);
    }
    return Number(total % moduloBy);
  }
}

function countGoodNumbersBI(n: number): bigint {
  let half = BigInt(n) / BigInt(2);
  let moduloBy = BigInt(100000007);
  if (n % 2 === 1) {
    let total = BigInt(1);
    for (let i = 0; i < half; i++) {
      total *= BigInt(20);
    }
    total *= BigInt(5);
    return total;
  } else {
    let total = BigInt(1);
    for (let i = 0; i < half; i++) {
      total *= BigInt(20);
    }
    return total;
  }
}

// function countGoodNumbers(n: number): number {
//   if (n === 0) return 0;
//   if (n === 1) return 5;
//   if (n === 2) return 20;
//   let result: bigint = n % 2 == 1 ? BigInt(5) : BigInt(20);
//   for (let i = n; i > 2; i -= 2) {
//     result = result * BigInt(20);
//   }
//   return Number(result % BigInt(100000007));
// }

// can calculate number of values
// * 4 for number of odd digits
// * 4 for first digit, otherwise * 5 for every even digit
// 5 * 4 * 5 * 4

// 2 cases
// 0000
// 00000
// 01234

for (let i = 1; i < 60; i++) {
  console.log(`${i}: ${countGoodNumbers(i)}`);
  console.log(`${i}: ${countGoodNumbersBI(i)}`);
}
