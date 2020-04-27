"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.

Example 2:

Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:

    N is in range [1,200].
    M[i][i] = 1 for all students.
    If M[i][j] = 1, then M[j][i] = 1.
"""
from collections import deque

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def bfs(person):
            seen = set([person])
            queue = deque([person])
            while len(queue) != 0:
                curr = queue.popleft()
                friends = M[curr]
                for i in range(len(M)):
                    if friends[i] == 1 and i not in seen:
                        queue.append(i)
                        seen.add(i)
            return seen
        unseen = set()
        count = 0
        while len(unseen) < len(M):
            next_person = [i for i in range(len(M)) if i not in unseen][0]
            unseen = unseen.union(bfs(next_person))
            count += 1
        return count


ans = Solution()
print(ans.findCircleNum(
    [[1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]]))

print(ans.findCircleNum(
    [[1,1,0],
    [1,1,0],
    [0,0,1]]))

print(ans.findCircleNum(
    [[1,1,0],
    [1,1,1],
    [0,1,1]]))
