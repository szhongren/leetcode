"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_chars = {}
        bulls = 0
        for (s_ch, g_ch) in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                if secret_chars.__contains__(s_ch):
                    secret_chars[s_ch] += 1
                else:
                    secret_chars[s_ch] = 1
        cows = 0
        for (s_ch, g_ch) in zip(secret, guess):
            if s_ch == g_ch or not secret_chars.__contains__(g_ch):
                continue
            elif secret_chars[g_ch] != 0:
                secret_chars[g_ch] -= 1
                cows += 1
        return str(bulls) + 'A' + str(cows) + 'B'

ans = Solution()
print(ans.getHint("1807", "7810"))
print(ans.getHint("1123", "0111"))