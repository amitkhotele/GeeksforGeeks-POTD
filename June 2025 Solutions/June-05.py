class Solution:
    def countPaths(self, edges, V, src, dest):
        from collections import defaultdict
        
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # Step 2: Memoization cache
        memo = {}

        # Step 3: DFS with memoization
        def dfs(node):
            if node == dest:
                return 1
            if node in memo:
                return memo[node]
            
            total_paths = 0
            for neighbor in graph[node]:
                total_paths += dfs(neighbor)

            memo[node] = total_paths
            return total_paths

        return dfs(src)
