from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        approach
        recursive
        len = 0, return [[]]
        len = 1, return [[a]]
        prev = recur(nums[1:])
        for every item in prev, add nums[0] to every possible spot
        return
        """
        n = len(nums)
        if n == 0:
            return [[]]

        def permuteRecur(nums: List[int]):
            n = len(nums)
            if n == 1:
                return [[nums[0]]]
            prev = permuteRecur(nums[1:])
            result = []
            for permutation in prev:
                for i in range(len(permutation) + 1):
                    result.append(permutation[:i] + [nums[0] + permutation[i:]])
            return result

        return permuteRecur(nums)
