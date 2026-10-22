# Linked list ka definition
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Dummy node banate hain taaki edge cases (jaise head remove karna) easy ho
        root = ListNode(0)
        root.next = head
        
        # Dono pointers ko dummy node pe set karo
        first = root
        second = root
        
        # first pointer ko n+1 steps aage badhao, taaki dono ke beech n nodes ka gap bane
        for _ in range(n + 1):
            first = first.next
            
        # Jab tak first end pe nahi pahuncha, dono pointers ko saath-saath aage badhao
        while first is not None:
            first = first.next
            second = second.next
            
        # Ab second, remove karne wale node ke theek pehle hai -- use skip kar do
        second.next = second.next.next
        
        # Dummy ke baali list return karo
        return root.next   