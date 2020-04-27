"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        signatures = {}
        for s in strs:
            sig = ''.join(sorted(s))
            if sig in signatures:
                signatures[sig].append(s)
            else:
                signatures[sig] = [s]
        res = []
        for ls in signatures.values():
            res.append(ls)
        return res

ans = Solution()
print(ans.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))