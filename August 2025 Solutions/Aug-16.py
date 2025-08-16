from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Convert all integers to strings
        arr = list(map(str, arr))
        
        # Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1   # x should come before y
            elif x + y < y + x:
                return 1    # y should come before x
            else:
                return 0
        
        # Sort using comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Join all numbers
        result = ''.join(arr)
        
        # Handle leading zeros (like "0000" -> "0")
        return result if result[0] != '0' else '0'
