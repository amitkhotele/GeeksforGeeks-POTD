# User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check mid
            if arr[mid] == target:
                return mid
            
            # Check mid-1 (only if mid > low)
            if mid > low and arr[mid - 1] == target:
                return mid - 1
            
            # Check mid+1 (only if mid < high)
            if mid < high and arr[mid + 1] == target:
                return mid + 1
            
            # Decide search direction
            if target < arr[mid]:
                high = mid - 2
            else:
                low = mid + 2
        
        return -1
