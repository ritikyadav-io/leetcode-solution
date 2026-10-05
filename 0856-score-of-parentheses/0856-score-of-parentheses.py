class Solution(object):
    def scoreOfParentheses(self, s):
        ans=0
        depth=0
        for i in range(len(s)):
            if s[i]=="(":
                depth +=1 
            else:
                depth-=1
            
                if s[i-1]=="(":
                    ans+=1 <<depth
        return ans