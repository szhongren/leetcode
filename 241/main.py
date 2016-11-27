"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        if len(input) == 0:
            return res
        for i in range(len(input)):
            curr = input[i]

            if curr.isdigit():
               continue

            left = self.diffWaysToCompute(input[0:i])
            right = self.diffWaysToCompute(input[i+1:])

            for a in left:
                for b in right:
                    res.append(calc(a, b, curr))

        if len(res) == 0:
            res.append(int(input))

        return res

ans = Solution()
print(ans.diffWaysToCompute("2-1-1"))
print(ans.diffWaysToCompute("2*3-4*5"))
