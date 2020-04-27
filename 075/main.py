"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red_i = 0
        blue_i = len(nums) - 1
        curr_i = 0
        while curr_i <= blue_i:
            color = nums[curr_i]
            if color == 0: # red
                nums[red_i], nums[curr_i] = nums[curr_i], nums[red_i]
                red_i += 1
            elif color == 2: # blue
                nums[blue_i], nums[curr_i] = nums[curr_i], nums[blue_i]
                blue_i -= 1
                curr_i -= 1
            curr_i += 1
        return nums

ans = Solution()
print(ans.sortColors([1, 2, 0, 0, 0, 1, 2, 0, 2, 1, 0, 1, 1, 2]))