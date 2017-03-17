"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []
        self.restoreIpAddressesRecur(s, 4, [])
        return self.ans

    def restoreIpAddressesRecur(self, s, segments, curr):
        l = len(s)
        if l < segments or l > segments * 3:
            return
        if l == 0 and segments == 0:
            self.ans.append('.'.join(curr))
            return
        for i in range(1, min(l + 1, 4)):
            segment = s[:i]
            val = int(segment)
            if val > 255 or (segment[0] == '0' and i > 1):
                break
            self.restoreIpAddressesRecur(s[i:], segments - 1, curr + [segment])

ans = Solution()
# print(ans.restoreIpAddresses("25525511135"))
# print(ans.restoreIpAddresses("0000"))
print(ans.restoreIpAddresses("010010"))
