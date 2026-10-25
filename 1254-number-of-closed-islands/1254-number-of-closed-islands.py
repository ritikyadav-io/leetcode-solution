class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: out of bounds or water
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 1:
                return
            # Mark the current land cell as visited by turning it into water
            grid[r][c] = 1
            # Traverse all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Eliminate all land connected to the grid boundaries
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and grid[r][c] == 0:
                    dfs(r, c)
                    
        # Step 2: Count the remaining closed islands
        closed_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c)
                    closed_islands += 1
                    
        return closed_islands
