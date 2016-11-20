"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1 = 0
        p2 = len(numbers) - 1
        while True:
            curr_sum = numbers[p1] + numbers[p2]
            if curr_sum == target:
                break
            elif curr_sum < target:
                p1 += 1
            elif curr_sum > target:
                p2 -= 1
        return [p1 + 1, p2 + 1]

ans = Solution()
print(ans.twoSum([2, 7, 11, 15], 9))
print(ans.twoSum([5,25,75], 100))
print(ans.twoSum([2,3,4], 6))
print(ans.twoSum([3,24,50,79,88,150,345], 200))