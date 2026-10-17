class Solution:
    def minSwaps(self, nums):
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        # Element format: (digit_sum, numerical_value, original_index)
        elements = [(get_digit_sum(val), val, i) for i, val in enumerate(nums)]
        elements.sort()
        
        swaps = 0
        i = 0
        while i < len(nums):
            correct_idx = elements[i][2]
            
            # If the item at index `i` is not at its correct original home,
            # swap it into its correct place.
            if correct_idx != i:
                elements[i], elements[correct_idx] = elements[correct_idx], elements[i]
                swaps += 1
            else:
                i += 1
                
        return swaps
