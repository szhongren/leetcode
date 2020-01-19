class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        jewels = set(list(J))
        for stone in S:
            if stone in jewels:
                result += 1
        return result


ans = Solution()
print(ans.numJewelsInStones('aA', 'aAAbbbb'))
