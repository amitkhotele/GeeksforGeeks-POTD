class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict

        event_map = defaultdict(int)

        # Step 1: Mark +1 at start, -1 at end + 1
        for start, end in intervals:
            event_map[start] += 1
            event_map[end + 1] -= 1

        # Step 2: Sort event points
        sorted_keys = sorted(event_map.keys())
        
        current = 0
        max_powerful = -1

        # Step 3: Sweep line
        for i in range(len(sorted_keys) - 1):
            point = sorted_keys[i]
            current += event_map[point]

            next_point = sorted_keys[i + 1]

            if current >= k:
                # All numbers from point to next_point - 1 are powerful
                max_powerful = max(max_powerful, next_point - 1)

        return max_powerful
