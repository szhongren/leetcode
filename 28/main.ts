function strStr(haystack: string, needle: string): number {
  if (needle.length > haystack.length) return -1;
  for (let i = 0; i < haystack.length; i++) {
    for (let j = 0; j <= needle.length; j++) {
      if (j === needle.length) return i;
      if (i + j >= haystack.length) return -1;
      if (haystack[i + j] !== needle[j]) break;
    }
  }
  return -1;
}
