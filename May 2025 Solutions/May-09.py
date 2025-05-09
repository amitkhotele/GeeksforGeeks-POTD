class Solution:
    def findMaximumNum(self, s, k):
        self.ans = s

        def solve(s_list, k):
            if k == 0:
                return

            n = len(s_list)
            for i in range(n):
                max_digit = max(s_list[i:])
                if max_digit != s_list[i]:
                    for j in range(n - 1, i, -1):
                        if s_list[j] == max_digit:
                            s_list[i], s_list[j] = s_list[j], s_list[i]
                            current = ''.join(s_list)
                            if current > self.ans:
                                self.ans = current
                            solve(s_list, k - 1)
                            s_list[i], s_list[j] = s_list[j], s_list[i]
                    return  # Important: only try swaps on first mismatch to avoid TLE

        solve(list(s), k)
        return self.ans
