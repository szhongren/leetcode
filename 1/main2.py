from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            if target - value in seen:
                return [i, seen[target - value]]
            else:
                seen[value] = i

ans = Solution()
print(ans.twoSum([2, 7, 11, 15], 9))
print(ans.twoSum([3, 2, 4], 6))
print(ans.twoSum([3, 3], 6))
