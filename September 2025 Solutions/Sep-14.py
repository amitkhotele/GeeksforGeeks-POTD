class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        total_gas = sum(gas)
        total_cost = sum(cost)

        # If total gas is less than total cost, no solution
        if total_gas < total_cost:
            return -1

        start = 0
        tank = 0

        for i in range(n):
            tank += gas[i] - cost[i]
            # If tank goes negative, reset start
            if tank < 0:
                start = i + 1
                tank = 0

        return start
