import math

class Solution:
    def kokoEat(self, arr, k):
        # Code here

        def check(s):
            """
            Helper function to calculate the total hours Koko takes to eat all bananas
            with a given speed 's'.
            """
            total_hours = 0
            for bananas in arr:
                total_hours += math.ceil(bananas / s)
            return total_hours <= k

        low = 1
        high = max(arr)  # Maximum possible speed is the largest pile size
        ans = high       # Initialize ans with a valid upper bound

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                # If mid is a valid speed, it could be our answer.
                # Try to find an even smaller speed.
                ans = mid
                high = mid - 1
            else:
                # If mid is too slow, we need a faster speed.
                low = mid + 1
        return ans
