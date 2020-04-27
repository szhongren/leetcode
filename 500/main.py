"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

American keyboard

Example 1:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.res = []
        for word in words:
            self.checkWord(word)
        return self.res

    def checkWord(self, word):
        rows = [
            'qwertyuiopQWERTYUIOP',
            'asdfghjklASDFGHJKL',
            'zxcvbnmZXCVBNM'
        ]
        for row in rows:
            if len(list(filter(lambda ch: ch in row, word))) == len(word):
                self.res.append(word)
                return

ans = Solution()
print(ans.findWords(["Hello", "Alaska", "Dad", "Peace"]))
