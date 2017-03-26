"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greatest = {}
        for i, v in enumerate(nums):
            # stack is not empty and last value on stack is less than curr val
            while stack and stack[-1][1] < v:
                a, b = stack.pop()
                next_greatest[a] = v
            stack.append((i, v))
        for i, v in enumerate(nums):
            while stack and stack[-1][1] < v:
                a, b = stack.pop()
                next_greatest[a] = v
            stack.append((i, v))
        ans = [-1 for _ in range(len(nums))]
        for i, v in enumerate(nums):
            if i in next_greatest:
                ans[i] = next_greatest[i]
        return ans

ans = Solution()
print(ans.nextGreaterElements([1, 2, 1]))
