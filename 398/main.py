"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""

import random as rnd

class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        rnd.seed()
        index = 0
        while self.nums[index] != target:
            index += 1
        count = 1
        for i in range(index + 1, len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if rnd.randrange(count) == 0:
                    index = i
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
ans = Solution([1, 2, 3, 3, 3])
results = []
for i in range(1000):
    results.append(ans.pick(3))
for i in range(6):
    print(i, results.count(i))

# reservoir sampling