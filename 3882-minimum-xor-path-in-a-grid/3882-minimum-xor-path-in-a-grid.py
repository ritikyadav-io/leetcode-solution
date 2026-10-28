class Solution(object):
    def minCost(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # Ek 2D matrix banayi jisme har cell par ek set() hoga.
        # Yeh set us cell tak pahunchne ke saare unique XOR values ko store karega.
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Base case: Shuruat top-left (0,0) se ho rahi hai, toh wahan ki value set mein daal di.
        dp[0][0].add(grid[0][0])
        
        # Poori grid ko scan karenge
        for r in range(m):
            for c in range(n):
                # Pehla cell skip karo kyunki wahan humne pehle hi value set kar di hai
                if r == 0 and c == 0:
                    continue
                
                # Agar upar se niche (Down move) aa sakte hain
                if r > 0:
                    for prev_xor in dp[r-1][c]:
                        dp[r][c].add(prev_xor ^ grid[r][c])
                
                # Agar left se right (Right move) jaa sakte hain
                if c > 0:
                    for prev_xor in dp[r][c-1]:
                        dp[r][c].add(prev_xor ^ grid[r][c])
                        
        # Destination cell (bottom-right) ke set mein se sabse choti (minimum) value return kar do
        return min(dp[m-1][n-1])
