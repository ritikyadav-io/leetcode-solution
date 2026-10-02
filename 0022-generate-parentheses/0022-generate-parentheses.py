class Solution(object):
    def generateParenthesis(self, n):
       
        ans = []
        
        # Helper function jo recursion chalayega
        def backtrack(current_string, open_count, close_count):
            # Base Case: Agar string ki length 2 * n ho gayi, matlab saare brackets use ho gaye
            if len(current_string) == 2 * n:
                ans.append(current_string)
                return
            
            # Rule 1: Agar opening brackets bache hain, toh '(' lagao
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # Rule 2: Agar closing brackets, opening se kam hain, toh ')' lagao
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
        
        # Shuruat khali string, 0 open aur 0 close brackets se karenge
        backtrack("", 0, 0)
        return ans

        