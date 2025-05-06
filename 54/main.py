from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        brute force this
        have visited locations
        have a direction to go in
        if can continue, go in same direction
        else turn
        until I cannot turn
        """
        m = len(matrix)
        n = len(matrix[0])
        left = (0, -1)
        up = (-1, 0)
        right = (0, 1)
        down = (1, 0)

        next_direction = {right: down, down: left, left: up, up: right}
        result = []
        visited = set([(0, n), (m, n - 1), (m - 1, -1)])
        visiting = (0, 0)
        direction = right

        def get_next(visiting):
            x, y = visiting
            nonlocal direction
            a, b = direction
            c, d = direction
            if (x + a, y + b) in visited:
                c, d = next_direction[direction]
                if (x + c, y + d) in visited:
                    return None
            direction = (c, d)
            return (x + c, y + d)

        while True:
            i, j = visiting
            result.append(matrix[i][j])
            visited.add(visiting)
            visiting = get_next(visiting)
            if not visiting:
                break
        return result
