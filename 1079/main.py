class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        approach:
        brute force?
        A -> A - 1
        AB -> A, B, AB, BA - 4
        AA -> A, AA -> 2
        AAA -> A, AA, AAA -> 3
        ABC -> A, B, C, AB, AC, BA, BC, CA, CB, ABC, ACB, BAC, BCA, CAB, CBA - 15
        ABB -> A, B, AB, BA, BB, ABB, BAB, BBA - 8
        """
        pass
