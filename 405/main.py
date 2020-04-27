"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        if num == 0:
            return "0"
        elif num > 0:
            while num != 0:
                curr = num % 16
                num = num // 16
                result = getHex(curr) + result
        else:
            end = self.toHex(abs(num) - 1)
            l = len(end)
            end = '0' * (8 - l) + end
            result = ''.join(list(map(flipChar, end)))
        return result

def getHex(val):
    if val == 0:
        return '0'
    elif val == 1:
        return '1'
    elif val == 2:
        return '2'
    elif val == 3:
        return '3'
    elif val == 4:
        return '4'
    elif val == 5:
        return '5'
    elif val == 6:
        return '6'
    elif val == 7:
        return '7'
    elif val == 8:
        return '8'
    elif val == 9:
        return '9'
    elif val == 10:
        return 'a'
    elif val == 11:
        return 'b'
    elif val == 12:
        return 'c'
    elif val == 13:
        return 'd'
    elif val == 14:
        return 'e'
    elif val == 15:
        return 'f'

def flipChar(hex):
    if hex == '0':
        return 'f'
    elif hex == '1':
        return 'e'
    elif hex == '2':
        return 'd'
    elif hex == '3':
        return 'c'
    elif hex == '4':
        return 'b'
    elif hex == '5':
        return 'a'
    elif hex == '6':
        return '9'
    elif hex == '7':
        return '8'
    elif hex == '8':
        return '7'
    elif hex == '9':
        return '6'
    elif hex == 'a':
        return '5'
    elif hex == 'b':
        return '4'
    elif hex == 'c':
        return '3'
    elif hex == 'd':
        return '2'
    elif hex == 'e':
        return '1'
    elif hex == 'f':
        return '0'

ans = Solution()
print(ans.toHex(514))
for i in range(-17, 26):
    print(i, ans.toHex(i))