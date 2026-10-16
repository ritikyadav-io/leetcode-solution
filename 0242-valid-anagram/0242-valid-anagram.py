class Solution(object):
    def isAnagram(self, s, t):
        d ={}
        if len(s)!=len(t):
            return False

        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        for j in t:
            if j not in d:
                return False
            d[j]-=1

            if d[j]==-1:
                return False
        return True 
