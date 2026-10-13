class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left ,right=0,len(nums)-1
        result = [0] *len(nums)
        index = len(nums)-1

        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[index]=nums[left]**2
                left+=1
            else:
                result[index]=abs(nums[right])**2
                right-=1
            index-=1
        return result
            