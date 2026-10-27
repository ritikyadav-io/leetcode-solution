'''class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
                
            if count==1:
                return nums[i]'''


class Solution(object):
    def singleNumber(self, nums):
        result = 0

        for x in nums:
            result = result ^ x

        return result
