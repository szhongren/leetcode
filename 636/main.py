from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Stack-based approach:
        - Keep track of (function_id, start_time) on stack
        - For each end time, calculate duration and update total time
        - Handle nested calls by subtracting child durations from parent
        """

        def parse_log(s: str):
            func_id, action, timestamp = s.split(":")
            return int(func_id), action, int(timestamp)

        stack = []  # [(function_id, start_time)]
        total_time = [0] * n  # Initialize array instead of dict

        for log in logs:
            func_id, action, timestamp = parse_log(log)

            if action == "start":
                stack.append((func_id, timestamp))
            else:  # end
                start_func, start_time = stack.pop()
                duration = timestamp - start_time + 1
                total_time[func_id] += duration

                # If there's a parent function, subtract this duration
                if stack:
                    parent_func = stack[-1][0]
                    total_time[parent_func] -= duration

        return total_time


sol = Solution()
print(
    sol.exclusiveTime(
        2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    )
)
