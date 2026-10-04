class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        temp =[]
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])

        while len(temp)<n:
            temp.append(0)
            nums[:] = temp
            