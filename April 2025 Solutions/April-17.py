class Solution:
    def findMinCycle(self, V, edges):
        INF = float('inf')

        # Initialize graph and dist matrix
        graph = [[INF] * V for _ in range(V)]
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        dist = [row[:] for row in graph]  # copy of graph
        min_cycle = INF

        for k in range(V):
            # Try to find cycles involving vertex k
            for i in range(k):
                for j in range(i + 1, k):
                    if dist[i][j] != INF and graph[i][k] != INF and graph[k][j] != INF:
                        cycle_weight = dist[i][j] + graph[i][k] + graph[k][j]
                        min_cycle = min(min_cycle, cycle_weight)

            # Update dist[i][j] using k as intermediate
            for i in range(V):
                for j in range(V):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]

        return min_cycle if min_cycle != INF else -1
