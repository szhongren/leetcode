from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set()
        slow, fast = 0, 0
        for fast in range(len(nums)):
            if nums[fast] not in seen:
                seen.add(nums[fast])
                nums[slow] = nums[fast]
                slow += 1
        return slow


[1, 1, 1]
0, 0
1, 1
1, 2
