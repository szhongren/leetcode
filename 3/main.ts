function lengthOfLongestSubstring(s: string): number {
  let lengthOfLongestSubstring = 0;
  let leftPointer = -1;
  let lettersInWindow = new Map();
  for (let rightPointer = 0; rightPointer < s.length; rightPointer++) {
    let currentChar = s[rightPointer];
    if (
      lettersInWindow.has(currentChar) &&
      lettersInWindow.get(currentChar) > leftPointer
    ) {
      leftPointer = lettersInWindow.get(currentChar);
      lengthOfLongestSubstring = Math.max(
        lengthOfLongestSubstring,
        rightPointer - leftPointer
      );
    } else {
      lengthOfLongestSubstring = Math.max(
        lengthOfLongestSubstring,
        rightPointer - leftPointer + 1
      );
    }
    lettersInWindow.set(currentChar, rightPointer);
  }
  return lengthOfLongestSubstring;
}

// approach
// abcabcbb -> 3
// 0
// if (s[i] not in lettersInWindow)
// lengthOfCurrentWindow++
// if (lengthOfCurrentWindow > lengthOfLongestSubstring)
// lengthOflongestSubstring = lengthOfCurrentWindow
// lettersInWindow.set(s[i], i)
// else if (s[i] in lettersInWindow)
// lengthOfCurrentWindow = i - lettersInWindow[s[i]]
// lettersInWindow[s[i]] = i

console.log(lengthOfLongestSubstring("tmmzuxt"));
