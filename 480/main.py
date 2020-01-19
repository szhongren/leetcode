MAX = lambda x, y: x > y
MIN = lambda x, y: x < y

class HashHeap(object):
    def __init__(self, heap_cmp=MIN):
        self.len = 0
        self.heap = [None]
        self.cmp = heap_cmp
        self.indexes = {}

    def values(self):
        return self.heap[1:self.len + 1]

    def peek(self):
        return self.heap[1]

    def insert(self, value):
        self.heap.append(value)
        self.len += 1
        self.sift_up(self.len)

    def pop(self):
        top = self.heap[1]
        self.heap[1] = self.heap[self.len]
        self.len -= 1
        self.heap.pop()
        self.sift_down(1)
        return top

    def sift_down(self, i):
        while i < self.len:
            swap_child_i = self.swap_child_i(i)
            if i == swap_child_i:
                break
            if self.cmp(self.heap[swap_child_i], self.heap[i]):
                self.swap(i, swap_child_i)
            i = swap_child_i


    def sift_up(self, i):
        while i // 2 > 0:
            if self.cmp(self.heap[i], self.heap[i // 2]):
                self.swap(i, i // 2)
            i //= 2

    def swap_child_i(self, i):
        if i * 2 > self.len:
            return i
        left_i = i * 2
        left_v = self.heap[left_i]
        if i * 2 + 1 > self.len:
            return left_i
        right_i = i * 2 + 1
        right_v = self.heap[right_i]
        curr_v = self.heap[i]
        if self.cmp(curr_v, left_v) and self.cmp(curr_v, right_v):
            return i
        if self.cmp(left_v, right_v):
            return left_i
        else:
            return right_i

    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def remove(self, value):
        removed_i = self.heap.index(value)
        self.swap(removed_i, self.len)
        self.len -= 1
        self.heap.pop()
        if removed_i == 1:
            self.sift_down(removed_i)
        elif removed_i == self.len + 1:
            return
        else:
            if self.cmp(self.heap[removed_i], self.heap[removed_i // 2]):
                self.sift_up(removed_i)
            else:
                self.sift_down(removed_i)

class SlidingWindow(object):
    def __init__(self, k, vals):
        self.k = k
        self.values = vals

    def __iter__(self):
        self.min_heap = HashHeap()
        self.max_heap = HashHeap(MAX)
        for i in range(self.k):
            value = self.values[i]
            self.insert(value)

        self.curr_i = self.k
        return self

    def __next__(self):
        i = self.curr_i
        if i >= len(self.values):
            raise StopIteration
        curr_value = self.values[i]
        remove_value = self.values[i - self.k]
        # self.min_heap.pretty_print()
        # self.max_heap.pretty_print()
        result = self.median()
        self.remove(remove_value)
        self.insert(curr_value)
        self.curr_i += 1
        return result


    next = __next__

    def insert(self, value):
        l_min, l_max = self.min_heap.len, self.max_heap.len
        if l_min + l_max == 0:
            self.max_heap.insert(value)
        elif l_min + l_max == 1:
            if l_min == 1:
                self.max_heap.insert(value)
            if l_max == 1:
                self.min_heap.insert(value)
            if self.max_heap.peek() > self.min_heap.peek():
                self.max_heap.cmp, self.min_heap.cmp = self.min_heap.cmp, self.max_heap.cmp
                self.max_heap, self.min_heap = self.min_heap, self.max_heap
        elif l_min == l_max:
            if value < self.max_heap.peek():
                self.max_heap.insert(value)
            elif value >= self.max_heap.peek() and value <= self.min_heap.peek():
                self.max_heap.insert(value)
            elif value > self.min_heap.peek():
                self.min_heap.insert(value)
        elif l_min > l_max:
            if value <= self.min_heap.peek():
                self.max_heap.insert(value)
            else:
                self.max_heap.insert(self.min_heap.pop())
                self.min_heap.insert(value)
        elif l_min < l_max:
            if value >= self.max_heap.peek():
                self.min_heap.insert(value)
            else:
                self.min_heap.insert(self.max_heap.pop())
                self.max_heap.insert(value)

    def median(self):
        if self.min_heap.len == self.max_heap.len:
            return (self.min_heap.peek() + self.max_heap.peek()) / 2.0
        elif self.min_heap.len > self.max_heap.len:
            return self.min_heap.peek()
        elif self.min_heap.len < self.max_heap.len:
            return self.max_heap.peek()

    def remove(self, value):
        if self.min_heap.len > 0 and value >= self.min_heap.peek():
            self.min_heap.remove(value)
        elif self.max_heap.len > 0 and value <= self.max_heap.peek():
            self.max_heap.remove(value)
        if self.min_heap.len == self.max_heap.len + 2:
            self.max_heap.insert(self.min_heap.pop())
        if self.max_heap.len == self.min_heap.len + 2:
            self.min_heap.insert(self.max_heap.pop())

class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        meds = SlidingWindow(k, list(map(float, nums)))
        result = [x for x in meds]
        result.append(meds.median())
        return result

ans = Solution()
print(ans.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(ans.medianSlidingWindow([1, 2], 1))
