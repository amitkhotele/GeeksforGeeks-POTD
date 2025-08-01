class Solution:
    def countBalanced(self, arr):
        from collections import defaultdict
        
        def net_balance(s):
            vowels = set("aeiou")
            bal = 0
            for ch in s:
                if ch in vowels:
                    bal += 1
                else:
                    bal -= 1
            return bal

        balance_count = defaultdict(int)
        balance_count[0] = 1  # balance = 0 before starting

        count = 0
        balance = 0

        for word in arr:
            balance += net_balance(word)
            count += balance_count[balance]
            balance_count[balance] += 1

        return count
