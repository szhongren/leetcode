function reverseWords(s: string): string {
  return s.trim().split(/ +/).reverse().join(" ");
}

// trim string
// for char in string
// if space, add prev word to the list of words
// else, it's part of a word, continue
