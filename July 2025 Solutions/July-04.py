class Solution:
    def countAtMostK(self, arr, k):
        from collections import defaultdict

        count = defaultdict(int)
        start = 0
        result = 0
        distinct = 0

        for end in range(len(arr)):
            if count[arr[end]] == 0:
                distinct += 1
            count[arr[end]] += 1

            # Shrink window until distinct <= k
            while distinct > k:
                count[arr[start]] -= 1
                if count[arr[start]] == 0:
                    distinct -= 1
                start += 1

            result += end - start + 1

        return result
