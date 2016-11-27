"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        l = len(nums)
        if l == 0:
            return res
        else:
            nums.append(nums[-1])
            start = nums[0]
            if_range = False
            for i in range(1, l + 1):
                if nums[i] - nums[i - 1] == 1:
                    if_range = True
                else:
                    add = str(start)
                    if if_range:
                        add = add + "->" + str(nums[i - 1])
                    res.append(add)
                    start = nums[i]
                    if_range = False

        return res

ans = Solution()
print(ans.summaryRanges([0,1,2,4,5,7]))