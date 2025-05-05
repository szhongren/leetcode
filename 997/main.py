from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        approach
        count in degree
        every time we have a person who trusts, remove that person from the pool of potential judges
        judge is the person with n - 1 in degree and 0 out degree
        off by 1
        edge cases:
        []
        [1] -> 1
        """
        in_degrees = {k: 0 for k in range(1, n + 1)}
        potential_judges = [True] * (n + 1)  # ignore first one
        for trust_edge in trust:
            truster, trustee = trust_edge[0], trust_edge[1]
            potential_judges[truster] = False
            in_degrees[trustee] += 1
        maybe_result = []
        for i in range(1, n + 1):
            if not potential_judges[i]:
                continue
            if in_degrees[i] == n - 1:
                maybe_result.append(i)
        if len(maybe_result) != 1:
            return -1
        return maybe_result[0]
