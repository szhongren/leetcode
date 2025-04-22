import re


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        1. +/- ?
        2. (\d+|\d+\.\d*|\.\d+)(e[+-]?\d+)?
        """
        pass
        return re.search("^[+-]?(\d+|\d+\.\d*|\.\d+)([eE][+-]?\d+)?$", s) is not None
