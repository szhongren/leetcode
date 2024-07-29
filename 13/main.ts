let romanValues = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

function romanToInt(s: string): number {
  let accumulator = romanValues[s[0]];
  for (let i = 1; i < s.length; i++) {
    let currChar = s[i];
    let prevChar = s[i - 1];
    if (prevChar === "I" && currChar === "V") accumulator -= 2;
    if (prevChar === "I" && currChar === "X") accumulator -= 2;
    if (prevChar === "X" && currChar === "L") accumulator -= 20;
    if (prevChar === "X" && currChar === "C") accumulator -= 20;
    if (prevChar === "C" && currChar === "D") accumulator -= 200;
    if (prevChar === "C" && currChar === "M") accumulator -= 200;
    accumulator += romanValues[currChar];
  }
  return accumulator;
}

// for each char
// look at next, if it's one of the special cases, subtract
// else add
