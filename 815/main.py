from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        # build stop → set(buses) map
        stop_to_buses = defaultdict(set)
        for bus_idx, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(bus_idx)

        visited_stops = {source}
        visited_buses = set()
        q = deque([(source, 0)])  # (current stop, buses taken so far)

        while q:
            stop, buses = q.popleft()
            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for nxt in routes[bus]:
                    if nxt == target:
                        return buses + 1
                    if nxt not in visited_stops:
                        visited_stops.add(nxt)
                        q.append((nxt, buses + 1))
        return -1


sol = Solution()
print(sol.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
print(
    sol.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12)
)
