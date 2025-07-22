class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Place each number in its correct position
        i = 0
        while i < n:
            correct_index = arr[i] - 1
            if 1 <= arr[i] <= n and arr[i] != arr[correct_index]:
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
            else:
                i += 1

        # Step 2: Find the first location where index + 1 != value
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1

        # If all numbers from 1 to n are present
        return n + 1
