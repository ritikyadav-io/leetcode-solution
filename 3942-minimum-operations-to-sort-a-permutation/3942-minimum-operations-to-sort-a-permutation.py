class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        # 0 ka original index dhoondo
        idx_zero = nums.index(0)
        
        # Step 1: Check karo agar array increasing valid cyclic shift hai
        is_increasing = True
        for i in range(n):
            if nums[i] != (i - idx_zero) % n:
                is_increasing = False
                break
                
        if is_increasing:
            # Agar array increasing cyclic order me hai, toh 2 raste hain:
            
            # Option A: Sirf Left Rotations se '0' ko aage lana
            op_a = idx_zero
            
            # Option B: Reverse -> Rotate -> Reverse karke sequence badalna
            # Total steps: 1 (reverse) + (n - idx_zero) % n (left rotations) + 1 (reverse)
            op_b = 1 + ((n - idx_zero) % n) + 1
            
            return min(op_a, op_b)
            
        # Step 2: Check karo agar array decreasing valid cyclic shift hai
        is_decreasing = True
        for i in range(n):
            if nums[i] != (idx_zero - i) % n:
                is_decreasing = False
                break
                
        if is_decreasing:
            # Agar array decreasing cyclic order me hai, toh bhi 2 raste hain:
            
            # Option A: Pehle Left Rotate fir Reverse
            op_a = ((idx_zero + 1) % n) + 1
            
            # Option B: Pehle Reverse fir Left Rotate
            op_b = n - idx_zero
            
            return min(op_a, op_b)
            
        # Step 3: Agar dono me se koi valid cyclic shift nahi hai toh impossible hai
        return -1
