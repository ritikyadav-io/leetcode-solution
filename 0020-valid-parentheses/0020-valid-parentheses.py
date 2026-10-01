class Solution(object):
    def isValid(self, s):
        stack = []
        
        for char in s:
            
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                
           
            else:
               
                if not stack:
                    return False
                    
                top = stack.pop()
                
                # Check if the opening and closing brackets match up
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
                    
        if len(stack) == 0:
            return True
        else:
            return False
