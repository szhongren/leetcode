"""
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

# Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

# Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

# Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

# Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

# getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

# Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

# getRandom should return 1 and 2 both equally likely.
collection.getRandom();
"""

import random as rnd

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indices = {}
        self.data = []
        self.len = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if len(self.data) != self.len:
            self.data[self.len] = val
        else:
            self.data.append(val)
        if val in self.indices:
            self.indices[val].append(self.len)
            self.len += 1
            return False
        else:
            self.indices[val] = [self.len]
            self.len += 1
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.indices:
            swap = self.data[self.len - 1]
            if val == swap:
                self.indices[val].remove(self.len - 1)
                self.len -= 1
                if len(self.indices[val]) == 0:
                    del self.indices[val]
                return True
            self.indices[swap].remove(self.len - 1)
            self.indices[swap].append(self.indices[val][-1])
            self.data[self.indices[val][-1]], self.data[self.len - 1] = self.data[self.len - 1], self.data[self.indices[val][-1]]
            self.indices[val] = self.indices[val][:-1]
            # need to change the index of the value we swapped with
            if len(self.indices[val]) == 0:
                del self.indices[val]
            self.len -= 1
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.data[rnd.randrange(self.len)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Init an empty collection.
col = RandomizedCollection()

for i in range(20):
    col.insert(rnd.randrange(10))

print(col.data)
for (k, v) in col.indices.items():
    print(k, '\t', v)

for i in range(15):
    v = rnd.randrange(7)
    print()
    print("remove", v, col.remove(v))
    print(col.len)
    print(col.data)
    print((col.len * 3) * ' ', '^')
    for (k, v) in col.indices.items():
        print(k, '\t', v)


print(sorted(col.data))
print(col.data)
print(col.indices)
print(col.len)

