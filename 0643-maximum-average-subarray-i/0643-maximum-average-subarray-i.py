class Solution(object):
    def findMaxAverage(self, nums, k):
        # Pehle 'k' elements ka sum nikaal lo
        a = sum(nums[:k])
        max_array = a
        
        # Loop start karo k se lekar array ke end tak
        for i in range(k, len(nums)):
            # Purana element (nums[i-k]) window se bahar niklega -> minus (-) karo
            # Naya element (nums[i]) window ke andar aayega -> plus (+) karo
            a = a + nums[i] - nums[i-k]
            
            # Agar naya sum pehle wale max se bada hai, toh update karo
            max_array = max(max_array, a)
            
        # Max sum ko k se divide karke average return karo
        return float(max_array) / k
