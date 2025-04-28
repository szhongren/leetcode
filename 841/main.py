from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        approach
        go to zero, get keys, put onto queue
        while queue:
            pop
            visit room
        """
        queue = deque(rooms[0])
        visited = set([0])
        while queue:
            room_to_visit = queue.popleft()
            visited.add(room_to_visit)
            for next_room in rooms[room_to_visit]:
                if next_room not in visited:
                    queue.append(next_room)
        return len(visited) == len(rooms)
