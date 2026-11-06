# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None


        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        
        prev = None
        current = head 
        j = 0
        while current is not None:
            j += 1 
            tail = current
            if (j >= (length // 2 + 1)):
                present = current
                current = current.next
                present.next = prev 
                prev = present
            else:  
                current = current.next




        currentl = head 
        currentr = tail 
        i = 0
        while currentr is not None and (currentr != currentl):
            presentl = currentl
            currentl = currentl.next
            presentl.next = currentr
            if currentr is not None and (currentr.next == presentl or currentl == currentr.next or currentl == currentr):
                currentr.next = currentl
                currentl.next = None
                break
                
            presentr = currentr
            currentr = currentr.next
            presentr.next = currentl


