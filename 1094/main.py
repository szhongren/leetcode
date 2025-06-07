from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        approach
        preprocess trips into start and ends, in the same list and sort
        iterate through list, and keep a count of total passengers currently
        if > capacity, return false
        at end return true
        """
        stops = []
        for passengers, start, end in trips:
            stops.append((start, passengers))
            stops.append((end, -passengers))

        stops.sort()
        current_passengers = 0
        for stop, passengers in stops:
            current_passengers += passengers
            if current_passengers > capacity:
                return False
        return True
