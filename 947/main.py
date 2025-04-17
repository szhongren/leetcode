from typing import List, Tuple


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        approach:
        * find largest island size, answer is size - 1
        """
        to_visit = set([(stone[0], stone[1]) for stone in stones])
        row_stones = {}
        col_stones = {}
        max_removal = 0
        for stone in stones:
            a, b = stone[0], stone[1]
            if a not in row_stones:
                row_stones[a] = set()
            row_stones[a].add((a, b))
            if b not in col_stones:
                col_stones[b] = set()
            col_stones[b].add((a, b))

        def bfs(stone: Tuple[int, int]):
            to_visit.remove(stone)
            print(f"visiting {stone}")
            a, b = stone
            to_check = [stone for stone in row_stones[a]] + [
                stone for stone in col_stones[b]
            ]
            print(f"to_check: {to_check}")
            size = 1
            for next_stone in to_check:
                if next_stone in to_visit:
                    size += bfs(next_stone)
            print(f"returning size {size} for stone {stone}")
            return size

        for x, y in stones:
            if (x, y) not in to_visit:
                # already visited
                continue
            max_removal += bfs((x, y)) - 1
        return max_removal


sol = Solution()
print(sol.removeStones([[3, 2], [3, 1], [4, 4], [1, 1], [0, 2], [4, 0]]))
