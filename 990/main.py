from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        same as union find
        2 passes
        for every a == b, we union the 2
        then, for second pass, for every !=, check if they have different parents
        if they have the same parent, false
        """

        def find_parent(node: str):
            if parents[node] == node:
                return node
            parents[node] = find_parent(parents[node])
            return parents[node]

        def union(a: str, b: str):
            pa, pb = find_parent(a), find_parent(b)
            if pa != pb:
                parents[pb] = pa

        # 1st pass
        parents = {}
        for equation in equations:
            a, b = equation[0], equation[3]
            if a not in parents:
                parents[a] = a
            if b not in parents:
                parents[b] = b
            if equation[1] == "!":
                continue
            union(a, b)

        # 2nd pass
        for equation in equations:
            if equation[1] == "=":
                continue
            a, b = equation[0], equation[3]
            pa, pb = find_parent(a), find_parent(b)
            if pa == pb:
                return False
        return True
