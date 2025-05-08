class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        approach
        split by \n
        then, keep a stack
        for each line, if len(stack) > number of \t, pop until equal
        then push
        check max if file
        else, if len(stack) < number of \t, shouldn't happen

        [], dir
        [dir], \ta
        [dir, a], \tb
        [dir, b], \t\ta.txt
        [dir, b, a.txt], \t\tb
        """
        lines = input.split("\n")
        stack = []
        max_len = 0
        for line in lines:
            count_of_t = 0
            for i in range(len(line)):
                if line[i] != "\t":
                    break
                count_of_t += 1
            if len(stack) > count_of_t:
                while len(stack) != count_of_t:
                    stack.pop()
            stack.append(line[count_of_t:])
            if "." in line:
                max_len = max(max_len, len("/".join(stack)))
        return max_len
