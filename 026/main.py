"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        else:
            slow = 0
            fast = 1
            while fast < len(nums):
                """
                if fast >= len(nums) or nums[slow] != nums[fast]:
                    nums = nums[:slow + 1] + nums[fast:]
                    slow += 1
                    fast = slow + 1
                else:
                    fast += 1
                """
                if nums[fast] == nums[slow]:
                    fast += 1
                else:
                    slow += 1
                    nums[slow] = nums[fast]
                    fast += 1
        return slow + 1

ans = Solution()
print(ans.removeDuplicates([1, 2, 2]))
print(ans.removeDuplicates([1, 1, 2, 2, 2, 2, 2]))
print(ans.removeDuplicates([1, 1, 2, 2, 3, 3, 3, 3, 4]))
print(ans.removeDuplicates([1, 1, 1, 1]))
print(ans.removeDuplicates([1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 7]))
