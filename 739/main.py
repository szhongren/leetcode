from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        approach
        use a stack. and an array to keep track of the answers
        use stack to keep track of days where we are still looking for a warmer day
        keep it strictly decreasing so that we can use the same warm day for several different previous days
        basically, push onto the stack when we see a temperature, and pop it off and log the number of days when we see a warmer temperature
        """
        n = len(temperatures)
        stack = []
        answer = [0] * n
        for day, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                answer[prev_day] = day - prev_day
            stack.append(day)
        return answer
