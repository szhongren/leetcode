from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        approach
        2 binary searches
        one to find left bound
        one to find right bound
        """

        def get_left_bound(i: int, j: int) -> int:
            result = -1
            while i <= j:
                midpoint = (i + j) // 2
                print(i, j, midpoint)
                if nums[midpoint] > target:
                    j = midpoint - 1
                elif nums[midpoint] < target:
                    i = midpoint + 1
                elif nums[midpoint] == target:
                    result = midpoint
                    j = midpoint - 1
            return result

        def get_right_bound(i: int, j: int) -> int:
            result = -1
            while i <= j:
                midpoint = (i + j) // 2
                if nums[midpoint] > target:
                    j = midpoint - 1
                elif nums[midpoint] < target:
                    i = midpoint + 1
                elif nums[midpoint] == target:
                    result = midpoint
                    i = midpoint + 1
            return result

        return [get_left_bound(0, len(nums) - 1), get_right_bound(0, len(nums) - 1)]


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
