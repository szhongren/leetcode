from typing import List
from pprint import pprint


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """
        approach
        create union find sets, and compress paths
        """
        """
        a / b == v
        a = b * v
        """
        paths = {}
        for equation, value in zip(equations, values):
            a, b = equation[0], equation[1]
            """
            a / b = value
            b * value = a
            a * (1/value) = b
            """
            if a not in paths:
                paths[a] = {}
            if b not in paths:
                paths[b] = {}
            paths[a][b] = 1 / value
            paths[b][a] = value

        def find_target(current, target, path):
            if current not in paths:
                return None
            if current == target:
                return 1.0
            next_nodes = [key for key in paths[current].keys() if key not in path]
            print(f"{current} -> {target}, path={path}, next_nodes={next_nodes}")
            if len(next_nodes) == 0:
                return None
            for next_node in next_nodes:
                path.append(next_node)
                result = find_target(next_node, target, path)
                if result != None:
                    return paths[current][next_node] * result
                path.pop()

        result = []
        for query in queries:
            x, y = query[0], query[1]
            multiplier = find_target(x, y, [x])
            if multiplier is not None:
                result.append(1 / multiplier)
            else:
                result.append(-1)

        return result


sol = Solution()
print(
    sol.calcEquation(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    )
)
print(
    sol.calcEquation(
        [["a", "b"], ["b", "c"], ["bc", "cd"]],
        [1.5, 2.5, 5.0],
        [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
    )
)
print(
    sol.calcEquation(
        [["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    )
)
