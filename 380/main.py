from random import randint


class RandomizedSet:
    """
    approach:
    have a list to get random with O(1) time
    """

    def __init__(self):
        self.set = set()
        self.val_to_i = {}
        self.list = []

    def insert(self, val: int) -> bool:
        was_in_set = val in self.set
        self.set.add(val)
        if not was_in_set:
            self.val_to_i[val] = len(self.list)
            self.list.append(val)
        return not was_in_set

    def remove(self, val: int) -> bool:
        was_in_set = val in self.set
        if was_in_set:
            self.set.remove(val)
            i = self.val_to_i[val]
            self.list[i], self.list[len(self.list) - 1] = (
                self.list[len(self.list) - 1],
                self.list[i],
            )
            self.val_to_i[self.list[i]] = i
            del self.val_to_i[val]
            self.list.pop()
        return was_in_set

    def getRandom(self) -> int:
        return self.list[randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

thing = RandomizedSet()
print(thing.insert(0))
print(thing.insert(1))
print(thing.remove(0))
print(thing.insert(2))
print(thing.remove(1))
print(thing.getRandom())
