from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        approach
        use a minheap to keep track of meeting end times
        """
        intervals.sort()  # Sort by start time
        heap = []  # Min-heap of end times

        for start, end in intervals:
            # If room is free (earliest end <= current start)
            if heap and heap[0] <= start:
                heapq.heappop(heap)  # Free up the room
            heapq.heappush(heap, end)  # Assign room to current meeting

        return len(heap)  # Number of rooms needed
