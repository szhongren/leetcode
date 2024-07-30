function longestCommonPrefix(strs: string[]): string {
  let min_length = Math.min(...strs.map((x) => x.length));
  for (let i = 0; i < min_length; i++) {
    let currChar = strs[0][i];
    for (let word of strs) {
      if (currChar !== word[i]) return word.slice(0, i);
    }
  }
  return strs[0].slice(0, min_length);
}

// loop through each word in the list
// for each word, loop through each char
// on first iteration, set char == word1[0]
// if any of word2[0], word3[0] don't work, return string up to current not inclusive
// else continue
