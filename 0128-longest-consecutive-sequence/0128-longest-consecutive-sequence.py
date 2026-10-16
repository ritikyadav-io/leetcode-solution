class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        longest = 0
        s = set(nums)

        for x in s:
            if x-1 not in s:
                current_streak=1
                
                while x+current_streak in s:
                    current_streak+=1
            

                longest=max(current_streak,longest)

        return longest
        """
        :type nums: List[int]
        :rtype: int
        """
        