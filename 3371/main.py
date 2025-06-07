from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
        approach
        from the largest number, check if rest of the numbers summed / 2 is in the array
        """
        nums.sort(reverse=True)
        n = len(nums)
        total = sum(nums)

        # Create a set for O(1) lookups
        num_set = set(nums)

        for i in range(n):
            # Calculate sum without the current element
            sum_without = total - nums[i]
            target = sum_without / 2

            # Check if target exists in the array (but is not the same element)
            if target in num_set:
                # Special case: if target equals nums[i], we need at least 2 occurrences
                if target == nums[i]:
                    count = nums.count(nums[i])
                    if count > 1:
                        return nums[i]
                else:
                    return nums[i]

        return -1  # No outlier found


sol = Solution()
print(sol.getLargestOutlier([2, 3, 5, 10]))
print(sol.getLargestOutlier([-2, -1, -3, -6, 4]))
