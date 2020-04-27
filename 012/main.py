"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

roman_values = [
(1000, "M"),
(900, "CM"),
(500, "D"),
(400, "CD"),
(100, "C"),
(90, "XC"),
(50, "L"),
(40, "XL"),
(10, "X"),
(9, "IX"),
(5, "V"),
(4, "IV"),
(1, "I"),
]

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        while num != 0:
            for (v, s) in roman_values:
                if v <= num:
                    result += s
                    num -= v
                    break
        return result

ans = Solution()
for i in range(100):
    print(ans.intToRoman(i))