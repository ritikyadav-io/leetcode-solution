class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Save a copy of the original exponent to handle the sign at the end
        abs_n = abs(n)
        
        result = 1.0
        current_product = x
        
        while abs_n > 0:
            if abs_n % 2 == 1:
                result *= current_product
            current_product *= current_product
            abs_n //= 2
            
        # If the original exponent was negative, invert the final result
        return result if n >= 0 else 1.0 / result
