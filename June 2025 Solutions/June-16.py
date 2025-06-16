class Solution:
    def minCost(self, heights, cost):
        n = len(heights)
        towers = sorted(zip(heights, cost))  # Sort by height

        # prefix sums
        prefix_cost = [0] * n
        prefix_hc = [0] * n
        prefix_cost[0] = towers[0][1]
        prefix_hc[0] = towers[0][0] * towers[0][1]

        for i in range(1, n):
            h, c = towers[i]
            prefix_cost[i] = prefix_cost[i-1] + c
            prefix_hc[i] = prefix_hc[i-1] + h * c

        total_cost = prefix_cost[-1]
        total_hc = prefix_hc[-1]

        res = float('inf')
        for i in range(n):
            h_i, _ = towers[i]
            # Cost to make all heights to h_i
            left_cost = h_i * prefix_cost[i] - prefix_hc[i]
            right_cost = (total_hc - prefix_hc[i]) - h_i * (total_cost - prefix_cost[i])
            res = min(res, left_cost + right_cost)

        return res
