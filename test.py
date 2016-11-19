class Solution(object):
    def dup(self, l):
        ans = []
        for i in range(len(l)):
            if l[abs(l[i]) - 1] >= 0:
                l[abs(l[i]) - 1] = -l[abs(l[i]) - 1]
            else:
                ans.append(abs(l[i]))
        return ans

ans = Solution()
print(ans.dup([4, 3, 2, 7, 8, 3, 1, 8]))
"""
zero
one
two
three
four
five
six
seven
eight
nine
"""