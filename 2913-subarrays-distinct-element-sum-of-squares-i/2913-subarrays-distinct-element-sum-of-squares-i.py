from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Traverse every possible starting index of the subarray
        for i in range(n):
            distinct_elements = set()
            # Expand the subarray by changing the ending index
            for j in range(i, n):
                distinct_elements.add(nums[j])
                # Add the square of the distinct count to the total sum
                total_sum += len(distinct_elements) ** 2
                
        return total_sum
