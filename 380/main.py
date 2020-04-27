"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet ans = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
ans.insert(1);

// Returns false as 2 does not exist in the set.
ans.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
ans.insert(2);

// getRandom should return either 1 or 2 randomly.
ans.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
ans.remove(1);

// 2 was already in the set, so return false.
ans.insert(2);

// Since 1 is the only number in the set, getRandom always return 1.
ans.getRandom();
"""

import random as rnd

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_i = {} # keeps track of values we have
        self.vals = [] # used for O(1) random time
        self.len = 0 # helpful to keep track of where to swap, not technically needed but allows us to cut self.vals anywhere we want

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_i:
            return False
        else:
            self.val_to_i[val] = self.len
            self.vals = self.vals[:self.len] # cut the pool from which we can draw the random
            self.vals.append(val) # put at back of list
            self.len += 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_i:
            self.val_to_i[self.vals[self.len - 1]] = self.val_to_i[val]
            # set the index of the value we are swapping to the index of the value we are removing
            self.vals[self.val_to_i[val]], self.vals[self.len - 1] = self.vals[self.len - 1], self.vals[self.val_to_i[val]]
            # swap, we know where the val to remove is in list, and we know where the end of list is
            self.len -= 1
            del self.val_to_i[val] # delete the val from the set of keys
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.vals[rnd.randrange(self.len)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
ans = RandomizedSet()

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
for i in range(20):
    ans.insert(rnd.randrange(40))

# getRandom should return either 1 or 2 randomly.
for i in range(10):
    print(ans.getRandom())

# Removes 1 from the set, returns true. Set now contains [2].
for i in range(15):
    ans.remove(i)

# Since 1 is the only number in the set, getRandom always return 1.
for i in range(10):
    print(ans.getRandom())