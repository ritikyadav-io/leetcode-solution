class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # 1. Sort logs by their timestamp
        logs.sort(key=lambda log: log[1])
        
        # 2. Pair queries with their original indices and sort by query time
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        # Frequency map to count active requests per server in the current window
        server_counts = [0] * (n + 1)
        unique_servers = 0
        
        ans = [0] * len(queries)
        left = 0
        right = 0
        m = len(logs)
        
        # 3. Process each query using the sliding window
        for original_idx, q_time in sorted_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand the window to include all logs <= window_end
            while right < m and logs[right][1] <= window_end:
                s_id = logs[right][0]
                if server_counts[s_id] == 0:
                    unique_servers += 1
                server_counts[s_id] += 1
                right += 1
                
            # Shrink the window from the left to remove logs < window_start
            while left < m and logs[left][1] < window_start:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    unique_servers -= 1
                left += 1
            
            # The remaining servers have 0 requests in this interval
            ans[original_idx] = n - unique_servers
            
        return ans
