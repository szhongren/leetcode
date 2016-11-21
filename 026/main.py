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
            back_p = 0
            front_p = 1
            while front_p < len(nums):
                """
                if front_p >= len(nums) or nums[back_p] != nums[front_p]:
                    nums = nums[:back_p + 1] + nums[front_p:]
                    back_p += 1
                    front_p = back_p + 1
                else:
                    front_p += 1
                """
                if nums[front_p] == nums[back_p]:
                    front_p += 1
                else:
                    back_p += 1
                    nums[back_p] = nums[front_p]
                    front_p += 1
        return back_p + 1

ans = Solution()
print(ans.removeDuplicates([1, 2, 2]))
print(ans.removeDuplicates([1, 1, 2, 2, 2, 2, 2]))
print(ans.removeDuplicates([1, 1, 2, 2, 3, 3, 3, 3, 4]))
print(ans.removeDuplicates([1, 1, 1, 1]))
print(ans.removeDuplicates([1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 7]))