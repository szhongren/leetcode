from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        approach
        construct 2 lists
        l_count, from left how many to move to ith box
        r_count, from right how many to move to ith box
        then, sum the 2, that's the answer

        for each list, I can do a running count
        every time I move 1, total = prev + running_count
        if 1, running_count += 1
        boxes = "110"
        r = "1,0,0"
        l = "0,1,3"
        boxes = "001011"
        r = "11,8,5,3,1,0"
        l = "0,0,0,1,2,4"
        """
        n = len(boxes)
        l_acc = [0] * n
        r_acc = [0] * n

        running_count = 1 if boxes[0] == "1" else 0
        for i in range(1, n):
            l_acc[i] = l_acc[i - 1] + running_count
            running_count += 1 if boxes[i] == "1" else 0

        running_count = 1 if boxes[-1] == "1" else 0
        for i in range(n - 2, -1, -1):
            r_acc[i] = r_acc[i + 1] + running_count
            running_count += 1 if boxes[i] == "1" else 0

        return [a + b for a, b in zip(r_acc, l_acc)]
