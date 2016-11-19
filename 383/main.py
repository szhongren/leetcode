"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        needed = {}
        for c in magazine:
            if needed.__contains__(c):
                needed[c] += 1
            else:
                needed[c] = 1
        for c in ransomNote:
            if not needed.__contains__(c) or needed[c] == 0:
                return False
            else:
                needed[c] -= 1
        return True

ans = Solution()
print(ans.canConstruct("aa", "aab"))