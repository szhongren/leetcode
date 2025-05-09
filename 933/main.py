from heapq import heappush, heappop


class RecentCounter:

    def __init__(self):
        self.heap = []

    def ping(self, t: int) -> int:
        heappush(self.heap, t)
        while t - self.heap[0] > 3000:
            heappop(self.heap)
        return len(self.heap)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
