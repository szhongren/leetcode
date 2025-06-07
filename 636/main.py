from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        approach
        push starts onto stack
        then, when we meet an end, calculate the duration, and subtract that duration from the immediate parent (each start/end handles the subtraction for its parent)
        """

        def parse_log(log: str):
            return log.split(":")

        stack = []
        time_run = [0] * n
        for log in logs:
            func_id, operation, timestamp = parse_log(log)
            if operation == "start":
                stack.append((func_id, timestamp))
            elif operation == "end":
                _, start_time = stack.pop()
                total_duration = timestamp - start_time + 1
                time_run[func_id] += total_duration

                if len(stack) > 0:
                    parent_id = stack[-1][0]
                    time_run[parent_id] -= total_duration
        return time_run


sol = Solution()
print(
    sol.exclusiveTime(
        2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    )
)
