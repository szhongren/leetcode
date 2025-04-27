class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {}
        for i, ch in enumerate(order):
            order_map[ch] = i
        return sorted(s, key=lambda x: order_map.get(x, 0))
