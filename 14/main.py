from typing import List


class Trie:
    def __init__(self):
        self.next = {}
        self.is_end = False

    def add_word(self, word: str, i: int = 0):
        if i == len(word):
            self.is_end = True
            return
        first = word[i]
        if first not in self.next:
            self.next[first] = Trie()
        self.next[first].add_word(word, i + 1)

    def longest_prefix(self):
        if self.is_end or len(self.next) > 1:
            return ""
        char = list(self.next.keys())[0]
        return char + self.next[char].longest_prefix()


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        approach
        use a trie
        then, from the root, while next has 1 element, create the prefix
        edge cases:
        "" -> prefix = ""

        """
        trie = Trie()
        for word in strs:
            trie.add_word(word)

        return trie.longest_prefix()
