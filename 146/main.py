class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"<key: {self.key}, value: {self.value}, prev: {self.prev.key if self.prev else None}, next: {self.next.key if self.next else None}>"


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        # If node is already head, just return
        if node == self.head:
            return node.value

        # Update prev/next pointers
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # Update tail if needed
        if node == self.tail:
            self.tail = node.prev

        # Move to front
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].value = value
            self.get(key)  # Move to front
            return

        # Create new node
        node = Node(key, value)
        self.key_to_node[key] = node

        # If first node
        if not self.head:
            self.head = self.tail = node
            return

        # Add to front
        node.next = self.head
        self.head.prev = node
        self.head = node

        # Remove from end if over capacity
        if len(self.key_to_node) > self.capacity:
            lru_key = self.tail.key
            if self.tail.prev:
                self.tail.prev.next = None
            self.tail = self.tail.prev
            del self.key_to_node[lru_key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def print_cache(cache: LRUCache):
    print(cache.capacity)
    print(cache.head)
    print(cache.tail)
    print(cache.key_to_node)


cache = LRUCache(2)
cache.put(1, 1)
print_cache(cache)
cache.put(2, 2)
print_cache(cache)
cache.get(1)
print_cache(cache)
cache.put(3, 3)
print_cache(cache)
cache.get(2)
print_cache(cache)
