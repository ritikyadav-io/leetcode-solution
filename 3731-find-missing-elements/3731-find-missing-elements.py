class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        low = high = nums[0]
        seen = [False] * 101 
        
        for num in nums:
            if num < low: low = num
            if num > high: high = num
            seen[num] = True
            
        return [x for x in range(low, high + 1) if not seen[x]]
