# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 
        current = head 
        while current is not None:
            length += 1 
            current = current.next 

        if (n == length):
            return head.next
        m = length - n


        i = 0 
        current = head 
        prev = None 
        while current is not None:
            if (i == m):
                prev.next = current.next
                return head
            else:
                i += 1
                prev = current
                current = current.next
        
        return head