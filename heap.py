from random import randint
# 0
# 1 2
# 3 4 5 6 
class Heap(object):
    def __init__(self):
        self.heap = []
        self.len = 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (i * 2) + 1

    def right_child(self, i):
        return (i * 2) + 2

    def peek(self):
        return self.heap[0]

    def __str__(self) -> str:
        out = ""
        start_index = 0
        end_index = 1
        while start_index < self.len:
            out += f"\n{self.heap[start_index:end_index]}"
            start_index = start_index * 2 + 1
            end_index = end_index * 2 + 1
        return out

    def pop(self):
        print("pop")
        # swap first and last
        self.heap[0], self.heap[self.len - 1] = self.heap[self.len - 1], self.heap[0]
        self.len -= 1
        self.top_down_heapify(i)
        return self.heap.pop()

    def insert(self, val):
        print(f"insert {val}")
        self.heap.append(val)
        self.len += 1
        self.bottom_up_heapify()

    def bottom_up_heapify(self):
        # start from the end
        start = self.len - 1
        for i in range(start, 0, -1):
            print(f"{i}, {self.heap}")
            if self.heap[i] >= self.heap[self.parent(i)]:
                print("swap")
                self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i] 
        print("-" * 20)

    def top_down_heapify(self, i):
        largest = i
        l = self.left_child(i)
        r = self.right_child(i)

        if l < self.len and self.heap[l] > self.heaap[largest]:
            largest = l

        if r < self.len and self.heap[r] > self.heaap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.top_down_heapify(largest)

h = Heap()
for i in range(20):
    h.insert(randint(-50, 50))
    if randint(0, 1) == 1:
        print(f"popped {h.pop()}")
    print(h)
