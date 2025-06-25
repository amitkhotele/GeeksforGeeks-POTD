from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        freq_values = list(freq.values())
        freq_count = Counter(freq_values)

        # Case 1: All characters have the same frequency
        if len(freq_count) == 1:
            return True

        # Case 2: Only two different frequencies
        if len(freq_count) == 2:
            keys = list(freq_count.keys())
            val1, val2 = keys[0], keys[1]
            cnt1, cnt2 = freq_count[val1], freq_count[val2]

            # Case 2.1: One character with frequency 1 (can remove it)
            if (val1 == 1 and cnt1 == 1) or (val2 == 1 and cnt2 == 1):
                return True

            # Case 2.2: One character has frequency 1 more than others and appears once
            if (abs(val1 - val2) == 1):
                if (val1 > val2 and cnt1 == 1) or (val2 > val1 and cnt2 == 1):
                    return True

        # Otherwise, not possible
        return False
from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        freq_values = list(freq.values())
        freq_count = Counter(freq_values)

        # Case 1: All characters have the same frequency
        if len(freq_count) == 1:
            return True

        # Case 2: Only two different frequencies
        if len(freq_count) == 2:
            keys = list(freq_count.keys())
            val1, val2 = keys[0], keys[1]
            cnt1, cnt2 = freq_count[val1], freq_count[val2]

            # Case 2.1: One character with frequency 1 (can remove it)
            if (val1 == 1 and cnt1 == 1) or (val2 == 1 and cnt2 == 1):
                return True

            # Case 2.2: One character has frequency 1 more than others and appears once
            if (abs(val1 - val2) == 1):
                if (val1 > val2 and cnt1 == 1) or (val2 > val1 and cnt2 == 1):
                    return True

        # Otherwise, not possible
        return False
