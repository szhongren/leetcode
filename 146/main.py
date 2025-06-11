class LinkedListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    approach
    map and linked list
    for every get, move item to front of linked list
    for every put, move the value to front of linked list if exists, else add to front and remove last
    """

    def __init__(self, capacity: int):
        self.items = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        item = self.items[key]
        if item == self.head:
            return item.value

        if item.prev:
            item.prev.next = item.next
        if item.next:
            item.next.prev = item.prev

        if item == self.tail:
            self.tail = item.prev

        item.prev = None
        item.next = self.head
        self.head.prev = item
        self.head = item
        return item.value

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items[key].value = value
            self.get(key)
            return

        new_node = LinkedListNode(key, value)
        self.items[key] = new_node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        if len(self.items) > self.capacity:
            key_to_remove = self.tail.key
            if self.tail.prev:
                self.tail.prev.next = None
            self.tail = self.tail.prev
            self.items.pop(key_to_remove)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
