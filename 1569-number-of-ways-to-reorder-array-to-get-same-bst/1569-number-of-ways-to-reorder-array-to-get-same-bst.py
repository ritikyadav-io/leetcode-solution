class Solution:

  def numOfWays(self, nums: list[int]) -> int:
    MOD = 10**9 + 7

    def dfs(arr):
      if len(arr) <= 2:
        return 1

      root = arr[0]
      left = [x for x in arr if x < root]
      right = [x for x in arr if x > root]

      # Combinations: choose len(left) positions out of len(left) + len(right)
      ways_left = dfs(left)
      ways_right = dfs(right)

      res = (
        math.comb(len(left) + len(right), len(left)) * ways_left * ways_right
      ) % MOD
      return res

    import math

    return (dfs(nums) - 1) % MOD
