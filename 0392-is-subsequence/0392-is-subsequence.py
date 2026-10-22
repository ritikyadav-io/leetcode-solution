class Solution(object):
    def isSubsequence(self, s, t):
        i,j=0,0

        if len(s)==0:
            return True
        
        while i<len(s) and j<len(t):
            if s[i]!=t[j]:
                j+=1
            else:
                j+=1
                i+=1

            if i == len(s):
                return True
        return i==len(s)