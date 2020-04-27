"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""

import random as rnd

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for curr in nums:
            if count < 2 or curr > nums[count - 2]:
                nums[count] = curr
                count += 1
        return count

    #     return self.removeDuplicatesRecur(nums)

    # def removeDuplicatesRecur(self, nums):
    #     if len(nums) == 0:
    #         return 0
    #     if nums[0] == nums[-1]:
    #         return min(len(nums), 2)
    #     ptr = 1
    #     while nums[ptr] == nums[0]:
    #         ptr += 1
    #     pos = min(2, ptr)
    #     return min(2, ptr) + self.removeDuplicatesRecur(nums[ptr:])

ans = Solution()
for _ in range(10):
    input = [rnd.randrange(4) for _ in range(rnd.randrange(10))]
    input = sorted(input)
    print(input, ans.removeDuplicates(input))
