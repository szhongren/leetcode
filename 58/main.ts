function lengthOfLastWord(s: string): number {
  let words = s.trim().split(/ +/);
  return words[words.length - 1].length;
}
