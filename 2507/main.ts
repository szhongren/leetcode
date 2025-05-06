function smallestValue(n: number): number {
  let min = n;
  while (!isPrime(n)) {
    let factors: number[] = getPrimeFactors(n);
    let sum = factors.reduce((a, b) => a + b, 0);
    min = Math.min(sum, n);
    if (n === sum) break;
    n = sum;
  }
  return min;
}

function getPrimeFactors(n: number): number[] {
  let result: number[] = [];
  while (!isPrime(n)) {
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        result.push(i);
        n = n / i;
        break;
      }
    }
  }
  result.push(n);
  return result;
}

let primeNumbersCache = new Map();

function isPrime(n: number): boolean {
  if (primeNumbersCache.has(n)) return primeNumbersCache.get(n);
  if (n <= 1) return false;
  if (n === 2) return true;
  if (n === 3) return true;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      primeNumbersCache.set(n, false);
      return false;
    }
  }
  primeNumbersCache.set(n, true);
  return true;
}

// approach
// keep track of min
// take number
// prime factorize
// add factors
// new number, loop

for (let i = 2; i < 50; i++) {
  console.log(getPrimeFactors(i));
}
console.log(primeNumbersCache);
