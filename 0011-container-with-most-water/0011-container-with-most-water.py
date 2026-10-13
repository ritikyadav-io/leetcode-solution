class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0  # Initializing to 0 is sufficient for areas
        
        while l < r:
            # Corrected: Multiply the minimum height by the width (r - l)
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            
            # Corrected: Move the right pointer inward when height[l] >= height[r]
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1  # Fixed from r += 1
                
        return max_area
