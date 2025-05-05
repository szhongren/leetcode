from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        approach
        go through and get the exits first, put into a set
        bfs
        """
        seen = set()
        queue = deque([(entrance[0], entrance[1])])
        nearest_exit = 0
        while queue:
            new_queue = []
            for i in range(len(queue)):
                x, y = queue.popleft()
                seen.add((x, y))
                if (
                    x != entrance[0]
                    and y != entrance[1]
                    and (
                        x == 0 or y == 0 or x == len(maze) - 1 or y == len(maze[0]) - 1
                    )
                ):
                    return nearest_exit
                if x != 0 and maze[x - 1][y] != "+":
                    new_queue.append((x - 1, y))
                if x != len(maze) - 1 and maze[x + 1][y] != "+":
                    new_queue.append((x + 1, y))
                if y != 0 and maze[x][y - 1] != "+":
                    new_queue.append((x, y - 1))
                if y != len(maze[0]) - 1 and maze[x][y + 1] != "+":
                    new_queue.append((x, y + 1))
            queue = deque(new_queue)
            nearest_exit += 1
        return -1
