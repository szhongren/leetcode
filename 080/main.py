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
        if len(nums) <= 1:
            return len(nums)
        else:
            back_p = 0
            front_p = 1
            found = False
            while front_p < len(nums):
                if nums[front_p] == nums[back_p]:
                    if found:
                        back_p += 1
                    else:
                        found = True
                    front_p += 1
                else:
                    back_p += 1
                    nums[back_p] = nums[front_p]
                    front_p += 1
                    found = False
        return back_p + 1



ans = Solution()
for _ in range(10):
    input = [rnd.randrange(4) for _ in range(rnd.randrange(10))]
    input = sorted(input)
    print(input, ans.removeDuplicates(input))
