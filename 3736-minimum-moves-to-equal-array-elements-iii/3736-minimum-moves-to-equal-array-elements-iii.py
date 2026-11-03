class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mx = max(nums)
        s = sum(nums)
        n = len(nums)
        return mx * n - s
