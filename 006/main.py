"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
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