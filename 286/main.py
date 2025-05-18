from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        approach
        bfs from each gate, and for every non cell > 0, set it to min of current value and the level of the bfs
        """
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] != 0:
                    continue
                queue = deque([(i, j)])
                level = 1
                while queue:
                    new_queue = deque()
                    for _ in range(len(queue)):
                        a, b = queue.popleft()
                        if a > 0 and rooms[a - 1][b] > 0 and rooms[a - 1][b] > level:
                            rooms[a - 1][b] = level
                            new_queue.append((a - 1, b))
                        if (
                            a < m - 1
                            and rooms[a + 1][b] > 0
                            and rooms[a + 1][b] > level
                        ):
                            rooms[a + 1][b] = level
                            new_queue.append((a + 1, b))
                        if b > 0 and rooms[a][b - 1] > 0 and rooms[a][b - 1] > level:
                            rooms[a][b - 1] = level
                            new_queue.append((a, b - 1))
                        if (
                            b < n - 1
                            and rooms[a][b + 1] > 0
                            and rooms[a][b + 1] > level
                        ):
                            rooms[a][b + 1] = level
                            new_queue.append((a, b + 1))

                    level += 1
                    queue = new_queue
