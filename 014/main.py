"""
Write a function to find the longest common prefix string amongst an array of strings.

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        first = strs[0]
        common_len = len(first)
        for str in strs[1:]:
            if common_len == 0:
                break
            curr_common = 0
            for ch_i in range(min(len(str), common_len)):
                if str[ch_i] != first[ch_i]:
                    break
                else:
                    curr_common += 1
            common_len = min(curr_common, common_len)
        return first[:common_len]

ans = Solution()
print(ans.longestCommonPrefix([]))
print(ans.longestCommonPrefix(["abc", "ab"]))