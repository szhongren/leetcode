from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        approach
        use a stack, if will collide, collide
        then return stack
        """
        stack = []
        for asteroid in asteroids:
            print(stack)
            if len(stack) == 0:
                stack.append(asteroid)
                continue
            if not (stack[-1] > 0 and asteroid < 0):
                stack.append(asteroid)
                continue
            while (
                len(stack) > 0
                and stack[-1] > 0
                and asteroid < 0
                and stack[-1] < -asteroid
            ):
                stack.pop()
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroid)
                continue
            if stack[-1] == -asteroid:
                stack.pop()
                continue

        return stack
