"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""

def hash(str):
    res = 0
    seen = {}
    for ch in str:
        if ch in seen:
            continue
        seen[ch] = True
    for ch in seen.keys():
        res |= 1 << (ord(ch) - ord('a'))
    return res

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_len = 0
        seen = {}
        lengths = [len(w) for w in words]
        hashes = [hash(w) for w in words]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if hashes[i] & hashes[j] == 0:
                    max_len = max(max_len, lengths[i] * lengths[j])
        return max_len

ans = Solution()
print(ans.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(ans.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(ans.maxProduct(["a", "aa", "aaa", "aaaa"]))