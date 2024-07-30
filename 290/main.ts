function wordPattern(pattern: string, s: string): boolean {
  let forwardMap = new Map();
  let backwardMap = new Map();
  let words = s.split(" ");
  if (pattern.length !== words.length) return false;
  for (let i = 0; i < pattern.length; i++) {
    let char = pattern[i];
    let word = words[i];
    if (forwardMap.has(char) && forwardMap.get(char) !== word) return false;
    if (backwardMap.has(word) && backwardMap.get(word) !== char) return false;
    forwardMap.set(char, word);
    backwardMap.set(word, char);
  }
  return true;
}

// approach: 2 maps, one forward, one backward
// first, if lengths are not equal, return false
// add to the maps as we iterate through
// if key exists and value not equals, return false
