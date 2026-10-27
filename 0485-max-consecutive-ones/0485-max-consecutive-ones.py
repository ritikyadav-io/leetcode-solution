class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maximum = 0

        for x in nums:
            if x==1:
                count+=1

                if count>maximum:
                    maximum = count
            else:
                count=0
        return maximum

