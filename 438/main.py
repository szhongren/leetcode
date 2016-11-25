"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

def sig_equal(l, s):
    for (k, v) in s.items():
        if k not in l:
            return False
        elif l[k] != v:
            return False
    return True

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # l = len(p)
        # signature = {}
        # for ch in p:
        #     if ch in signature:
        #         signature[ch] += 1
        #     else:
        #         signature[ch] = 1
        # result = []
        # i = 0
        # while i <= len(s) - l:
        #     local = {}
        #     for j in range(l):
        #         if s[i + j] not in signature:
        #             i = i + j
        #             break
        #         else:
        #             if s[i + j] not in local:
        #                 local[s[i + j]] = 1
        #             else:
        #                 local[s[i + j]] += 1
        #                 if local[s[i + j]] > signature[s[i + j]]:
        #                     break
        #     if sig_equal(local, signature):
        #         result.append(i)
        #     i += 1
        # return result
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0]*123, [0]*123
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m-1]:
            shash[ord(x)] += 1
        for i in range(m-1, n):
            shash[ord(s[i])] += 1
            if i-m >= 0:
                shash[ord(s[i-m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res

ans = Solution()
print(ans.findAnagrams("cbaebabacd", "abc"))
print(ans.findAnagrams("abab", "ab"))