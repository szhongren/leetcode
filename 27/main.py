from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        * 2 pointers
        * one for where to put, one for where to look
        * end when look pointer reaches end
        * k = slow
        """
        slow, fast = 0, 0
        while fast < len(nums):
            nums[slow] = nums[fast]
            if nums[fast] != val:
                slow += 1
            fast += 1
        return slow
