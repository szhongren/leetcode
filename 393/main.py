"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
"""
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        curr = 0
        for byte in data:
            if curr == 0:
                if byte < 128:
                    continue
                elif byte >= 240: # 0x11110000
                    curr = 3
                    continue
                elif byte >= 224: # 0x11100000
                    curr = 2
                    continue
                elif byte >= 192: # 0x11000000
                    curr = 1
                    continue
                else:
                    return False
            else:
                if byte >= 128 and byte < 192:
                    curr -= 1
                else:
                    return False
        return curr == 0



ans = Solution()
print(ans.validUtf8([197, 130, 1]))
print(ans.validUtf8([235, 140, 4]))