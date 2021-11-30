from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_reach_pacific = set()
        can_reach_atlantic = set()
        number_of_rows = len(heights)
        number_of_cols = len(heights[0])
        pacific_search_list = []
        atlantic_search_list = []
        for i in range(number_of_cols):
            can_reach_pacific.add((0, i))
            pacific_search_list.append((0, i))
            can_reach_atlantic.add((number_of_rows - 1, i))
            atlantic_search_list.append((number_of_rows - 1, i))
        for i in range(number_of_rows):
            can_reach_pacific.add((i, 0))
            pacific_search_list.append((i, 0))
            can_reach_atlantic.add((i, number_of_cols - 1))
            atlantic_search_list.append((i, number_of_cols - 1))

        def valid_cell(cell, last_value, seen):
            x, y = cell
            if x < 0 or y < 0:
                return False
            if x >= number_of_rows or y >= number_of_cols:
                return False
            if cell in seen:
                return False
            return heights[x][y] >= last_value

        def dfs(cell, seen, search_list):
            x, y = cell
            if cell not in seen:
                seen.add(cell)
            search_list.extend(
                [
                    cell
                    for cell in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                    if valid_cell(cell, heights[x][y], seen)
                ]
            )

        while len(pacific_search_list) != 0:
            dfs(pacific_search_list.pop(), can_reach_pacific, pacific_search_list)
        while len(atlantic_search_list) != 0:
            dfs(atlantic_search_list.pop(), can_reach_atlantic, atlantic_search_list)
        return can_reach_pacific.intersection(can_reach_atlantic)


print(
    Solution().pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)
print(Solution().pacificAtlantic([[2, 1], [1, 2]]))
