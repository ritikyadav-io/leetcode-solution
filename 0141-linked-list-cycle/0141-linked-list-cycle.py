class Solution(object):
    def hasCycle(self, head):
        # Ek khali 'set' banaya taaki hum visited nodes ko track kar sakein
        seen = set()
        
        # Jab tak head Null (None) nahi hota, tab tak loop chalega
        while head:
            # Agar current node pehle se 'seen' set mein hai, matlab cycle mil gayi!
            if head in seen:
                return True 
            
            # Agar node naya hai, toh usko 'seen' set mein add kar do
            seen.add(head)
            
            # Agle node par move kar jao
            head = head.next
            
        # Agar loop khatam ho gaya aur koi repeat nahi hua, matlab cycle nahi hai
        return False
