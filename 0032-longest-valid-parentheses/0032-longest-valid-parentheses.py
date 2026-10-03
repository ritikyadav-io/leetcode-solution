class Solution(object):
    def longestValidParentheses(self, s):
       max_len =0 
       stack = [-1]

       for i in range(len(s)):
        if s[i]=="(":
            stack.append(i)
        else:
            stack.pop()

        if not stack:
            stack.append(i)
        else:
           current_len = i - stack[-1]
           max_len = max(max_len, current_len)
                
       return max_len
        


