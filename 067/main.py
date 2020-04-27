"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = False
        len_a = len(a)
        len_b = len(b)
        if a == "0" and a == b:
            return "0"
        if len_a < len_b:
            return self.addBinary(b, a)
        b = "0" * (len_a - len_b) + b
        result = ""
        for i in range(len_a - 1, -1, -1):
            digit_a = a[i]
            digit_b = b[i]
            new_digit = '*'
            if carry:
                if digit_a == digit_b:
                    if digit_a == '1':
                        carry = True
                    else:
                        carry = False
                    new_digit = '1'
                else:
                    new_digit = '0'
                    carry = True
            else:
                if digit_a == digit_b:
                    if digit_a == '1':
                        carry = True
                    else:
                        carry = False
                    new_digit = '0'
                else:
                    new_digit = '1'
                    carry = False
            result = new_digit + result
        if carry:
            return '1' + result
        else:
            return result

ans = Solution()
print(ans.addBinary("1", "1"))