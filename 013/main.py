"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
roman_values = {
"I":    1,
"IV":   4,
"V":    5,
"IX":	9,
"X":	10,
"XL":	40,
"L":	50,
"XC":	90,
"C":	100,
"CD":	400,
"D":	500,
"CM":	900,
"M":	1000,
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mark = 0
        value = 0
        while mark < len(s):
            two = s[mark]
            if mark + 2 <= len(s):
                two = s[mark: mark + 2]
            one = s[mark]
            if roman_values.__contains__(two):
                value += roman_values[two]
                mark += 2
            else:
                value += roman_values[one]
                mark += 1
        return value

ans = Solution()
print(ans.romanToInt("VII"))
print(ans.romanToInt("VIII"))
print(ans.romanToInt("IIX"))
print(ans.romanToInt("IX"))
print(ans.romanToInt("VIIII"))
print(ans.romanToInt("X"))
print(ans.romanToInt("XI"))
print(ans.romanToInt("XII"))
print(ans.romanToInt("XIII"))
print(ans.romanToInt("XIV"))
print(ans.romanToInt("XV"))
print(ans.romanToInt("XVI"))
print(ans.romanToInt("XVII"))
print(ans.romanToInt("XVIII"))
print(ans.romanToInt("XIX"))
print(ans.romanToInt("XX"))
print(ans.romanToInt("XXI"))
print(ans.romanToInt("XXII"))
print(ans.romanToInt("XXIII"))
print(ans.romanToInt("XXIV"))
print(ans.romanToInt("XXV"))
print(ans.romanToInt("XXVI"))
print(ans.romanToInt("XXVII"))
print(ans.romanToInt("XXVIII"))
print(ans.romanToInt("XXIX"))
print(ans.romanToInt("XXX"))
print(ans.romanToInt("XXXI"))
print(ans.romanToInt("XXXII"))
print(ans.romanToInt("XXXIII"))
print(ans.romanToInt("XXXIV"))
print(ans.romanToInt("XXXV"))
print(ans.romanToInt("XXXVI"))
print(ans.romanToInt("XXXVII"))
print(ans.romanToInt("XXXVIII"))
print(ans.romanToInt("XXXIX"))
print(ans.romanToInt("XL"))
print(ans.romanToInt("XLI"))
print(ans.romanToInt("XLII"))
print(ans.romanToInt("XLIII"))
print(ans.romanToInt("XLIV"))
print(ans.romanToInt("XLV"))
print(ans.romanToInt("XLVI"))
print(ans.romanToInt("XLVII"))
print(ans.romanToInt("XLVIII"))
print(ans.romanToInt("XLIX"))
print(ans.romanToInt("L"))