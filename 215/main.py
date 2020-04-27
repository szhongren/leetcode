"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
from random import randint

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(start, end):
            """
            :type target: int
            :type start: int
            :type end: int
            """
            pivot = nums[start]
            front = start + 1
            back = end - 1
            while front <= back:
                curr_val = nums[front]
                if curr_val >= pivot:
                    front += 1
                else:
                    nums[front], nums[back] = nums[back], nums[front]
                    back -= 1
            nums[start], nums[back] = nums[back], nums[start]
            if back + 1 == k:
                return nums[back]
            if back + 1 < k:
                return partition(back + 1, end)
            if back + 1 > k:
                return partition(start, back)
        return partition(0, len(nums))

ans = Solution()

for i in range(10):
    nums = [randint(0, 25) for _ in range(randint(1, 13))]
    print(nums)
    print(ans.findKthLargest(nums, randint(1, len(nums))))
    print(nums)
    print()
