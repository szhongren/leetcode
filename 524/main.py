"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Example 2:

Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"

Note:

    All the strings in the input will only contain lower-case letters.
    The size of the dictionary won't exceed 1,000.
    The length of all the strings in the input won't exceed 1,000.
"""

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isSubsequence(word):
            s_i = 0
            word_i = 0
            while word_i < len(word):
                if s_i == len(s):
                    return False
                if word[word_i] == s[s_i]:
                    word_i += 1
                s_i += 1
            return True
        ans = ""
        d.sort()
        max_length = 0
        for word in d:
            if isSubsequence(word):
                if len(word) > max_length:
                    max_length = len(word)
                    ans = word
        return ans

ans = Solution()
print(ans.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(ans.findLongestWord("abpcplea", ["a", "b", "c"]))
