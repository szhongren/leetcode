function isPalindrome(s: string): boolean {
  let start = 0;
  let end = s.length - 1;
  while (start <= end) {
    while (start <= end && !isAlphanumeric(s.charAt(start))) {
      start++;
    }
    while (start <= end && !isAlphanumeric(s.charAt(end))) {
      end--;
    }
    if (start > end) return true;
    if (s.charAt(start++).toLowerCase() !== s.charAt(end--).toLowerCase()) {
      return false;
    }
  }
  return true;
}

function isAlphanumeric(c: string): boolean {
  return c.match(/[a-zA-Z0-9]/) !== null;
}

console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome(" "));
console.log(isPalindrome("     "));
console.log(isPalindrome("a     "));
console.log(isPalindrome("     a"));
console.log(isPalindrome("     a     "));
