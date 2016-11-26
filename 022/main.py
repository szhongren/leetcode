"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        if n == 0:
            return self.res
        else:
            self.generateParenthesisRecur(n, n, "")
            return self.res

    def generateParenthesisRecur(self, open, close, curr):
        """
        :type open: int
        :type close: int
        :type curr: str
        :rtype: void
        """
        if open == 0 and close == 0:
            self.res.append(curr)
        elif open != 0 and open <= close:
            self.generateParenthesisRecur(open - 1, close, curr + "(")
        elif close <= 0:
            return
        self.generateParenthesisRecur(open, close - 1, curr + ")")

ans = Solution()
for i in range(4):
    print(i)
    for x in ans.generateParenthesis(i):
        print(x)
    print("------")