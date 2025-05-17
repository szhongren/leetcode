class Solution:
    def maximumLength(self, s: str) -> int:
        """
        approach
        count number of consecutive chars which are the same
        count freqs of chars
        then, if not sequence >= 3: 1 if any freq >= 3, else -1
        otherwise, return longest sequence - 2
        * doesn't work for edge cases where there's more than one long sequence of the same char
        need to count frequencies of each substring
        """
        frequencies = {}
        max_seq_length = 0
        curr_seq_length = 0
        curr_char = None
        char_has_3 = False
        for ch in s:
            if ch not in frequencies:
                frequencies[ch] = 0
            frequencies[ch] += 1
            if frequencies[ch] == 3:
                char_has_3 = True
            if ch != curr_char:
                max_seq_length = max(max_seq_length, curr_seq_length)
                curr_seq_length = 0
                curr_char = ch
            curr_seq_length += 1
        max_seq_length = max(max_seq_length, curr_seq_length)

        if max_seq_length >= 3:
            return max_seq_length - 2
        if char_has_3:
            return 1
        return -1

    def maximumLength_model(self, s: str) -> int:
        # Create a dictionary to store the count of all substrings.
        count = {}
        for start in range(len(s)):
            character = s[start]
            substring_length = 0
            for end in range(start, len(s)):
                # If the string is empty, or the current character is equal to
                # the previously added character, then add it to the map.
                # Otherwise, break the iteration.
                if character == s[end]:
                    substring_length += 1
                    count[(character, substring_length)] = (
                        count.get((character, substring_length), 0) + 1
                    )
                else:
                    break

        # Create a variable ans to store the longest length of substring with
        # frequency atleast 3.
        ans = -1
        for i in count.items():
            length = i[0][1]
            if i[1] >= 3 and length > ans:
                ans = length

        return ans
