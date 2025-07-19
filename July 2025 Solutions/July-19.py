from itertools import product, permutations
from collections import defaultdict
import math

class Solution:
    def vowelCount(self, s: str) -> int:
        vowels = 'aeiou'
        vowel_positions = defaultdict(list)

        # Collect positions (not needed specifically, just count is enough)
        for ch in s:
            if ch in vowels:
                vowel_positions[ch].append(ch)

        unique_vowels = list(vowel_positions.keys())
        if not unique_vowels:
            return 0

        # For each vowel, count how many times it appears
        counts = [len(vowel_positions[v]) for v in unique_vowels]

        # Total combinations = product of counts (choose one occurrence per vowel)
        total_combinations = 1
        for c in counts:
            total_combinations *= c

        # Each such combination gives factorial(len(unique_vowels)) permutations
        perm_count = math.factorial(len(unique_vowels))

        return total_combinations * perm_count
