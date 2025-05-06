function checkInclusion(s1: string, s2: string): boolean {
  if (s1.length > s2.length) return false;
  let charFrequency = Array.from({ length: 26 }, (v, i) => 0);
  let charCodeA = "a".charCodeAt(0);
  for (let char of s1) {
    charFrequency[char.charCodeAt(0) - charCodeA]++;
  }
  //   console.log(charFrequency);

  let isPermutation = (runningSignature: number[]) => {
    for (let i = 0; i < charFrequency.length; i++) {
      if (charFrequency[i] !== runningSignature[i]) return false;
    }
    return true;
  };
  // have the signature
  let runningCharFrequency = Array.from({ length: 26 }, (v, i) => 0);
  for (let i = 0; i < s1.length; i++) {
    runningCharFrequency[s2[i].charCodeAt(0) - charCodeA]++;
  }
  //   console.log(runningCharFrequency);
  if (isPermutation(runningCharFrequency)) return true;

  for (let i = s1.length; i < s2.length; i++) {
    runningCharFrequency[s2[i].charCodeAt(0) - charCodeA]++;
    runningCharFrequency[s2[i - s1.length].charCodeAt(0) - charCodeA]--;
    // console.log(i);
    // console.log(s2[i]);
    // console.log(s2[i - s1.length]);
    // console.log(runningCharFrequency);
    if (isPermutation(runningCharFrequency)) return true;
  }
  return false;
}

// approach
// get signature of s1 as a char frequency
// iterate through s2

console.log(checkInclusion("ab", "eidboaoo"));
console.log(checkInclusion("ab", "eidbaooo"));
