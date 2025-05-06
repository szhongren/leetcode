function isSubsequence(s: string, t: string): boolean {
  let subsequenceIndex = 0;
  for (let i = 0; i < t.length; i++) {
    if (subsequenceIndex === s.length) return true;
    if (t[i] === s[subsequenceIndex]) subsequenceIndex++;
  }
  return subsequenceIndex === s.length;
}
