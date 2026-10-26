class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        divisible_islands = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(m):
            for c in range(n):
                # If we hit land, explore the whole island
                if grid[r][c] > 0:
                    island_sum = 0
                    stack = [(r, c)]
                    island_sum += grid[r][c]
                    grid[r][c] = 0  # Sink the land immediately to mark it visited
                    
                    while stack:
                        curr_r, curr_c = stack.pop()
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Sink it
                                stack.append((nr, nc))
                    
                    # Verify divisibility condition
                    if island_sum % k == 0:
                        divisible_islands += 1
                        
        return divisible_islands
