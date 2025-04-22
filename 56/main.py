from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        approach
        use a stack
        sort intervals, then iterate through
        pick out one, and if it's not got any more after, just append to results
        if it's got ones after, check first one and see if it's intersecting
        if not intersecing, append to results
        if intersecting, merge and repeat
        """
        intervals = sorted(intervals)
        stack = [intervals[0]]
        i = 1
        while i < len(intervals):
            next_interval = intervals[i]
            if stack[-1][-1] >= next_interval[0]:
                # should merge
                stack[-1] = [stack[-1][0], max(stack[-1][1], next_interval[1])]
            else:
                stack.append(next_interval)
            i += 1
        return stack
