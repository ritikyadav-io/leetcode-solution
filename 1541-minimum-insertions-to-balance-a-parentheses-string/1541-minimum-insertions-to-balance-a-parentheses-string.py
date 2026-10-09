class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_right = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # A '(' needs two ')'
                needed_right += 2
                # If we had an odd number of needed rights, it means a previous '(' 
                # only got one ')'. We must fix it by adding one ')' immediately.
                if needed_right % 2 != 0:
                    insertions += 1
                    needed_right -= 1
                i += 1
            else:
                # We found a ')'
                # Check if it's followed by another ')' to make a consecutive pair '))'
                if i + 1 < n and s[i + 1] == ')':
                    needed_right -= 2
                    i += 2  # Skip both
                else:
                    needed_right -= 2
                    insertions += 1  # Insert one ')' to make it a pair
                    i += 1
                
                # If we have too many closing parentheses, we need to insert a '('
                if needed_right < 0:
                    insertions += 1
                    needed_right += 2  # The inserted '(' expects 2 rights, minus the current pair
                    
        return insertions + needed_right

