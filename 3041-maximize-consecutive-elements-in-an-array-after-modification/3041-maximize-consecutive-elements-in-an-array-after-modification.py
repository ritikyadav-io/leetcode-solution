class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        dp: dict[int, int] = {}
        ans = 0

        for x in sorted(nums):
            dp[x + 1] = dp.get(x, 0) + 1
            dp[x] = dp.get(x - 1, 0) + 1
            ans = max(ans, dp[x + 1], dp[x])

        return ans
