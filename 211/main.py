"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.
You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
"""

class TrieNode(object):
    def __init__(self, if_terminal = False):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.terminal = if_terminal

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.terminal = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def searchRecur(node, s):
            if len(s) == 0:
                return node.terminal
            else:
                ch = s[0]
                ans = False
                if ch == '.':
                    for child in node.children.values():
                        ans |= searchRecur(child, s[1:])
                elif ch not in node.children:
                    ans = False
                else:
                    ans = searchRecur(node.children[ch], s[1:])
                return ans

        return searchRecur(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
trie = WordDictionary()
trie.addWord("bad")
trie.addWord("dad")
trie.addWord("mad")
print(trie.search("pad"))
print(trie.search("bad"))
print(trie.search(".ad"))
print(trie.search("b.."))
