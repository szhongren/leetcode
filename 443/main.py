from typing import List
from collections import deque


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        approach
        use current_char and current_count to store stream
        append " " to the end, so we can just append to the list
        if different from current_char, append ch
        if count > 1, append str(count), push ones digit to a stack, then pop off stack and append to chars
        return len(result[n + 1:])

        # n = 10
        # "aaabbcccc "
        # "aaabbcccc a"
        """
        n = len(chars)
        chars.append(" ")
        if len(chars) == 0:
            return 0
        current_char = chars[0]
        current_count = 0
        current_replace_i = 0
        for i in range(n + 1):
            if current_char != chars[i]:
                chars[current_replace_i] = current_char
                current_replace_i += 1
                if not current_count == 1:
                    stack = []
                    while current_count > 0:
                        stack.append(str(current_count % 10))
                        current_count = current_count // 10
                    while stack:
                        chars[current_replace_i] = stack.pop()
                        current_replace_i += 1
                current_char = chars[i]
                current_count = 1
            else:
                current_count += 1
        print(chars)
        return current_replace_i


sol = Solution()
print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))
