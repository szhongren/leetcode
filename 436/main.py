"""
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
"""
import bisect

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        invs = sorted((x.start, i) for i, x in enumerate(intervals))
        ans = []
        for x in intervals:
            idx = bisect.bisect_right( invs, (x.end,) )
            ans.append(invs[idx][1] if idx < len(intervals) else -1)
        return ans

# TODO: UNDERSTAND CODE

ans = Solution()
print(ans.findRightInterval([ Interval(1,4), Interval(2,3), Interval(3,4) ]))
print(ans.findRightInterval([Interval(1,2) ]))
print(ans.findRightInterval([ Interval(3,4), Interval(2,3), Interval(1,2) ]))