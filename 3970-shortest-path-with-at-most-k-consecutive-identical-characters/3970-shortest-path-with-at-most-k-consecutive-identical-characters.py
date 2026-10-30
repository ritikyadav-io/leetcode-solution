from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Step 2: Track min distances for each state: (node, consecutive_streak)
        # Initialize everything to infinity
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        
        # Step 3: Priority Queue: elements are (cost, current_node, consecutive_streak)
        # Node 0 starts with cost 0 and a streak of 1
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        # Step 4: Process states using Dijkstra's Algorithm
        while pq:
            d, u, run = heapq.heappop(pq)
            
            # Destination reached
            if u == n - 1:
                return d
                
            # If we found a shorter path to this state already, skip it
            if d > dist[u][run]:
                continue
                
            # Traverse neighboring nodes
            for v, w in adj[u]:
                # Calculate consecutive run count for the neighbor node v
                next_run = (run + 1) if labels[u] == labels[v] else 1
                
                # Verify rule constraint (at most k consecutive identical characters)
                if next_run <= k and d + w < dist[v][next_run]:
                    dist[v][next_run] = d + w
                    heapq.heappush(pq, (d + w, v, next_run))
                    
        return -1
