class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        diff = numRows * 2 - 2
        res = ""
        for i in range(numRows):
            offset = diff - i * 2
            pos = i
            while pos < len(s):
                next_char = s[pos]
                res += next_char
                if offset == 0:
                    offset = diff
                pos += offset
                offset = diff - offset
                if offset == 0:
                    offset = diff
        return res


ans = Solution()
print(ans.convert("A", 1))