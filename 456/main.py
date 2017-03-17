"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        patt = [nums[0]]
        for v in nums[1:]:
            if len(patt) == 2:
                if v in patt or v < patt[0]:
                    patt = [v]
                elif v > patt[1]:
                    patt.append(v)
                    patt = patt[1:]
                elif v < patt[1] and v > patt[0]:
                    patt.append(v)

            elif len(patt) == 1:
                if v > patt[0] + 1:
                    patt.append(v)
                else:
                    patt = [v]


            elif len(patt) == 3:
                return True

        return False


ans = Solution()
# print(ans.find132pattern([1, 2, 3, 4]))
# print(ans.find132pattern([3, 1, 4, 2]))
# print(ans.find132pattern([-1, 3, 2, 0]))
print(ans.find132pattern([3,5,0,3,4]))
