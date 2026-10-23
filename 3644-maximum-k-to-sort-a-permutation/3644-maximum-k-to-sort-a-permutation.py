class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1  # Initialized to all bits set to 1
        
        for i, x in enumerate(nums):
            if i != x:
                ans &= x  # Accumulate bitwise AND for misplaced elements
                
        # If ans remains -1, the array was already sorted (return 0).
        # Otherwise, return the accumulated bitwise AND value.
        return max(ans, 0)
