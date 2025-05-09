from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        brute force
        for every word in words1, check to see if word in words2 has ch counts less than word
        if yes, append to answer
        preprocess both_lists to become ch counts
        """
        m = len(words1)
        n = len(words2)

        counts1 = [{} for _ in range(m)]
        for i, word in enumerate(words1):
            for ch in word:
                if ch not in counts1[i]:
                    counts1[i][ch] = 0
                counts1[i][ch] += 1

        counts2 = {}
        for word in words2:
            curr_counts = {}
            for ch in word:
                if ch not in curr_counts:
                    curr_counts[ch] = 0
                curr_counts[ch] += 1
            for ch in curr_counts.keys():
                if ch not in counts2:
                    counts2[ch] = curr_counts[ch]
                counts2[ch] = max(curr_counts[ch], counts2[ch])

        result = []
        for i, count1 in enumerate(counts1):
            skip = False
            for ch in counts2.keys():
                if ch not in count1:
                    skip = True
                    break
                if count1[ch] < counts2[ch]:
                    skip = True
                    break
            if not skip:
                result.append(words1[i])
        return result
