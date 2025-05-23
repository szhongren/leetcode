from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        approach
        sort the intervals
        use a stack, push onto stack first item
        then, for ever item, if it intersects with the top of the stack, pop, merge, push
        do this until does not intersect, then push a new item on
        return stack
        """
        n = len(intervals)
        intervals.sort()
        stack = [intervals[0]]

        def intersecting(a: List[int], b: List[int]):
            """
            [] ()
            [(])
            ([])
            ([)]
            """
            a1, a2 = a
            b1, b2 = b
            return b2 >= a1 and b1 <= a2

        for i in range(1, n):
            if intersecting(stack[-1], intervals[i]):
                a1, a2 = stack.pop()
                b1, b2 = intervals[i]
                stack.append([min(a1, b1), max(a2, b2)])
            else:
                stack.append(intervals[i])
        return stack
