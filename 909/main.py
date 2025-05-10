from typing import List
from collections import deque
from math import inf


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        simplified = [0]  # 0-indexed, so square k is at simplified[k]
        n = len(board)
        forward = True
        for i in range(n - 1, -1, -1):
            if forward:
                simplified.extend(board[i])
            else:
                simplified.extend(board[i][::-1])
            forward = not forward

        steps = [inf] * (n * n + 1)
        steps[1] = 0
        queue = deque([1])

        while queue:
            current_square = queue.popleft()

            if current_square == n * n:
                return steps[current_square]

            for dice_roll in range(1, 7):
                next_square_after_dice = current_square + dice_roll

                if next_square_after_dice > n * n:
                    # Optimization: further rolls will also be out of bounds
                    break

                # Determine the actual landing square after snake/ladder
                final_destination_square = simplified[next_square_after_dice]
                if final_destination_square == -1:  # No snake or ladder
                    final_destination_square = next_square_after_dice

                new_cost = steps[current_square] + 1

                if new_cost < steps[final_destination_square]:
                    steps[final_destination_square] = new_cost
                    queue.append(final_destination_square)

        return -1


sol = Solution()
print(
    sol.snakesAndLadders(
        [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
    )
)
print(sol.snakesAndLadders([[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]))
