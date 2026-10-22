class Solution(object):
    def sortColors(self, nums):
        low = 0
        mid =0
        high = len(nums)-1
        result = []

        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1;
            else:
                if nums[mid]==2:
                    nums[mid],nums[high]=nums[high],nums[mid]
                    high-=1; 

