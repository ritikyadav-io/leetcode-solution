import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Track the number of requests handled by each server
        request_counts = [0] * k
        
        # Min-heap to track busy servers: (free_time, server_id)
        busy_servers = []
        
        # Sorted list of available server IDs
        available_servers = SortedList(range(k))
        
        for i, (start_time, duration) in enumerate(zip(arrival, load)):
            # 1. Free up all servers that finished before or at the current arrival time
            while busy_servers and busy_servers[0][0] <= start_time:
                _, server_id = heapq.heappop(busy_servers)
                available_servers.add(server_id)
            
            # 2. If no servers are available, the request is dropped
            if not available_servers:
                continue
            
            # 3. Find the ideal server index (i % k)
            ideal_server = i % k
            
            # Binary search for the first available server >= ideal_server
            idx = available_servers.bisect_left(ideal_server)
            
            # If no server >= ideal_server, wrap around to the beginning (index 0)
            if idx == len(available_servers):
                idx = 0
                
            chosen_server = available_servers.pop(idx)
            
            # 4. Assign the request to the chosen server
            request_counts[chosen_server] += 1
            heapq.heappush(busy_servers, (start_time + duration, chosen_server))
            
        # Find the maximum requests handled by any server
        max_requests = max(request_counts)
        
        # Return all server IDs that achieved this maximum
        return [server_id for server_id, count in enumerate(request_counts) if count == max_requests]
