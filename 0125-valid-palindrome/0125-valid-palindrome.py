class Solution(object):
    def isPalindrome(self, s):
        ans = ""
        for char in s:
            char = char.lower()
            if char.isalnum() :
                ans+=char
        return ans==ans[::-1]
        
        