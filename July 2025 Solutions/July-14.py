class Solution:
    def cuts(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * n
        
        def is_power_of_5(bin_str):
            if bin_str[0] == '0':
                return False
            num = int(bin_str, 2)
            while num > 1:
                if num % 5 != 0:
                    return False
                num //= 5
            return num == 1

        for i in range(n):
            for j in range(i + 1):
                sub = s[j:i+1]
                if is_power_of_5(sub):
                    if j == 0:
                        dp[i] = 1
                    elif dp[j - 1] != float('inf'):
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return -1 if dp[n - 1] == float('inf') else dp[n - 1]
