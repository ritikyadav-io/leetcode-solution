class Solution(object):
    def groupAnagrams(self, strs):
        d = defaultdict(list)

        for word in strs:
            key=''.join(sorted(word))
            d[key].append(word)

        return list(d.values())
        