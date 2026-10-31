class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        memo = {}

        def dfs(r, c, direction):
            # Out of bounds boundary checks
            if r >= m or c >= n:
                return 0
            
            # Mirror redirection mechanics
            if grid[r][c] == 1:
                if direction == 'R':
                    return dfs(r + 1, c, 'D')
                else:
                    return dfs(r, c + 1, 'R')
            
            # Destination check
            if r == m - 1 and c == n - 1:
                return 1
            
            state = (r, c, direction)
            if state in memo:
                return memo[state]
            
            # Empty cell choices
            move_right = dfs(r, c + 1, 'R')
            move_down = dfs(r + 1, c, 'D')
            
            memo[state] = (move_right + move_down) % MOD
            return memo[state]
        
        if m == 1 and n == 1:
            return 1
            
        return (dfs(0, 1, 'R') + dfs(1, 0, 'D')) % MOD
