class Solution:
    def isSumString(self, s: str) -> bool:
        def is_valid(a: str) -> bool:
            return len(a) == 1 or a[0] != '0'
        
        def helper(a: str, b: str, remaining: str) -> bool:
            if not is_valid(a) or not is_valid(b):
                return False
            
            sum_val = str(int(a) + int(b))
            if not remaining.startswith(sum_val):
                return False
            
            if remaining == sum_val:
                return True  # We've reached the end successfully
            
            return helper(b, sum_val, remaining[len(sum_val):])
        
        n = len(s)
        for i in range(1, n):  # First number ends at i
            for j in range(i+1, n):  # Second number ends at j
                a = s[:i]
                b = s[i:j]
                remaining = s[j:]
                if helper(a, b, remaining):
                    return True
        return False
