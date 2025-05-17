class Solution:
    def sortArray(self, arr, A, B, C):
        def quad(x):
            return A * x * x + B * x + C
        
        n = len(arr)
        result = [0] * n
        l, r = 0, n - 1
        idx = n - 1 if A >= 0 else 0  # Fill from end if A >= 0, else from start

        while l <= r:
            left_val = quad(arr[l])
            right_val = quad(arr[r])
            
            if A >= 0:
                if left_val > right_val:
                    result[idx] = left_val
                    l += 1
                else:
                    result[idx] = right_val
                    r -= 1
                idx -= 1
            else:
                if left_val < right_val:
                    result[idx] = left_val
                    l += 1
                else:
                    result[idx] = right_val
                    r -= 1
                idx += 1

        return result
