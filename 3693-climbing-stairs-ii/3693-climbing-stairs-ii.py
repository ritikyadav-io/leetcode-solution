class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        # dp[i] will store the minimum cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Starting point cost is 0
        
        for i in range(1, n + 1):
            landing_cost = costs[i - 1]
            
            # Look back up to 3 steps (i-1, i-2, i-3)
            for j in range(max(0, i - 3), i):
                jump_dist = i - j
                penalty = jump_dist * jump_dist
                
                dp[i] = min(dp[i], dp[j] + landing_cost + penalty)
                
        return dp[n]
