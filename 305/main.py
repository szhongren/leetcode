from typing import List, Tuple


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        approach
        for each new land, look at neighbors, if any neighbors, union find with them
        simple: count number of union sets
        optimization: maybe some other way of keeping track
        """
        parent_of = {}

        def find_parent(xy: Tuple[int, int]):
            if parent_of[xy] == xy:
                return xy
            parent_of[xy] = find_parent(parent_of[xy])
            return parent_of[xy]

        def union(ab: Tuple[int, int], cd: Tuple[int, int]):
            parent_ab, parent_cd = find_parent(ab), find_parent(cd)
            if parent_ab == parent_cd:
                return
            parent_of[parent_cd] = parent_ab

        result = []
        unique_islands = 0
        for position in map(tuple, positions):
            x, y = position
            if position in parent_of:
                result.append(unique_islands)
                continue

            parent_of[position] = position
            unique_islands += 1
            if (x - 1, y) in parent_of and find_parent(position) != find_parent(
                (x - 1, y)
            ):
                union(position, (x - 1, y))
                unique_islands -= 1
            if (x + 1, y) in parent_of and find_parent(position) != find_parent(
                (x + 1, y)
            ):
                union(position, (x + 1, y))
                unique_islands -= 1
            if (x, y - 1) in parent_of and find_parent(position) != find_parent(
                (x, y - 1)
            ):
                union(position, (x, y - 1))
                unique_islands -= 1
            if (x, y + 1) in parent_of and find_parent(position) != find_parent(
                (x, y + 1)
            ):
                union(position, (x, y + 1))
                unique_islands -= 1
            result.append(unique_islands)
        return result
