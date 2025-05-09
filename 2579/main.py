class Solution:
    def coloredCells(self, n: int) -> int:
        """
        approach
        manually count, and find a pattern, I think theres' a mathematical pattern I can use
        1 -> 1
        2 -> 1 + 3 + 1 = 5 + 4
        3 -> 1 + 3 + 5 + 3 + 1 = 13 + 8
        4 -> 1 + 3 + 5 + 7 + 5 + 3 + 1 = 25 + 12
        5 -> 1 + 3 + 5 + 7 + 9 + 7 + 5 + 3 + 1 = 41 + 16
        thus, every time, we + 4 * n - 1
        or (n * 2)-1 is the max, and we can just sum till 1 **
        """
        max_height = (n * 2) - 1
        acc = max_height
        while max_height > 1:
            max_height -= 2
            acc += 2 * max_height
        return acc
