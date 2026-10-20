class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        sum_of_k = 0
        
        # KMP helper function to find if pattern exists in text
        def kmp_search(text, pattern):
            m = len(pattern)
            if m == 0:
                return True
            
            # Compute Pi array (LPS table)
            lps = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
            
            # Match pattern in text
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    return True
            return False

        # Try every divisor k of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            is_valid_k = True
            
            # Check each block of length k
            for i in range(0, n, k):
                orig_block = nums[i : i + k]
                sorted_block = sorted_nums[i : i + k]
                
                # A cyclic rotation of sorted_block will always be a sublist of (sorted_block + sorted_block)
                text = sorted_block + sorted_block[:-1]
                
                if not kmp_search(text, orig_block):
                    is_valid_k = False
                    break
            
            if is_valid_k:
                sum_of_k += k
                
        return sum_of_k
