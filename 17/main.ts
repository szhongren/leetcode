function letterCombinations(digits: string): string[] {
  let mapping = {
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
    "0": [],
  };
  function getCombinationsRecur(digits: string): string[] {
    if (digits.length === 0) {
      return [];
    }
    if (digits.length === 1) {
      return mapping[digits];
    }
    const previousCombinations = getCombinationsRecur(digits.slice(1));
    const currLetters = mapping[digits[0]];
    return previousCombinations.flatMap((combination) =>
      currLetters.map((letter) => letter + combination)
    );
  }
  return getCombinationsRecur(digits);
}

console.log(letterCombinations("2"));
console.log(letterCombinations("23"));
console.log(letterCombinations("32"));
// console.log(letterCombinations("21"));
