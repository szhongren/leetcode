function canConstruct(ransomNote: string, magazine: string): boolean {
  let counts = new Map();
  for (let char of magazine) {
    if (!counts.has(char)) {
      counts.set(char, 0);
    }
    counts.set(char, counts.get(char) + 1);
  }
  for (let char of ransomNote) {
    if (!counts.has(char)) {
      return false;
    }
    if (counts.get(char) <= 0) {
      return false;
    }
    counts.set(char, counts.get(char) - 1);
  }
  return true;
}
