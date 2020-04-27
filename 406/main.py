"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x: x[0])
        inserts = []
        if len(people) == 0:
            return []
        else:
            curr = people[0][0]
            i = 0
            while i < len(people):
                if people[i][0] == curr:
                    inserts.append(people[i])
                    i += 1
                else:
                    break
            inserts.sort(key = lambda x: x[1])
            ans = self.reconstructQueue(people[i:])
            for i in range(len(inserts)):
                ans.insert(inserts[i][1], inserts[i])
            return ans

ans = Solution()
print(ans.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
print(ans.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))