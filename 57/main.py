from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        use a stack
        for item in intervals, push onto stack
        if top of stack overlaps with insert, pop, merge and push back onto stack
        if not overlaps and top of stack completely smaller than insert, pop, insert insert, and insert top back onto stack. set inserted = True
        else if not overlaps, continue
        """

        if len(intervals) == 0:
            return [newInterval]

        def overlapping(a: List[int], b: List[int]):
            return a[0] <= b[1] and b[0] <= a[1]

        stack = []
        inserted = False
        for interval in intervals:
            stack.append(interval)
            if not inserted:
                top_of_stack = stack[-1]
                if overlapping(top_of_stack, newInterval):
                    stack = stack[:-1]
                    newInterval = [
                        min(top_of_stack[0], newInterval[0]),
                        max(top_of_stack[1], newInterval[1]),
                    ]
                else:
                    if top_of_stack[1] < newInterval[0]:
                        pass
                    else:
                        stack[-1] = newInterval
                        stack.append(top_of_stack)
                        inserted = True
        if not inserted:
            stack.append(newInterval)
        return stack
