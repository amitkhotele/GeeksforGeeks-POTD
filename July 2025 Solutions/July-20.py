class Solution:
    def countValid(self, n, arr):
        arr_set = set(arr)
        all_digits = set(range(10))
        allowed = list(all_digits - arr_set)

        # Total n-digit numbers
        total = 9 * (10 ** (n - 1))

        if not allowed:
            return total  # All numbers must contain at least one digit from arr

        # Count how many n-digit numbers can be formed using only 'allowed' digits
        allowed_set = set(allowed)

        def count_without_arr():
            count = 0
            for first_digit in allowed:
                if first_digit == 0:
                    continue  # Can't be leading zero
                curr = 1
                for _ in range(n - 1):
                    curr *= len(allowed)
                count += curr
            return count

        invalid_count = count_without_arr()

        return total - invalid_count
