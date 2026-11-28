from typing import List
from functools import cmp_to_key

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        min_price = float('inf')
        
        for factor, price in items:
            freq[factor] += 1
            if price < min_price:
                min_price = price
                
        # mult_count[f] = total items whose factor is a multiple of f
        mult_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                for multiple in range(f, n + 1, f):
                    mult_count[f] += freq[multiple]
                    
        # Options: (price, gain, max_purchases)
        options = []
        for factor, price in items:
            free_limit = mult_count[factor] - 1
            # Only consider 2-item bundles if they are strictly better than buying 2 singles
            if free_limit > 0 and price < 2 * min_price:
                options.append((price, 2, free_limit))
                
        # Add the cheapest 1-item single with unlimited supply
        options.append((min_price, 1, budget // min_price))
        
        # Sort by price / gain ascending (cross-multiply to avoid float precision issues)
        def compare(a, b):
            p1, g1, _ = a
            p2, g2, _ = b
            if p1 * g2 != p2 * g1:
                return -1 if p1 * g2 < p2 * g1 else 1
            return -1 if p1 < p2 else (1 if p1 > p2 else 0)
            
        options.sort(key=cmp_to_key(compare))
        
        total_items = 0
        for price, gain, limit in options:
            if budget < price:
                continue
            can_buy = min(limit, budget // price)
            total_items += can_buy * gain
            budget -= can_buy * price
            
        return total_items
