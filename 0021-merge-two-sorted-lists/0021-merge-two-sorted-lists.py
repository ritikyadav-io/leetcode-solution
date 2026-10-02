class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        i = list1
        j = list2
        
        
        while i is not None and j is not None:
            if i.val <= j.val:
                tail.next = i
                i = i.next
            else:
                tail.next = j
                j = j.next
            tail = tail.next  
            
        if i is not None:
            tail.next = i
        elif j is not None:
            tail.next = j
            
        return dummy.next
