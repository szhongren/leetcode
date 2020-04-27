"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution(object):
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

        # if nums is strictly increasing or equal, swap last 2
        # if nums is strictly decreasing or equal
        # if prev is None, sort nums
        # else swap smallest val > prev, and sort nums, append to prev and before
        # go through list one by one, if
        # go from the back, less logic to deal with

ans = Solution()
test = [5, 4, 3, 2, 1] # → 1,3,2
for _ in range(25):
    print(test)
    ans.nextPermutation(test)

print()
test = [2, 3, 1, 2, 2, 7, 2, 4, 5] # → [2,3,1,2,2,2,4,5,7] [4,3,2,4,4]
for _ in range(20):
    print(test)
    ans.nextPermutation(test)

print()
test = [5,1,1] # → 1,5,1
for _ in range(7):
    print(test)
    ans.nextPermutation(test)
