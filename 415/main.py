"""
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

def digit_val(ch):
    return ord(ch) - 48

def digit_ch(v):
    return chr(v + 48)

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            num1 = "0" * (l2 - l1) + num1
        elif l1 > l2:
            num2 = "0" * (l1 - l2) + num2
        result = ""
        carry = 0
        for i in range(len(num1) - 1, -1, -1):
            digit_sum = digit_val(num1[i]) + digit_val(num2[i]) + carry
            carry = digit_sum // 10
            result = digit_ch(digit_sum % 10) + result
        if carry == 1:
            return "1" + result
        else:
            return result
