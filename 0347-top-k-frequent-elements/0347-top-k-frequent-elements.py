class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}

        for x in nums:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1

        topk = sorted(d,key=d.get,reverse=True)[:k]

        return topk
        