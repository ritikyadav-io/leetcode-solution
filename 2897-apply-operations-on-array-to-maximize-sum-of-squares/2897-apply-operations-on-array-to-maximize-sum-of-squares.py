class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 1_000_000_007
        bit_counts = [0] * 30
        
        # Step 1: Count bit frequencies
        for num in nums:
            for i in range(30):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        total_sum_squares = 0
        
        # Step 2: Extract bits greedily to build the k largest numbers
        for _ in range(k):
            current_num = 0
            for i in range(30):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            total_sum_squares = (total_sum_squares + current_num ** 2) % MOD
            
        return total_sum_squares
