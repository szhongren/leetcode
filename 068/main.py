"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.
Corner Cases:

    A line other than the last line might contain only one word. What should you do in this case?
    In this case, that line should be left-justified.
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        if maxWidth == 0:
            return [v for v in words if len(v) == 0]
        pos = 0
        ans = []
        curr_words = []
        while True:
            while sum(map(len, curr_words)) + len(curr_words) + len(words[pos]) <= maxWidth:
                curr_words.append(words[pos])
                pos += 1
                if pos >= len(words):
                    last_line = ' '.join(curr_words)
                    last_line += (maxWidth - len(last_line)) * " "
                    ans.append(last_line)
                    return ans
            words_length = sum(map(len, curr_words))
            if len(curr_words) == 1:
                ans.append(curr_words[0] + (maxWidth - words_length) * " ")
            else:
                join_spaces = (maxWidth - words_length) // (len(curr_words) - 1)
                extra_spaces = (maxWidth - words_length) % (len(curr_words) - 1)
                for i in range(extra_spaces):
                    curr_words[i] += " "
                ans.append((' ' * join_spaces).join(curr_words))
            curr_words = []

            # better way: ' '.join words, then chop off each group of words based on the indices of the spaces
            # for each chunk, split, do same thing as above to calculate the spaces to join with
            # append to ans, end when len(joined_string) <= 16

ans = Solution()
print(ans.fullJustify([""], 16))
print(ans.fullJustify([""], 0))
print(ans.fullJustify(["this", "is"], 0))
print(ans.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(ans.fullJustify(["This", "is", "an", "example", "of", "text", "justification.", "exhaustively"], 16))
