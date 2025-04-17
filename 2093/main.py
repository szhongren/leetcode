from typing import List, Set
from math import inf
import heapq


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        """
        approach:
        * recursive call, with caching
        * at each node, for each path, we have 2 choices, use discount or not
        """

        highways_map = {}
        for highway in highways:
            a, b, cost = highway[0], highway[1], highway[2]
            if a not in highways_map:
                highways_map[a] = {}
            highways_map[a][b] = cost
            if b not in highways_map:
                highways_map[b] = {}
            highways_map[b][a] = cost
        if 0 not in highways_map:
            highways_map[0] = {}
        cache = {}

        def bfs(city: int, target: int, visited: Set[int], discounts: int):
            """
            also implicitly return whether we can reach the target
            """
            cache_key = (city, discounts, tuple(sorted(visited)))
            if cache_key in cache:
                return cache[cache_key]
            if city == target:
                cache[cache_key] = 0
                return 0
            next_cities = [
                next_city
                for next_city in highways_map[city]
                if next_city not in visited
            ]
            if len(next_cities) == 0:
                cache[cache_key] = inf
                return inf
            min_path_cost = inf
            for next_city in next_cities:
                cost = highways_map[city][next_city]
                visited.add(city)
                visit_costs = [
                    bfs(next_city, target, visited, discounts) + cost,
                ]
                if discounts > 0:
                    visit_costs.append(
                        bfs(next_city, target, visited, discounts - 1) + int(cost / 2)
                    )
                visited.remove(city)
                min_path_cost = min(*visit_costs, min_path_cost)
            cache[cache_key] = min_path_cost
            return min_path_cost

        def dijkstra(city: int, target: int, visited: Set[int], discounts: int):
            # Using tuple of (cost, city, discounts_left)
            pq = [(0, 0, discounts)]  # (cost, current_city, remaining_discounts)
            seen = set()  # (city, discounts) pairs we've processed

            while pq:
                cost, curr, disc = heapq.heappop(pq)

                # Skip if we've seen this state with same or more discounts
                if (curr, disc) in seen:
                    continue
                seen.add((curr, disc))

                if curr == target:
                    return cost

                # Try all neighbors
                for next_city, next_cost in highways_map[curr].items():
                    # Try without discount
                    heapq.heappush(pq, (cost + next_cost, next_city, disc))

                    # Try with discount if available
                    if disc > 0:
                        discounted_cost = cost + next_cost // 2
                        heapq.heappush(pq, (discounted_cost, next_city, disc - 1))

            return inf

        result = dijkstra(0, n - 1, set(), discounts)
        if result == inf:
            return -1
        return result


sol = Solution()
print(sol.minimumCost(5, [[0, 1, 4], [2, 1, 3], [1, 4, 11], [3, 2, 3], [3, 4, 2]], 1))
print(sol.minimumCost(4, [[1, 3, 17], [1, 2, 7], [3, 2, 5], [0, 1, 6], [3, 0, 20]], 20))
print(sol.minimumCost(4, [[0, 1, 3], [2, 3, 2]], 0))
print(
    sol.minimumCost(
        9,
        [
            [5, 0, 17],
            [7, 0, 46],
            [2, 5, 87],
            [0, 1, 38],
            [1, 4, 50],
            [7, 2, 98],
            [4, 2, 57],
            [2, 1, 78],
            [1, 5, 67],
            [6, 3, 20],
            [6, 5, 64],
            [5, 3, 38],
            [8, 5, 21],
            [4, 0, 15],
            [4, 6, 25],
            [4, 7, 16],
            [8, 7, 5],
            [3, 7, 90],
            [6, 0, 63],
            [6, 7, 72],
            [3, 0, 46],
            [8, 1, 16],
            [4, 8, 78],
            [1, 6, 98],
            [4, 3, 15],
            [8, 6, 3],
            [8, 3, 44],
            [0, 8, 59],
        ],
        119,
    )
)
