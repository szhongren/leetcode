"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].
1, 5, 10, 6, 15, 11, 16
1, 5, 6, 10, 11, 15, 16

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # self.found = [0 for i in range(n + 1)]
        self.sums = {}
        self.getSums(nums, 0, n)
        patch_count = 0
        while True:
            patch = 0
            while patch in self.sums:
                patch += 1
            if patch > n:
                if n not in self.sums:
                    patch_count += 1
                break
            new_sums = {}
            for i in self.sums.keys():
                new_sums[i] = 1
                if i + patch <= n:
                    new_sums[i + patch] = 1
            self.sums = new_sums
            patch_count += 1

        # while sum(self.found) != n + 1:
        #     patch = 0
        #     while self.found[patch] == 1:
        #         patch += 1
        #     for seen_sum in self.sums.keys():
        #         if seen_sum + patch < len(self.found):
        #             self.found[seen_sum + patch] = 1
        #     for i, v in enumerate(self.found):
        #         if v == 1:
        #             self.sums[i] = 1
        #     patch_count += 1
        return patch_count

    def getSums(self, nums, curr_sum, n):
        if len(nums) == 0:
            if curr_sum <= n:
                self.sums[curr_sum] = 1
        else:
            self.getSums(nums[1:], curr_sum, n)
            self.getSums(nums[1:], curr_sum + nums[0], n)

ans = Solution()
print(ans.minPatches([1,2,31,33], 2147483647))
# print(ans.minPatches([1, 3], 6))
# print(ans.minPatches([1, 5, 10], 20))
# print(ans.minPatches([1, 2, 2], 5))
