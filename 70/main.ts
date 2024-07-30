function climbStairs(n: number): number {
  if (n === 1) return 1;
  let sequence = [1, 1];
  for (let i = 0; i < n - 1; i++) {
    sequence.push(
      sequence[sequence.length - 1] + sequence[sequence.length - 2]
    );
  }
  return sequence[sequence.length - 1];
}

// for each step, look 1 and 2 steps before it, and add the 2

// this is fibonacci offset by 1

// 1, 2, 3, 5

// 1 1 1 1
// 1 1 2
// 1 2 1
// 1 1 2
// 2 2
