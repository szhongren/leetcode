"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = nums[0]
        p = 1
        if first == target:
            return 0
        elif first < target:
            while nums[p] > nums[p - 1]:
                if nums[p] == target:
                    return p
                p += 1
            return -1
        else:
            p = len(nums) - 2
            if nums[p] == target:
                return p
            while nums[p + 1] > nums[p]:
                if nums[p] == target:
                    return p
                p -= 1
            return -1


ans = Solution()
print(ans.search([4, 5, 6, 7, 0, 1, 2], 0))