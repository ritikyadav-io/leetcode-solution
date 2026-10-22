class Solution(object):
    def removeNthFromEnd(self, head, n):
        root = ListNode(0)
        root.next = head
        first = root
        second =root

        for i in range(n+1):
            first = first.next
        
        while first is not None:
            first = first.next
            second = second.next

        second.next =second.next.next 

        return root.next


        