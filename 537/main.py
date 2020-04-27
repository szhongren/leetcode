"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:

Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:

    The input strings will not have extra blank.
    The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_coef = list(map(int, a[:-1].split('+')))
        b_coef = list(map(int, b[:-1].split('+')))
        i = a_coef[0] * b_coef[0]
        j = a_coef[1] * b_coef[1]
        k = a_coef[0] * b_coef[1]
        l = a_coef[1] * b_coef[0]
        return str(i - j) + '+' + str(k + l) + 'i'

ans = Solution()
print(ans.complexNumberMultiply("1+1i", "1+1i"))
print(ans.complexNumberMultiply("1+-1i", "1+-1i"))
