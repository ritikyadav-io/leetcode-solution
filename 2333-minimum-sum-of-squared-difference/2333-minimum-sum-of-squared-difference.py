class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        if max_diff == 0:
            return 0
            
        bucket = [0] * (max_diff + 1)
        for d in diffs:
            bucket[d] += 1
            
        for d in range(max_diff, 0, -1):
            if bucket[d] == 0:
                continue
            if k >= bucket[d]:
                k -= bucket[d]
                bucket[d - 1] += bucket[d]
                bucket[d] = 0
            else:
                bucket[d - 1] += k
                bucket[d] -= k
                k = 0
                break
                
        ans = 0
        for d in range(1, max_diff + 1):
            if bucket[d] > 0:
                ans += bucket[d] * (d ** 2)
                
        return ans
