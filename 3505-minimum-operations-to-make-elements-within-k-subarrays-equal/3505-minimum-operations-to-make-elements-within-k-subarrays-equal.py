import heapq
from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        
        # Part 1: Calculate the minimum cost to equalize every window of size x
        min_ops = [0] * (n - x + 1)
        
        # Dual heaps for tracking the median
        left_heap = []   # Max-heap (invert values for heapq)
        right_heap = []  # Min-heap
        
        left_sum = 0
        right_sum = 0
        
        left_size = 0
        right_size = 0
        
        # Lazy deletion dictionary to track out-of-window elements
        to_delete = defaultdict(int)
        
        def add_num(num):
            nonlocal left_sum, right_sum, left_size, right_size
            if not left_heap or num <= -left_heap[0]:
                heapq.heappush(left_heap, -num)
                left_sum += num
                left_size += 1
            else:
                heapq.heappush(right_heap, num)
                right_sum += num
                right_size += 1
            rebalance()

        def remove_num(num):
            nonlocal left_sum, right_sum, left_size, right_size
            to_delete[num] += 1
            if num <= -left_heap[0]:
                left_sum -= num
                left_size -= 1
            else:
                right_sum -= num
                right_size -= 1
            rebalance()

        def rebalance():
            nonlocal left_sum, right_sum, left_size, right_size
            # Clean tops of both heaps if they contain lazy-deleted elements
            clean_heaps()
            
            # Left heap should hold ceil(x / 2) elements, right heap should hold floor(x / 2)
            target_left = (x + 1) // 2
            
            while left_size > target_left:
                val = -heapq.heappop(left_heap)
                left_sum -= val
                left_size -= 1
                
                heapq.heappush(right_heap, val)
                right_sum += val
                right_size += 1
                clean_heaps()
                
            while left_size < target_left and right_heap:
                val = heapq.heappop(right_heap)
                right_sum -= val
                right_size -= 1
                
                heapq.heappush(left_heap, -val)
                left_sum += val
                left_size += 1
                clean_heaps()

        def clean_heaps():
            while left_heap and to_delete[-left_heap[0]] > 0:
                to_delete[-left_heap[0]] -= 1
                heapq.heappop(left_heap)
            while right_heap and to_delete[right_heap[0]] > 0:
                to_delete[right_heap[0]] -= 1
                heapq.heappop(right_heap)

        # Initialize the first window
        for i in range(x):
            add_num(nums[i])
            
        median = -left_heap[0]
        # Total L1 cost formula relative to the median
        min_ops[0] = (left_size * median - left_sum) + (right_sum - right_size * median)
        
        # Slide across the remaining elements
        for i in range(1, n - x + 1):
            remove_num(nums[i - 1])
            add_num(nums[i + x - 1])
            
            median = -left_heap[0]
            min_ops[i] = (left_size * median - left_sum) + (right_sum - right_size * median)

        # Part 2: 2D Dynamic Programming to pick k non-overlapping windows
        # dp[i][j] represents the minimum operations to pick j windows from suffix nums[i:]
        inf = float('inf')
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        
        # Base case: 0 subarrays required costs 0 operations
        for i in range(n + 1):
            dp[i][0] = 0
            
        for j in range(1, k + 1):
            for i in range(n - 1, -1, -1):
                # Option A: Skip the current element
                res = dp[i + 1][j]
                
                # Option B: Pick the window starting at index i (if valid)
                if i + x <= n:
                    cost_pick = min_ops[i] + dp[i + x][j - 1]
                    if cost_pick < res:
                        res = cost_pick
                        
                dp[i][j] = res
                
        return dp[0][k] if dp[0][k] != inf else -1
