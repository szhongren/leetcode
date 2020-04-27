"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [nums]
        orig = nums[:]
        self.nextPermutation(nums)
        while nums != orig:
            ans.append(nums[:])
            self.nextPermutation(nums)
        return ans

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        slow = len(nums) - 1
        fast = len(nums) - 2
        while nums[fast] == nums[slow] and fast > 0:
            slow -= 1
            fast -= 1
        if nums[fast] < nums[slow]:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            return
        # strictly decreasing
        while nums[fast] >= nums[slow] and fast >= 0:
            slow -= 1
            fast -= 1
        if slow == 0:
            nums.sort()
            return
        swap_v = nums[slow]
        swap_i = slow
        for i in range(slow, len(nums)):
            if nums[i] > nums[fast]:
                swap_v = nums[i]
                swap_i = i
        nums[swap_i], nums[fast] = nums[fast], nums[swap_i]
        for i, v in enumerate(sorted(nums[slow:])):
            nums[i + slow] = v



ans = Solution()
print(ans.permuteUnique([1, 1, 2]))
