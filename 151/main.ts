function reverseWords(s: string): string {
  s = s.trim();
  let words: string[] = [];
  let wordStartIndex = 0;
  for (let i = 0; i < s.length; i++) {
    if (i === s.length - 1 || s[i] === ' ') {
      words.push(s.slice(wordStartIndex, i));
      wordStartIndex
    }
    if ()
  }
}

// trim string
// for char in string
// if space, add prev word to the list of words
// else, it's part of a word, continue
