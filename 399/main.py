from typing import Dict, List, Set
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge:
    def __init__(self, operation, value, target):
        self.operation = operation
        self.value = value
        self.target = target

    def __repr__(self):
        return f"<{self.operation}, {self.value}, {self.target}>"


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """
        approach:
        build graph, and then bfs
        """
        nodes: Dict[str, Node] = {}
        for equation, value in zip(equations, values):
            a, b = equation[0], equation[1]
            node_a = Node(a)
            node_b = Node(b)
            if a in nodes:
                node_a = nodes[a]
            if b in nodes:
                node_b = nodes[b]
            node_a.edges.append(Edge("/", value, b))
            node_b.edges.append(Edge("*", value, a))
            nodes[a] = node_a
            nodes[b] = node_b
        result = []

        for query in queries:
            a, b = query[0], query[1]
            if a not in nodes or b not in nodes:
                result.append(-1.0)
                continue
            if a == b:
                result.append(1.0)
                continue
            queue = deque()
            queue.append(a)
            seen = Set()
            path = []
            while len(queue) != 0:
                curr = queue.popleft()
                if curr in seen:
                    continue
                seen.add(curr)
                curr_node = nodes[curr]


sol = Solution()
sol.calcEquation(
    [["a", "b"], ["b", "c"]],
    [2.0, 3.0],
    [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
)
