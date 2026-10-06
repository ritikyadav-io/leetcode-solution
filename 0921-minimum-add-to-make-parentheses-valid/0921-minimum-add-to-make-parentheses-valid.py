class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        count = 0

        for ch in s:
            if ch == "(":
                stack.append(ch)

            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    count += 1

        return count + len(stack)