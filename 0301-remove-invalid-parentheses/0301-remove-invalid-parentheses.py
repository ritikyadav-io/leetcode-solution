class Solution(object):
    def removeInvalidParentheses(self, s):
        def isValid(string):
            count = 0
            for char in string:
                if char == '(': count += 1
                elif char == ')': count -= 1
                if count < 0: return False
            return count == 0

        level = [s]
        
        while True:
            valid = [string for string in level if isValid(string)]
            if valid:
                return valid
            
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
            
            if not next_level:
                return [""]
                
            level = list(next_level)
