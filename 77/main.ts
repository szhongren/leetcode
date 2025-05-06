function combine(n: number, k: number): number[][] {
  function combineRecur(
    numbers: number[],
    k: number,
    selected: number[]
  ): number[][] {
    if (k === 0) {
      return [selected];
    }
    if (numbers.length === 0) {
      return [];
    }
    const newNumbers = numbers.slice(1);
    return combineRecur(newNumbers, k, selected).concat(
      combineRecur(newNumbers, k - 1, [...selected, numbers[0]])
    );
  }
  let numbers: number[] = [];
  for (let i = 1; i <= n; i++) {
    numbers.push(i);
  }
  return combineRecur(numbers, k, []);
}

// approach:
// start at root
// full list, remaining k, selected values
// recurse down

console.log(combine(1, 1));
console.log(combine(2, 1));
console.log(combine(3, 1));

console.log(combine(2, 2));
console.log(combine(3, 2));
console.log(combine(4, 2));
console.log(combine(5, 2));

console.log(combine(3, 3));
console.log(combine(4, 3));
console.log(combine(5, 3));
console.log(combine(6, 3));
