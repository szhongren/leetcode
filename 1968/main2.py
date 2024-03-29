"""
You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]
Explanation:
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.

Example 2:

Input: nums = [6,2,0,9,7]
Output: [9,7,6,2,0]
Explanation:
When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
"""


from typing import List
from random import sample, randint


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # sort list by value
        nums.sort()
        front = nums[: len(nums) // 2]
        back = reversed(nums[len(nums) // 2 :])
        result = [a for b in zip(front, back) for a in b]
        if len(result) != len(nums):
            result.append(list(back)[-1])
        return result


ans = Solution()
print(ans.rearrangeArray([1, 2, 3, 4, 5]))
print(ans.rearrangeArray([6, 2, 0, 9, 7]))
print(ans.rearrangeArray([1, 5, 2, 6, 3, 7, 4, 8]))
a = sample(range(1, 12), randint(3, 10))
print(a)
b = sample(range(1, 12), randint(3, 10))
print(b)
print(ans.rearrangeArray(a))
print(ans.rearrangeArray(b))
