class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        for i in range(len(strs[0])):
             current_char = strs[0][i]
             for s in strs:
                if i>=len(s) or current_char!=s[i]:
                    return ans
             ans+=current_char 
        return ans

        