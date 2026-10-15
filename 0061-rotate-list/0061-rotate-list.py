class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head

        length = 1
        dummy=head

        while dummy.next:
            dummy=dummy.next
            length+=1
        
        k = k%length
        if k ==0:
            return head

        current = head

        i=1

        while i<=length-k-1:

            current=current.next
            i = i+1  

        new_head= current.next 
        current.next=None
        dummy.next=head

        return new_head

