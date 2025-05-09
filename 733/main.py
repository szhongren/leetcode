from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        approach
        BFS
        """
        m = len(image)
        n = len(image[0])
        original_color = image[sr][sc]

        seen = set()

        def bfs(a: int, b: int):
            if (a, b) in seen:
                return
            image[a][b] = color
            seen.add((a, b))
            if a > 0 and (a - 1, b) not in seen and image[a - 1][b] == original_color:
                bfs(a - 1, b)
            if b > 0 and (a, b - 1) not in seen and image[a][b - 1] == original_color:
                bfs(a, b - 1)
            if (
                a < m - 1
                and (a + 1, b) not in seen
                and image[a + 1][b] == original_color
            ):
                bfs(a + 1, b)
            if (
                b < n - 1
                and (a, b + 1) not in seen
                and image[a][b + 1] == original_color
            ):
                bfs(a, b + 1)

        bfs(sr, sc)

        return image
