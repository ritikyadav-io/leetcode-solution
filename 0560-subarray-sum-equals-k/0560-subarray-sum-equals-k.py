class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        seen = {0: 1}

        for num in nums:
            total = total + num
            needed = total - k

            if needed in seen:
                count = count + seen[needed]

            if total in seen:
                seen[total] = seen[total] + 1
            else:
                seen[total] = 1

        return count
