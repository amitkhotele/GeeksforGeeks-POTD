class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # if first element is 0, we cannot move
        if n == 0 or arr[0] == 0:
            return -1
        if n == 1:
            return 0
        
        maxReach = arr[0]   # maximum index we can reach
        steps = arr[0]      # steps left within the current jump
        jumps = 1           # we need at least one jump
        
        for i in range(1, n):
            if i == n - 1:  # reached the end
                return jumps
            
            maxReach = max(maxReach, i + arr[i])
            steps -= 1  # using one step to move forward
            
            if steps == 0:
                jumps += 1
                if i >= maxReach:
                    return -1
                steps = maxReach - i
        
        return -1
