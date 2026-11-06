# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        prev = None
        current = head 
        j = 0
        while current.next is not None:
            current.prev = prev
            prev = current
            current = current.next 

        current.prev = prev
        tail = current


        currentl = head 
        currentr = tail 
        i = 0
        while (currentr != currentl):
            presentl = currentl
            currentl = currentl.next
            presentl.next = currentr
            if (currentr.prev == presentl or currentl == currentr.prev or currentl == currentr):
                currentr.next = currentl
                currentl.next = None
                break
            currentr.next = currentl

            currentr = currentr.prev


