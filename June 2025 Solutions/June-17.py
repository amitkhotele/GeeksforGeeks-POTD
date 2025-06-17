import bisect

class Solution:
    def minimumCoins(self, arr, k):
        n = len(arr)
        if n <= 1:
            return 0

        arr.sort()

        # Calculate prefix sums
        # prefix_sums[x] stores the sum of arr[0] to arr[x-1]
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + arr[i]

        min_total_removed = float('inf')

        # Iterate through each element arr[i] and consider it as the minimum value (L)
        # in the final set of remaining piles.
        # The target range for remaining piles will be [arr[i], arr[i] + k].
        for i in range(n):
            current_removed_coins = 0

            # 1. Coins to remove from piles smaller than arr[i] (L)
            # These are arr[0] to arr[i-1]. They must be removed entirely.
            current_removed_coins += prefix_sums[i]

            # 2. Determine the upper bound (R) for the current target range
            max_allowed_val = arr[i] + k

            # Find the index 'j' of the first element in 'arr' that is strictly
            # greater than max_allowed_val.
            # All piles from arr[j] to arr[n-1] are too large ( > R).
            # These piles must be reduced to max_allowed_val.
            right_start_idx = bisect.bisect_right(arr, max_allowed_val)

            # Sum of coins in piles that need to be reduced
            sum_of_piles_to_reduce = prefix_sums[n] - prefix_sums[right_start_idx]
            
            # Number of piles that need to be reduced
            count_of_piles_to_reduce = n - right_start_idx

            # Coins removed by reducing these piles: (sum of original coins) - (sum after reduction)
            coins_removed_by_reduction = sum_of_piles_to_reduce - (count_of_piles_to_reduce * max_allowed_val)
            
            current_removed_coins += coins_removed_by_reduction
            
            min_total_removed = min(min_total_removed, current_removed_coins)

        return min_total_removed
